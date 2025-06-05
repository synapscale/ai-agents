# ÍNDICE MESTRE DO CONHECIMENTO EXPANSÍVEL (CAMADA 2)

---
version: 1.0  
status: Ativo  
last_updated: 2025-04-15  
purpose: Mapa central de navegação do conhecimento especializado  
related_systems: ["Núcleo Fundamental", "Mecanismos de Evolução"]  
knowledge_management_level: META  
---

## INSTRUÇÕES DE NAVEGAÇÃO PARA O AGENTE

Este índice funciona como o atlas completo do seu sistema de conhecimento expansível. Sua função principal é guiar decisões rápidas e precisas sobre quais documentos consultar em diferentes situações.

### Protocolo de Consulta
1. **Análise da Consulta:** Identifique conceitos-chave e intenção do usuário
2. **Mapeamento para Domínio:** Determine qual área de conhecimento é mais relevante
3. **Seleção de Documento:** Escolha o documento primário mais apropriado
4. **Verificação de Interdependências:** Identifique documentos complementares necessários
5. **Síntese de Conhecimento:** Combine informações em uma resposta coesa
6. **Adaptação ao Contexto:** Ajuste ao nível técnico e necessidade específica

### Tipos de Consultas e Documentos Recomendados

| Tipo de Consulta | Documentos Primários | Documentos Secundários |
|------------------|----------------------|------------------------|
| **Definição de Conceito** | `glossario_termos.md`, domínio específico | `taxonomia_parametros.md` |
| **Implementação Técnica** | `templates_datalayer.md`, `snippets_codigo.md` | `validacao_qa.md` |
| **Arquitetura de Solução** | `integracao_plataformas.md`, domínio específico | `diagramas_fluxo.md` |
| **Troubleshooting** | `validacao_qa.md`, domínio específico | `checklists_implementacao.md` |
| **Best Practices** | Domínio específico | `seguranca_privacidade.md` |

## 1. FUNDAMENTOS TÉCNICOS

| Documento | Propósito Principal | Consultar Quando | Conecta-se Com | Palavras-chave |
|-----------|---------------------|------------------|----------------|----------------|
| [`engenharia_parametros_intro.md`](BANCOS_DE_CONHECIMENTO/engenharia_parametros_intro.md) | Framework conceitual para enriquecimento de dados | Explicar **por que** a qualidade de parâmetros importa; justificar implementações detalhadas | `taxonomia_parametros.md`, `taxonomia_eventos.md` | fundamentos, filosofia, granularidade, ROI analytics, valor dados, estratégia parâmetros |
| [`taxonomia_parametros.md`](BANCOS_DE_CONHECIMENTO/taxonomia_parametros.md) | **Catálogo definitivo** de parâmetros com definição, formato, exemplos e uso | Identificar ou definir parâmetros específicos; criar esquemas de eventos | `coleta_persistencia.md`, todos documentos de implementação | user_id, client_id, session_id, utm_source, fbclid, gclid, event_id, custom_parameters, parameter_format |
| [`coleta_persistencia.md`](BANCOS_DE_CONHECIMENTO/coleta_persistencia.md) | Métodos técnicos para captura e retenção de dados | Implementar mecanismos para coletar e preservar parâmetros; resolver problemas de persistência | `redundancia_fallbacks.md`, `snippets_codigo.md` | cookies, localStorage, sessionStorage, dataLayer, cross-domain, cookie_duration, captura_parâmetros |
| [`redundancia_fallbacks.md`](BANCOS_DE_CONHECIMENTO/redundancia_fallbacks.md) | Arquitetura à prova de falhas para dados críticos | Criar sistemas resilientes; lidar com parâmetros ausentes ou corrompidos | `coleta_persistencia.md`, `validacao_qa.md` | fallback, contingência, dados_ausentes, degradação_graceful, prioridade_parâmetros, identificação_robusta |
| [`taxonomia_eventos.md`](BANCOS_DE_CONHECIMENTO/taxonomia_eventos.md) | **Framework estrutural** para todos os tipos de eventos | Determinar quais eventos devem ser rastreados e sua estrutura; padronizar implementação | `templates_datalayer.md`, `validacao_qa.md` | purchase, pageview, lead, signup, search, engagement, add_to_cart, event_structure, required_parameters |
| [`validacao_qa.md`](BANCOS_DE_CONHECIMENTO/validacao_qa.md) | Processos de garantia de qualidade para implementações | Verificar implementações; criar protocolos de teste; resolver discrepâncias | `checklists_implementacao.md`, `integracao_plataformas.md` | debugger, testing, validation, QA_process, data_integrity, data_quality, error_detection |
| [`integracao_plataformas.md`](BANCOS_DE_CONHECIMENTO/integracao_plataformas.md) | Arquiteturas de sincronização entre sistemas | Configurar rastreamento server-side; sincronizar múltiplas plataformas | `diagramas_fluxo.md`, `seguranca_privacidade.md` | server-side, GTM_SS, Meta_CAPI, API_integration, data_sync, cross-platform |
| [`seguranca_privacidade.md`](BANCOS_DE_CONHECIMENTO/seguranca_privacidade.md) | Governança, conformidade e proteção de dados | Implementar tracking respeitando privacidade; hash PII; configurar consentimento | `coleta_persistencia.md`, `integracao_plataformas.md` | GDPR, LGPD, CCPA, consent, CMP, PII, data_retention, SHA-256, anonymization, pseudonymization |

## 2. IMPLEMENTAÇÃO PRÁTICA

| Documento | Propósito Principal | Consultar Quando | Conecta-se Com | Palavras-chave |
|-----------|---------------------|------------------|----------------|----------------|
| [`templates_datalayer.md`](FRAMEWORKS_PRÁTICOS/templates_datalayer.md) | Snippets prontos para uso com dataLayer estruturado | Implementar eventos específicos; garantir consistência; acelerar deployment | `taxonomia_eventos.md`, `snippets_codigo.md` | dataLayer.push, e-commerce, enhanced_e-commerce, event_template, ready-to-use, GTM_implementation |
| [`checklists_implementacao.md`](FRAMEWORKS_PRÁTICOS/checklists_implementacao.md) | Guias passo-a-passo para implementações completas | Conduzir setup de rastreamento; garantir que nenhuma etapa seja perdida | `validacao_qa.md`, documentos específicos de domínio | implementation_steps, setup_guide, technical_onboarding, verification_list, launch_checklist |
| [`snippets_codigo.md`](FRAMEWORKS_PRÁTICOS/snippets_codigo.md) | Funções JavaScript para tracking e utilidades | Resolver casos específicos; implementar lógicas complexas de tracking | `coleta_persistencia.md`, `templates_datalayer.md` | javascript_functions, utilities, helpers, tracking_code, parameter_extraction, cookie_management |

## 3. RECURSOS DE REFERÊNCIA

| Documento | Propósito Principal | Consultar Quando | Conecta-se Com | Palavras-chave |
|-----------|---------------------|------------------|----------------|----------------|
| [`glossario_termos.md`](RECURSOS_DE_REFERÊNCIA/glossario_termos.md) | Definições autoritativas de termos técnicos | Esclarecer terminologia; garantir comunicação precisa | Todos os documentos | definitions, terminology, jargon, technical_terms, vocabulary, concepts |
| [`tabelas_conversao.md`](RECURSOS_DE_REFERÊNCIA/tabelas_conversao.md) | Mapeamento entre sistemas, formatos e padrões | Traduzir entre plataformas; mapear eventos e parâmetros | `integracao_plataformas.md`, `taxonomia_eventos.md` | mapping_tables, event_names, parameter_conversion, platform_equivalence, code_tables |
| [`diagramas_fluxo.md`](RECURSOS_DE_REFERÊNCIA/diagramas_fluxo.md) | Representações visuais de arquiteturas e processos | Entender fluxos complexos; visualizar integrações | `integracao_plataformas.md`, estruturas específicas de implementação | flow_diagrams, architecture, visualization, data_flow, system_integration, process_illustration |

## 4. ÁREAS DE CONHECIMENTO EMERGENTES
*Seção para documentos em desenvolvimento ou áreas identificadas para expansão*

| Área de Conhecimento | Status | Prioridade | Conecta-se Com | 
|----------------------|--------|------------|----------------|
| **Analytics API Avançadas** | Planejado | Alta | `integracao_plataformas.md` |
| **Tracking Server-First** | Em Desenvolvimento | Média | `integracao_plataformas.md`, `redundancia_fallbacks.md` |
| **Machine Learning para Analytics** | Planejado | Baixa | `engenharia_parametros_intro.md` |

## MATRIZ DE DECISÃO PARA CONSULTA RÁPIDA

Para questões sobre **QUAIS PARÂMETROS** utilizar:
- **Consulta primária:** `taxonomia_parametros.md`
- **Consulta complementar:** `taxonomia_eventos.md`

Para questões sobre **COMO IMPLEMENTAR** tecnicamente:
- **Consulta primária:** `templates_datalayer.md` ou `snippets_codigo.md`
- **Consulta complementar:** `checklists_implementacao.md`

Para questões sobre **INTEGRAÇÃO ENTRE PLATAFORMAS**:
- **Consulta primária:** `integracao_plataformas.md`
- **Consulta complementar:** `diagramas_fluxo.md`, `tabelas_conversao.md`

Para questões sobre **VALIDAÇÃO E PROBLEMAS**:
- **Consulta primária:** `validacao_qa.md`
- **Consulta complementar:** Documento específico do domínio do problema

Para questões sobre **PRIVACIDADE E CONFORMIDADE**:
- **Consulta primária:** `seguranca_privacidade.md`
- **Consulta complementar:** `coleta_persistencia.md`

## METADADOS DE EVOLUÇÃO
- **Última Atualização:** 2024-02-20
- **Documentos Atualizados Recentemente:** `integracao_plataformas.md`, `taxonomia_parametros.md`
- **Áreas Identificadas para Expansão:** API avançadas, Machine Learning para otimização
- **Próxima Revisão Programada:** 2024-05-20

---

**Este índice é um documento vivo.** Ao identificar lacunas de conhecimento ou novas necessidades através dos Mecanismos de Evolução Dirigida, registre-as na seção "Áreas de Conhecimento Emergentes" e proponha expansões ao Sistema de Conhecimento.