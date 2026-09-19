# 📄 Fichamento Bibliográfico 01

## 📌 Identificação da Obra
- **Título**: *Out of Style: RAG’s Fragility to Linguistic Variation*
- **Autores**: Pesquisadores das instituições associadas (2024/2025).
- **Arquivo local**: [`referencias/Out of Style RAG’s Fragility to Linguistic Variation.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Out%20of%20Style%20RAG%E2%80%99s%20Fragility%20to%20Linguistic%20Variation.pdf)
- **Área**: Information Retrieval, RAG Robustness, Natural Language Processing.

---

## 🎯 Problema e Objetivo
Avaliar como **variações linguísticas nas perguntas dos usuários** afetam o desempenho fim a fim de sistemas RAG.
A maioria dos benchmarks avalia RAG com perguntas gramaticalmente perfeitas e padronizadas, ignorando que usuários reais escrevem de forma informal, cerimoniosa, com vocabulário rebuscado ou com erros de digitação e ausência de acentos.

---

## 🔬 As 4 Dimensões Linguísticas Investigadas
1. **Formalidade $\downarrow$**: Perguntas reescritas em tom coloquial e casual.
2. **Legibilidade $\downarrow$**: Perguntas com vocabulário rebuscado e sintaxe complexa/erudita.
3. **Polidez $\uparrow$**: Perguntas com excesso de cortesia e preâmbulos cerimoniosos.
4. **Correção Gramatical $\downarrow$**:
   - **Typos**: Erros de digitação, omissão/troca de caracteres.
   - **RTT (Round-Trip Translation)**: Tradução ida-e-volta para induzir alterações sintáticas naturais.

---

## ⚖️ Metodologia de Validação Semântica (Semantic Consistency)
Para garantir que a pergunta modificada ainda exige a mesma resposta da original:
- **Filtro Automático de Embeddings**: Similaridade de cosseno via `all-mpnet-base-v2`.
- **Limiar de Corte**: Variações com similaridade **$< 0.70$** são descartadas por suspeita de desvio semântico.
- **Validação de Resposta**: 94,67% das perguntas preservaram exatamente a resposta padrão-ouro original (*Gold Answer*).

---

## 📊 Principais Resultados Encontrados
- A modificação gramatical (erros de digitação/typos) foi a que causou a **queda mais severa no Recall** da recuperação de documentos.
- A geração final do LLM sofreu degradação média de **16,52% (Answer Match)**, **41,15% (Exact Match)** e **19,60% (F1 Score)**.
- **Aumentar o tamanho do LLM (ex: de 8B para 70B) não eliminou a perda de desempenho**, provando que o gargalo está na sensibilidade do componente de busca aos estilos de consulta.

---

## 💡 Como Citar Este Artigo no seu Artigo de Mestrado:
- **Na Introdução**: Citar para justificar que *avaliar sistemas RAG apenas com perguntas canônicas e formais mascara sua fragilidade no mundo real*.
- **Na Metodologia**: Citar como base teórica para a escolha das dimensões de perturbação linguística adotadas no Módulo 3.
- **Na Validação**: Citar para fundamentar o uso do corte de similaridade de cosseno ($> 0.70$) como filtro de qualidade de dados sintéticos.
- **No Gap de Pesquisa**: Destacar que o artigo focou no idioma **inglês**, abrindo a oportunidade inédita de investigar essas dimensões no **Português do Brasil**, especialmente em documentos públicos complexos (como licitações).
