# 📄 Fichamento Bibliográfico 07

## 📌 Identificação da Obra
- **Título**: *Investigating the Robustness of Retrieval-Augmented Generation at the Query Level*
- **Autores**: Sezen Perçin, Xin Su, Qutub Sha Syed, Phillip Howard, Aleksei Kuvshinov, Leo Schwinn, Kay-Ulrich Scholl
- **Instituições**: Technical University of Munich (TUM), Intel Labs e Thoughtworks
- **Ano**: 2024 / 2025
- **Arquivo Local**: [`referencias/Investigating the Robustness of Retrieval-Augmented Generation at the Query Level.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Investigating%20the%20Robustness%20of%20Retrieval-Augmented%20Generation%20at%20the%20Query%20Level.pdf)
- **Área**: Robustez de RAG, Perturbações no Nível da Consulta (*Query-Level*), Avaliação Comparativa de Retrievers e LLMs.

---

## 🎯 Problema e Objetivo da Pesquisa
- **O Problema da Dependência da Consulta**: Quase todos os benchmarks de RAG avaliam o sistema assumindo perguntas perfeitamente formuladas. No entanto, o desempenho do RAG é criticamente dependente da forma como o usuário expressa sua dúvida. Pequenas variações ortográficas, prolixidade ou formalidade excessiva podem desestabilizar o buscador (*retriever*), o gerador (*LLM*) ou ambos em efeito cascata.
- **Objetivo**: Conduzir um estudo empírico exaustivo (com mais de **1.092 experimentos**) para **desacoplar as sensibilidades** de cada módulo do RAG, medindo o impacto isolado e combinado de 4 tipos de perturbações frequentes na vida real.

---

## 🔬 As 4 Perturbações no Nível da Consulta (*Query-Level*)

Os autores aplicam 5 amostras perturbadas para cada pergunta original:

1. **Erros de Digitação (*Typo Insertion* - 10% e 25%)**:
   - Inserção de erros ortográficos baseados na proximidade de teclas no teclado QWERTY (usando a biblioteca *TextAttack*).
   - Simula a digitação rápida no celular ou teclado de usuários comuns.
2. **Informação Redundante (*Redundant Information / Prolixidade*)**:
   - Adiciona preâmbulos longos, contexto excessivo e detalhes desnecessários à pergunta.
3. **Tom Formal (*Formal Tone*)**:
   - Reescreve a pergunta com linguagem formal, rebuscada e cerimoniosa.
4. **Ambiguidade (*Ambiguity*)**:
   - Induz termos polissêmicos ou generalizações que tornam a busca mais difusa.

---

## 📊 Principais Descobertas e Métricas (Mais de 1.000 Experimentos!)

### 1. Métricas Utilizadas:
- **No Retriever**: **Recall@k** (com $k \in \{1, 3, 5, 10, 20\}$).
- **No Gerador e Fim a Fim**: **Match (Exact Match de Span)** (avaliação determinística sem viés de LLM).

### 2. O Grande Duelo: Recuperadores Densos (Embeddings) vs. Esparsos (BM25):
- **Diante de Prolixidade (Informações Redundantes)**: Os modelos densos (embeddings) são muito mais resilientes do que o BM25, pois capturam o significado global mesmo com palavras extras.
- **Diante de Typos (Erros de Digitação)**: O BM25 foi surpreendentemente mais tolerante em níveis moderados, enquanto alguns modelos de embeddings quebraram severamente porque erros de digitação fragmentam as palavras em sub-tokens desconhecidos no vocabulário do tokenizer.
- **Tom Formal**: Teve o menor impacto negativo em ambos os modelos.
- **Typos a 25%**: Foi a perturbação mais destrutiva em todos os 12 pipelines avaliados.

---

## 💡 Como e Onde Citar Este Artigo no seu Artigo de Mestrado:

Este artigo da TUM e Intel Labs é o **complemento experimental perfeito** para o seu trabalho:

- **Na Introdução e Motivação**:
  - Citar Perçin et al. (2024/2025) para justificar a necessidade de avaliar RAGs **especificamente no nível da consulta (*Query Level*)**, argumentando que a sensibilidade da busca a pequenos ruídos é o principal calcanhar de Aquiles de aplicações corporativas e públicas.
  - Citar a estatística dos 1.092 experimentos como evidência de que a comunidade científica internacional considera a robustez a nível de query um problema aberto urgente.

- **No Módulo 03 (Estilos e Ruídos) e Módulo 04 (Avaliação)**:
  - **Justificar a escolha dos Typos a 10% e 25%**: Citar a metodologia de Perçin et al. para fundamentar a injeção determinística de erros de teclado nos prompts de ruído do seu pipeline.
  - **Adotar a estratégia de desacoplamento**: No seu experimento, avaliar a robustez primeiro no Retriever (Recall@k) e depois na Geração (Ragas/Fidelidade), mostrando exatamente em qual ponto o sistema de licitações públicas começa a falhar.

- **Na Discussão dos Resultados**:
  - Comparar se os seus resultados no Português do Brasil com o Docling e embeddings multilíngues (ou BM25) confirmam a tese de Perçin et al. sobre o comportamento divergente de buscas densas vs. esparsas diante de ruído.
