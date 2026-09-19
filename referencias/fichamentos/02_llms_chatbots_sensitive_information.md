# 📄 Fichamento Bibliográfico 02

## 📌 Identificação da Obra
- **Título**: *Large Language Models for chatbot applications handling sensitive information*
- **Autores**: Hilário Tomaz Alves de Oliveira, Álvaro Alvares De Carvalho César Sobrinho, Andrey dos Reis Cadima Dias, André Magno Costa de Araújo, Rafael Dias Araújo, Diego Dermeval Medeiros da Cunha Matos, Sebastian Munoz-Najar Galvez
- **Instituições**: NEES/UFAL, IFES, UFAPE, UFU, Harvard University
- **Periódico**: *Expert Systems With Applications* (Elsevier), Volume 299, Artigo 130145, 2026. (Qualis A1)
- **Arquivo Local**: [`referencias/Large Language Models for Chatbot Applications Handling Sensitive Information.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Large%20Language%20Models%20for%20Chatbot%20Applications%20Handling%20Sensitive%20Information.pdf)
- **Área**: RAG, Chatbots, LGPD / Privacidade, NLP em Português do Brasil, Políticas Públicas.

---

## 🎯 Problema e Objetivo da Pesquisa
- **Problema**: Como projetar chatbots baseados em LLMs que sejam de **alto desempenho** e **baixo custo**, capazes de responder sobre documentos institucionais atualizados, mas garantindo **privacidade e conformidade com a LGPD** ao lidar com informações sensíveis ou proprietárias da administração pública.
- **Objetivo**: Propor uma arquitetura híbrida de RAG que combina modelos locais/offline (para garantir privacidade e retenção de dados) e modelos online eficientes (especializados em língua portuguesa), avaliando o impacto da variação de perguntas (paráfrases) e de ataques de injeção de prompt.

---

## 🔬 Metodologia e Datasets
- **Estudo de Caso**: Política pública educacional brasileira (Programa Nacional do Livro e do Material Didático - PNLD).
- **Corpus de Teste**: 591 pares de pergunta-resposta em **Português do Brasil**, extraídos de documentos oficiais institucionais.
- **Variação Linguística**: Geração de perguntas parafraseadas via GPT-4o-mini (com ~46% de diferença vocabular em relação às originais).
- **Modelos de Recuperação (Retrievers / Embeddings)**:
  - Esparsos: BM25
  - Densos: SBERT-MPNet, MiniLM-L12-v2, E5 Multilingual Large, OpenAI Embeddings (Small e Large).
- **Modelos Geradores (LLMs)**:
  - Nacionais / Especializados em PT-BR: **Sabiazinho-3** (Maritaca AI).
  - Família Llama 3: 1B, 3B, 8B (offline) e 70B (online).
  - Família Gemma 3: 1B, 4B e 12B (offline).
  - Raciocínio / Destilados: DeepSeek-R1-Distill-Llama-70B.
  - Abordagem Híbrida proposta: Gemma 3 12B (local) + Sabiazinho-3 (online).

---

## 📊 Métricas Utilizadas e Principais Achados

### 1. Métricas de Recuperação (Retrieval):
- **Recall@n** (para $n \in \{1, 3, 5, 10, 20\}$): Proporção de chunks relevantes recuperados.
- **Volume Médio de Tokens Recuperados** e **Estimativa de Custo em US$**.
- *Achado*: Perguntas parafraseadas causaram queda de desempenho em todos os modelos. O **OpenAI Large** e o **E5 Multilingual Large** foram os mais resilientes, enquanto BM25, MiniLM e MPNet sofreram quedas acentuadas.

### 2. Métricas de Geração Tradicionais:
- **ROUGE-L** e **BERTScore** (similaridade léxica e semântica com o gabarito).
- *Achado*: A estratégia híbrida atingiu BERTScore médio de **0,758**, cobrindo 96,67% das respostas.

### 3. Métricas de Avaliação via LLM-as-a-Judge (Framework RAGAS):
- **Faithfulness (Fidelidade / Aterramento)**: Avalia se a resposta gerada está estritamente contida nas evidências recuperadas (evita alucinação).
- **Answer Relevancy (Relevância)**: Avalia se a resposta atende à intenção da pergunta do usuário.
- **Answer Correctness (Exatidão)**: Mede a precisão factual em relação à resposta esperada.
- *Trade-off identificado*: O **Sabiazinho-3** destacou-se em relevância (0,780) e exatidão (0,636), sendo excelente em compreender o usuário em português. A abordagem **Híbrida (Gemma 3 12B + Sabiazinho-3)** obteve a maior fidelidade (**0,906 a 0,918**), essencial para o setor público.

### 4. Segurança e Robustez:
- Avaliação da capacidade de recusar perguntas fora de domínio e resistência a **Prompt Injections** (Sabiazinho-3 obteve 0 vulnerabilidades de injeção).

---

## ⚠️ Limitações e Gaps de Pesquisa (Oportunidades)
1. **Escopo Restrito de Variação Linguística**: O artigo testou apenas **um tipo** de variação (paráfrase sintática). Ele não explorou erros de digitação intencionais (*typos*), consultas truncadas por palavras-chave, nem variações extremas de formalidade/coloquialismo ou legibilidade complexa.
2. **Geração Semi-Manual do Corpus**: O dataset de 591 perguntas foi construído e curado com forte intervenção para aquele domínio específico, sem uma metodologia automatizada e agnóstica para geração em lote a partir de qualquer PDF complexo.
3. **Ausência de Documentos com Tabelas Pesadas e Múltiplos Anexos**: O foco foi em documentos institucionais predominantemente textuais, sem o desafio de cruzar tabelas orçamentárias e múltiplos editais/anexos (como ocorre em licitações).

---

## 💡 Como e Onde Citar Este Artigo no seu Mestrado (FUNDAMENTAL!)

Como este artigo é do seu orientador (**Prof. Dr. Hilário Tomaz Alves de Oliveira**) e publicado em periódico de ponta (**Expert Systems With Applications - A1**), ele deve ser uma das **referências centrais da sua dissertação**:

- **Na Introdução**:
  - Citar como evidência de que *sistemas RAG aplicados a políticas e documentos da administração pública brasileira exigem alto aterramento factual (Faithfulness) e conformidade com a LGPD* (Oliveira et al., 2026).
  - Citar que trabalhos recentes do grupo já demonstraram que variações em perguntas afetam a recuperação de documentos em português.

- **Na Seção de Trabalhos Relacionados**:
  - Dedicar uma subseção a Oliveira et al. (2026), detalhando sua arquitetura e resultados com o Sabiazinho-3 e RAGAS em dados educacionais brasileiros.

- **Na Metodologia (Defesa da sua Contribuição Científica)**:
  - **O seu trabalho avança diretamente o trabalho do Prof. Hilário**: Enquanto Oliveira et al. (2026) avaliaram o impacto de paráfrases em um conjunto estático, a sua dissertação propõe uma **metodologia automatizada para sintetizar e estressar datasets sob um espectro muito mais amplo de variações (as 4 dimensões de estilo e ruído)**.
  - Justificar a adoção do **framework RAGAS (Faithfulness, Relevancy, Correctness)** e das métricas **Recall@n** e **BERTScore**, herdando o rigor metodológico já validado pelo orientador.

- **Na Discussão de Resultados**:
  - Comparar se os comportamentos de queda de desempenho frente a ruídos observados na sua pesquisa corroboram os achados de Oliveira et al. (2026) frente a paráfrases.
