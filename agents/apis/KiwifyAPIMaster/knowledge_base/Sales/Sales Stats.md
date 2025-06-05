# API Kiwify - Vendas - Consultar Estatísticas de Vendas (Sales Stats)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Vendas - Consultar Estatísticas de Vendas (Sales Stats)` |
| **Identificador Interno** | `kiwify_sales_001`                   |
| **Título Curto (Ref.)**   | `Kiwify Sales Stats`           |
| **Versão do Documento**   | `1.0.0`                                |
| **Data de Criação**       | `2025-04-11`                                                  |
| **Última Atualização**    | `2025-04-11`                                                  |
| **Autor/Responsável**     | `Equipe de Documentação API`                                    |
| **Fonte Original**        | `https://docs.kiwify.com.br/api-reference/sales/stats`  |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/sales/stats` |
| **Status do Documento**   | `Em Uso`                              |
| **Ambiente de Referência**| `Produção`                                |
| **Idioma Original**       | `Português (BR)`                                  |
| **Formato de Datas (API)**| `String (ISO 8601)` |




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 2. Contexto




> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint de estatísticas de vendas da Kiwify.




O endpoint de Consulta de Estatísticas de Vendas fornece insights essenciais sobre o desempenho comercial de produtos na plataforma Kiwify. Este serviço permite aos desenvolvedores e gestores de negócios acessar métricas críticas como taxas de aprovação de pagamentos, valores totais, números de vendas e indicadores de performance financeira. Estas informações são fundamentais para análises de desempenho, relatórios financeiros, otimização de estratégias de vendas e monitoramento da saúde geral do negócio na plataforma.




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 3. Visão Geral da API/Endpoint(s)




> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint de estatísticas de vendas.




O endpoint de Estatísticas de Vendas é uma interface RESTful que fornece acesso a métricas agregadas relacionadas às transações de vendas. Diferentemente de endpoints que retornam dados brutos de transações individuais, este serviço entrega indicadores calculados que oferecem uma visão consolidada do desempenho comercial em determinado período. 


Este endpoint é particularmente útil para:
- Monitoramento de dashboards de desempenho de vendas
- Geração de relatórios periódicos (diários, semanais, mensais)
- Análise de eficácia de campanhas de marketing
- Avaliação da saúde financeira de produtos específicos
- Verificação de taxas de conversão de pagamentos




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 4. Detalhes Técnicos




> **Resumo:** Especificações técnicas detalhadas do endpoint, incluindo URL, método HTTP e requisitos de autenticação.




### `Endpoint: /v1/stats`




* **Endpoint URL:** `https://public-api.kiwify.com/v1/stats`
* **Método HTTP:** `GET`
* **Autenticação:** `OAuth 2.0 Bearer Token + API Key no cabeçalho`
  * Requer token de acesso no cabeçalho `Authorization: Bearer <token>`
  * Requer ID da conta Kiwify no cabeçalho `x-kiwify-account-id: <api-key>`




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 5. Parâmetros de Entrada




> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados nas requisições ao endpoint de estatísticas.




### `Endpoint: /v1/stats` (`Query / Header Parameters`)




| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `x-kiwify-account-id` (Header) | ID da conta Kiwify para autenticação | string | Sim | Exemplo: `acc_eK5TGfgn2XkSPfcP` |
| `Authorization` (Header) | Token OAuth 2.0 para autenticação | string | Sim | Formato: `Bearer <token>` |
| `product_id` (Query) | ID do produto para filtrar estatísticas | string | Não | Exemplo: `ba385b7c-cac1-4422-925d-7f707d8267d2` |
| `start_date` (Query) | Data inicial do período para análise | string (ISO 8601) | Não | Exemplo: `2023-01-01` |
| `end_date` (Query) | Data final do período para análise | string (ISO 8601) | Não | Exemplo: `2023-01-31` |




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)




> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint na resposta bem-sucedida.




### `Endpoint: /v1/stats`




#### 6.1.1 Estrutura Geral




| Campo             | Descrição | Tipo   |
| :---------------- | :-------- | :----- |
| `credit_card_approval_rate` | Taxa de aprovação de pagamentos com cartão de crédito | number (percentual) |
| `total_sales` | Número total de vendas concluídas no período | number (inteiro) |
| `total_net_amount` | Valor total líquido das vendas em centavos | number (inteiro) |
| `refund_rate` | Percentual de vendas que resultaram em reembolso | number (percentual) |
| `chargeback_rate` | Percentual de vendas que resultaram em chargeback | number (percentual) |
| `total_boleto_generated` | Quantidade de boletos bancários gerados | number (inteiro) |
| `total_boleto_paid` | Quantidade de boletos bancários efetivamente pagos | number (inteiro) |
| `boleto_rate` | Taxa de conversão de boletos (pagos/gerados) | number (percentual) |




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 7. Exemplos de Requisição e Resposta




> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint de estatísticas.




### `Endpoint: /v1/stats`




#### 7.1.1 Exemplo de Requisição (cURL)




```bash
curl --request GET \
  --url 'https://public-api.kiwify.com/v1/stats?product_id=ba385b7c-cac1-4422-925d-7f707d8267d2&start_date=2023-01-01&end_date=2023-01-31' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  --header 'x-kiwify-account-id: acc_eK5TGfgn2XkSPfcP'
```




#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)




```json
{
  "credit_card_approval_rate": 50,
  "total_sales": 3,
  "total_net_amount": 25956,
  "refund_rate": 25,
  "chargeback_rate": 0,
  "total_boleto_generated": 2,
  "total_boleto_paid": 1,
  "boleto_rate": 50
}
```




#### 7.1.3 Exemplo de Resposta (JSON - Erro)




```json
{
  "error": {
    "code": "authentication_required",
    "message": "Autenticação inválida ou expirada",
    "request_id": "req_OjPt5s3fKwqN"
  }
}
```




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 8. Códigos de Status e Tratamento de Erros




> **Resumo:** Descrição completa dos códigos de status HTTP retornados pelo endpoint e como gerenciar erros.




| Status Code               | Descrição Geral                                    |
| :------------------------ | :------------------------------------------------- |
| `200 OK`                  | Sucesso. A requisição foi processada com sucesso e as estatísticas foram retornadas.  |
| `400 Bad Request`         | Erro na requisição (parâmetros inválidos ou faltando). Verifique os dados enviados. |
| `401 Unauthorized`        | Falha na autenticação. Credenciais inválidas ou token expirado. |
| `403 Forbidden`           | Sem permissão. O usuário não tem direitos para acessar estatísticas deste produto ou conta. |
| `404 Not Found`           | Recurso não encontrado. O produto especificado não existe ou não está acessível. |
| `429 Too Many Requests`   | Rate Limit excedido. Aguarde antes de fazer novas solicitações. |
| `500 Internal Server Error`| Erro no servidor da API. Contate o suporte se persistir. |




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)




> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint de estatísticas.




1.  **Obter estatísticas gerais de vendas para todos os produtos**
    *   Objetivo: `Recuperar métricas consolidadas de todos os produtos da conta`
    *   Como Fazer: `GET /v1/stats`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


2.  **Consultar estatísticas de um produto específico**
    *   Objetivo: `Analisar o desempenho comercial de um único produto`
    *   Como Fazer: `GET /v1/stats?product_id=ba385b7c-cac1-4422-925d-7f707d8267d2`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


3.  **Analisar desempenho de vendas do mês atual**
    *   Objetivo: `Obter estatísticas do mês corrente para análise periódica`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-01&end_date=2023-09-15`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


4.  **Comparar estatísticas de vendas entre períodos**
    *   Objetivo: `Realizar análise comparativa de desempenho entre diferentes períodos`
    *   Como Fazer: `Duas chamadas: GET /v1/stats?start_date=2023-08-01&end_date=2023-08-31 e GET /v1/stats?start_date=2023-09-01&end_date=2023-09-30`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


5.  **Verificar taxa de aprovação de cartões no último trimestre**
    *   Objetivo: `Analisar tendências na taxa de aprovação de pagamentos com cartão`
    *   Como Fazer: `GET /v1/stats?start_date=2023-07-01&end_date=2023-09-30`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


6.  **Monitorar taxa de reembolso de um produto específico**
    *   Objetivo: `Verificar indicador de satisfação e qualidade através da taxa de reembolsos`
    *   Como Fazer: `GET /v1/stats?product_id=ba385b7c-cac1-4422-925d-7f707d8267d2`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


7.  **Avaliar eficiência de pagamentos por boleto**
    *   Objetivo: `Analisar a conversão entre boletos gerados e efetivamente pagos`
    *   Como Fazer: `GET /v1/stats e observar os campos total_boleto_generated, total_boleto_paid e boleto_rate`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


8.  **Criar dashboard semanal de vendas**
    *   Objetivo: `Obter dados recorrentes para alimentar um dashboard de monitoramento`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-10&end_date=2023-09-16`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


9.  **Analisar desempenho de vendas após campanha de marketing**
    *   Objetivo: `Medir o impacto de uma campanha específica nas vendas`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-01&end_date=2023-09-15 (período da campanha)`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


10. **Verificar incidência de chargebacks**
    *   Objetivo: `Monitorar e identificar possíveis problemas com chargebacks`
    *   Como Fazer: `GET /v1/stats e analisar o campo chargeback_rate`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


11. **Gerar relatório anual de vendas**
    *   Objetivo: `Compilar estatísticas de vendas para relatório anual`
    *   Como Fazer: `GET /v1/stats?start_date=2023-01-01&end_date=2023-12-31`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


12. **Monitorar vendas durante evento promocional**
    *   Objetivo: `Acompanhar em tempo real o desempenho durante promoção especial`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-15&end_date=2023-09-15 (dia atual)`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


13. **Analisar melhor produto em vendas**
    *   Objetivo: `Comparar estatísticas entre diferentes produtos para identificar o mais vendido`
    *   Como Fazer: `Múltiplas chamadas com product_id diferentes e comparar total_sales`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


14. **Verificar receita líquida total no período**
    *   Objetivo: `Obter dados financeiros consolidados para contabilidade`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-01&end_date=2023-09-30 e analisar total_net_amount`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


15. **Comparar métodos de pagamento mais eficientes**
    *   Objetivo: `Analisar qual método de pagamento apresenta maior conversão`
    *   Como Fazer: `GET /v1/stats e comparar credit_card_approval_rate com boleto_rate`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


16. **Identificar problemas em processamento de pagamentos**
    *   Objetivo: `Detectar quedas na taxa de aprovação para intervir rapidamente`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-14&end_date=2023-09-15 e monitorar credit_card_approval_rate`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


17. **Analisar desempenho de vendas por sazonalidade**
    *   Objetivo: `Identificar padrões sazonais nas vendas`
    *   Como Fazer: `Múltiplas chamadas com diferentes períodos e comparar resultados`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


18. **Reconciliar dados financeiros**
    *   Objetivo: `Confirmar montantes recebidos para reconciliação contábil`
    *   Como Fazer: `GET /v1/stats?start_date=2023-09-01&end_date=2023-09-30 e validar total_net_amount`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


19. **Configurar alertas para quedas em vendas**
    *   Objetivo: `Estabelecer sistema de alerta quando vendas caírem abaixo do esperado`
    *   Como Fazer: `GET /v1/stats com período recente e comparar total_sales com métricas históricas`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*


20. **Avaliar impacto de alterações de preço**
    *   Objetivo: `Medir como alterações de preço afetam volume de vendas e receita`
    *   Como Fazer: `GET /v1/stats?product_id=ba385b7c-cac1-4422-925d-7f707d8267d2 antes e depois da alteração`
    *(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 10. Notas Adicionais




> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint.




*   **Precisão dos Dados:** `As estatísticas são calculadas em tempo real no momento da requisição, considerando transações efetivamente processadas e registradas no sistema até o momento da consulta.`


*   **Valores Monetários:** `Todos os valores monetários (como total_net_amount) são representados em centavos da moeda base da conta (geralmente BRL), sem casas decimais.`


*   **Taxas Percentuais:** `Valores como credit_card_approval_rate, refund_rate, chargeback_rate e boleto_rate são expressos como números inteiros representando percentuais (ex: 50 significa 50%).`


*   **Período Padrão:** `Se start_date e end_date não forem especificados, a API retorna estatísticas dos últimos 30 dias.`


*   **Escopo dos Dados:** `As estatísticas são limitadas à conta especificada no cabeçalho x-kiwify-account-id e contemplam apenas transações a que o usuário autenticado tem permissão de acesso.`


*   **Atualização de Dados:** `As estatísticas podem ter um atraso de até 15 minutos para refletir as transações mais recentes.`




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)




> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.




```json
{
  "doc_id": "kiwify_sales_001",
  "api_provider": "Kiwify",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Consultar Estatísticas", "Obter Métricas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Confidential",
  "integration_priority": "Medium",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Estatísticas", "Vendas", "Pagamentos", "Produtos"],
  "context_level": ["intermediate"],
  "topic_cluster": ["vendas", "relatórios", "métricas"],
  "db_relations": { 
    "tables": ["sales", "products", "payments"], 
    "schemas": ["public", "reports"] 
  },
  "related_concepts": ["dashboard", "conversão", "aprovação", "reembolso", "chargeback"],
  "question_embeddings": [
    "Qual a taxa de aprovação de cartões de crédito na minha conta?",
    "Como posso consultar o valor total líquido de vendas de um produto?",
    "Qual a taxa de reembolso dos meus produtos?",
    "Como verificar quantos boletos foram pagos no mês passado?",
    "Como comparar estatísticas de vendas entre períodos diferentes?"
  ],
  "reasoning_pathways": ["comparative", "analytical", "sequential"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "API Key"],
  "typical_integration_points": ["Dashboard", "BI Systems", "Financial Reports"],
  "common_error_patterns": ["authentication_failure", "invalid_date_range", "product_not_found"]
}
```




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 12. Checklist de Implementação (Opcional)




> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação do endpoint.




- [ ] Autenticação
  - [ ] Implementar mecanismo de obtenção do token OAuth 2.0
  - [ ] Armazenar de forma segura o ID da conta (x-kiwify-account-id)
  - [ ] Configurar renovação automática do token expirado




- [ ] Tratamento de Erros (4xx, 5xx)
  - [ ] Implementar handlers para códigos comuns (401, 403, 404, 429)
  - [ ] Adicionar logging detalhado para debug
  - [ ] Apresentar mensagens amigáveis ao usuário final




- [ ] Validação de Entrada
  - [ ] Validar formatos de data (ISO 8601)
  - [ ] Verificar formato de UUID para product_id
  - [ ] Tratar campos obrigatórios vs. opcionais




- [ ] Mapeamento de Resposta
  - [ ] Converter valores percentuais para formato decimal se necessário
  - [ ] Transformar total_net_amount de centavos para unidades monetárias
  - [ ] Mapear campos para modelos de dados internos




- [ ] Logs & Monitoramento
  - [ ] Registrar tempo de resposta de cada chamada
  - [ ] Monitorar taxa de erros
  - [ ] Implementar rastreamento de requisições (request_id)




- [ ] Cache
  - [ ] Implementar cache para resultados frequentes (TTL: 15 minutos)
  - [ ] Definir estratégias de invalidação




- [ ] Testes
  - [ ] Criar testes unitários para mappers
  - [ ] Implementar testes de integração com mock
  - [ ] Verificar cenários de erro e exceção




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 13. Glossário de Termos Técnicos




> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados na documentação.




| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Taxa de Aprovação`       | `Percentual de transações com cartão de crédito que foram aprovadas pelo emissor do cartão em relação ao total tentado` |
| `Total Líquido`           | `Valor total das vendas após descontar taxas, impostos e outros custos operacionais` |
| `Taxa de Reembolso`       | `Percentual de vendas que resultaram em devolução do valor ao cliente em relação ao total de vendas` |
| `Chargeback`              | `Estorno forçado pelo emissor do cartão após contestação do cliente, geralmente sem consentimento do vendedor` |
| `Taxa de Chargeback`      | `Percentual de vendas que resultaram em chargeback em relação ao total de vendas` |
| `Boleto`                  | `Método de pagamento brasileiro que utiliza um documento bancário para liquidação posterior` |
| `Taxa de Boleto`          | `Percentual de boletos efetivamente pagos em relação ao total de boletos gerados` |
| `OAuth 2.0`               | `Protocolo de autorização que permite acesso seguro a recursos protegidos via tokens temporários` |
| `Bearer Token`            | `Tipo de token de autenticação que deve ser incluído no cabeçalho HTTP Authorization` |
| `Rate Limit`              | `Número máximo de requisições permitidas em um período de tempo específico` |




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


## 14. Observações Finais sobre Formatação




> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.




*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados e comparativos.
*   Use blocos de código (``` ```) com indicação de linguagem para exemplos de código e JSON.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa.
*   Formate nomes de parâmetros, campos e valores de exemplo com backticks (`exemplo`).
*   **Crucial:** Inclua `(Ref: [TITULO_CURTO], ID [ID_INTERNO])` no final de **CADA SEÇÃO PRINCIPAL (##)** e opcionalmente em subitens/chunks.
*   Mantenha os resumos de seção concisos (1-2 linhas) e informativos.
*   Use listas e bullets para informações sequenciais ou enumeradas.
*   Evite abreviações não explicadas ou jargão não definido no documento.




*(Ref: Kiwify Sales Stats, ID kiwify_salesstats_001)*
---


**(FIM DO DOCUMENTO)**