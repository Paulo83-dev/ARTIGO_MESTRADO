# ⚖️ Módulo 04: Avaliação de Perguntas e Auditoria Semântica

Este módulo atua como o **comitê de ética e qualidade dos dados**, garantindo que as variações geradas no Módulo 03 não sofreram **desvio semântico** (*Semantic Drift*) antes de serem testadas no sistema RAG.

---

## 🎯 Critérios de Validação Baseados no Artigo "Out of Style"

Para uma pergunta modificada ser considerada **válida**, ela deve atender aos seguintes filtros:

### 1. Similaridade de Embeddings (Corte $> 0.70$)
- Calculamos os embeddings da **pergunta original** e da **pergunta modificada** usando modelos de sentença (ex: `all-mpnet-base-v2`, `bge-m3` ou `paraphrase-multilingual-mpnet-base-v2`).
- Calculamos a **similaridade de cosseno**:
  $$\text{Similaridade} = \cos(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$
- **Critério**: Se a similaridade for inferior a **0.70**, a variação é marcada como suspeita de alucinação ou fuga de tema e é **descartada automaticamente**.

### 2. Preservação da Resposta (*Answer Invariance*)
- Uma variação é válida se, e somente se, a **resposta factual padrão-ouro** (*Gold Answer*) original responder perfeitamente à nova pergunta.
- Pode ser auditada via amostragens humanas ou por um **LLM-as-a-Judge** com prompt determinístico.

---

## 📂 Entradas e Saídas

- **Entrada**: `dados/04_qa_diversificado/qa_diversificado.json`.
- **Saída**: `dados/05_relatorios/`
  - `qa_validado.json`: Apenas as perguntas que passaram no crivo de qualidade.
  - `relatorio_auditoria.json` / `.csv`: Métricas de descarte, similaridade média por dimensão de estilo e distribuição de scores.
