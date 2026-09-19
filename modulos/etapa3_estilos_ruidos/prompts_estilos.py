"""
Templates de Prompts para o Módulo 03: Diversificação de Estilos e Injeção de Ruídos.
Baseado na metodologia do artigo:
'Out of Style: RAG's Fragility to Linguistic Variation'
"""

# 1. Dimensão: Baixa Formalidade (Informalidade / Coloquialismo)
PROMPT_BAIXA_FORMALIDADE = """Reescreva a pergunta a seguir de forma informal, coloquial e descontraída, como se fosse um usuário comum conversando no WhatsApp ou fórum, mas preservando EXATAMENTE a mesma informação que está sendo solicitada.

Pergunta original: {pergunta_original}

Diretrizes:
- Use gírias leves ou expressões coloquiais em português brasileiro (ex: "fala aí", "me diz uma coisa", "onde que tá...").
- Mantenha a intenção original para que a resposta factual continue sendo a mesma.
- Retorne APENAS a pergunta reescrita.
"""

# 2. Dimensão: Baixa Legibilidade (Linguagem Rebuscada / Complexa)
PROMPT_BAIXA_LEGIBILIDADE = """Reescreva a pergunta a seguir tornando-a intencionalmente complexa, com vocabulário rebuscado, construções sintáticas eruditas e estilo acadêmico denso (baixa legibilidade), mas mantendo estritamente a mesma solicitação de informação.

Pergunta original: {pergunta_original}

Diretrizes:
- Utilize termos técnicos ou formais arcaicos sem alterar o fato investigado.
- Retorne APENAS a pergunta reescrita.
"""

# 3. Dimensão: Alta Polidez / Cortesia Excessiva
PROMPT_ALTA_POLIDEZ = """Reescreva a pergunta a seguir com um grau excessivo de polidez, cortesia cerimoniosa e gentileza formal.

Pergunta original: {pergunta_original}

Diretrizes:
- Use introduções gentis (ex: "Seria possível a gentileza de me esclarecer...", "Peço encarecidamente a informação referente a...").
- Preserve a mesma informação procurada.
- Retorne APENAS a pergunta reescrita.
"""

# 4. Dimensão: Busca por Palavras-Chave (Telegráfica)
PROMPT_PALAVRAS_CHAVE = """Converta a pergunta a seguir em uma busca telegráfica por palavras-chave, simulando como um usuário digita rapidamente no Google (sem pontuação, sem preposições, apenas termos centrais).

Pergunta original: {pergunta_original}

Diretrizes:
- Remova stopwords (artigos, preposições, saudações).
- Deixe apenas os substantivos, números e termos principais.
- Retorne APENAS a sequência de palavras-chave.
"""
