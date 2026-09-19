"""
Templates de Prompts para o Módulo 02: Geração de Perguntas e Respostas Canônicas (Ground Truth).
"""

PROMPT_SISTEMA_GERACAO_QA = """Você é um assistente acadêmico rigoroso especializado em criar datasets de avaliação para sistemas RAG.
Seu objetivo é analisar o trecho de documento fornecido e formular perguntas e respostas precisas e factuais."""

PROMPT_USUARIO_GERACAO_QA = """Abaixo está um trecho extraído de um documento acadêmico/relatório técnico:

---
DOCUMENTO: {nome_documento}
PÁGINA(S): {paginas}
SEÇÃO / CONTEXTO: {secao}

CONTEÚDO:
{conteudo}
---

Com base ESTRITAMENTE nas informações presentes no texto acima, formule:
1. Uma PERGUNTA CLARA e OBJETIVA (Canônica), sem ambiguidades.
2. A RESPOSTA CORRETA E CONCISA, que possa ser comprovada diretamente pelo texto.
3. O TIPO DA PERGUNTA: "Factual" (dado explícito, ano, número), "Conceitual" (definição) ou "Tabular" (dados de tabela).

Retorne sua resposta estritamente no formato JSON:
{{
  "pergunta_original": "...",
  "resposta_esperada": "...",
  "tipo_pergunta": "Factual | Conceitual | Tabular",
  "trecho_evidencia": "frase exata do texto que comprova a resposta",
  "metadados": {{
    "documento": "{nome_documento}",
    "paginas": "{paginas}",
    "secao": "{secao}"
  }}
}}
"""
