# 📄 Fichamento Bibliográfico 06

## 📌 Identificação da Obra
- **Título**: *Improving the Robustness of Question Answering Systems to Question Paraphrasing*
- **Autores**: Wee Chung Gan e Hwee Tou Ng
- **Instituição**: National University of Singapore (NUS)
- **Publicação**: *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL 2019)*, páginas 6065–6075. (Qualis A1 / Conferência de topo em NLP)
- **Arquivo Local**: [`referencias/Improving the Robustness of Question Answering Systems to Question Paraphrasing.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Improving%20the%20Robustness%20of%20Question%20Answering%20Systems%20to%20Question%20Paraphrasing.pdf)
- **Área**: Question Answering (QA), Robustez a Paráfrases, Exemplos Adversariais, Avaliação de Sensibilidade.

---

## 🎯 Problema e Objetivo da Pesquisa
- **O Problema da Hiper-sensibilidade (*Over-sensitivity*)**: Modelos de Question Answering atingem desempenhos impressionantes (muitas vezes superando humanos nos conjuntos de teste fechados como o SQuAD), mas são extremamente **frágeis a pequenas paráfrases**. Quando uma pergunta é reescrita com palavras sinônimas ou estrutura sintática ligeiramente diferente, o modelo frequentemente muda sua resposta para uma palavra incorreta.
- **Objetivo**: Avaliar sistematicamente a robustez de múltiplos modelos de QA líderes de mercado contra conjuntos de testes parafraseados (tanto naturais quanto adversariais) e propor uma técnica de aumento de dados (*data augmentation*) para mitigar essa vulnerabilidade.

---

## 🔬 Metodologia: Dois Tipos de Testes de Estresse

Os autores criaram dois benchmarks parafraseados a partir do SQuAD:

### 1. Conjunto Parafraseado Não-Adversarial (1.062 perguntas)
- Perguntas reescritas com pequenas alterações lexicais e sintáticas naturais.
- **Objetivo**: Testar a **hiper-sensibilidade** dos modelos frente à forma natural como diferentes pessoas perguntam a mesma coisa (ex: *"What was happening to..."* $\rightarrow$ *"What was going on with..."*).

### 2. Conjunto Parafraseado Adversarial (56 perguntas)
- Perguntas reescritas intencionalmente utilizando palavras do contexto que estão próximas de um **candidato a resposta incorreto** (do mesmo tipo de entidade da resposta correta).
- **Objetivo**: Avaliar se o modelo é facilmente enganado por sobreposição de palavras (*word overlap*) superficiais perto de distratores no texto.

---

## 📊 Principais Resultados Encontrados
- **Queda Drástica de Desempenho**: Todos os modelos avaliados (incluindo modelos de ponta baseados em BERT que superavam humanos no SQuAD) sofreram **quedas severas** nas métricas de **Exact Match (EM)** e **F1 Score** ao serem testados nas versões parafraseadas.
- No teste adversarial (com distratores contextuais), o desempenho dos modelos despencou ainda mais, comprovando que os modelos dependem de atalhos lexicais (*spurious correlations*) em vez de compreender verdadeiramente a semântica da pergunta.
- O treinamento com aumento de dados parafraseados melhorou a robustez dos modelos sem degradar a acurácia nos dados originais.

---

## 💡 Como e Onde Citar Este Artigo no seu Mestrado:

- **Na Introdução**:
  - Citar Gan & Ng (ACL 2019) para evidenciar que *a fragilidade a paráfrases é um problema estrutural conhecido em modelos de linguagem, que se estende aos modernos sistemas RAG*.
  - Justificar que *avaliar modelos apenas em benchmarks de perguntas originais superestima sua capacidade de generalização no mundo real*.
- **No Módulo 03 (Estilos e Variações de Perguntas)**:
  - Citar este artigo como referência fundamental para a inclusão de **paráfrases não-adversariais e adversariais**: explicar que além de estilos de linguagem, o dataset deve testar a sensibilidade a palavras que aparecem em outras partes do documento (como em tabelas e anexos diferentes de um edital de licitação).
- **Na Justificativa do Estudo de Caso (Licitações Públicas)**:
  - Documentos de licitação são repletos de termos repetidos em cláusulas diferentes. A lição de Gan & Ng (2019) mostra que se um licitante parafrasear uma pergunta usando termos de outro lote ou cláusula, o sistema corre sério risco de retornar o lote errado se não for avaliado com rigor.
