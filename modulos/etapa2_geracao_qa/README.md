# 🎯 Módulo 02: Geração de Perguntas e Respostas Base (Ground Truth)

Este módulo é responsável por sintetizar o conjunto padrão-ouro (*Ground Truth*) de perguntas canônicas e respostas esperadas a partir dos documentos extraídos no Módulo 01.

---

## 🎯 Objetivo Metodológico
Para testar a fragilidade de um sistema RAG a variações linguísticas, precisamos primeiro de uma **âncora perfeita**:
- Perguntas gramaticalmente corretas, claras e sem ambiguidades.
- Respostas factuais com evidência direta no texto (*grounding*).
- Metadados vinculados (nome do documento, página, seção).

---

## 📂 Entradas e Saídas

- **Entrada**: Documentos processados em `dados/02_chunks/`.
- **Saída**: Arquivo estruturado `dados/03_qa_base/qa_base.json`.

Formato de cada item gerado:
```json
{
  "id": "qa_001",
  "pergunta_original": "Qual foi a taxa de reincidência penitenciária identificada no relatório do Ipea?",
  "resposta_esperada": "A taxa média foi de 24,4%.",
  "tipo_pergunta": "Factual",
  "evidencia": "A pesquisa estimou uma taxa média de reincidência penitenciária de 24,4%...",
  "metadados": {
    "documento": "Relatorio_Ipea",
    "pagina": 15,
    "secao": "3.1 Resultados Principais"
  }
}
```

---

## 💡 Estratégias Futuras a Implementar
- Seleção automática de chunks com alta densidade informacional.
- Suporte a múltiplos LLMs geradores (OpenAI, Gemini, Ollama/Qwen local).
- Categorização de perguntas: Factuais, Conceituais e baseadas em Tabelas.
