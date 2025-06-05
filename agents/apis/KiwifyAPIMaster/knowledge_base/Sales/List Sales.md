# API Kiwify - Vendas - Listar Vendas (List Sales)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS




# 1. Cabeçalho e Identificação




| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Vendas - Listar Vendas (List Sales)` |
| **Identificador Interno** | `kiwify_sales_001`                   |
| **Título Curto (Ref.)**   | `Kiwify List Sales`           |
| **Versão do Documento**   | `1.0.0`                                |
| **Data de Criação**       | `2025-04-11`                                                  |
| **Última Atualização**    | `2025-04-11`                                                  |
| **Autor/Responsável**     | `Equipe de Documentação`                                    |
| **Fonte Original**        | `Documentação Oficial API Kiwify`  |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/sales/list` |
| **Status do Documento**   | `Em Uso`                              |
| **Ambiente de Referência**| `Produção`                                |
| **Idioma Original**       | `Português (BR)`                                  |
| **Formato de Datas (API)**| `ISO 8601 (YYYY-MM-DDTHH:MM:SS.sssZ)` |




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 2. Contexto




> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint de listagem de vendas da Kiwify.




O endpoint de Listar Vendas fornece acesso aos dados de transações comerciais realizadas na plataforma Kiwify. Este endpoint é fundamental para produtores de conteúdo digital e integradores que precisam monitorar, gerenciar e analisar as vendas dos seus produtos digitais, permitindo automação de processos financeiros, relatórios e conciliação. É uma parte essencial do ecossistema de APIs comerciais da Kiwify.




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 3. Visão Geral da API/Endpoint(s)




> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint de listagem de vendas.




O endpoint Listar Vendas permite a recuperação de dados detalhados sobre as transações de venda realizadas na plataforma Kiwify. Ele suporta filtragem por diversos parâmetros como status de pagamento, método de pagamento, período de tempo, produto específico e afiliado. Os resultados são paginados e incluem informações completas sobre cada venda, incluindo dados do cliente, produto, pagamento, comissões de afiliados e parceiros de receita.




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 4. Detalhes Técnicos




> **Resumo:** Especificações técnicas detalhadas do endpoint, incluindo URLs, métodos HTTP e requisitos de autenticação.




### `Endpoint: /v1/sales`




* **Endpoint URL:** `https://public-api.kiwify.com/v1/sales`
* **Método HTTP:** `GET`
* **Autenticação:** `OAuth 2.0 com cabeçalho Authorization: Bearer <token> e x-kiwify-account-id`




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 5. Parâmetros de Entrada




> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados nas requisições ao endpoint de listagem de vendas.




### `Endpoint: /v1/sales` (Query Parameters)




| Parâmetro              | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :--------------------- | :-------- | :--- | :----------- | :-------------- |
| `status`               | O status da venda | string | Não | Valores possíveis: `approved`, `authorized`, `chargedback`, `paid`, `pending`, `pending_refund`, `processing`, `refunded`, `refund_requested`, `refused`, `waiting_payment` |
| `view_full_sale_details` | Indica se os detalhes completos da venda devem ser visualizados | boolean | Não | `true` ou `false` |
| `payment_method`       | O método de pagamento utilizado | string | Não | Valores possíveis: `boleto`, `credit_card`, `pix` |
| `product_id`           | Identificador do produto | string | Não | Exemplo: `ba385b7c-cac1-4422-925d-7f707d8267d2` |
| `affiliate_id`         | Identificador do afiliado | string | Não | Exemplo: `ba385b7c-cac1-4422-925d-7f707d8267d2` |
| `page_size`            | Número de resultados por página | string | Não | Exemplo: `10` |
| `page_number`          | Número da página atual | string | Não | Exemplo: `1` |
| `start_date`           | Data de início do período de vendas a ser consultado | string | Sim | Formato ISO 8601 |
| `end_date`             | Data de término do período de vendas a ser consultado | string | Sim | Formato ISO 8601 |
| `updated_at_start_date` | Data de início para atualização das vendas | string | Não | Formato ISO 8601 |
| `updated_at_end_date`  | Data de término para atualização das vendas | string | Não | Formato ISO 8601 |




### `Headers`




| Parâmetro              | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :--------------------- | :-------- | :--- | :----------- | :-------------- |
| `Authorization`        | Token de acesso OAuth 2.0 | string | Sim | Formato: `Bearer <token>` |
| `x-kiwify-account-id`  | Identificador da conta Kiwify | string | Sim | Identificador único da conta |




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 6. Parâmetros de Saída (Estrutura da Resposta JSON)




> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint de listagem de vendas.




### `Endpoint: /v1/sales`




#### 6.1.1 Estrutura Geral




| Campo             | Descrição | Tipo   |
| :---------------- | :-------- | :----- |
| `pagination`      | Informações de paginação dos resultados | object |
| `data`            | Lista de vendas retornadas pela API | array |




#### 6.1.2 Detalhes do Objeto `pagination`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `count`               | Número total de itens na página atual | number | |
| `page_number`         | Número da página atual | number | |
| `page_size`           | Número de itens por página | number | |




#### 6.1.3 Detalhes do Objeto `data[]` (Venda)




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id`                  | Identificador único da venda | string | Formato UUID |
| `reference`           | Referência da venda | string | |
| `type`                | Tipo de venda | string | Ex: "product" |
| `created_at`          | Data e hora de criação da venda | string | Formato ISO 8601 |
| `updated_at`          | Data e hora da última atualização | string | Formato ISO 8601 |
| `product`             | Informações sobre o produto vendido | object | Ver 6.1.4 |
| `shipping`            | Informações sobre o envio | object | Ver 6.1.5 |
| `status`              | Status atual da venda | string | Ex: "paid", "refunded" |
| `payment_method`      | Método de pagamento utilizado | string | Ex: "boleto", "credit_card", "pix" |
| `net_amount`          | Valor líquido da venda | number | Em centavos |
| `currency`            | Moeda da venda | string | Ex: "BRL" |
| `customer`            | Informações sobre o cliente | object | Ver 6.1.6 |
| `approved_date`       | Data e hora de aprovação da venda | string | Formato ISO 8601 |
| `boleto_url`          | URL para o boleto, quando aplicável | string | Pode ser null |
| `card_last_digits`    | Últimos dígitos do cartão utilizado | string | |
| `card_rejection_reason` | Motivo de rejeição do cartão | string | Pode ser null |
| `card_type`           | Tipo do cartão utilizado | string | Ex: "mastercard" |
| `installments`        | Número de parcelas da venda | number | |
| `is_one_click`        | Indica compra com um clique | boolean | |
| `parent_order_id`     | ID do pedido pai, se existir | string | Pode ser null |
| `payment`             | Detalhes financeiros do pagamento | object | Ver 6.1.7 |
| `refunded_at`         | Data e hora do reembolso | string | Formato ISO 8601, pode ser null |
| `sale_type`           | Tipo de venda comercial | string | Ex: "producer" |
| `tracking`            | Informações de rastreamento | object | Ver 6.1.8 |
| `two_cards`           | Indica uso de dois cartões | boolean | |
| `revenue_partners`    | Parceiros de receita/coprodutores | array | Ver 6.1.9 |
| `affiliate_commission` | Informações sobre comissão de afiliado | object | Ver 6.1.10 |




#### 6.1.4 Detalhes do Objeto `product`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id`                  | Identificador único do produto | string | Formato UUID |
| `name`                | Nome do produto | string | |




#### 6.1.5 Detalhes do Objeto `shipping`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id`                  | Identificador do método de envio | string | Formato UUID |
| `name`                | Nome do método de envio | string | |
| `price`               | Preço do envio | number | Em centavos |




#### 6.1.6 Detalhes do Objeto `customer`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id`                  | Identificador único do cliente | string | Formato UUID |
| `name`                | Nome completo do cliente | string | |
| `email`               | Email do cliente | string | |
| `cpf`                 | CPF do cliente | string | |
| `mobile`              | Número de celular do cliente | string | Formato internacional |
| `instagram`           | Nome de usuário no Instagram | string | Pode ser null |
| `country`             | País do cliente | string | Código ISO (Ex: "BR") |
| `address`             | Endereço completo do cliente | object | Ver 6.1.6.1 |




#### 6.1.6.1 Detalhes do Objeto `customer.address`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `street`              | Nome da rua | string | |
| `number`              | Número do endereço | string | |
| `complement`          | Complemento do endereço | string | Pode ser null |
| `neighborhood`        | Bairro | string | |
| `city`                | Cidade | string | |
| `state`               | Estado | string | Código UF (Ex: "SP") |
| `zipcode`             | CEP | string | |




#### 6.1.7 Detalhes do Objeto `payment`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `charge_amount`       | Valor total cobrado | number | Em centavos |
| `charge_currency`     | Moeda do valor cobrado | string | Ex: "BRL" |
| `net_amount`          | Valor líquido | number | Em centavos |
| `product_base_price`  | Preço base do produto | number | Em centavos |
| `product_base_currency` | Moeda do preço base | string | Ex: "BRL" |
| `settlement_amount`   | Valor de liquidação | number | Em centavos |
| `settlement_currency` | Moeda da liquidação | string | Ex: "USD" |
| `fee`                 | Taxa cobrada | number | Em centavos |
| `fee_currency`        | Moeda da taxa | string | Ex: "USD" |
| `sale_tax_rate`       | Taxa percentual de imposto | number | Percentual (Ex: 5.6) |
| `sale_tax_amount`     | Valor do imposto | number | Em centavos |




#### 6.1.8 Detalhes do Objeto `tracking`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `sck`                 | Código de rastreamento SCK | string | Pode ser null |
| `src`                 | Código de rastreamento SRC | string | Pode ser null |
| `utm_campaign`        | Parâmetro UTM de campanha | string | Pode ser null |
| `utm_content`         | Parâmetro UTM de conteúdo | string | Pode ser null |
| `utm_medium`          | Parâmetro UTM de meio | string | Pode ser null |
| `utm_source`          | Parâmetro UTM de origem | string | Pode ser null |
| `utm_term`            | Parâmetro UTM de termo | string | Pode ser null |
| `s1`, `s2`, `s3`      | Parâmetros de rastreamento personalizados | string | Podem ser null |




#### 6.1.9 Detalhes do Objeto `revenue_partners[]`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `account_id`          | ID da conta do parceiro | string | |
| `legal_name`          | Nome legal do parceiro | string | |
| `document_id`         | Documento do parceiro (CPF/CNPJ) | string | |
| `percentage`          | Percentual de participação | number | |
| `net_amount_split`    | Valor líquido do parceiro | number | Em centavos |
| `charge_amount_split` | Valor bruto do parceiro | number | Em centavos |




#### 6.1.10 Detalhes do Objeto `affiliate_commission`




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `name`                | Nome do afiliado | string | |
| `document`            | Documento do afiliado (CPF/CNPJ) | string | |
| `email`               | Email do afiliado | string | |
| `amount`              | Valor da comissão | number | Em centavos |




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 7. Exemplos de Requisição e Resposta




> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint de listagem de vendas.




### `Endpoint: /v1/sales`




#### 7.1.1 Exemplo de Requisição (cURL)




```bash
curl --request GET \
  --url "https://public-api.kiwify.com/v1/sales?start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z&status=paid&payment_method=boleto&page_size=10&page_number=1" \
  --header "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  --header "x-kiwify-account-id: acc_12345abcde"
```




#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 200)




```json
{
  "pagination": {
    "count": 10,
    "page_number": 1,
    "page_size": 10
  },
  "data": [
    {
      "id": "5cbb3832-7b5f-4cf2-b04e-ca6a4289d896",
      "reference": "9dAQA5a",
      "type": "product",
      "created_at": "2023-10-31T16:53:05.119Z",
      "updated_at": "2023-10-31T16:57:01.810Z",
      "product": {
        "id": "aaa86f40-d7ae-11ed-acc6-e1c45591a30e",
        "name": "my product"
      },
      "shipping": {
        "id": "255f7ae0-8694-40f9-b905-7507fe6bc58f",
        "name": "Entrega Grátis",
        "price": 0
      },
      "status": "paid",
      "payment_method": "boleto",
      "net_amount": 0,
      "currency": "BRL",
      "customer": {
        "id": "29eb9963-8f4f-4c03-9897-63bdba0d5eb2",
        "name": "my customer",
        "email": "mycustomer@mail.com",
        "cpf": "99999999999",
        "mobile": "+5599999999999",
        "instagram": "y_instagram",
        "country": "BR",
        "address": {
          "street": "Rua Danilo",
          "number": "407",
          "complement": "Apt. 123",
          "neighborhood": "Jardim dos Jardineiros",
          "city": "Paulista",
          "state": "SE",
          "zipcode": "46121-175"
        }
      },
      "approved_date": "2023-10-31T16:34:35.491Z",
      "boleto_url": null,
      "card_last_digits": "1115",
      "card_rejection_reason": null,
      "card_type": "mastercard",
      "installments": 12,
      "is_one_click": true,
      "parent_order_id": null,
      "payment": {
        "charge_amount": 10388,
        "charge_currency": "BRL",
        "net_amount": 8853,
        "product_base_price": 60037,
        "product_base_currency": "BRL",
        "settlement_amount": 8853,
        "settlement_currency": "USD",
        "fee": 984,
        "fee_currency": "USD",
        "sale_tax_rate": 5.6,
        "sale_tax_amount": 551
      },
      "refunded_at": null,
      "sale_type": "producer",
      "tracking": {
        "sck": null,
        "src": null,
        "utm_campaign": null,
        "utm_content": null,
        "utm_medium": null,
        "utm_source": null,
        "utm_term": null,
        "s1": null,
        "s2": null,
        "s3": null
      },
      "two_cards": false,
      "revenue_partners": [
        {
          "account_id": "RpL2PsVt7gEN50Q",
          "legal_name": "My Coproducer",
          "document_id": "12345678910",
          "percentage": 50,
          "net_amount_split": 4426,
          "charge_amount_split": 5000
        }
      ],
      "affiliate_commission": {
        "name": "My affiliate",
        "document": "123456789",
        "email": "myaffiliate@email.com",
        "amount": 2849
      }
    }
  ]
}
```




#### 7.1.3 Exemplo de Resposta (JSON - Erro)




```json
{
  "error": {
    "code": "invalid_date_range",
    "message": "O período entre start_date e end_date não pode exceder 90 dias",
    "request_id": "req_AbC123xYz"
  }
}
```




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 8. Códigos de Status e Tratamento de Erros




> **Resumo:** Descrição completa dos códigos de status HTTP retornados pelo endpoint e como gerenciar erros.




| Status Code               | Descrição Geral                                    |
| :------------------------ | :------------------------------------------------- |
| `200 OK`                  | Sucesso. A requisição foi processada e a resposta contém a lista de vendas solicitada. |
| `400 Bad Request`         | Parâmetros inválidos ou ausentes. Verifique o período de datas (máximo 90 dias) e outros parâmetros. |
| `401 Unauthorized`        | Falha na autenticação. Token inválido, expirado ou ausente. |
| `403 Forbidden`           | Sem permissão. A conta não tem acesso a esta funcionalidade. |
| `404 Not Found`           | Recurso não encontrado. Verifique o endpoint utilizado. |
| `429 Too Many Requests`   | Limite de requisições excedido. Aguarde antes de fazer novas solicitações. |
| `500 Internal Server Error`| Erro interno no servidor da API. Entre em contato com o suporte se o problema persistir. |




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 9. Casos de Uso Comuns (20 Exemplos Específicos)




> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint de listagem de vendas.




1.  **Obter todas as vendas pagas no último mês**
    *   Objetivo: `Recuperar todas as transações bem-sucedidas para contabilidade mensal`
    *   Como Fazer: `GET /v1/sales?status=paid&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




2.  **Listar vendas de um produto específico**
    *   Objetivo: `Analisar o desempenho comercial de um produto digital específico`
    *   Como Fazer: `GET /v1/sales?product_id=aaa86f40-d7ae-11ed-acc6-e1c45591a30e&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




3.  **Consultar vendas geradas por um afiliado específico**
    *   Objetivo: `Verificar o desempenho de um afiliado para calcular comissões`
    *   Como Fazer: `GET /v1/sales?affiliate_id=ba385b7c-cac1-4422-925d-7f707d8267d2&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




4.  **Buscar vendas com paginação otimizada**
    *   Objetivo: `Recuperar grandes volumes de dados divididos em páginas gerenciáveis`
    *   Como Fazer: `GET /v1/sales?start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z&page_size=50&page_number=3`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




5.  **Filtrar vendas por método de pagamento**
    *   Objetivo: `Obter apenas vendas realizadas via PIX para análise de desempenho deste método`
    *   Como Fazer: `GET /v1/sales?payment_method=pix&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




6.  **Consultar vendas com status pendente**
    *   Objetivo: `Identificar transações que precisam de acompanhamento ou ação adicional`
    *   Como Fazer: `GET /v1/sales?status=pending&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




7.  **Verificar vendas reembolsadas**
    *   Objetivo: `Auditar devoluções para análise financeira e reconciliação contábil`
    *   Como Fazer: `GET /v1/sales?status=refunded&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




8.  **Monitorar vendas recusadas**
    *   Objetivo: `Identificar problemas com pagamentos para melhorar taxas de conversão`
    *   Como Fazer: `GET /v1/sales?status=refused&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




9.  **Buscar vendas recentes atualizadas**
    *   Objetivo: `Sincronizar dados com sistemas externos identificando apenas registros modificados`
    *   Como Fazer: `GET /v1/sales?updated_at_start_date=2023-10-30T00:00:00Z&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




10. **Analisar vendas com parcelamento**
    *   Objetivo: `Avaliar o impacto das vendas parceladas no fluxo de caixa`
    *   Como Fazer: `GET /v1/sales?payment_method=credit_card&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




11. **Verificar vendas em processamento**
    *   Objetivo: `Monitorar transações que estão em fase de processamento para acompanhamento`
    *   Como Fazer: `GET /v1/sales?status=processing&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




12. **Consultar vendas com chargeback**
    *   Objetivo: `Identificar disputas de pagamento para gestão de fraudes e resolução de problemas`
    *   Como Fazer: `GET /v1/sales?status=chargedback&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




13. **Analisar vendas com detalhes completos**
    *   Objetivo: `Obter informações detalhadas de cada venda para análise profunda`
    *   Como Fazer: `GET /v1/sales?view_full_sale_details=true&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




14. **Consultar vendas aguardando pagamento**
    *   Objetivo: `Acompanhar boletos e outros métodos pendentes para follow-up`
    *   Como Fazer: `GET /v1/sales?status=waiting_payment&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




15. **Verificar vendas com solicitação de reembolso**
    *   Objetivo: `Identificar pedidos de reembolso para processamento e análise de satisfação`
    *   Como Fazer: `GET /v1/sales?status=refund_requested&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




16. **Analisar vendas com parceiros de receita**
    *   Objetivo: `Verificar transações com coproduções para cálculo de divisão de receitas`
    *   Como Fazer: `GET /v1/sales?status=paid&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z` e depois filtrar resultados com revenue_partners
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




17. **Verificar vendas para um período específico de 7 dias**
    *   Objetivo: `Analisar desempenho de vendas durante uma semana específica (ex: Black Friday)`
    *   Como Fazer: `GET /v1/sales?start_date=2023-11-20T00:00:00Z&end_date=2023-11-27T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




18. **Consultar vendas com UTM específico**
    *   Objetivo: `Analisar eficácia de campanhas de marketing através de parâmetros UTM`
    *   Como Fazer: `GET /v1/sales?start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z` e depois filtrar os resultados por tracking.utm_source
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




19. **Analisar vendas por múltiplos status**
    *   Objetivo: `Obter tanto vendas pagas quanto aguardando pagamento para follow-up completo`
    *   Como Fazer: `Realizar múltiplas chamadas com diferentes valores de status e combinar resultados`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




20. **Verificar vendas autorizada mas ainda não capturadas**
    *   Objetivo: `Identificar transações que foram autorizadas mas ainda não foram efetivadas`
    *   Como Fazer: `GET /v1/sales?status=authorized&start_date=2023-10-01T00:00:00Z&end_date=2023-10-31T23:59:59Z`
    *(Ref: Kiwify List Sales, ID kiwify_listsales_001)*




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 10. Notas Adicionais




> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint de listagem de vendas.




* **Limite de Período:** `O período entre os parâmetros start_date e end_date não pode exceder 90 dias. Requisições com intervalos maiores serão rejeitadas com erro 400.`


* **Formato de Datas:** `Todas as datas devem ser fornecidas e são retornadas no formato ISO 8601 (YYYY-MM-DDTHH:MM:SS.sssZ). As datas são interpretadas em UTC.`


* **Paginação:** `Por padrão, a API retorna 10 registros por página. Use os parâmetros page_size e page_number para navegar pelos resultados. O tamanho máximo de página é 100.`


* **Valores Monetários:** `Todos os valores monetários na resposta são representados em centavos (sem pontos decimais). Por exemplo, R$ 103,88 é representado como 10388.`


* **Campos Nulos:** `Alguns campos podem ser retornados como null quando não aplicáveis ao tipo de venda ou método de pagamento.`


* **Cross-Reference:** `Utilize o campo id para referenciar uma venda específica em outras operações da API, como consultas de detalhes ou reembolsos.`


* **Dados Sensíveis:** `Informações como CPF e dados de cartão são parcialmente mascarados por motivos de segurança.`


* **Cache:** `As respostas podem ser cacheadas por até 5 minutos. Para garantir dados em tempo real, use o parâmetro de consulta fresh=true.`




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 11. Metadados Internos (Para Indexação e RAG)




> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.




```json
{
  "doc_id": "kiwify_sales_001",
  "api_provider": "Kiwify",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Listar Vendas", "Recuperar Transações"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Confidential",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Vendas", "Produtos", "Clientes", "Pagamentos", "Afiliados"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["e-commerce", "vendas digitais", "transações financeiras"],
  "db_relations": { 
    "tables": ["sales", "customers", "products", "payments"], 
    "schemas": ["public", "financial"] 
  },
  "related_concepts": ["pagamentos", "produtos digitais", "afiliação", "reembolsos"],
  "question_embeddings": [
    "Como consultar vendas na Kiwify por período?",
    "Qual o formato para listar transações pagas na API Kiwify?",
    "Como filtrar vendas por método de pagamento na Kiwify?",
    "Como obter vendas de um afiliado específico via API?",
    "Quais são os status possíveis ao listar vendas na Kiwify?"
  ],
  "reasoning_pathways": ["conditional", "sequential"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "Account ID"],
  "typical_integration_points": ["ERP", "Analytics", "CRM", "Dashboards"],
  "common_error_patterns": ["date_range_too_large", "missing_required_parameters", "authentication_failure"]
}
```




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 12. Checklist de Implementação (Opcional)




> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação do endpoint de listagem de vendas.




- [ ] Autenticação
  - [ ] Implementar obtenção do token OAuth 2.0
  - [ ] Configurar renovação automática do token expirado
  - [ ] Armazenar com segurança o valor de x-kiwify-account-id




- [ ] Tratamento de Erros (4xx, 5xx)
  - [ ] Implementar handlers para erros de período inválido (>90 dias)
  - [ ] Adicionar logging para falhas de autenticação
  - [ ] Criar mensagens de erro amigáveis para o usuário final




- [ ] Retries (429, 5xx)
  - [ ] Implementar backoff exponencial para casos de rate limit
  - [ ] Definir número máximo de 3 tentativas
  - [ ] Adicionar jitter de 100-500ms para evitar sincronização




- [ ] Paginação
  - [ ] Suportar navegação através de múltiplas páginas
  - [ ] Implementar controle de paginação com page_size e page_number
  - [ ] Detectar final dos resultados (quando count < page_size)




- [ ] Validação de Entrada
  - [ ] Validar formato ISO 8601 para parâmetros de data
  - [ ] Verificar que o período máximo não excede 90 dias
  - [ ] Validar enum values (status, payment_method)




- [ ] Mapeamento de Resposta
  - [ ] Converter valores monetários de centavos para formato com decimais
  - [ ] Mapear campos para modelos de domínio internos
  - [ ] Lidar com valores nulos em campos opcionais




- [ ] Logs & Monitoramento
  - [ ] Registrar tempo de resposta de cada chamada
  - [ ] Monitorar taxa de erros
  - [ ] Implementar rastreamento de requisições (request_id)




- [ ] Cache
  - [ ] Implementar cache para resultados frequentes
  - [ ] Definir estratégias de invalidação
  - [ ] Respeitar cabeçalhos Cache-Control




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
---




## 13. Glossário de Termos Técnicos




> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados na documentação.




| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Venda`                   | `Transação comercial concluída ou em andamento entre um comprador e um vendedor através da plataforma Kiwify` |
| `Token de Autenticação`   | `Credencial de segurança temporária usada para autorizar requisições à API via cabeçalho Authorization` |
| `Rate Limit`              | `Número máximo de requisições permitidas em um período de tempo específico` |
| `Paginação`               | `Técnica para dividir conjuntos grandes de resultados em páginas gerenciáveis via parâmetros page_size e page_number` |
| `Afiliado`                | `Parceiro de marketing que promove produtos e recebe comissões por vendas geradas` |
| `Coprodutor`              | `Parceiro de receita que compartilha os resultados financeiros de um produto digital` |
| `Chargeback`              | `Estorno forçado iniciado pelo cliente junto à operadora do cartão, geralmente após disputa` |
| `UTM`                     | `Parâmetros de rastreamento (Urchin Tracking Module) usados para identificar fontes de tráfego` |
| `Webhook`                 | `Mecanismo de notificação onde a API envia requisições HTTP para um URL configurado quando eventos ocorrem` |
| `Idempotência`            | `Propriedade onde múltiplas requisições idênticas têm o mesmo efeito que uma única requisição` |




*(Ref: Kiwify List Sales, ID kiwify_listsales_001)*
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




**(FIM DO DOCUMENTO)**