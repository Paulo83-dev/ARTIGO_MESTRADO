# 📄 Fichamento Bibliográfico 05

## 📌 Identificação da Obra
- **Título**: *Addressing Semantic Drift in Question Generation for Semi-Supervised Question Answering*
- **Autores**: Shiyue Zhang e Mohit Bansal
- **Instituição**: University of North Carolina at Chapel Hill (UNC Chapel Hill)
- **Publicação**: *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP 2019)*, páginas 2495–2509. (Qualis A1 / Uma das principais conferências mundiais de NLP)
- **Arquivo Local**: [`referencias/Addressing Semantic Drift in Question Generation for Semi-Supervised Question Answering.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Addressing%20Semantic%20Drift%20in%20Question%20Generation%20for%20Semi-Supervised%20Question%20Answering.pdf)
- **Área**: Question Generation (QG), Desvio Semântico (Semantic Drift), Filtragem de Dados Sintéticos, Data Augmentation.

---

## 🎯 Problema e Objetivo da Pesquisa
- **O Problema do Desvio Semântico (*Semantic Drift*)**: Modelos automáticos de geração de perguntas (QG) frequentemente sofrem de desvio semântico: a pergunta gerada se afasta do contexto e da resposta alvo, passando a perguntar sobre fatos não contidos no texto, invertendo premissas lógicas ou tornando-se sem resposta (*unanswerable*).
- **O Risco dos Dados Sintéticos Sem Filtro**: Os autores provam que **jogar dados sintéticos sem filtro no dataset piora o desempenho dos modelos**, pois os exemplos ruidosos ou com desvio semântico ensinam premissas falsas.
- **Objetivo**: Propor mecanismos baseados em semântica (recompensas QPP e QAP) e um **Filtro de Dados (Data Filter)** rigoroso para eliminar perguntas que sofreram desvio antes de compor o dataset final.

---

## 🔬 As Duas Regras para Combater o Desvio Semântico

O artigo estabelece dois pilares conceituais fundamentais para validar se uma pergunta gerada é válida:

### 1. QPP (*Question Paraphrasing Probability* - Equivalência Semântica)
- Avalia se a pergunta gerada mantém a **mesma intenção semântica da pergunta canônica original**, em vez de exigir correspondência exata de palavras.
- Na prática moderna: medido via similaridade de cosseno de embeddings de sentenças ou classificadores de paráfrase.

### 2. QAP (*Question Answering Probability* - Consistência de Ida-e-Volta / Respondibilidade)
- Avalia se, ao entregar a pergunta gerada e o contexto original para um modelo leitor, **ele consegue encontrar com sucesso a resposta padrão-ouro original**.
- Se o modelo não conseguir responder ou apontar para outro trecho, significa que a pergunta sofreu *semantic drift* e perdeu o vínculo com o fato de origem.

### 3. O Filtro de Dados (*Data Filter*)
- Os autores implementaram uma etapa de **poda (filtering)**: perguntas que caem abaixo de um limiar mínimo de probabilidade/similaridade são **descartadas sumariamente**.
- Essa filtragem foi o fator determinante para que o dataset sintético superasse os baselines.

---

## 📊 Principais Resultados Encontrados
- Métricas superficiais como BLEU falham gravemente em avaliar perguntas, pois penalizam paráfrases legítimas ou perguntas criativas válidas.
- A introdução de recompensas semânticas atingiu o estado da arte na geração de perguntas sobre o SQuAD.
- O uso de **dados sintéticos filtrados** proporcionou ganhos consistentes em modelos robustos (incluindo BERT e BiDAF), comprovando o valor de enriquecer datasets com perguntas variadas, desde que auditadas contra desvios.

---

## 💡 Como e Onde Citar Este Artigo no seu Mestrado (A FUNDAMENTAÇÃO DO MÓDULO 04!):

Este artigo é a **âncora teórica perfeita para justificar a existência do seu Módulo 04 (Auditoria e Controle de Qualidade)**:

- **Na Introdução / Definição do Problema**:
  - Citar Zhang & Bansal (EMNLP 2019) para **definir formalmente o conceito de *Semantic Drift* (Desvio Semântico)**: explicar que ao sintetizar variações de perguntas para avaliar RAGs, existe o risco inerente do modelo gerar perguntas que fogem do texto legal/editalício.
  - Citar a evidência empírica dos autores de que *gerar dados sintéticos sem uma etapa rigorosa de filtragem contamina o benchmark*.

- **No Módulo 04 (Metodologia de Filtragem e Auditoria Semântica)**:
  - Justificar que o seu Módulo 04 atua exatamente como o **Data Filter** de Zhang & Bansal:
    1. O cálculo de **similaridade de embeddings (> 0.70)** implementa o princípio do **QPP** (preservação da intenção da pergunta).
    2. A verificação de que a resposta original continua válida implementa o princípio do **QAP** (respondibilidade factual).
  - Explicar que essa dupla checagem garante que o dataset final de licitações públicas esteja livre de ruídos espúrios ou perguntas alucinadas.
