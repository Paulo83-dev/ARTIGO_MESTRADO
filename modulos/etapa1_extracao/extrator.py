"""
Módulo 01: Extração e Estruturação de Documentos com Docling
Converte PDFs em Markdown integral e gera chunks enriquecidos com metadados estruturais (HybridChunker).
"""

import sys
import json
import logging
from pathlib import Path
from typing import Optional, Union, List, Dict, Any, Tuple

from tqdm import tqdm
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.chunking import HybridChunker

# Suporte para importação relativa (como módulo) ou direta (execução isolada)
try:
    from .config import (
        DIR_ENTRADA_PADRAO,
        DIR_SAIDA_PADRAO,
        DEVICE,
        NUM_THREADS,
        DO_OCR,
        DO_TABLE_STRUCTURE,
        GENERATE_PICTURE_IMAGES,
        MARKDOWN_ENCODING,
        JSON_ENCODING,
    )
except ImportError:
    from config import (
        DIR_ENTRADA_PADRAO,
        DIR_SAIDA_PADRAO,
        DEVICE,
        NUM_THREADS,
        DO_OCR,
        DO_TABLE_STRUCTURE,
        GENERATE_PICTURE_IMAGES,
        MARKDOWN_ENCODING,
        JSON_ENCODING,
    )

# Suprime logs verbosos de bibliotecas subjacentes
logging.getLogger("docling").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

# Garante suporte a UTF-8 no console do Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def criar_conversor() -> DocumentConverter:
    """
    Instancia o DocumentConverter com aceleração por GPU (se disponível)
    e opções otimizadas para PDFs digitais (sem OCR desnecessário).
    """
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = DO_OCR
    pipeline_options.do_table_structure = DO_TABLE_STRUCTURE
    pipeline_options.generate_picture_images = GENERATE_PICTURE_IMAGES
    pipeline_options.accelerator_options.device = DEVICE
    pipeline_options.accelerator_options.num_threads = NUM_THREADS

    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )


def criar_chunker() -> HybridChunker:
    """
    Instancia o HybridChunker nativo do Docling com os hiperparâmetros
    padrão (default) da ferramenta, conforme decisão metodológica da pesquisa.
    """
    # Padrão nativo do Docling: tokenizer 'all-MiniLM-L6-v2' com max_tokens=256.
    # Caso deseje customizar o limite de tokens no futuro, utilize por exemplo:
    # return HybridChunker(max_tokens=512)
    return HybridChunker()


def contar_tokens(chunker: HybridChunker, texto: str) -> int:
    """Calcula a contagem precisa de tokens utilizando o tokenizer nativo do chunker."""
    try:
        if hasattr(chunker, "tokenizer") and hasattr(chunker.tokenizer, "count_tokens"):
            return chunker.tokenizer.count_tokens(texto)
    except Exception:
        pass
    # Fallback heurístico caso o tokenizer falhe pontualmente (1 token ~ 4 caracteres)
    return max(1, len(texto) // 4)


def processar_pdf(
    pdf_path: Path,
    caminho_saida: Path,
    converter: DocumentConverter,
    chunker: HybridChunker,
    force: bool = False
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Processa um único PDF:
    - Verifica cache incremental (pula se já existir e não for 'force')
    - Gera Markdown integral (<doc>.md)
    - Fatia o documento com HybridChunker preservando tabelas e seções
    - Salva chunks.json com metadados para RAG
    """
    nome_doc = pdf_path.stem
    pasta_doc = caminho_saida / nome_doc
    arquivo_chunks = pasta_doc / "chunks.json"
    arquivo_md = pasta_doc / f"{nome_doc}.md"

    # 1. Modo Incremental: verifica se já foi processado anteriormente
    if not force and arquivo_chunks.exists() and arquivo_md.exists():
        try:
            with open(arquivo_chunks, "r", encoding=JSON_ENCODING) as f:
                chunks_existentes = json.load(f)
            return {
                "nome": nome_doc,
                "status": "ignorado",
                "motivo": "ja_processado",
                "chunks": len(chunks_existentes)
            }, chunks_existentes
        except Exception:
            # Se o JSON estiver corrompido, reprocessa
            pass

    pasta_doc.mkdir(parents=True, exist_ok=True)

    # 2. Conversão via Docling
    result = converter.convert(str(pdf_path))

    # 3. Exportação do Markdown integral
    md_content = result.document.export_to_markdown()
    with open(arquivo_md, "w", encoding=MARKDOWN_ENCODING) as f:
        f.write(md_content)

    # 4. Segmentação Híbrida (Layout-Aware Chunking)
    chunks_doc = []
    docling_chunks = list(chunker.chunk(result.document))

    for idx, chunk in enumerate(docling_chunks):
        # Trilha hierárquica de seções pai
        headings = list(chunk.meta.headings) if chunk.meta.headings else []

        # Proveniência de páginas
        pages = sorted(list({
            prov.page_no
            for item in (chunk.meta.doc_items or [])
            for prov in (getattr(item, "prov", None) or [])
            if hasattr(prov, "page_no") and prov.page_no is not None
        }))

        chunk_record = {
            "chunk_id": f"{nome_doc}_chunk_{idx + 1:04d}",
            "documento": pdf_path.name,
            "text": chunk.text,
            "headings": headings,
            "pages": pages,
            "char_count": len(chunk.text),
            "token_count": contar_tokens(chunker, chunk.text)
        }
        chunks_doc.append(chunk_record)

    # 5. Salva dataset individual de chunks
    with open(arquivo_chunks, "w", encoding=JSON_ENCODING) as f:
        json.dump(chunks_doc, f, indent=2, ensure_ascii=False)

    return {
        "nome": nome_doc,
        "status": "processado",
        "chunks": len(chunks_doc)
    }, chunks_doc


def extrair_documentos(
    dir_entrada: Optional[Union[str, Path]] = None,
    dir_saida: Optional[Union[str, Path]] = None,
    force: bool = False
) -> Dict[str, Any]:
    """
    Processa todos os PDFs do diretório de entrada com suporte a processamento
    incremental e gera um índice consolidado de chunks para o Módulo 2.
    """
    caminho_entrada = Path(dir_entrada or DIR_ENTRADA_PADRAO).resolve()
    caminho_saida = Path(dir_saida or DIR_SAIDA_PADRAO).resolve()

    caminho_entrada.mkdir(parents=True, exist_ok=True)
    caminho_saida.mkdir(parents=True, exist_ok=True)

    arquivos_pdf = sorted(list(caminho_entrada.glob("*.pdf")))

    if not arquivos_pdf:
        print(f"⚠️  Nenhum arquivo PDF encontrado em: {caminho_entrada}")
        print(f"👉 Copie seus arquivos .pdf para '{caminho_entrada}' e execute novamente.")
        return {"processados": 0, "ignorados": 0, "falhas": 0, "total_chunks": 0}

    print(f"\n🚀 [MÓDULO 01 - EXTRAÇÃO & CHUNKING]")
    print(f"📂 Entrada:     {caminho_entrada}")
    print(f"📁 Saída:       {caminho_saida}")
    print(f"⚡ Dispositivo: {DEVICE.upper()} (Threads: {NUM_THREADS})")
    print(f"🔄 Modo:        {'Reprocessamento forçado (--force)' if force else 'Incremental (pula existentes)'}")
    print(f"📄 Documentos:  {len(arquivos_pdf)} arquivo(s) encontrado(s)\n")

    converter = criar_conversor()
    chunker = criar_chunker()

    estatisticas = {
        "processados": 0,
        "ignorados": 0,
        "falhas": 0,
        "total_chunks": 0,
        "documentos": []
    }
    todos_os_chunks = []

    pbar = tqdm(arquivos_pdf, desc="Processando PDFs", unit="doc")

    for pdf_path in pbar:
        nome_doc = pdf_path.stem
        pbar.set_postfix_str(f"{nome_doc[:25]}...")

        try:
            res_doc, chunks_doc = processar_pdf(
                pdf_path=pdf_path,
                caminho_saida=caminho_saida,
                converter=converter,
                chunker=chunker,
                force=force
            )

            if res_doc["status"] == "processado":
                estatisticas["processados"] += 1
            else:
                estatisticas["ignorados"] += 1

            estatisticas["total_chunks"] += len(chunks_doc)
            estatisticas["documentos"].append(res_doc)
            todos_os_chunks.extend(chunks_doc)

        except Exception as e:
            estatisticas["falhas"] += 1
            estatisticas["documentos"].append({
                "nome": nome_doc,
                "status": "falha",
                "erro": str(e)
            })
            tqdm.write(f"❌ Erro ao processar '{nome_doc}': {e}")

    # 6. Salva índice consolidado global reunindo todos os chunks
    arquivo_consolidado = caminho_saida / "indice_chunks_consolidado.json"
    with open(arquivo_consolidado, "w", encoding=JSON_ENCODING) as f:
        json.dump(todos_os_chunks, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print("📊 [MÓDULO 01] RESUMO DA EXTRAÇÃO E CHUNKING")
    print("=" * 60)
    print(f"✅ Documentos novos processados: {estatisticas['processados']}")
    print(f"⏭️  Documentos mantidos (cache):   {estatisticas['ignorados']}")
    if estatisticas["falhas"] > 0:
        print(f"❌ Falhas de processamento:     {estatisticas['falhas']}")
    print(f"🧩 Total de chunks no dataset:   {estatisticas['total_chunks']}")
    print(f"📦 Índice consolidado:           {arquivo_consolidado}")
    print("=" * 60 + "\n")

    return estatisticas


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Módulo 01: Extração e Chunking com Docling")
    parser.add_argument("--input", "-i", default=None, help="Diretório de entrada com os PDFs")
    parser.add_argument("--output", "-o", default=None, help="Diretório de saída para os resultados")
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Reprocessa todos os PDFs mesmo que já tenham sido extraídos anteriormente"
    )
    args = parser.parse_args()

    extrair_documentos(dir_entrada=args.input, dir_saida=args.output, force=args.force)
