# API Hotmart - Assinaturas - Obter Compras de Assinantes (Get Subscription Purchases)


# 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Assinaturas - Obter Compras de Assinantes (Get Subscription Purchases) |
| **Identificador Interno** | hotmart_sub_001                                                 |
| **Título Curto (Ref.)**   | Hotmart Get Purchases                                           |
| **Versão do Documento**   | 1.0.0                                                           |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação Técnica                                  |
| **Fonte Original**        | Documentação Oficial Hotmart                                    |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/v1/subscription/get-subscription-purchases/ |
| **Status do Documento**   | Em Uso                                                          |
| **Ambiente de Referência**| Produção                                                        |
| **Idioma Original**       | Português (BR)                                                  |
| **Formato de Datas (API)**| Timestamp (ms)                                                  |
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 2. Contexto
Este endpoint permite listar os pagamentos de recorrências (assinaturas) vinculados a um subscriber_code específico na plataforma Hotmart. É fundamental para a gestão financeira de produtos de assinatura, permitindo acompanhar o histórico completo de transações, identificar status de pagamentos e realizar operações de pós-venda como reembolsos e análises de churn. A consulta é feita usando o código único do assinante, retornando todos os pagamentos recorrentes associados àquela assinatura, incluindo tanto pagamentos bem-sucedidos quanto falhos ou em processamento.
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 3. Visão Geral da API/Endpoint(s)
Este endpoint fornece uma interface completa para recuperar o histórico de transações de um assinante específico na plataforma Hotmart. Ele retorna um array com todas as transações realizadas, incluindo informações detalhadas como valor, moeda, status, método de pagamento, data de aprovação e número da recorrência. Esses dados são essenciais para relatórios financeiros, acompanhamento de ciclo de vida do cliente, processamento de reembolsos e análise de comportamento de pagamento. A consulta é feita exclusivamente via HTTP GET e requer autenticação por bearer token.
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 4. Detalhes Técnicos
### Obter Compras de Assinantes
* **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/subscriptions/:subscriber_code/purchases`
* **Método HTTP:** `GET`
* **Autenticação:** Bearer Token no header de Authorization (formato: `Authorization: Bearer :access_token`)
* **Content-Type:** application/json
* **Rate Limiting:** Os limites de requisição padrão da API Hotmart se aplicam (consulte documentação geral para valores atualizados)
* **Versão da API:** v1
* **Serviço:** payments API
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 5. Parâmetros de Entrada
### Obter Compras de Assinantes (Path Parameters)
| Parâmetro          | Descrição | Tipo |  Notas / Exemplo |
| :----------------- | :-------- | :--- | :-------------- |
| `subscriber_code`  | Código único que identifica um assinante no ecossistema Hotmart. Este código é gerado automaticamente quando uma assinatura é criada e permanece consistente durante toda a vida útil da assinatura, mesmo após renovações ou alterações de plano. | string | Exemplo: "ASUB123456". Não confundir com o ID do usuário ou código da compra. Este código é específico da relação de assinatura. |
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Obter Compras de Assinantes
#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `transaction` | Código único de referência da transação no sistema Hotmart. Este identificador pode ser usado em outras operações como reembolsos ou consultas específicas. | string |
| `approved_date` | Data e hora exatas em que o pagamento foi aprovado pela operadora financeira. Representado como timestamp Unix em milissegundos (epoch). | integer (timestamp) |
| `payment_engine` | Plataforma de processamento de pagamento utilizada para processar a transação. Pode ser "HotPay" (para pagamentos locais em alguns países) ou "HotPay Internacional" (para pagamentos internacionais). | string |
| `status` | Status atual do pagamento no ciclo de vida da transação. Este campo indica a situação exata da transação no momento da consulta. Veja a lista completa de status possíveis na seção de Notas Adicionais. | string |
| `price` | Objeto contendo informações detalhadas sobre o valor monetário da transação e moeda utilizada. | object |
| `payment_type` | Categoria ampla do método de pagamento utilizado pelo comprador. Indica o tipo de instrumento financeiro (cartão, boleto, transferência, etc). | string |
| `payment_method` | Método específico de pagamento dentro da categoria. Fornece detalhes precisos sobre o instrumento de pagamento, como bandeira do cartão ou tipo específico de transferência bancária. | string |
| `recurrency_number` | Número sequencial que indica qual recorrência da assinatura esta compra representa. Começa em 1 para o primeiro pagamento e incrementa a cada ciclo de cobrança. | integer |
| `under_warranty` | Indicador booleano que mostra se a transação ainda está dentro do período de garantia definido para o produto. Relevante para políticas de reembolso. | boolean |
| `purchase_subscription` | Indicador booleano que confirma se esta compra está associada a um produto de assinatura (recorrente) em oposição a uma compra única. Para este endpoint, normalmente será sempre "true". | boolean |


#### 6.1.2 Detalhes do Objeto `price`
| Campo Aninhado | Descrição | Tipo | Notas |
| :------------- | :-------- | :--- | :---- |
| `value` | Valor monetário da transação. Representa o montante exato cobrado do cliente nesta recorrência específica, incluindo descontos ou acréscimos aplicados. | float | Usa ponto como separador decimal. Exemplo: 108.0, 29.99, 199.90 |
| `currency_code` | Código da moeda utilizada na transação, seguindo o padrão internacional ISO 4217 de três letras. | string | Exemplos: "BRL" (Real Brasileiro), "USD" (Dólar Americano), "EUR" (Euro), "MXN" (Peso Mexicano) |
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 7. Exemplos de Requisição e Resposta
### Obter Compras de Assinantes
#### 7.1.1 Exemplo de Requisição (cURL)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/subscriptions/ASUB12345678/purchases' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```
#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
[
  {
    "transaction": "HP12315823516751",
    "approved_date": 1583331578000,
    "payment_engine": "HotPay",
    "status": "APPROVED",
    "price": {
      "value": 108.0,
      "currency_code": "BRL"
    },
    "payment_type": "CREDIT_CARD",
    "payment_method": "CREDIT_CARD_VISA",
    "recurrency_number": 1,
    "under_warranty": false,
    "purchase_subscription": true
  },
  {
    "transaction": "HP12319946872159",
    "approved_date": 1586009978000,
    "payment_engine": "HotPay",
    "status": "APPROVED",
    "price": {
      "value": 108.0,
      "currency_code": "BRL"
    },
    "payment_type": "CREDIT_CARD",
    "payment_method": "CREDIT_CARD_VISA",
    "recurrency_number": 2,
    "under_warranty": false,
    "purchase_subscription": true
  }
]
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro 404)
```json
{
  "code": "resource_not_found",
  "message": "Não foi encontrado o código de assinante informado"
}
```
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code | Descrição Geral |
| :---------- | :-------------- |
| `200 OK` | Sucesso. Retorna a lista de compras vinculadas ao assinante. Se o assinante existe mas não possui compras, retorna um array vazio `[]`. |
| `400 Bad Request` | Erro na requisição. Geralmente ocorre quando o formato do subscriber_code é inválido ou mal-formado. Verifique se está enviando um código no formato correto. |
| `401 Unauthorized` | Falha na autenticação. O token de acesso é inválido, expirou ou não tem as permissões necessárias. Obtenha um novo token de acesso. |
| `403 Forbidden` | Sem permissão. O token é válido, mas o usuário não tem permissão para acessar este recurso específico. Verifique se a conta tem as permissões necessárias na plataforma Hotmart. |
| `404 Not Found` | Assinante não encontrado. O subscriber_code fornecido não existe no sistema Hotmart ou pertence a outro produtor/vendedor. |
| `429 Too Many Requests` | Limite de requisições excedido. Respeite os limites de rate limiting da API Hotmart. |
| `500 Internal Server Error` | Erro interno no servidor da API Hotmart. Tente novamente mais tarde. Se o erro persistir, contate o suporte Hotmart. |
| `503 Service Unavailable` | Serviço temporariamente indisponível. A API Hotmart pode estar em manutenção ou experimentando alto volume de requisições. |
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1. **Verificar o histórico completo de pagamentos de um assinante**
   * Objetivo: Obter cronologia completa de todos os pagamentos realizados por um determinado assinante
   * Como Fazer: Realizar requisição GET com o subscriber_code e ordenar os resultados por recurrency_number ou approved_date
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


2. **Verificar status do último pagamento de assinatura**
   * Objetivo: Confirmar se o pagamento mais recente foi processado com sucesso
   * Como Fazer: Ordenar os resultados por recurrency_number (decrescente) e verificar o status do primeiro item. Por exemplo, se status="APPROVED", o último pagamento foi bem-sucedido
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


3. **Calcular o valor total gasto por um assinante**
   * Objetivo: Somar todos os pagamentos aprovados de um assinante para análise de LTV (Lifetime Value)
   * Como Fazer: Filtrar registros com status="APPROVED" e somar os valores price.value. Exemplo: assinante com 12 pagamentos de R$108,00 = R$1.296,00 de LTV
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


4. **Identificar pagamentos em atraso**
   * Objetivo: Encontrar assinaturas com pagamentos pendentes para followup
   * Como Fazer: Verificar registros com status="OVERDUE" e agrupar por subscriber_code para criar uma lista de assinantes com pagamentos atrasados
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


5. **Processar reembolso para um pagamento específico**
   * Objetivo: Obter o transaction ID necessário para iniciar um processo de reembolso
   * Como Fazer: Localizar o pagamento específico pelo recurrency_number e extrair o código transaction (ex: "HP12315823516751") para usar na API de reembolso
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


6. **Verificar se compra está no período de garantia**
   * Objetivo: Determinar se cliente tem direito a reembolso por garantia contratual
   * Como Fazer: Verificar o campo under_warranty=true na transação específica. Se true, o cliente ainda está dentro do período de garantia e tem direito ao reembolso automático
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


7. **Rastrear o histórico de um pagamento específico**
   * Objetivo: Obter detalhes completos de uma transação específica para resolução de disputas
   * Como Fazer: Filtrar a resposta da API pelo código transaction específico (ex: "HP12315823516751") para isolar os dados daquela transação
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


8. **Determinar a data do próximo pagamento**
   * Objetivo: Prever quando ocorrerá a próxima cobrança para comunicação proativa com cliente
   * Como Fazer: Pegar approved_date da última transação (maior recurrency_number), converter de timestamp para data legível e adicionar o período da assinatura (30 dias para mensal, 365 para anual)
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


9. **Verificar método de pagamento atual**
   * Objetivo: Identificar qual instrumento de pagamento está sendo utilizado para recorrências
   * Como Fazer: Observar os campos payment_type (ex: "CREDIT_CARD") e payment_method (ex: "CREDIT_CARD_VISA") da transação com maior recurrency_number
   *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


10. **Identificar mudanças no valor da assinatura**
    * Objetivo: Detectar alterações no valor cobrado ao longo do tempo que possam indicar upgrades, downgrades ou promoções
    * Como Fazer: Comparar o campo price.value entre diferentes payments ordenados por recurrency_number. Exemplo: se recurrency_number 1-3 tem price.value=99.90 e 4-6 tem price.value=149.90, houve um upgrade ou aumento de preço
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


11. **Identificar pagamentos com chargebacks**
    * Objetivo: Localizar transações contestadas pelo cliente junto à operadora de cartão
    * Como Fazer: Filtrar registros com status="CHARGEBACK" para identificar disputas abertas ou finalizadas contra o produtor
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


12. **Verificar a quantidade de recorrências já pagas**
    * Objetivo: Determinar há quanto tempo o cliente é assinante e sua fidelidade
    * Como Fazer: Contar o número de registros com status="APPROVED" ou verificar o maior valor de recurrency_number. Exemplo: recurrency_number=12 indica um ano de assinatura mensal
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


13. **Comparar taxas de conversão entre métodos de pagamento**
    * Objetivo: Avaliar quais métodos de pagamento têm maior taxa de aprovação para otimizar checkout
    * Como Fazer: Agrupar registros por payment_method e calcular % de status="APPROVED" vs outros status. Exemplo: 98% de aprovação em CREDIT_CARD_VISA vs 85% em BILLET
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


14. **Gerar relatório de assinaturas canceladas**
    * Objetivo: Listar assinaturas encerradas por cancelamento para análise de churn
    * Como Fazer: Filtrar registros com status="CANCELLED" e agrupar por subscriber_code, calculando quando ocorreu o cancelamento (após qual recurrency_number)
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


15. **Verificar a moeda utilizada nas transações**
    * Objetivo: Identificar em qual moeda o cliente realiza os pagamentos para relatórios financeiros segmentados
    * Como Fazer: Verificar o campo price.currency_code (ex: "BRL", "USD", "EUR") para identificar a moeda de cobrança de cada assinante
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


16. **Identificar falhas em processamento de pagamento**
    * Objetivo: Detectar problemas técnicos com processamento de pagamentos para resolução proativa
    * Como Fazer: Filtrar registros com status="PROCESSING_TRANSACTION" com approved_date anterior a 24h, indicando possível falha no processamento
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


17. **Verificar histórico de reembolsos parciais**
    * Objetivo: Identificar pagamentos que receberam reembolso parcial para controle financeiro
    * Como Fazer: Filtrar registros com status="PARTIALLY_REFUNDED" e analisar o impacto financeiro das devoluções parciais
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


18. **Monitorar pagamentos em análise de risco**
    * Objetivo: Acompanhar pagamentos retidos em análise antifraude para comunicação adequada com clientes
    * Como Fazer: Filtrar registros com status="UNDER_ANALISYS" e monitorar quanto tempo permanecem neste estado antes da aprovação ou rejeição
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


19. **Verificar fidelidade do assinante**
    * Objetivo: Determinar há quanto tempo (em dias) o cliente mantém a assinatura ativa para programas de fidelidade
    * Como Fazer: Calcular o período entre o primeiro (menor approved_date) e o último pagamento aprovado (maior approved_date). Exemplo: (1612137600000 - 1583331578000) / (1000 * 60 * 60 * 24) = 334 dias de assinatura
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*


20. **Identificar pagamentos aguardando confirmação**
    * Objetivo: Listar pagamentos pendentes de confirmação para acompanhamento
    * Como Fazer: Filtrar registros com status="WAITING_PAYMENT" e monitorar sua evolução, especialmente boletos (BILLET) que aguardam compensação bancária
    *(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 10. Notas Adicionais
* **Descrição Detalhada dos Status de Compra:** 
  * `APPROVED`: Pagamento aprovado e processado com sucesso
  * `BLOCKED`: Pagamento bloqueado por questões de segurança ou compliance
  * `CANCELLED`: Assinatura cancelada pelo usuário ou produtor
  * `CHARGEBACK`: Transação contestada pelo cliente junto à operadora do cartão
  * `COMPLETE`: Transação finalizada com sucesso (usado em alguns cenários específicos)
  * `EXPIRED`: O período para pagamento expirou (comum em boletos)
  * `NO_FUNDS`: Transação recusada por insuficiência de fundos
  * `OVERDUE`: Pagamento em atraso
  * `PARTIALLY_REFUNDED`: Reembolso parcial foi processado
  * `PRE_ORDER`: Pré-venda (raro em assinaturas)
  * `PRINTED_BILLET`: Boleto foi gerado mas ainda não foi pago
  * `PROCESSING_TRANSACTION`: Pagamento em processamento
  * `PROTESTED`: Pagamento com problema grave reportado
  * `REFUNDED`: Transação totalmente reembolsada
  * `STARTED`: Processo de pagamento iniciado
  * `UNDER_ANALISYS`: Pagamento em análise de risco/fraude
  * `WAITING_PAYMENT`: Aguardando confirmação de pagamento


* **Detalhes sobre Métodos de Pagamento:** 
  * A disponibilidade de métodos de pagamento varia por país e configuração da conta Hotmart
  * O campo payment_type indica a categoria geral (ex: CREDIT_CARD, BILLET, PIX)
  * O campo payment_method é mais específico e inclui bandeiras de cartão ou variantes específicas (ex: CREDIT_CARD_VISA, CREDIT_CARD_MASTERCARD)


* **Recomendações de Implementação:**
  * Armazene o subscriber_code em seu sistema para consultas futuras
  * Implemente cache para reduzir chamadas repetidas ao endpoint
  * Para assinaturas ativas, consulte este endpoint regularmente (a cada 24h) para detectar mudanças de status
  * Tenha tratamento especial para status de transição como PROCESSING_TRANSACTION e WAITING_PAYMENT


* **Limitações Importantes:**
  * Este endpoint retorna apenas compras dentro da assinatura, não outras compras do mesmo cliente
  * Não são retornados dados pessoais do assinante, apenas da transação
  * O timestamp approved_date está em UTC/GMT
  * Para assinaturas antigas ou com muitas recorrências, considere implementar paginação na sua aplicação para processar os resultados


* **Segurança e Compliance:**
  * Todos os dados financeiros retornados devem ser tratados conforme regulamentações locais (LGPD, PCI-DSS, etc.)
  * Recomenda-se não armazenar informações completas de pagamento em seu sistema
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sub_001",
  "api_provider": "Hotmart",
  "api_product_area": "Assinaturas",
  "endpoint_focus": ["Obter Compras", "Listar Pagamentos"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Financial",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Assinante", "Compra", "Pagamento", "Recorrência"],
  "context_level": ["intermediate"],
  "topic_cluster": ["pagamentos", "assinaturas", "financeiro", "recorrência"],
  "db_relations": { 
    "tables": ["subscribers", "purchases", "payments", "subscriptions"], 
    "schemas": ["hotmart_financial", "hotmart_customers"] 
  },
  "related_concepts": [
    "reembolso", 
    "garantia", 
    "status de pagamento", 
    "recorrência", 
    "chargeback",
    "ciclo de vida do assinante",
    "LTV",
    "churn"
  ],
  "question_embeddings": [
    "Quais são as compras de um assinante específico?",
    "Como verificar o histórico de pagamentos de uma assinatura?",
    "O que significa cada status de pagamento na API Hotmart?",
    "Como identificar se um cliente está no período de garantia?",
    "Como obter o código de transação para processar um reembolso?",
    "Qual é o método de pagamento atual de um assinante?",
    "Quantas recorrências um assinante já pagou?"
  ],
  "reasoning_pathways": [
    "identificação", 
    "validação", 
    "análise financeira",
    "cálculo de LTV",
    "detecção de churn",
    "processamento de reembolso",
    "previsão de pagamentos futuros"
  ],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*
---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação com Bearer Token
- [ ] Validação do formato do subscriber_code antes do envio
- [ ] Tratamento de Erros (4xx, 5xx)
- [ ] Retries com backoff exponencial para erros 429 e 5xx
- [ ] Validação de resposta (verificar se é uma lista válida)
- [ ] Mapeamento de Response para modelo de dados interno
- [ ] Logs com transactionId para rastreabilidade
- [ ] Monitoramento de tempo de resposta da API
- [ ] Cache da resposta por 1h para subscriber_codes frequentemente consultados
- [ ] Testes para cenários de assinante com múltiplas compras
- [ ] Testes para assinante inexistente
- [ ] Tratamento dos diferentes status de pagamento
- [ ] Implementação de lógica para cálculo de próximo pagamento
- [ ] Funcionalidade para detectar alterações de status entre consultas
- [ ] Sistema de alerta para transações problemáticas (CHARGEBACK, OVERDUE)
- [ ] Rotina de sincronização periódica para assinantes ativos
*(Ref: Hotmart Get Subscription Purchases, ID hotmart_getsubscriptionpurchases_001)*