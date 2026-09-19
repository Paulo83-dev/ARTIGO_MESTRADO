# 🎭 Módulo 03: Diversificação de Estilos e Injeção de Ruídos

Este módulo implementa a metodologia de perturbação linguística inspirada no artigo científico:
> **"Out of Style: RAG’s Fragility to Linguistic Variation"** *(disponível na pasta `referencias/`)*.

---

## 🔬 As 4 Dimensões Linguísticas Aplicadas

| Dimensão | Operação | Objetivo no RAG |
| :--- | :--- | :--- |
| **Formalidade $\downarrow$** | Transforma em linguagem casual, coloquial e informal | Avalia a robustez do retriever com gírias e pontuação livre |
| **Legibilidade $\downarrow$** | Reescreve com vocabulário rebuscado e sintaxe invertida | Avalia se a complexidade lexical confunde o embedding |
| **Polidez $\uparrow$** | Adiciona preâmbulos cerimoniosos e cortesia excessiva | Avalia se o excesso de *padding* cerimonial distrai o modelo |
| **Gramática & Typos $\downarrow$** | Injeta erros ortográficos, ausência de acentos e digitação | Avalia a quebra de tokens no vocabulário do tokenizer |

---

## 📂 Entradas e Saídas

- **Entrada**: `dados/03_qa_base/qa_base.json` (perguntas originais).
- **Saída**: `dados/04_qa_diversificado/qa_diversificado.json` contendo cada pergunta com suas 4+ variantes geradas.

Formato do arquivo de saída:
```json
{
  "id_base": "qa_001",
  "pergunta_original": "Qual foi a taxa média de reincidência penitenciária?",
  "variacoes": {
    "informal": "E aí, qual que foi a média de reincidência nas cadeias segundo o relatório?",
    "rebuscada": "Qual o coeficiente percentual correspondente ao retorno à custódia penal?",
    "polida": "Por gentileza, o senhor poderia me informar qual foi a taxa média apurada de reincidência penitenciária?",
    "palavras_chave": "taxa media reincidencia penitenciaria ipea",
    "typos": "qual foi a taxa media de reincidencia peniteciaria"
  }
}
```
