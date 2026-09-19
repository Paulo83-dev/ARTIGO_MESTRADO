# 📄 Fichamento Bibliográfico 04

## 📌 Identificação da Obra
- **Título**: *Improving Consistency in Retrieval-Augmented Systems with Group Similarity Rewards* (**Con-RAG**)
- **Autores**: Faisal Hamman, Chenyang Zhu, Anoop Kumar, Xujun Peng, Sanghamitra Dutta, Daben Liu, Alfy Samuel
- **Instituições**: University of Maryland (College Park) e Capital One
- **Ano**: 2025 / 2026
- **Arquivo Local**: [`referencias/Improving Consistency in Retrieval Augmented Systems with Group Similarity Rewards.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Improving%20Consistency%20in%20Retrieval%20Augmented%20Systems%20with%20Group%20Similarity%20Rewards.pdf)
- **Área**: RAG Robustness, Consistência de Informação, Métricas de Avaliação, Aprendizado por Reforço (GRPO).

---

## 🎯 Problema e Objetivo da Pesquisa
- **Problema**: Em domínios de alta criticidade (jurídico, financeiro, administração pública e saúde), os usuários esperam que um RAG seja **consistente**: se duas pessoas fizerem a mesma pergunta de maneiras diferentes (ex: uma formal e outra informal), o sistema deve entregar o **mesmo conteúdo factual essencial**. No entanto, pequenas variações na pergunta frequentemente fazem o buscador trazer documentos diferentes, levando o LLM a dar respostas divergentes ou contraditórias.
- **Objetivo**: 
  1. Criar um **framework formal para medir a consistência** em sistemas RAG, decompondo a inconsistência em três níveis: no buscador (*Retriever*), no gerador (*LLM*) e de ponta a ponta (*End-to-End*).
  2. Propor o **Con-RAG**, uma abordagem que treina o sistema para manter a consistência de informação entre grupos de perguntas equivalentes.

---

## 🔬 Conceito Chave: Consistência Lexical vs. Consistência de Informação
- **Consistência Lexical (Superficial)**: Exigir que as respostas usem as mesmas palavras exatas. (Muito rígida e indesejada, pois penaliza sinônimos naturais).
- **Consistência de Informação (Semântica e Factual)**: O que realmente importa! Exige que o **núcleo de fatos e orientações seja idêntico**, mesmo que redigido com palavras diferentes.

---

## 📊 As Métricas Formais de Consistência (Ouro para a sua Dissertação!)

Este artigo resolve com elegância matemática a sua dúvida sobre **quais métricas usar para avaliar as variações de perguntas**:

### 1. Consistência do Recuperador ($C_{\text{ret}}$ - Jaccard Index)
Mede se o buscador traz os mesmos documentos quando a pergunta varia de estilo:
$$C_{\text{ret}}(q_0) = \frac{2}{n(n-1)} \sum_{i < j} \frac{|R(p_i) \cap R(p_j)|}{|R(p_i) \cup R(p_j)|}$$
- **O que significa na prática**: Se para a pergunta original e para a pergunta com gíria o buscador trouxe os mesmos trechos do edital, o índice de Jaccard é 1.0 (perfeito). Se trouxe documentos totalmente diferentes, o índice cai para perto de 0.

### 2. Consistência do Gerador / LLM ($C_{\text{LLM}}$)
Fixa os mesmos documentos e muda apenas a pergunta para o LLM. Mede se a inconsistência é culpa do LLM que se confundiu com o estilo da pergunta, ou se foi culpa do buscador.

### 3. Consistência Fim a Fim ($C_{\text{gen}}$ - End-to-End Information Consistency)
Mede a concordância factual entre todas as respostas geradas para a família de perguntas:
$$C_{\text{gen}}(q_0) = \frac{1}{n(n-1)} \sum_{i \neq j} \text{sim}(y_i, y_j)$$
Calculada via **Similaridade Semântica (BERTScore)** ou via **LLM-as-a-Judge** (perguntando a um juiz se as respostas $y_i$ e $y_j$ concordam entre si ou se contradizem).

---

## 💡 Como e Onde Citar Este Artigo no seu Artigo de Mestrado:

Este artigo é a peça que faltava para fechar a seção de **Métricas de Avaliação**:

- **Na Introdução**:
  - Citar Hamman et al. (2025/2026) para justificar a gravidade da inconsistência em RAGs no setor público: *em licitações públicas, fornecer respostas divergentes para perguntas semanticamente equivalentes gera quebra de isonomia, insegurança jurídica e riscos regulatórios*.
- **No Módulo 04 (Métricas de Avaliação do Dataset)**:
  - **Adotar formalmente as métricas de Hamman et al.**:
    1. Usar a métrica de **Similaridade de Jaccard no Retriever** para medir o impacto das suas 4 dimensões de estilo/ruído na recuperação de trechos do Edital.
    2. Usar a **Consistência de Informação Fim a Fim** para avaliar se o RAG mantém o mesmo parecer factual quando a consulta sofre variações.
- **Na Discussão Metodológica**:
  - Defender a importância de diferenciar *Consistência Léxica* de *Consistência de Informação*, explicando que seu benchmark foca na preservação factual dos direitos e prazos da licitação.
