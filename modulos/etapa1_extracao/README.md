# 📑 Módulo 01: Extração e Chunking Estrutural de Documentos

Este módulo é responsável por ingerir os editais e documentos de licitação em formato PDF, convertendo-os em unidades estruturadas de informação com rastreabilidade completa para o pipeline de avaliação de RAG.

---

## 🔬 Fundamentação Metodológica

Em vez de fatiar os documentos por contagens cegas de tamanho fixo com sobreposição (*fixed-size sliding window*), este projeto adota uma abordagem de **Layout-Aware Chunking** viabilizada nativamente pelo **Docling (Auer et al., 2024)**.

Conforme demonstrado no levantamento de **Gao et al. (2024)** (*Retrieval-Augmented Generation for Large Language Models: A Survey*):
1. **Truncamento Intrafrasal**: Divisões cegas por número fixo de caracteres ou tokens quebram frases no meio e separam linhas de tabelas, corrompendo a recuperação semântica;
2. **Equilíbrio Semântico**: O `HybridChunker` do Docling preserva a integridade de parágrafos, tópicos e tabelas completas, respeitando as fronteiras semânticas naturais do autor;
3. **Hiperparâmetros Padrão**: Conforme aprovado pela orientação, adota-se a configuração *default* do `HybridChunker` (tokenizer fast baseado em *MiniLM-L6-v2* com teto de 256 tokens para chunking denso), garantindo reprodutibilidade científica sem dependência de valores arbitrários.

---

## ⚡ Otimização de Hardware (RTX 2050 4 GB)

- **Aceleração por GPU (`CUDA`)**: Os modelos de segmentação de layout (**DocLayNet**) e reconstrução de tabelas (**TableFormer**) rodam com aceleração por GPU.
- **`do_ocr = False`**: Como o escopo prioriza PDFs nativos digitais (texto vetorial selecionável), o OCR fica desligado, economizando VRAM e eliminando riscos de estouro de memória (*Out of Memory - OOM*).
- **Processamento Incremental**: PDFs que já possuem seus chunks extraídos são detectados e ignorados automaticamente, poupando minutos de reprocessamento desnecessário.

---

## 📂 Entradas e Saídas

- **Entrada**: `dados/01_brutos/*.pdf`
- **Saídas**:
  - `dados/02_chunks/<nome_documento>/<nome_documento>.md`: Texto integral em Markdown estruturado para inspeção humana.
  - `dados/02_chunks/<nome_documento>/chunks.json`: Dataset dos chunks com metadados do documento.
  - `dados/02_chunks/indice_chunks_consolidado.json`: Índice global acumulando todos os chunks de todos os documentos processados (pronto para alimentar o Módulo 02).

### Estrutura do `chunks.json` (Contrato com o Módulo 2)
```json
[
  {
    "chunk_id": "edital_pregao_01_chunk_0001",
    "documento": "edital_pregao_01.pdf",
    "text": "### 5. DA HABILITAÇÃO TÉCNICA\nAs licitantes deverão comprovar...",
    "headings": [
      "5. DAS CONDIÇÕES DE PARTICIPAÇÃO",
      "5.1 Da Habilitação Técnica"
    ],
    "pages": [14, 15],
    "char_count": 1280,
    "token_count": 242
  }
]
```

---

## 🚀 Como Executar

### 1. Execução padrão (Incremental)
Processa apenas os PDFs que ainda não foram extraídos:
```bash
python modulos/etapa1_extracao/extrator.py
```
ou através do orquestrador principal:
```bash
python executar_pipeline.py -m 1
```

### 2. Forçar reprocessamento de tudo (`--force` / `-f`)
```bash
python modulos/etapa1_extracao/extrator.py --force
# ou
python executar_pipeline.py -m 1 -f
```

### 3. Diretórios customizados
```bash
python modulos/etapa1_extracao/extrator.py --input "meus_editais" --output "minha_saida"
```

---

## ⚠️ Observações Empíricas e Limitações Conhecidas

- **Tabelas Inseridas como Imagem/Bitmap**:
  - Em documentos técnicos e planos de negócios (ex: `Produto 05 - Plano de Negócios.pdf`), algumas tabelas são coladas no documento original como figuras rasterizadas (capturas de tela/imagens) em vez de tabelas vetoriais nativas.
  - Como a configuração padrão atual opera com `DO_OCR = False` (para priorizar velocidade e evitar sobrecarga de VRAM na RTX 2050), o Docling classifica essas regiões visuais como figuras (`PictureItem`), capturando apenas legendas de texto adjacentes (ex: *"Tabela 12 Resumo - Avaliação econômico-financeira"*), mas não extrai os dados numéricos internos das células.
  - **Tratamento Futuro**: Caso seja indispensável recuperar dados dessas tabelas específicas para a geração de perguntas do benchmark, basta ativar temporariamente `DO_OCR = True` em `config.py` e forçar o reprocessamento do documento (`--force`).
