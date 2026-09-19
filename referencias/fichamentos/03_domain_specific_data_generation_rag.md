# 📄 Fichamento Bibliográfico 03

## 📌 Identificação da Obra
- **Título**: *Domain-Specific Data Generation Framework for RAG Adaptation* (Framework **RAGen**)
- **Autores**: Chris Xing Tian, Weihao Xie, Zhen Chen, Hui Liu, Zhengyuan Yi, Haoliang Li, Shiqi Wang, Siwei Ma
- **Instituições**: Peng Cheng Laboratory, City University of Hong Kong, Peking University
- **Publicação**: *Findings of the Association for Computational Linguistics: ACL 2026* (páginas 19236–19250). (Qualis A1 / Principal conferência mundial de NLP)
- **Arquivo Local**: [`referencias/Domain-Specific Data Generation Framework for RAG Adaptation.pdf`](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/ARTIGO%20MESTRADO/referencias/Domain-Specific%20Data%20Generation%20Framework%20for%20RAG%20Adaptation.pdf)
- **Área**: Geração de Dados Sintéticos, Adaptação de RAG, Raciocínio Multi-hop, Taxonomia de Bloom.

---

## 🎯 Problema e Objetivo da Pesquisa
- **Problema**: A escassez de dados de treinamento e avaliação específicos de domínio de alta qualidade para adaptar sistemas RAG. As abordagens tradicionais geram perguntas superficiais baseadas em um único chunk pequeno (*single-chunk*), incapazes de avaliar raciocínio profundo ou sintetizar evidências distribuídas ao longo de documentos complexos.
- **Objetivo**: Propor o **RAGen**, um framework modular e centrado em dados (*data-centric*) para sintetizar automaticamente triplas de **Pergunta–Resposta–Contexto (QAC)** ricas e fundamentadas, controlando a complexidade cognitiva das perguntas e gerando contextos distratores para testar a robustez do sistema.

---

## 🔬 Metodologia e Inovações do Framework RAGen

O framework é estruturado em três estágios principais:

### 1. Extração de Conceitos do Documento (*Document Concepts Extraction*)
- Realiza chunking semântico e extrai conceitos-chave no nível de chunks.
- Utiliza **K-means sobre embeddings** para fundir conceitos similares e identificar os temas globais do documento, eliminando redundâncias.

### 2. Montagem de Evidências Multi-Chunk (*Concept-Centered Evidence Assembly*)
- Diferente de pipelines que geram perguntas olhando para um parágrafo isolado, o RAGen faz **recuperação cruzada de múltiplos chunks** relacionados ao mesmo conceito global.
- Isso permite formular perguntas que exigem cruzar informações espalhadas pelo documento (*cross-chunk reasoning*).

### 3. Geração de QAC com Taxonomia de Bloom e Variantes de Contexto
- **Controle Cognitivo via Taxonomia de Bloom**:
  - *Fácil (Remembering / Understanding)*: Perguntas de lembrança factual direta.
  - *Médio (Applying / Analyzing)*: Perguntas que exigem decompor informações e comparar evidências.
  - *Difícil (Evaluating / Creating)*: Perguntas que demandam julgamento crítico, síntese ou tomada de decisão.
- **Construtor de Variantes de Contexto (Distratores)**:
  Associa cada par de pergunta-resposta a 4 tipos de contexto para avaliar o retriever e o gerador:
  1. **Fully-supportive**: Contém todas as evidências necessárias para responder.
  2. **Partially-supportive**: Evidência incompleta, forçando inferência parcial.
  3. **Irrelevant**: Texto do mesmo domínio, mas sobre outro assunto.
  4. **Misleading (Distrator Enganoso)**: Texto que compartilha termos parecidos com a pergunta, mas NÃO a responde (o teste perfeito para pegar alucinações de RAG!).

---

## 📊 Principais Resultados e Métricas
- Testado em múltiplos domínios corporativos e científicos complexos.
- Demonstrou ganhos substanciais tanto na etapa de **recuperação (Recall / NDCG)** quanto na **geração de respostas (precisão factual e profundidade)**.
- Provou que perguntas guiadas por níveis superiores da Taxonomia de Bloom e avaliadas contra contextos distratores (*misleading*) expõem falhas em RAGs que passavam despercebidas em benchmarks com perguntas simples.

---

## ⚠️ Limitações e Gaps de Pesquisa (Oportunidades)
1. **Foco predominante em língua inglesa**: O framework foi concebido e testado em inglês, sem explorar especificidades morfossintáticas e variações do Português do Brasil.
2. **Não combina perturbações de estilo do usuário com os níveis de Bloom**: O RAGen varia a dificuldade cognitiva da pergunta e o contexto documental, mas mantém a linguagem da pergunta relativamente formal. Ele não investiga o que acontece quando a pergunta de nível alto vem com erros ortográficos, informalidade ou gírias (como feito no paper *Out of Style*).
3. **Não foi aplicado a documentos públicos de contratações/licitações**, onde a relação interdocumental (Edital x Anexo) é mandatória por lei.

---

## 💡 Como e Onde Citar Este Artigo no seu Mestrado:

- **Na Introdução e Fundamentação**:
  - Citar como referência máxima de **estado da arte (ACL 2026)** para justificar a importância de abordagens *data-centric* (geração de datasets de alta qualidade) para o sucesso de RAGs em domínios específicos.
- **No Módulo 02 (Geração de QA Base)**:
  - **Adotar a Taxonomia de Bloom**: Citar Tian et al. (2026) para justificar a categorização das perguntas do seu dataset em níveis de complexidade cognitiva (perguntas factuais diretas x perguntas de análise comparativa entre Edital e Planilha Orçamentária).
  - Justificar a importância de formular perguntas a partir de **múltiplos chunks / anexos** em vez de parágrafos isolados.
- **No Gap da sua Dissertação (O "Triângulo Perfeito")**:
  - O seu trabalho unifica os três pilares:
    1. A necessidade de RAG em políticas públicas no Brasil (**Oliveira et al., 2026**);
    2. O controle de profundidade cognitiva e multi-chunk (**Tian et al., 2026 - RAGen**);
    3. A fragilidade linguística sob ruídos e estilos reais de usuários (**Out of Style, 2024/2025**).
