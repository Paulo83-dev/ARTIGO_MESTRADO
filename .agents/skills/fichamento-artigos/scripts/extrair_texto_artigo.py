"""
Script auxiliar para extrair texto e metadados de artigos científicos em PDF
para apoiar a geração automática de fichamentos bibliográficos.
"""

import sys
import json
from pathlib import Path

# Suporte a UTF-8 no Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def extrair_secoes_artigo(caminho_pdf: str, max_paginas: int = 10) -> dict:
    """Extrai texto e estrutura inicial do artigo para leitura pelo agente."""
    import pypdf

    pdf_path = Path(caminho_pdf).resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

    reader = pypdf.PdfReader(str(pdf_path))
    total_paginas = len(reader.pages)

    paginas_texto = []
    limite = min(max_paginas, total_paginas)

    for i in range(limite):
        texto = reader.pages[i].extract_text() or ""
        paginas_texto.append({
            "pagina": i + 1,
            "texto": texto
        })

    # Metadados do PDF se existirem
    meta = reader.metadata or {}
    metadados = {
        "titulo": meta.get("/Title", "") or pdf_path.stem,
        "autor": meta.get("/Author", ""),
        "total_paginas": total_paginas,
        "arquivo": pdf_path.name
    }

    return {
        "metadados": metadados,
        "paginas": paginas_texto
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python extrair_texto_artigo.py <caminho_do_pdf>")
        sys.exit(1)

    caminho = sys.argv[1]
    resultado = extrair_secoes_artigo(caminho)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
