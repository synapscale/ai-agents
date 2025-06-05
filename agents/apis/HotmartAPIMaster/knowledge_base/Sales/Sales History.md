# API Hotmart - Vendas - Obter Histórico de Vendas (Sales History)


## 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Vendas - Obter Histórico de Vendas (Sales History) |
| **Identificador Interno** | hotmart_sales_001                                               |
| **Título Curto (Ref.)**   | Hotmart Sales History                                           |
| **Versão do Documento**   | 1.0.0                                                           |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação API                                      |
| **Fonte Original**        | https://developers.hotmart.com/docs/pt-BR/v1/sales/sales-history/ |
| **URL de Referência**     | https://developers.hotmart.com/payments/api/v1/sales/history    |
| **Status do Documento**   | Em Uso                                                          |
| **Ambiente de Referência**| Produção                                                        |
| **Idioma Original**       | Português (BR)                                                  |
| **Formato de Datas (API)**| Timestamp (ms) desde 1970-01-01 00:00:00 UTC                    |
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 2. Contexto
Este endpoint permite aos usuários da plataforma Hotmart acessar o histórico de vendas realizadas, fornecendo informações detalhadas sobre transações, compradores, produtos e status de pagamento. É uma ferramenta essencial para monitoramento de vendas, análise financeira e gestão de clientes na plataforma Hotmart. O endpoint faz parte da API de Pagamentos da Hotmart, que fornece acesso programático a dados financeiros e transacionais da plataforma. Através deste endpoint, é possível extrair dados históricos de vendas para uso em relatórios, integrações com sistemas de CRM, análises financeiras e acompanhamento de desempenho de vendas.
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 3. Visão Geral da API/Endpoint(s)
O endpoint de Histórico de Vendas fornece uma lista completa das transações de vendas realizadas na Hotmart, com opções de filtragem por diversos parâmetros como status da transação, data, produto, nome do comprador e método de pagamento. Este endpoint retorna informações essenciais sobre cada venda, incluindo detalhes do produto, do comprador, do produtor e da própria transação. A resposta é paginada para facilitar o gerenciamento de grandes volumes de dados, possibilitando a navegação através de tokens de página.


O endpoint suporta diversos filtros que permitem consultas específicas, como vendas realizadas em um período particular, vendas de determinado produto, ou vendas com um status específico. Esta flexibilidade torna o endpoint uma ferramenta poderosa para análise de dados de vendas e monitoramento de negócios na plataforma Hotmart.
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
##
## 4. Detalhes Técnicos
### Histórico de Vendas
* **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/sales/history`
* **Método HTTP:** `GET`
* **Autenticação:** OAuth 2.0 - Bearer Token (Authorization: Bearer :access_token)
* **Base URL:** `https://developers.hotmart.com/payments/api/v1`
* **Content-Type:** `application/json`
* **Codificação:** UTF-8
* **Suporte CORS:** Sim
* **Rate Limits:** Não especificado na documentação, recomenda-se implementar backoff exponencial
* **Timeout recomendado:** 30 segundos
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 5. Parâmetros de Entrada
### Histórico de Vendas (/sales/history) (Query Parameters)
| Parâmetro          | Descrição | Tipo | Notas / Exemplo |
| :----------------- | :-------- | :--- | :-------------- |
| `transaction`      | Código único de referência para uma transação. Uma transação acontece quando um pedido é efetuado. | string | Exemplo: HP17715690036014. Este código é gerado automaticamente pela Hotmart e permite rastrear transações específicas. |
| `transaction_status` | Status atual da compra. Filtra transações pelo seu estado de processamento atual. | string | Valores possíveis incluem: APPROVED (Aprovada), BLOCKED (Bloqueada), CANCELLED (Cancelada), CHARGEBACK (Estorno), COMPLETE (Completa), EXPIRED (Expirada), NO_FUNDS (Sem fundos), OVERDUE (Atrasada), PARTIALLY_REFUNDED (Reembolso parcial), PRE_ORDER (Pré-venda), PRINTED_BILLET (Boleto impresso), PROCESSING_TRANSACTION (Em processamento), PROTESTED (Protestada), REFUNDED (Reembolsada), STARTED (Iniciada), UNDER_ANALISYS (Em análise), WAITING_PAYMENT (Aguardando pagamento). |
| `max_results`      | Número máximo de itens a serem retornados por página. Controla a quantidade de registros na resposta. | integer | Valores típicos: 10, 20, 50, 100. Se não fornecido, o sistema utilizará um valor padrão. |
| `page_token`       | Token de paginação que serve como cursor para a parte específica da lista que se deseja consultar. | string | Obtido da resposta anterior através dos campos next_page_token ou prev_page_token. Codificado em Base64. |
| `product_id`       | Identificador único (ID) do produto vendido. Permite filtrar vendas de um produto específico. | integer | Número de 7 dígitos que identifica o produto na plataforma Hotmart. Exemplo: 2125812. |
| `start_date`       | Data inicial do período para o filtro. Marca o início do intervalo de tempo para busca de vendas. | long | Timestamp em milissegundos desde 1970-01-01 00:00:00 UTC. Exemplo: 1622505600000 (01/06/2021 00:00:00). |
| `end_date`         | Data final do período para o filtro. Marca o fim do intervalo de tempo para busca de vendas. | long | Timestamp em milissegundos desde 1970-01-01 00:00:00 UTC. Exemplo: 1625097599000 (30/06/2021 23:59:59). |
| `sales_source`     | Código SRC utilizado no link da página de pagamento do produto para identificar a origem da venda. | string | Exemplos: INSTAGRAM, FACEBOOK, EMAIL_MARKETING. Utilizado para rastrear campanhas de marketing ou canais de aquisição. |
| `buyer_name`       | Nome da pessoa compradora. Permite filtrar vendas por nome do cliente. | string | Busca por nome completo ou parcial do comprador. Não diferencia maiúsculas/minúsculas. |
| `buyer_email`      | E-mail da pessoa compradora. Permite filtrar vendas pelo endereço de email do cliente. | string | Deve ser um endereço de email válido. Não diferencia maiúsculas/minúsculas. |
| `payment_type`     | Tipo de pagamento utilizado pela pessoa compradora para realizar a compra. | string | Valores possíveis incluem: BILLET (Boleto), CASH_PAYMENT (Dinheiro), CREDIT_CARD (Cartão de crédito), DIRECT_BANK_TRANSFER (Transferência bancária), DIRECT_DEBIT (Débito direto), FINANCED_BILLET (Boleto financiado), FINANCED_INSTALLMENT (Parcelamento financiado), GOOGLE_PAY, HOTCARD, HYBRID (Híbrido), MANUAL_TRANSFER (Transferência manual), PAYPAL, PAYPAL_INTERNACIONAL, PICPAY, PIX, SAMSUNG_PAY, WALLET (Carteira virtual). |
| `offer_code`       | Código de oferta do produto vendido. Identifica uma oferta específica dentro do produto. | string | Exemplo: k2pasun0. Utilizado para rastrear conversões de ofertas específicas. |
| `commission_as`    | Indica como o usuário da conta foi comissionado pela venda. | string | Valores possíveis: PRODUCER (comissionado como produtor), COPRODUCER (comissionado como coprodutor), AFFILIATE (comissionado como afiliado). |
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Histórico de Vendas (/sales/history)
#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `items`       | Lista de vendas retornadas conforme os filtros aplicados. Contém os detalhes completos de cada transação. | array |
| `page_info`   | Informações de paginação para facilitar a navegação entre os resultados. | object |


#### 6.1.2 Detalhes do Objeto `items`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `product`           | Dados do produto vendido. | object | Contém informações básicas do produto comercializado. |
| `product.name`      | Nome do produto. | string | Nome comercial do produto na plataforma Hotmart. |
| `product.id`        | Identificador único do produto. | integer | Número de 7 dígitos que identifica o produto. |
| `buyer`             | Dados do comprador da transação. | object | Informações disponíveis apenas se o comprador as forneceu no ato da compra. |
| `buyer.name`        | Nome do comprador. | string | Nome completo da pessoa que realizou a compra. |
| `buyer.ucode`       | Identificador único do comprador. | string | Código UUID que identifica o comprador na plataforma. |
| `buyer.email`       | E-mail do comprador. | string | Endereço de email fornecido pelo comprador. |
| `producer`          | Informações do produtor do produto. | object | Dados sobre o criador/vendedor do produto. |
| `producer.name`     | Nome do produtor. | string | Nome completo do produtor do conteúdo. |
| `producer.ucode`    | Identificador único do produtor. | string | Código UUID que identifica o produtor na plataforma. |
| `purchase`          | Detalhes completos da compra/transação. | object | Contém todas as informações relacionadas à transação. |


#### 6.1.3 Detalhes do Objeto `purchase`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `transaction`       | Código único de referência da transação. | string | Identificador único no formato HPXXXXXXXXXX. |
| `order_date`        | Data em que o pedido foi realizado. | long | Timestamp em ms desde 1970-01-01 00:00:00 UTC. |
| `approved_date`     | Data em que o pedido foi aprovado. | long | Timestamp em ms desde 1970-01-01 00:00:00 UTC. |
| `status`            | Status atual da transação. | string | Valores possíveis listados no parâmetro transaction_status. |
| `recurrency_number` | Número da recorrência para compras parceladas. | integer | 1 para primeira parcela, 2 para segunda, etc. |
| `is_subscription`   | Indica se o pedido é do tipo assinatura. | boolean | true para assinaturas, false para compras únicas. |
| `commission_as`     | Como o usuário da conta foi comissionado. | string | PRODUCER, COPRODUCER ou AFFILIATE. |
| `price`             | Detalhes do valor da compra. | object | Contém valor e moeda. |
| `price.value`       | Valor total pago pelo comprador. | float | Inclui taxas e juros. |
| `price.currency_code` | Código da moeda utilizada. | string | Padrão internacional de 3 letras (USD, BRL, EUR). |
| `payment`           | Informações sobre o método de pagamento. | object | Detalhes de como o pagamento foi processado. |
| `payment.method`    | Método específico de pagamento utilizado. | string | Equivalente ao payment_type nos parâmetros de entrada. |
| `payment.installments_number` | Número total de parcelas. | integer | 1 para pagamento à vista. |
| `payment.type`      | Tipo geral de pagamento utilizado. | string | Categoria do método de pagamento. |
| `tracking`          | Códigos de rastreamento da origem da venda. | object | Informações para análise de canais de venda. |
| `tracking.source_sck` | Código de rastreamento do produtor. | string | Código personalizado definido pelo produtor. |
| `tracking.source`   | Código de rastreamento referente ao campo src. | string | Identifica a fonte da venda (ex: HOTMART, INSTAGRAM). |
| `tracking.external_code` | Código de rastreamento externo. | string | Código adicional para rastreamento personalizado. |
| `warranty_expire_date` | Data de vencimento da garantia. | long | Timestamp em ms desde 1970-01-01 00:00:00 UTC. |
| `offer`             | Informações sobre a oferta do produto. | object | Detalhes da oferta específica adquirida. |
| `offer.payment_mode` | Modo de pagamento da compra. | string | Formato de cobrança (ex: INVOICE, SUBSCRIPTION). |
| `offer.code`        | Código identificador da oferta. | string | Código único da oferta dentro do produto. |
| `hotmart_fee`       | Informações sobre as tarifas cobradas pela Hotmart. | object | Detalhamento dos valores retidos pela plataforma. |
| `hotmart_fee.total` | Tarifa total cobrada pela Hotmart. | float | Soma das tarifas percentual e fixa. |
| `hotmart_fee.fixed` | Tarifa fixa cobrada pela Hotmart. | float | Valor fixo independente do valor da venda. |
| `hotmart_fee.currency_code` | Moeda das tarifas. | string | Padrão internacional de 3 letras. |
| `hotmart_fee.base`  | Valor base para cálculo da tarifa. | float | Valor sobre o qual o percentual é aplicado. |
| `hotmart_fee.percentage` | Percentual aplicado sobre o valor base. | float | Taxa percentual cobrada pela plataforma. |


#### 6.1.4 Detalhes do Objeto `page_info`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `total_results`     | Total de itens na lista completa. | integer | Número total de registros que correspondem aos filtros aplicados, independente da paginação. |
| `next_page_token`   | Token para acessar a próxima página. | string | String codificada em Base64 que deve ser usada no parâmetro page_token para avançar para a próxima página. Será null se não houver mais páginas. |
| `prev_page_token`   | Token para acessar a página anterior. | string | String codificada em Base64 que deve ser usada no parâmetro page_token para retornar à página anterior. Será null na primeira página. |
| `results_per_page`  | Quantidade de itens na página atual. | integer | Número de resultados retornados na resposta atual, pode ser menor que max_results na última página. |
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 7. Exemplos de Requisição e Resposta
### Histórico de Vendas (/sales/history)
#### 7.1.1 Exemplo de Requisição (cURL)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/sales/history?transaction_status=APPROVED&start_date=1622505600000&end_date=1625097599000&max_results=5' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
{
  "items": [
    {
      "product": {
        "name": "Product06",
        "id": 2125812
      },
      "buyer": {
        "name": "Ian Victor Baptista",
        "ucode": "839F1A4F-43DC-F60F-13FE-6C8BD23F6781",
        "email": "ian@teste.com"
      },
      "producer": {
        "name": "Bárbara Sebastiana Cardoso",
        "ucode": "252A74C5-4A97-143A-9349-E45D871C6018"
      },
      "purchase": {
        "transaction": "HP12455690122399",
        "order_date": 1622948400000,
        "approved_date": 1622948400000,
        "status": "UNDER_ANALISYS",
        "recurrency_number": 2,
        "is_subscription": false,
        "commission_as": "PRODUCER",
        "price": {
          "value": 235.76,
          "currency_code": "USD"
        },
        "payment": {
          "method": "BILLET",
          "installments_number": 1,
          "type": "BILLET"
        },
        "tracking": {
          "source_sck": "HOTMART_PRODUCT_PAGE",
          "source": "HOTMART",
          "external_code": "FD256D24-401C-7C93-284C-C5E0181CD5DB"
        },
        "warranty_expire_date": 1625022000000,
        "offer": {
          "payment_mode": "INVOICE",
          "code": "k2pasun0"
        },
        "hotmart_fee": {
          "total": 36.75,
          "fixed": 0,
          "currency_code": "EUR",
          "base": 11.12,
          "percentage": 9.9
        }
      }
    }
  ],
  "page_info": {
    "total_results": 14,
    "next_page_token": "eyJyb3dzIjo1LCJwYWdlIjozfQ==",
    "prev_page_token": "eyJyb3dzIjo1LCJwYWdlIjoxfQ==",
    "results_per_page": 5
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro)
```json
{
  "code": "UNAUTHORIZED",
  "message": "Invalid access token",
  "details": [
    "The provided authorization token has expired or is invalid"
  ]
}
```
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              |
| :--------------------- | :----------------------------------------------------------- |
| `200 OK`               | Sucesso. Retorna a lista de vendas conforme solicitado. O corpo da resposta conterá a estrutura de dados descrita na seção 6. |
| `400 Bad Request`      | Erro na requisição. Os parâmetros fornecidos são inválidos ou mal formatados. Verifique os tipos de dados, formatos de data e valores permitidos para cada parâmetro. |
| `401 Unauthorized`     | Falha na autenticação. O token de acesso é inválido, expirou ou não foi fornecido. Renove o token de acesso utilizando o fluxo de autenticação OAuth 2.0. |
| `403 Forbidden`        | Sem permissão. O token de acesso é válido, mas não possui as permissões necessárias para acessar os dados solicitados. Verifique os escopos do token. |
| `404 Not Found`        | Recurso não encontrado. O endpoint solicitado não existe ou os parâmetros fornecidos não retornam nenhum resultado. |
| `429 Too Many Requests`| Rate Limit excedido. Muitas requisições foram feitas em um curto período. Implemente um mecanismo de backoff exponencial e tente novamente após o período indicado no header Retry-After. |
| `500 Internal Server Error` | Erro no servidor da API Hotmart. Problema interno no processamento da requisição. Tente novamente mais tarde e, se o erro persistir, entre em contato com o suporte Hotmart. |
| `503 Service Unavailable` | Serviço temporariamente indisponível. A API está em manutenção ou sobrecarregada. Aguarde alguns minutos e tente novamente com uma estratégia de retry. |


### 8.1 Estratégia de Tratamento de Erros Recomendada
1. **Erros 4xx (exceto 429)**: Corrigir a requisição conforme a mensagem de erro retornada. Estes erros são causados por problemas na requisição e não devem ser retentados sem modificação.


2. **Erro 429**: Implementar retry com backoff exponencial, respeitando o header Retry-After se presente.
   ```javascript
   // Pseudocódigo para retry com backoff exponencial
   let retries = 0;
   const maxRetries = 5;
   const baseDelay = 1000; // 1 segundo
   
   function fetchWithRetry() {
     return fetch(url, options).catch(error => {
       if (error.status === 429 && retries < maxRetries) {
         const retryAfter = error.headers.get('Retry-After') || Math.pow(2, retries) * baseDelay;
         retries++;
         return new Promise(resolve => setTimeout(resolve, retryAfter)).then(fetchWithRetry);
       }
       throw error;
     });
   }
   ```


3. **Erros 5xx**: Implementar retry com backoff exponencial para erros temporários do servidor.
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1. **Listar todas as vendas aprovadas**
   * Objetivo: Obter uma lista de todas as vendas com status APPROVED
   * Como Fazer: Enviar GET request com parâmetro transaction_status=APPROVED
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


2. **Obter vendas de um período específico**
   * Objetivo: Recuperar vendas realizadas entre 01/06/2023 e 30/06/2023
   * Como Fazer: Utilizar parâmetros start_date=1685577600000 e end_date=1688169599000 (timestamps para as datas mencionadas)
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


3. **Filtrar vendas por produto específico**
   * Objetivo: Visualizar apenas vendas de um produto determinado
   * Como Fazer: Adicionar parâmetro product_id=2125812 (substitua pelo ID do seu produto)
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


4. **Localizar vendas por nome do comprador**
   * Objetivo: Encontrar todas as compras feitas por um cliente específico
   * Como Fazer: Usar parâmetro buyer_name="Ian Victor Baptista" (o sistema buscará correspondências parciais também)
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


5. **Filtrar vendas por e-mail do comprador**
   * Objetivo: Encontrar compras vinculadas a um e-mail específico
   * Como Fazer: Utilizar parâmetro buyer_email="ian@teste.com"
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


6. **Verificar vendas realizadas via PIX**
   * Objetivo: Listar apenas vendas cujo pagamento foi feito via PIX
   * Como Fazer: Adicionar parâmetro payment_type=PIX
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


7. **Verificar status de uma transação específica**
   * Objetivo: Obter detalhes de uma transação usando seu código único
   * Como Fazer: Usar parâmetro transaction=HP12455690122399 (substitua pelo código da transação específica)
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


8. **Listar vendas em análise**
   * Objetivo: Identificar todas as vendas com status "em análise" para acompanhamento
   * Como Fazer: Usar parâmetro transaction_status=UNDER_ANALISYS
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


9. **Verificar vendas que foram canceladas**
   * Objetivo: Obter lista de vendas canceladas para análise de churn
   * Como Fazer: Usar parâmetro transaction_status=CANCELLED
   *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


10. **Identificar vendas com chargebacks**
    * Objetivo: Rastrear vendas que sofreram estorno para gestão financeira
    * Como Fazer: Usar parâmetro transaction_status=CHARGEBACK
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


11. **Verificar vendas com pagamento pendente**
    * Objetivo: Listar vendas aguardando pagamento para acompanhamento
    * Como Fazer: Usar parâmetro transaction_status=WAITING_PAYMENT
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


12. **Verificar vendas realizadas via boleto**
    * Objetivo: Listar vendas com pagamento via boleto bancário para análise de método de pagamento
    * Como Fazer: Usar parâmetro payment_type=BILLET
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


13. **Verificar vendas com pagamento via cartão de crédito**
    * Objetivo: Listar apenas vendas pagas com cartão de crédito para análise de método de pagamento preferido
    * Como Fazer: Usar parâmetro payment_type=CREDIT_CARD
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


14. **Filtrar vendas por código de oferta**
    * Objetivo: Verificar vendas realizadas para uma oferta específica (ex: promoção ou pacote especial)
    * Como Fazer: Usar parâmetro offer_code=k2pasun0 (substitua pelo código da sua oferta)
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


15. **Listar vendas como produtor**
    * Objetivo: Visualizar vendas onde o usuário foi comissionado como produtor principal
    * Como Fazer: Usar parâmetro commission_as=PRODUCER
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


16. **Listar vendas como afiliado**
    * Objetivo: Visualizar vendas onde o usuário foi comissionado como afiliado para análise de performance de afiliação
    * Como Fazer: Usar parâmetro commission_as=AFFILIATE
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


17. **Obter vendas de uma origem específica**
    * Objetivo: Verificar vendas provenientes de um canal específico de marketing
    * Como Fazer: Usar parâmetro sales_source=INSTAGRAM (ou outro código de origem usado nos seus links)
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


18. **Controlar paginação para listas extensas**
    * Objetivo: Navegar entre páginas de resultados para grandes volumes de vendas
    * Como Fazer: Usar parâmetro page_token com o valor obtido em next_page_token da resposta anterior
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


19. **Limitar o número de resultados por página**
    * Objetivo: Definir um número específico de vendas a serem retornadas por página para melhor performance da aplicação
    * Como Fazer: Usar parâmetro max_results=20 (ou outro valor conforme necessidade)
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*


20. **Combinar múltiplos filtros para análise específica**
    * Objetivo: Criar relatório personalizado com diversos critérios combinados
    * Como Fazer: Combinar parâmetros como:
      ```
      /sales/history?product_id=2125812&transaction_status=APPROVED&start_date=1685577600000&end_date=1688169599000&payment_type=CREDIT_CARD
      ```
    * Este exemplo retorna vendas aprovadas do produto específico, realizadas em junho/2023 via cartão de crédito
    *(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 10. Notas Adicionais
* **Formato de Datas:** Todos os timestamps na API são representados em milissegundos (Unix timestamp) a partir de 1970-01-01 00:00:00 UTC. Para converter uma data legível para timestamp, pode-se usar:
  ```javascript
  // JavaScript exemplo: Converter data para timestamp
  const timestamp = new Date('2023-06-01').getTime();
  // Resultado: 1685577600000
  ```


* **Detalhamento de Participantes:** Para obter informações mais detalhadas sobre participantes, comissões e divisão dos valores, utilize os endpoints específicos da API Hotmart:
  - `/payments/api/v1/sales/{transaction}/participants` para informações sobre participantes
  - `/payments/api/v1/sales/{transaction}/commissions` para detalhes sobre comissões


* **Paginação Eficiente:** A paginação baseada em tokens (next_page_token/prev_page_token) é mais eficiente que a baseada em números de página para grandes conjuntos de dados. Armazene os tokens para navegação bidirecional.


* **Dados Pessoais (LGPD/GDPR):** Os dados pessoais dos compradores só são retornados caso eles tenham consentido em compartilhar essas informações no ato da compra. Implemente tratamento adequado para casos onde esses dados estão ausentes.


* **Rate Limits:** Embora não explicitamente documentados, é recomendável implementar:
  - Throttling de requisições (máximo de 10 requisições por minuto)
  - Mecanismo de retry com backoff exponencial em caso de erros 429
  - Cache de resultados frequentemente acessados


* **Status de Transação:** Os status de transação seguem um fluxo específico:
  1. STARTED → Transação iniciada, mas ainda sem confirmação de pagamento
  2. WAITING_PAYMENT → Aguardando a confirmação do pagamento
  3. APPROVED → Pagamento confirmado e aprovado
  4. COMPLETE → Transação finalizada com sucesso


* **Considerações de Desempenho:**
  - Utilize filtros para reduzir o volume de dados retornados
  - Defina max_results adequadamente para seu caso de uso
  - Implemente consultas incrementais para sincronização periódica (usando start_date baseado na última sincronização)


* **Tratamento de Moedas:** O sistema suporta múltiplas moedas (USD, BRL, EUR, etc.). Verifique o campo currency_code para realizar conversões necessárias em integrações.


* **Campos Adicionais Imprevistos:** A API pode, ocasionalmente, retornar campos adicionais não documentados. É recomendável que sua implementação seja resiliente a novos campos.
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sales_001",
  "api_provider": "Hotmart",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Listar Histórico de Vendas", "Filtrar Vendas", "Obter Transações"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Vendas", "Produtos", "Compradores", "Transações", "Pagamentos", "Ofertas", "Comissões"],
  "context_level": ["intermediate", "foundational"],
  "topic_cluster": ["e-commerce", "vendas online", "processamento de pagamentos", "análise financeira", "rastreamento de transações"],
  "db_relations": { 
    "tables": ["sales", "products", "buyers", "payments", "transactions", "commissions", "offers"], 
    "schemas": ["hotmart_payments", "hotmart_products"] 
  },
  "related_concepts": [
    "status de transação", 
    "métodos de pagamento", 
    "comissões", 
    "ofertas", 
    "paginação por token", 
    "filtros de data", 
    "rastreamento de origem"
  ],
  "question_embeddings": [
    "Como obter o histórico de vendas na Hotmart?",
    "Como filtrar vendas por status de transação na API Hotmart?",
    "Como verificar pagamentos realizados via PIX na Hotmart?",
    "Como localizar uma transação específica na Hotmart?",
    "Como encontrar vendas realizadas por um comprador específico?",
    "Como implementar paginação nas consultas de vendas da Hotmart?",
    "Como verificar vendas de um produto específico na API Hotmart?"
  ],
  "reasoning_pathways": ["filtering", "pagination", "transaction_tracking", "date_range_analysis", "payment_method_analysis"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*
---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação (Bearer Token)
- [ ] Tratamento de Erros (4xx, 5xx)
- [ ] Retries (429, 5xx)
- [ ] Paginação (Implementar controle via tokens)
- [ ] Validação de Entrada (Parâmetros válidos)
- [ ] Mapeamento de Resposta (Modelo para object items)
- [ ] Logs & Monitoramento (Registro de transações importantes)
- [ ] Cache (Para chamadas frequentes com os mesmos parâmetros)
- [ ] Testes (Casos normais, Edge-cases)
- [ ] Rate Limits (Monitoramento e backoff exponencial)
- [ ] Tratamento de Datas (Conversão de timestamps)
- [ ] Tratamento de Dados Ausentes (Comprador sem informações completas)
- [ ] Internacionalização (Múltiplas moedas)
- [ ] Segurança (Armazenamento seguro de dados sensíveis)
- [ ] Tratamento de Valores Financeiros (Uso de precisão decimal adequada)
*(Ref: Hotmart Sales History, ID hotmart_saleshistory_001)*