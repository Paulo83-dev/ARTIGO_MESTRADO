# 📄 Fichamento Bibliográfico 08

## 📌 Identificação da Obra
- **Título**: *Docling Technical Report* (Version 1.0)
- **Autores**: Christoph Auer, Maksym Lysak, Ahmed Nassar, Michele Dolfi, Nikolaos Livathinos, Panos Vagenas, Cesar Berrospi Ramis, Matteo Omenetti, Fabian Lindlbauer, Kasper Dinkla, Lokesh Mishra, Yusik Kim, Shubham Gupta, Rafael Teixeira de Lima, Valery Weber, Lucas Morin, Ingmar Meijer, Viktor Kuropiatnyk e Peter W. J. Staar
- **Instituição / Veículo**: IBM Research (AI4K Group, Rüschlikon, Suíça) / Relatório Técnico (arXiv:2408.09869, 2024)
- **Arquivo Local**: [`referencias/Docling Technical Report.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Docling%20Technical%20Report.pdf)
- **Área Temática**: Processamento de Documentos Multimodais, Layout Analysis, Table Structure Recognition, Preparação de Dados para RAG.

---

## 🎯 Problema e Objetivo da Pesquisa
- **Problema Abordado**: A conversão de documentos complexos em PDF para formatos processáveis por máquina (Markdown/JSON) é um dos maiores gargalos da IA moderna. PDFs descartam a estrutura lógica subjacente (hierarquia de seções, metadados, colunas e tabelas) em favor da fidelidade gráfica para impressão. Parsers convencionais baseados em extração cega de texto quebram a ordem de leitura, destroem a malha de tabelas e misturam colunas paralelas.
- **Objetivo Principal**: Apresentar o **Docling**, um pacote open-source autossuficiente e eficiente para converter PDFs em representações estruturadas e tipadas (`DoclingDocument`), combinando modelos especializados de aprendizado profundo (visão computacional) para segmentação de layout (**DocLayNet**) e reconstrução de tabelas (**TableFormer**) operando eficientemente em hardware de consumo (commodity hardware).

---

## 🔬 Metodologia e Datasets
1. **Pipeline em Camadas**:
   - **Camada Vetorial / Programática**: Extrai os caracteres nativos, posições espaciais e fontes via parsers vetoriais (`pypdfium2`).
   - **Visão Computacional para Layout (DocLayNet)**: Aplica detectores de objetos neurais treinados sobre o dataset DocLayNet para identificar classes visuais: `Title`, `Section-header`, `Text`, `Table`, `Picture`, `Caption`, `List-item`, `Page-header` e `Page-footer`.
   - **Reconhecimento de Estrutura de Tabelas (TableFormer)**: Vision-Transformer especializado treinado com vocabulário de tokens estruturais. Ele recebe a região da tabela e prediz a topologia completa de linhas, colunas, células mescladas (*spanning cells*) e cabeçalhos de coluna/linha.
   - **Montagem do `DoclingDocument`**: Fusão dos tokens de texto com as caixas delimitadoras inferidas para restaurar a ordem de leitura lógica e a árvore hierárquica do documento.
2. **Chunking Híbrido (`HybridChunker`)**:
   - Chunker nativo focado em RAG que respeita as unidades atômicas do documento (parágrafos, tópicos e tabelas), acoplando os cabeçalhos pai (*headings*) e números de página diretamente nos metadados de cada bloco, evitando truncamentos secos.

---

## 📊 Métricas e Principais Resultados
- **Desempenho de Detecção de Layout**: Avaliado via *Mean Average Precision* (mAP@0.5-0.95 no padrão COCO). No DocLayNet, modelos como YOLOv5x6 e Faster R-CNN atingiram precisões elevadas na detecção de tabelas e textos (> 82 mAP).
- **Tempo de Processamento**: Processamento de tabelas complexas pelo TableFormer dura entre 2 a 6 segundos por tabela em CPU. O pipeline completo opera de forma ordens de grandeza mais rápida quando comparado a Modelos de Visão de Grande Porte (VLMs) multimodais fechados.
- **Respeito à Malha Tabular**: O modelo recupera tabelas sem bordas, com células vazias e com múltiplos níveis de cabeçalho, exportando com precisão para Markdown, JSON e DataFrames (CSV).

---

## ⚠️ Limitações e Gaps Identificados
- **Custo Computacional do OCR**: Quando acionado em PDFs digitalizados/escaneados, o EasyOCR demanda bastante processamento e VRAM (o que justifica a decisão do nosso projeto de utilizar PDFs nativos com `do_ocr = False` na RTX 2050).
- **Equações Matemáticas e Figuras Complexas**: O relatório admite que a classificação fina de tipos de figuras e fórmulas matemáticas inline ainda são trabalhos em expansão na ferramenta.

---

## 💡 Como e Onde Citar no Artigo de Mestrado

- **Na Metodologia (Módulo 01 - Pré-processamento e Extração)**:
  > *"Para a ingestão e estruturação dos editais de licitação, adotou-se o framework Docling (Auer et al., 2024). A ferramenta combina a camada textual vetorial com o detector de layout DocLayNet e o modelo TableFormer para reconhecimento da topologia tabular, garantindo que cronogramas físico-financeiros e planilhas orçamentárias sejam convertidos com preservação íntegra de suas malhas de linhas e colunas."*

- **Na Justificativa de Chunking (Metodologia)**:
  > *"A segmentação textual dispensou o corte rígido por janela deslizante e empregou o HybridChunker nativo do Docling (Auer et al., 2024). Essa abordagem preserva as fronteiras naturais de cláusulas e tabelas, injetando metadados de proveniência (páginas de origem e hierarquia de seções) essenciais para a composição do gabarito (Ground Truth) de avaliação do RAG."*

- **Nos Trabalhos Relacionados**:
  > *"Enquanto parsers convencionais tratam documentos como fluxos planos de caracteres desprovidos de semântica espacial, soluções orientadas a layout como o Docling (Auer et al., 2024) restabelecem a hierarquia visual do autor, elemento crítico para que sistemas de recuperação não sofram com ruídos decorrentes de quebra incorreta de contexto."*
