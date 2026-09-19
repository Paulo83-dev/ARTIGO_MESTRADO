# 📌 CHECKPOINT DO PROJETO - ARTIGO DE MESTRADO
**Data da última atualização**: 19 de Setembro de 2026  
**Objetivo do Documento**: Ponto de restauração para retomar o desenvolvimento em uma nova sessão sem sobrecarga de contexto.

---

## 🚦 Status Atual dos Módulos

| Módulo | Descrição | Status | O que foi entregue / Arquivos Chave |
| :--- | :--- | :---: | :--- |
| **01. Extração & Chunking** | Ingestão com Docling + HybridChunker | **✅ CONCLUÍDO E VALIDADO** | [`extrator.py`](file:///c:/Users/paulo/OneDrive/Área de Trabalho/Cursos e Educação/ARTIGO MESTRADO/modulos/etapa1_extracao/extrator.py), [`config.py`](file:///c:/Users/paulo/OneDrive/Área de Trabalho/Cursos e Educação/ARTIGO MESTRADO/modulos/etapa1_extracao/config.py) |
| **02. QA Base (Ground Truth)** | Síntese de perguntas canônicas via LLM | **🟡 PRÓXIMA ETAPA** | [`prompts.py`](file:///c:/Users/paulo/OneDrive/Área de Trabalho/Cursos e Educação/ARTIGO MESTRADO/modulos/etapa2_geracao_qa/prompts.py) |
| **03. Estilos & Ruídos** | Injeção de 4 perturbações linguísticas | ⚪ Aguardando Módulo 2 | [`prompts_estilos.py`](file:///c:/Users/paulo/OneDrive/Área de Trabalho/Cursos e Educação/ARTIGO MESTRADO/modulos/etapa3_estilos_ruidos/prompts_estilos.py) |
| **04. Auditoria Semântica** | Filtro de qualidade e desvio semântico | ⚪ Aguardando Módulo 3 | [`modulos/etapa4_avaliacao/`](file:///c:/Users/paulo/OneDrive/Área de Trabalho/Cursos e Educação/ARTIGO MESTRADO/modulos/etapa4_avaliacao/) |

---

## 🎯 Resumo do Módulo 01 (O que está pronto e funcionando)
* **Validação Real**: Testado com sucesso no edital real `Edital_782_2025_SEA.pdf` (gerou **175 chunks** enriquecidos em apenas **17 segundos** usando GPU CUDA na RTX 2050).
* **Decisões Técnicas Consolidadas**:
  1. **Chunking Ciente de Layout**: `HybridChunker` padrão do Docling (amparado por Gao et al., 2024 e Auer et al., 2024, com aval da orientação).
  2. **Hardware**: GPU ativa (`CUDA`), `DO_OCR = False` (PDFs nativos digitais sem risco de estourar os 4 GB de VRAM), `GENERATE_PICTURE_IMAGES = False` (foco em texto e tabelas para RAG).
  3. **Processamento Incremental**: Pula arquivos já processados instantaneamente. Suporta `--force` (`-f`) para reprocessar se necessário.
* **Entregáveis Gerados em `dados/02_chunks/`**:
  * `<documento>.md`: Texto completo estruturado em Markdown.
  * `<documento>/chunks.json`: Lista de chunks com `chunk_id`, `documento`, `text`, `headings`, `pages`, `char_count`, `token_count`.
  * `indice_chunks_consolidado.json`: Índice global acumulando todos os chunks de todos os documentos para fácil leitura do Módulo 02.

---

## 📚 Base Teórica e Fichamentos Catalogados
Localização: [`referencias/fichamentos/`](file:///c:/Users/paulo/OneDrive/Área de Trabalho/Cursos e Educação/ARTIGO MESTRADO/referencias/fichamentos/) (Total de **9 obras fichadas** e catalogadas no `README.md`):
* **Ficha 01**: *Out of Style: RAG’s Fragility to Linguistic Variation* (Base das 4 dimensões de ruído).
* **Ficha 02**: *LLMs for chatbot applications handling sensitive information* (Obra do orientador Prof. Hilário).
* **Ficha 03**: *Domain-Specific Data Generation Framework for RAG Adaptation* (RAGen - Taxonomia de Bloom).
* **Ficha 04**: *Con-RAG* (Métricas de consistência e estabilidade).
* **Ficha 05**: *Addressing Semantic Drift in Question Generation* (Desvio semântico).
* **Ficha 06**: *Improving Robustness of QA Systems to Paraphrasing* (Fragilidade a paráfrases).
* **Ficha 07**: *Investigating Robustness of RAG at Query Level* (Estudo empírico de ruídos e typos).
* **Ficha 08**: *Docling Technical Report* (IBM Research - Layout-Aware Parsing e TableFormer).
* **Ficha 09**: *Retrieval-Augmented Generation for LLMs: A Survey* (IEEE TKDE - Gao et al., 2024).

---

## ⚠️ Observações Empíricas dos Documentos do Corpus
* **Tabelas como Imagem no `Produto 05 - Plano de Negócios.pdf`**:
  * No chunk `chunk_0121`, observou-se a presença do texto *"Tabela 12 Resumo - Avaliação econômico-financeira"*, mas os dados internos da tabela não viraram colunas/linhas porque foram colados no PDF original como uma **imagem estática (bitmap)**.
  * Como o pipeline opera com `DO_OCR = False`, o Docling lê o texto da legenda mas ignora o conteúdo gráfico da figura.
  * **Ação Futura (se necessário)**: Se essas tabelas de planos de negócios forem indispensáveis para o Ground Truth, podemos rodar pontualmente esse PDF com `DO_OCR = True`.

---

## 🚀 Próximos Passos (Para a Próxima Sessão - Módulo 02)

O objetivo da próxima sessão será construir o **Módulo 02: Geração de Perguntas e Respostas Padrão-Ouro (Ground Truth)**.

### Itens a Desenvolver:
1. **Definição do Provedor de LLM**: Escolher qual API será usada para sintetizar as perguntas (ex: OpenAI, Anthropic, Google Gemini, Groq ou modelo local Ollama).
2. **Estratégia de Amostragem de Chunks**:
   - Processar todos os chunks do `indice_chunks_consolidado.json` ou fazer uma amostragem estratificada (por seções do edital, tabelas, etc.)?
   - Quantas perguntas/respostas gerar por edital (ex: 50, 100, 200)?
3. **Script Gerador (`gerador_qa.py`)**:
   - Ler os chunks do `indice_chunks_consolidado.json`.
   - Chamar o LLM usando o template em `modulos/etapa2_geracao_qa/prompts.py`.
   - Extrair e validar o JSON estruturado (`pergunta_original`, `resposta_esperada`, `tipo_pergunta`, `trecho_evidencia`, `metadados`).
   - Salvar o gabarito final em `dados/03_qa_base/qa_base.json`.

---

## 💬 Mensagem para Iniciar a Próxima Sessão:
> *"Olá! Leia o arquivo `CHECKPOINT.md` para resgatar o contexto essencial do projeto. O Módulo 01 já está concluído e validado. Vamos trabalhar hoje no Módulo 02 (Geração de QA Base / Ground Truth)."*
