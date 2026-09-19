---
name: fichamento-artigos
description: >-
  Use esta skill sempre que o usuário fornecer, enviar, mencionar ou colar um novo artigo científico em PDF
  para compor a base de referências do projeto ('referencias/'), ou quando solicitar a leitura, análise,
  fichamento bibliográfico ou sugestão de citação de artigos para a pesquisa de mestrado sobre avaliação de RAG.
---

# Skill: Fichamento e Catalogação de Artigos Científicos

Esta skill guia o agente no processo de leitura, síntese analítica, catalogação e fichamento estruturado de obras científicas enviadas pelo usuário ou seu orientador.

---

## 🎯 Objetivo do Procedimento
Transformar cada novo artigo PDF em uma **Ficha de Leitura Acadêmica (Fichamento)** detalhada, salvando-a em `referencias/fichamentos/`, destacando:
1. O problema, objetivos e metodologia do artigo;
2. As métricas de avaliação utilizadas (para ajudar o usuário a entender e selecionar suas próprias métricas);
3. As limitações e lacunas de pesquisa apontadas pelos autores;
4. **Instruções explícitas de onde e como citar a obra** na dissertação/artigo de mestrado (Introdução, Metodologia, Trabalhos Relacionados, Discussão).

---

## 📋 Passo a Passo de Execução

### Passo 1: Localizar e Garantir o Arquivo na Pasta `referencias/`
- Verifique se o PDF está localizado na pasta `referencias/`.
- Se o arquivo estiver em outra pasta ou tiver sido carregado na raiz, copie/mova-o para `referencias/`.

### Passo 2: Extrair o Conteúdo Textual do Artigo
- Execute o script auxiliar da skill para inspecionar os metadados, resumo e seções iniciais:
  ```bash
  python .agents/skills/fichamento-artigos/scripts/extrair_texto_artigo.py "referencias/nome_do_artigo.pdf"
  ```
- Ou use um comando em Python com `pypdf` para inspecionar o Abstract, Introdução, Metodologia, Métricas e Conclusão.

### Passo 3: Criar o Fichamento Individual
- Descubra o próximo número sequencial examinando os arquivos em `referencias/fichamentos/` (ex: `01_...`, `02_...`, etc.).
- Crie o arquivo `referencias/fichamentos/<XX>_<nome_curto>.md` seguindo rigorosamente o template em `.agents/skills/fichamento-artigos/resources/template_fichamento.md`.
- As seções obrigatórias são:
  - **Identificação da Obra**: Título, Autores, Ano, Veículo/Conferência, Link local.
  - **Problema e Objetivo**: Qual lacuna o artigo atacou.
  - **Metodologia e Datasets**: Quais modelos, prompts e bases foram usados.
  - **Métricas Utilizadas e Resultados**: Explicar com clareza cada métrica medida (ex: Hit@K, MRR, NDCG, Ragas, F1, etc.).
  - **Limitações e Gaps**: Fraquezas admitidas pelos autores.
  - **Como e Onde Citar no Mestrado**: Sugestões práticas de parágrafos para o aluno citar no seu artigo.

### Passo 4: Atualizar o Índice Geral de Fichamentos
- Atualize o arquivo `referencias/fichamentos/README.md`, adicionando a nova linha na tabela do índice com:
  - Número
  - Título do Artigo
  - Autores / Ano
  - Papel / Como se conecta com a pesquisa
  - Link para o arquivo de fichamento

### Passo 5: Apresentar o Resumo ao Usuário
- Responda em Português do Brasil com:
  - O resumo conciso dos achados do artigo;
  - **Explicação das métricas** que o artigo usou (para ajudar o usuário a entendê-las de forma prática);
  - As recomendações de ouro sobre **como usar esse artigo para fortalecer o artigo de mestrado**.
