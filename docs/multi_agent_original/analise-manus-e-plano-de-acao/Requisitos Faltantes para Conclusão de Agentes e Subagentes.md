# Requisitos Faltantes para Conclusão de Agentes e Subagentes

## 1. Agentes APIs

### 1.1 APIUnifyMaster
- **Prompt Principal**: Já implementado
- **Tools Principal**: 
  - Definir ferramentas de integração com APIs externas
  - Configurar autenticação e autorização
  - Implementar manipulação de respostas e tratamento de erros
- **Subagentes**:
  - **Subagente 1 (API Connector)**: 
    - Prompt: Instruções para estabelecer conexões com APIs externas
    - Tools: Configuração de endpoints, métodos HTTP, headers
  - **Subagente 1 copy (Data Transformer)**:
    - Prompt: Instruções para transformação de dados entre diferentes formatos
    - Tools: Funções de parsing JSON/XML, mapeamento de campos
  - **Subagente 1 copy 2 (Error Handler)**:
    - Prompt: Instruções para identificação e tratamento de erros de API
    - Tools: Funções de retry, logging, notificação
  - **Subagente 1 copy 3 (Rate Limiter)**:
    - Prompt: Instruções para gerenciamento de limites de requisição
    - Tools: Controle de throttling, filas de requisição
  - **Subagente 1 copy 4 (Cache Manager)**:
    - Prompt: Instruções para gerenciamento de cache de respostas
    - Tools: Configuração de TTL, invalidação de cache

### 1.2 HotmartAPIMaster
- **Prompt Principal**: 
  - Definir comportamento geral do agente
  - Especificar conhecimento sobre a API Hotmart
  - Incluir exemplos de uso comum
- **Tools Principal**:
  - Configurar autenticação OAuth2 específica da Hotmart
  - Implementar endpoints principais (produtos, vendas, alunos)
  - Definir tratamento de webhooks
- **Subagentes**:
  - **Subagente 1 (Product Manager)**:
    - Prompt: Instruções para gerenciamento de produtos na Hotmart
    - Tools: CRUD de produtos, configuração de ofertas
  - **Subagente 1 copy (Sales Tracker)**:
    - Prompt: Instruções para acompanhamento de vendas
    - Tools: Consulta de transações, relatórios, comissões
  - **Subagente 1 copy 2 (Student Manager)**:
    - Prompt: Instruções para gerenciamento de alunos
    - Tools: Acesso a matrículas, progresso, certificados
  - **Subagente 1 copy 3 (Checkout Optimizer)**:
    - Prompt: Instruções para otimização de checkout
    - Tools: Configuração de páginas de vendas, upsells
  - **Subagente 1 copy 4 (Affiliate Manager)**:
    - Prompt: Instruções para gerenciamento de afiliados
    - Tools: Configuração de comissões, links, relatórios

### 1.3 KiwifyAPIMaster
- **Prompt Principal**:
  - Definir comportamento geral do agente
  - Especificar conhecimento sobre a API Kiwify
  - Incluir exemplos de uso comum
- **Tools Principal**:
  - Configurar autenticação específica da Kiwify
  - Implementar endpoints principais (produtos, vendas, assinaturas)
  - Definir tratamento de webhooks
- **Subagentes**:
  - **Subagente 1 (Product Catalog)**:
    - Prompt: Instruções para gerenciamento de produtos na Kiwify
    - Tools: CRUD de produtos, configuração de ofertas
  - **Subagente 1 copy (Subscription Manager)**:
    - Prompt: Instruções para gerenciamento de assinaturas
    - Tools: Criação, cancelamento, upgrades de planos
  - **Subagente 1 copy 2 (Payment Processor)**:
    - Prompt: Instruções para processamento de pagamentos
    - Tools: Consulta de transações, reembolsos
  - **Subagente 1 copy 3 (Customer Support)**:
    - Prompt: Instruções para suporte ao cliente
    - Tools: Acesso a dados de clientes, histórico de compras
  - **Subagente 1 copy 4 (Analytics Reporter)**:
    - Prompt: Instruções para geração de relatórios
    - Tools: Métricas de vendas, conversão, retenção

### 1.4 PaytAPIMaster
- **Prompt Principal**:
  - Definir comportamento geral do agente
  - Especificar conhecimento sobre a API Payt
  - Incluir exemplos de uso comum
- **Tools Principal**:
  - Configurar autenticação específica da Payt
  - Implementar endpoints principais (pagamentos, cobranças)
  - Definir tratamento de webhooks
- **Subagentes**:
  - **Subagente 1 (Payment Creator)**:
    - Prompt: Instruções para criação de pagamentos
    - Tools: Geração de links, QR codes, boletos
  - **Subagente 1 copy (Transaction Monitor)**:
    - Prompt: Instruções para monitoramento de transações
    - Tools: Consulta de status, notificações
  - **Subagente 1 copy 2 (Refund Processor)**:
    - Prompt: Instruções para processamento de reembolsos
    - Tools: Solicitação, aprovação, acompanhamento
  - **Subagente 1 copy 3 (Recurring Billing)**:
    - Prompt: Instruções para cobranças recorrentes
    - Tools: Configuração de planos, datas de cobrança
  - **Subagente 1 copy 4 (Financial Reporter)**:
    - Prompt: Instruções para relatórios financeiros
    - Tools: Balanços, fluxo de caixa, conciliação

### 1.5 PerfectpayAPIMaster
- **Prompt Principal**:
  - Definir comportamento geral do agente
  - Especificar conhecimento sobre a API Perfectpay
  - Incluir exemplos de uso comum
- **Tools Principal**:
  - Configurar autenticação específica da Perfectpay
  - Implementar endpoints principais (produtos, vendas, checkouts)
  - Definir tratamento de webhooks
- **Subagentes**:
  - **Subagente 1 (Product Setup)**:
    - Prompt: Instruções para configuração de produtos
    - Tools: CRUD de produtos, preços, opções
  - **Subagente 1 copy (Checkout Manager)**:
    - Prompt: Instruções para gerenciamento de checkouts
    - Tools: Configuração de páginas, upsells, downsells
  - **Subagente 1 copy 2 (Order Processor)**:
    - Prompt: Instruções para processamento de pedidos
    - Tools: Consulta, atualização, cancelamento
  - **Subagente 1 copy 3 (Affiliate System)**:
    - Prompt: Instruções para sistema de afiliados
    - Tools: Configuração de comissões, rastreamento
  - **Subagente 1 copy 4 (Metrics Analyzer)**:
    - Prompt: Instruções para análise de métricas
    - Tools: Conversão, ROI, LTV, CAC

## 2. Agentes Analytics

### 2.1 ANALYTICSGPT | Super Track
- **Subagentes**:
  - **Subagente 1 (Data Collector)**:
    - Prompt: Instruções para coleta de dados de múltiplas fontes
    - Tools: Conectores para Google Analytics, Facebook, etc.
  - **Subagente 1 copy (Data Cleaner)**:
    - Prompt: Instruções para limpeza e normalização de dados
    - Tools: Detecção de outliers, preenchimento de valores nulos
  - **Subagente 1 copy 2 (Insight Generator)**:
    - Prompt: Instruções para geração de insights a partir de dados
    - Tools: Análise de tendências, correlações, anomalias
  - **Subagente 1 copy 3 (Visualization Creator)**:
    - Prompt: Instruções para criação de visualizações
    - Tools: Geração de gráficos, dashboards, relatórios
  - **Subagente 1 copy 4 (Recommendation Engine)**:
    - Prompt: Instruções para recomendações baseadas em dados
    - Tools: Sugestões de otimização, próximas ações

## 3. Agentes Copywriters

### 3.1 Conversion Catalyst
- **Tools Principal**:
  - Implementar ferramentas de análise de copy
  - Configurar integração com bases de conhecimento
  - Definir métricas de conversão
- **Subagentes**:
  - **Command-Architect**:
    - Tools: Geração de CTAs, análise de eficácia
  - **Decision-Mapper**:
    - Tools: Mapeamento de jornada de decisão, pontos de fricção
  - **Risk-Neutralizer**:
    - Tools: Identificação de objeções, criação de garantias
  - **Urgency-Architect**:
    - Tools: Criação de gatilhos de escassez, prazos
  - **Value-Amplifier**:
    - Tools: Quantificação de benefícios, comparação de valor

### 3.2 Metaphor Architect
- **Tools Principal**:
  - Implementar ferramentas de análise semântica
  - Configurar base de conhecimento de domínios
  - Definir métricas de ressonância
- **Subagentes**:
  - **Concept-Dissector**:
    - Tools: Análise de conceitos complexos, decomposição
  - **Domain-Prospector**:
    - Tools: Identificação de domínios análogos, mapeamento
  - **Isomorphism-Engineer**:
    - Tools: Criação de estruturas paralelas, mapeamento
  - **Resonance-Calibrator**:
    - Tools: Teste de ressonância, ajuste de metáforas
  - **Sensory-Translator**:
    - Tools: Conversão entre modalidades sensoriais

### 3.3 Pain Detector
- **Tools Principal**:
  - Implementar ferramentas de análise de audiência
  - Configurar base de conhecimento de problemas comuns
  - Definir métricas de engajamento
- **Subagentes**:
  - **Consequence-Amplifier**:
    - Tools: Projeção de consequências, cenários futuros
  - **Context-Cartographer**:
    - Tools: Mapeamento de contexto social, econômico
  - **Digital-Ethnographer**:
    - Tools: Análise de comportamento online, linguagem
  - **Impact-Prioritizer**:
    - Tools: Classificação de impacto, priorização
  - **Symptom-Translator**:
    - Tools: Identificação de sintomas, causas raiz

### 3.4 Retention Architect
- **Tools Principal**:
  - Implementar ferramentas de análise de engajamento
  - Configurar integração com dados de clientes
  - Definir métricas de retenção

### 3.5 Neurohook Ultra
- **Status**: Implementação completa necessária
  - Definir prompt principal
  - Configurar ferramentas
  - Implementar subagentes

### 3.6 Paradigm Architect
- **Status**: Implementação completa necessária
  - Definir prompt principal
  - Configurar ferramentas
  - Implementar subagentes

## 4. Agentes Knowledge Bases Masters

### 4.1 DocRAGOptimizer
- **Tools Principal**:
  - Implementar ferramentas de processamento de documentos
  - Configurar integração com bases de conhecimento
  - Definir métricas de qualidade de recuperação
- **Subagentes**:
  - **Subagente 1 (Document Processor)**:
    - Prompt: Instruções para processamento de documentos
    - Tools: Extração de texto, OCR, normalização
  - **Subagente 1 copy (Chunking Specialist)**:
    - Prompt: Instruções para segmentação de documentos
    - Tools: Algoritmos de chunking, análise semântica
  - **Subagente 1 copy 2 (Embedding Generator)**:
    - Prompt: Instruções para geração de embeddings
    - Tools: Modelos de embedding, otimização
  - **Subagente 1 copy 3 (Query Optimizer)**:
    - Prompt: Instruções para otimização de consultas
    - Tools: Reformulação, expansão, filtragem
  - **Subagente 1 copy 4 (Retrieval Evaluator)**:
    - Prompt: Instruções para avaliação de recuperação
    - Tools: Métricas de precisão, recall, relevância

## 5. Agentes Planejados (Não Implementados)

### 5.1 AgentDevOps
- **Requisitos para implementação**:
  - Criar estrutura de pastas seguindo o modelo padrão
  - Definir prompt principal com foco em operações de infraestrutura
  - Configurar ferramentas para integração com sistemas DevOps
  - Implementar subagentes especializados:
    - **Monitoramento de Sistemas**: Prompt e tools para monitoramento
    - **Diagnóstico de Problemas**: Prompt e tools para troubleshooting
    - **Otimização de Recursos**: Prompt e tools para otimização
    - **Segurança e Compliance**: Prompt e tools para segurança

### 5.2 AgentCustomerSuccess
- **Requisitos para implementação**:
  - Criar estrutura de pastas seguindo o modelo padrão
  - Definir prompt principal com foco em relacionamento com clientes
  - Configurar ferramentas para integração com CRMs
  - Implementar subagentes especializados:
    - **Análise de Sentimento**: Prompt e tools para análise
    - **Previsão de Churn**: Prompt e tools para modelagem preditiva
    - **Recomendação de Ações**: Prompt e tools para recomendações
    - **Automação de Comunicação**: Prompt e tools para comunicação

### 5.3 AgentProductManager
- **Requisitos para implementação**:
  - Criar estrutura de pastas seguindo o modelo padrão
  - Definir prompt principal com foco em gestão de produtos
  - Configurar ferramentas para integração com sistemas de gestão
  - Implementar subagentes especializados:
    - **Análise de Mercado**: Prompt e tools para análise
    - **Priorização de Features**: Prompt e tools para priorização
    - **Roadmap Planning**: Prompt e tools para planejamento
    - **Análise de Feedback**: Prompt e tools para análise

### 5.4 AgentLegalAssistant
- **Requisitos para implementação**:
  - Criar estrutura de pastas seguindo o modelo padrão
  - Definir prompt principal com foco em assistência jurídica
  - Configurar ferramentas para acesso a bases de conhecimento legal
  - Implementar subagentes especializados:
    - **Análise de Contratos**: Prompt e tools para análise
    - **Verificação de Compliance**: Prompt e tools para verificação
    - **Pesquisa Jurídica**: Prompt e tools para pesquisa
    - **Geração de Documentos**: Prompt e tools para geração

## Requisitos Comuns para Todos os Agentes

### Prompts
- **Estrutura Consistente**:
  - Definição clara do papel e objetivo
  - Instruções detalhadas de comportamento
  - Exemplos de uso e casos de borda
  - Limitações e tratamento de erros

### Tools
- **Configuração Padronizada**:
  - Definição de endpoints e parâmetros
  - Autenticação e autorização
  - Tratamento de erros e retentativas
  - Logging e monitoramento

### Conhecimento
- **Base de Conhecimento**:
  - Documentação específica do domínio
  - Exemplos e casos de uso
  - FAQs e troubleshooting
  - Atualizações e versionamento

### Integração
- **Comunicação entre Agentes**:
  - Protocolos de mensagens
  - Formatos de dados
  - Gestão de estado
  - Tratamento de falhas
