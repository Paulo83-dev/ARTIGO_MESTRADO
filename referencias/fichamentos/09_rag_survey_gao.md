# 📄 Fichamento Bibliográfico 09

## 📌 Identificação da Obra
- **Título**: *Retrieval-Augmented Generation for Large Language Models: A Survey*
- **Autores**: Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang e Haofen Wang
- **Instituição / Veículo**: Tongji University & Fudan University (Xangai, China) / IEEE Transactions on Knowledge and Data Engineering (TKDE) / arXiv:2312.10997 (2024)
- **Arquivo Local**: [`referencias/Retrieval-Augmented Generation for Large Language Models - A Survey.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Retrieval-Augmented%20Generation%20for%20Large%20Language%20Models%20-%20A%20Survey.pdf)
- **Área Temática**: Retrieval-Augmented Generation (RAG), Taxonomia de Paradigmas (Naive/Advanced/Modular), Chunking e Indexação Estrutural, Métricas e Frameworks de Avaliação de RAG.

---

## 🎯 Problema e Objetivo da Pesquisa
- **Problema Abordado**: Modelos de Linguagem de Grande Porte (LLMs) enfrentam vulnerabilidades críticas em ambientes de produção, como alucinação factual (*hallucination*), conhecimento desatualizado e processos de raciocínio opacos e não auditáveis. O RAG emergiu como solução primária ao acoplar bases externas de conhecimento, mas a literatura encontrava-se fragmentada entre abordagens ingênuas e arquiteturas avançadas.
- **Objetivo Principal**: Apresentar um levantamento (*survey*) sistemático e exaustivo sobre a evolução dos paradigmas de RAG (Naive RAG, Advanced RAG e Modular RAG), categorizando as técnicas de pré-recuperação (chunking e indexação), recuperação (densos, esparsos, multi-retrieval), pós-recuperação (re-ranking e compressão) e os frameworks e métricas formais para avaliação da qualidade de sistemas RAG.

---

## 🔬 Metodologia e Taxonomia do Survey
1. **Os Três Paradigmas de RAG**:
   - **Naive RAG**: Pipeline sequencial clássico (Indexar -> Recuperar -> Gerar). Sofre de baixa precisão na recuperação, alucinações e perda de contexto.
   - **Advanced RAG**: Introduz estratégias sofisticadas de pré-recuperação (Layout-Aware Chunking, expansão de metadados, query rewriting) e pós-recuperação (re-ranking e síntese de contexto).
   - **Modular RAG**: Arquitetura flexível com módulos intercambiáveis (mecanismos de roteamento de query, busca iterativa/recursiva e validação reflexiva).
2. **Diretrizes Críticas de Pré-Recuperação (Seção III-A, pág. 8-9)**:
   - **Chunking Strategy**: Aponta que fatiar textos por número fixo de tokens (ex: 100, 256, 512) gera truncamento dentro de frases (*truncation within sentences*), falhando no equilíbrio entre completude semântica e contexto;
   - **Metadata Attachments**: Defende que os chunks devem ser enriquecidos com metadados estruturais (número de página, nome do arquivo, caminho hierárquico e autor) para limitar o escopo da busca e garantir rastreabilidade;
   - **Structural Index**: Enfatiza que documentos semiestruturados (como relatórios e editais com tabelas) sofrem severamente com cortes arbitrários de texto, exigindo índices hierárquicos que mantenham as relações pai-filho entre seções e suas respectivas tabelas.
3. **Métricas e Avaliação de RAG (Seção V, pág. 14-16)**:
   - Sistematiza a tríade essencial de avaliação (amplamente adotada pelo framework **RAGAS**):
     - **Relevância de Contexto (*Context Relevance*)**: Se os chunks recuperados são estritamente necessários para responder à pergunta.
     - **Fidelidade (*Faithfulness / Groundedness*)**: Se a resposta gerada é 100% ancorada no contexto recuperado (ausência de alucinação).
     - **Relevância da Resposta (*Answer Relevance*)**: Se a resposta atende diretamente ao que foi demandado na consulta do usuário.

---

## 📊 Principais Resultados e Consensos da Literatura
- **Superioridade do Chunking Ciente de Estrutura**: Modelos que incorporam fronteiras lógicas de seções e tabelas reduzem substancialmente o ruído na fase de recuperação em comparação com divisões baseadas apenas em contagem bruta de caracteres.
- **Vulnerabilidade do Gerador a Ruídos de Recuperação**: Contextos irrelevantes ou desordenados degradam a fidelidade do gerador, mesmo quando utilizados LLMs de grande porte (como GPT-4).
- **Consolidação dos Frameworks de Benchmarking**: Consolidação do RAGAS, ARES e TruLens como os padrões da indústria para aferir qualidade ponta a ponta.

---

## ⚠️ Limitações e Gaps Identificados
- **Falta de Robustez a Variações do Usuário no Mundo Real**: O levantamento aponta que a imensa maioria dos benchmarks avalia o RAG sobre perguntas sintéticas e bem formuladas, havendo uma lacuna crítica na literatura quanto ao comportamento dos sistemas diante de consultas com variações de estilo, ruídos, erros gramaticais e diferentes registros de formalidade (*lacuna exata que o seu mestrado investiga no Português do Brasil!*).

---

## 💡 Como e Onde Citar no Artigo de Mestrado

- **Na Introdução (Motivação do RAG e Riscos de Fragilidade)**:
  > *"Embora o paradigma de Geração Aumentada por Recuperação (RAG) tenha se consolidado como a principal estratégia para mitigar alucinações e integrar conhecimento factual a Modelos de Linguagem de Grande Porte (Gao et al., 2024), a literatura recente ainda carece de análises aprofundadas sobre a fragilidade desses sistemas sob variações linguísticas do usuário no mundo real."*

- **Nos Trabalhos Relacionados (Classificação do Pipeline)**:
  > *"Seguindo a taxonomia proposta no survey seminal de Gao et al. (2024), este trabalho situa-se no paradigma do Advanced RAG, implementando mecanismos estruturais de pré-recuperação e controles formais de avaliação da fidelidade e relevância."*

- **Na Metodologia (Justificativa Teórica do Chunking)**:
  > *"A opção pelo fatiamento estrutural (Layout-Aware) fundamenta-se nas recomendações de Gao et al. (2024), os quais demonstram que divisões cegas por limites fixos de caracteres introduzem truncamentos intrafrasais e fragmentam tabelas, corrompendo a semântica da recuperação. Portanto, os chunks deste trabalho preservam a integridade de parágrafos e tabelas, incorporando metadados hierárquicos e páginas de proveniência."*

- **Na Seleção de Métricas de Avaliação**:
  > *"A auditoria da qualidade do dataset e das respostas fundamenta-se nas três dimensões centrais categorizadas por Gao et al. (2024): relevância do contexto recuperado, fidelidade factual ao texto de origem (faithfulness) e relevância da resposta em relação à consulta do usuário."*
