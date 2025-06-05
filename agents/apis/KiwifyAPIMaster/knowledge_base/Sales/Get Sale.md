# API Kiwify - Vendas - Consultar Venda (Get Sale)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# API Kiwify - Vendas - Consultar Venda (Get Sale)


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Kiwify - Vendas - Consultar Venda (Get Sale) |
| **Identificador Interno** | kiwify_sales_001                   |
| **Título Curto (Ref.)**   | Kiwify Get Sale           |
| **Versão do Documento**   | 1.0.0                                |
| **Data de Criação**       | 2025-04-11                                                  |
| **Última Atualização**    | 2025-04-11                                                  |
| **Autor/Responsável**     | Equipe de Documentação                                    |
| **Fonte Original**        | https://docs.kiwify.com.br/api-reference/sales/single  |
| **URL de Referência**     | https://public-api.kiwify.com/v1/sales/{id} |
| **Status do Documento**   | Em Uso                              |
| **Ambiente de Referência**| Produção                                |
| **Idioma Original**       | Português (BR)                                  |
| **Formato de Datas (API)**| ISO 8601 (YYYY-MM-DDTHH:MM:SS.mmmZ) |




*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 2. Contexto


> **Resumo:** Este endpoint permite consultar detalhes completos de uma venda específica na plataforma Kiwify.


Este endpoint fornece acesso detalhado a informações de uma venda específica através de seu identificador único. É fundamental para sistemas que necessitam integrar dados de vendas para análise, suporte ao cliente, relatórios financeiros ou processamento pós-venda. O endpoint retorna informações abrangentes incluindo detalhes do produto, cliente, pagamento, rastreamento e comissões de afiliados, permitindo uma visão completa da transação.


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 3. Visão Geral da API/Endpoint(s)


> **Resumo:** Endpoint para consulta individual de transações de vendas com detalhes completos da operação.


Este endpoint realiza a consulta de uma transação de venda específica na plataforma Kiwify, retornando todos os detalhes associados. É essencial para sistemas que precisam verificar informações de vendas, confirmar status de pagamentos, acessar dados de clientes ou processar relatórios financeiros. A API retorna dados detalhados sobre a transação, incluindo informações do produto vendido, cliente, método de pagamento, valores e taxas, permitindo uma integração completa com sistemas de gestão, financeiro ou atendimento ao cliente.


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 4. Detalhes Técnicos


> **Resumo:** Especificações técnicas do endpoint para consulta de vendas, incluindo URL, método e autenticação.


### Endpoint 1: /sales/{id}


* **Endpoint URL:** `https://public-api.kiwify.com/v1/sales/{id}`
* **Método HTTP:** `GET`
* **Autenticação:** OAuth 2.0 com token Bearer no cabeçalho + API key específica da conta


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 5. Parâmetros de Entrada


> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados nas requisições aos endpoints.


### Endpoint 1: /sales/{id} (Path Parameters)


| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `id` (Path)   | Identificador único da venda a ser consultada | string | Sim | Ex: fc96cec5-1ff1-49b3-aa22-0e131f353b62 |


### Endpoint 1: /sales/{id} (Header Parameters)


| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `Authorization` | Token de acesso OAuth 2.0 | string | Sim | Format: "Bearer {token}" |
| `x-kiwify-account-id` | Identificador da conta Kiwify | string | Sim | Ex: "RpL2PsVt7gEN50Q" |


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)


> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint nas respostas bem-sucedidas.


### Endpoint 1: /sales/{id}


#### 6.1.1 Estrutura Geral


| Campo             | Descrição | Tipo   |
| :---------------- | :-------- | :----- |
| `id`  | Identificador único da venda | string |
| `reference` | Código de referência curto da venda | string |
| `type` | Tipo do objeto vendido (ex: "product") | string |
| `created_at` | Data e hora de criação da venda | string (ISO 8601) |
| `updated_at` | Data e hora da última atualização | string (ISO 8601) |
| `product` | Informações sobre o produto vendido | objeto |
| `shipping` | Informações sobre o método de entrega | objeto |
| `status` | Status atual da venda (ex: "paid") | string |
| `payment_method` | Método de pagamento utilizado | string |
| `net_amount` | Valor líquido da venda (após taxas) | number (integer) |
| `currency` | Moeda da transação | string |
| `customer` | Informações detalhadas do cliente | objeto |
| `approved_date` | Data e hora da aprovação do pagamento | string (ISO 8601) |
| `boleto_url` | URL do boleto (se aplicável) | string ou null |
| `card_last_digits` | Últimos dígitos do cartão (se aplicável) | string ou null |
| `card_rejection_reason` | Motivo da rejeição do cartão (se aplicável) | string ou null |
| `card_type` | Bandeira do cartão utilizado (se aplicável) | string ou null |
| `installments` | Número de parcelas | integer |
| `is_one_click` | Indica se foi compra com 1-click | boolean |
| `parent_order_id` | ID da ordem pai (se for uma ordem filha) | string ou null |
| `payment` | Detalhes financeiros da transação | objeto |
| `refunded_at` | Data e hora do reembolso (se aplicável) | string (ISO 8601) ou null |
| `sale_type` | Tipo da venda (ex: "producer") | string |
| `tracking` | Informações de rastreamento de marketing | objeto |
| `two_cards` | Indica se foram usados dois cartões | boolean |
| `revenue_partners` | Lista de parceiros de receita (coprodutores) | array de objetos |
| `affiliate_commission` | Informações sobre comissão de afiliado | objeto ou null |


#### 6.1.2 Detalhes do Objeto `product`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id` | Identificador único do produto | string | |
| `name` | Nome do produto | string | |


#### 6.1.3 Detalhes do Objeto `shipping`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id` | Identificador único do método de entrega | string | |
| `name` | Nome do método de entrega | string | |
| `price` | Preço do frete | number (integer) | Valor em centavos |


#### 6.1.4 Detalhes do Objeto `customer`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id` | Identificador único do cliente | string | |
| `name` | Nome completo do cliente | string | |
| `email` | Email do cliente | string | |
| `cpf` | CPF do cliente | string | |
| `mobile` | Telefone celular do cliente | string | Formato internacional |
| `instagram` | Usuário do Instagram (se disponível) | string | |
| `country` | País do cliente (código ISO) | string | Ex: "BR" |
| `address` | Informações de endereço | objeto | Ver detalhes abaixo |


#### 6.1.5 Detalhes do Objeto `customer.address`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `street` | Nome da rua | string | |
| `number` | Número do endereço | string | |
| `complement` | Complemento do endereço | string | |
| `neighborhood` | Bairro | string | |
| `city` | Cidade | string | |
| `state` | Estado (código de 2 letras) | string | Ex: "SE" |
| `zipcode` | CEP | string | |


#### 6.1.6 Detalhes do Objeto `payment`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `charge_amount` | Valor cobrado do cliente | number (integer) | Valor em centavos |
| `charge_currency` | Moeda da cobrança | string | Ex: "BRL" |
| `net_amount` | Valor líquido após taxas | number (integer) | Valor em centavos |
| `product_base_price` | Preço base do produto | number (integer) | Valor em centavos |
| `product_base_currency` | Moeda do preço base | string | Ex: "BRL" |
| `settlement_amount` | Valor de liquidação | number (integer) | Valor em centavos |
| `settlement_currency` | Moeda de liquidação | string | Ex: "USD" |
| `fee` | Taxa cobrada pela plataforma | number (integer) | Valor em centavos |
| `fee_currency` | Moeda da taxa | string | Ex: "USD" |
| `sale_tax_rate` | Percentual de imposto | number (float) | Ex: 5.6 |
| `sale_tax_amount` | Valor do imposto | number (integer) | Valor em centavos |


#### 6.1.7 Detalhes do Objeto `tracking`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `sck` | Código de rastreamento clickBank | string ou null | |
| `src` | Parâmetro de origem | string ou null | |
| `utm_campaign` | Parâmetro UTM de campanha | string ou null | |
| `utm_content` | Parâmetro UTM de conteúdo | string ou null | |
| `utm_medium` | Parâmetro UTM de meio | string ou null | |
| `utm_source` | Parâmetro UTM de origem | string ou null | |
| `utm_term` | Parâmetro UTM de termo | string ou null | |
| `s1` | Parâmetro personalizado s1 | string ou null | |
| `s2` | Parâmetro personalizado s2 | string ou null | |
| `s3` | Parâmetro personalizado s3 | string ou null | |


#### 6.1.8 Detalhes do Objeto `revenue_partners` (itens do array)


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `account_id` | ID da conta do parceiro | string | |
| `legal_name` | Nome legal do parceiro | string | |
| `document_id` | Documento do parceiro (CPF/CNPJ) | string | |
| `percentage` | Percentual de comissão | number (integer) | |
| `net_amount_split` | Valor líquido destinado ao parceiro | number (integer) | Valor em centavos |
| `charge_amount_split` | Valor bruto destinado ao parceiro | number (integer) | Valor em centavos |


#### 6.1.9 Detalhes do Objeto `affiliate_commission`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `name` | Nome do afiliado | string | |
| `document` | Documento do afiliado (CPF/CNPJ) | string | |
| `email` | Email do afiliado | string | |
| `amount` | Valor da comissão | number (integer) | Valor em centavos |


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 7. Exemplos de Requisição e Resposta


> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para cada endpoint.


### Endpoint 1: /sales/{id}


#### 7.1.1 Exemplo de Requisição (cURL)


```bash
curl -X GET "https://public-api.kiwify.com/v1/sales/fc96cec5-1ff1-49b3-aa22-0e131f353b62" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "x-kiwify-account-id: RpL2PsVt7gEN50Q" \
  -H "Content-Type: application/json"
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 200)


```json
{
  "id": "fc96cec5-1ff1-49b3-aa22-0e131f353b62",
  "reference": "iYJwhMP",
  "type": "product",
  "created_at": "2023-10-31T16:34:35.491Z",
  "updated_at": "2023-10-31T16:36:02.005Z",
  "product": {
    "id": "aaa86f40-d7ae-11ed-acc6-e1c45591a30e",
    "name": "My Product"
  },
  "shipping": {
    "id": "255f7ae0-8694-40f9-b905-7507fe6bc58f",
    "name": "Entrega Grátis",
    "price": 0
  },
  "status": "paid",
  "payment_method": "credit_card",
  "net_amount": 8853,
  "currency": "USD",
  "customer": {
    "id": "b17dd04e-5acc-41ae-a4b2-cba0d2436406",
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
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro)


```json
{
  "error": {
    "code": "not_found",
    "message": "Venda não encontrada",
    "request_id": "req_7f8g9h0j1k"
  }
}
```


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 8. Códigos de Status e Tratamento de Erros


> **Resumo:** Descrição completa dos códigos de status HTTP retornados pelos endpoints e como gerenciar erros.


| Status Code               | Descrição Geral                                    |
| :------------------------ | :------------------------------------------------- |
| `200 OK`                  | Sucesso. A requisição foi processada e os dados da venda foram retornados. |
| `400 Bad Request`         | Erro na requisição. Parâmetros inválidos ou formato incorreto. |
| `401 Unauthorized`        | Falha na autenticação. Token inválido ou expirado. |
| `403 Forbidden`           | Sem permissão. A conta não tem direitos para acessar esta venda. |
| `404 Not Found`           | Venda não encontrada. O ID fornecido não corresponde a nenhuma venda existente. |
| `429 Too Many Requests`   | Rate Limit excedido. Aguarde antes de fazer novas solicitações. |
| `500 Internal Server Error`| Erro no servidor da API. Problema interno da Kiwify. |


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)


> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas dos endpoints.


1.  **Verificar status de pagamento de uma venda específica**
    *   Objetivo: `Confirmar se um pagamento foi aprovado para atender à solicitação de um cliente`
    *   Como Fazer: `GET /sales/{id} e verificar o campo "status" da resposta`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


2.  **Obter informações de contato do cliente para suporte**
    *   Objetivo: `Acessar dados de contato do cliente para resolver uma questão de suporte`
    *   Como Fazer: `GET /sales/{id} e utilizar os dados do objeto "customer" na resposta`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


3.  **Confirmar valor líquido de uma venda para conciliação financeira**
    *   Objetivo: `Verificar o valor líquido recebido para reconciliação com sistema financeiro`
    *   Como Fazer: `GET /sales/{id} e consultar o campo "net_amount" e "currency"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


4.  **Verificar método de pagamento utilizado na compra**
    *   Objetivo: `Identificar qual forma de pagamento foi usada pelo cliente`
    *   Como Fazer: `GET /sales/{id} e verificar o campo "payment_method"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


5.  **Obter detalhes da divisão de receita com coprodutores**
    *   Objetivo: `Verificar como a receita foi distribuída entre parceiros de negócio`
    *   Como Fazer: `GET /sales/{id} e analisar o array "revenue_partners"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


6.  **Verificar comissões pagas a afiliados**
    *   Objetivo: `Conferir valor de comissão pago a um afiliado específico`
    *   Como Fazer: `GET /sales/{id} e verificar o objeto "affiliate_commission"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


7.  **Consultar endereço de entrega do cliente**
    *   Objetivo: `Obter o endereço completo para envio de produto físico`
    *   Como Fazer: `GET /sales/{id} e acessar o objeto "customer.address"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


8.  **Verificar parâmetros de rastreamento de marketing**
    *   Objetivo: `Analisar a eficácia de campanhas verificando origem da venda`
    *   Como Fazer: `GET /sales/{id} e verificar o objeto "tracking" com parâmetros UTM`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


9.  **Obter detalhes do produto comprado**
    *   Objetivo: `Identificar qual produto específico foi adquirido na transação`
    *   Como Fazer: `GET /sales/{id} e verificar o objeto "product"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


10. **Verificar detalhes de pagamento com cartão de crédito**
    *   Objetivo: `Obter informações sobre cartão usado e número de parcelas`
    *   Como Fazer: `GET /sales/{id} e verificar campos "card_type", "card_last_digits" e "installments"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


11. **Confirmar data de aprovação do pagamento**
    *   Objetivo: `Verificar quando o pagamento foi confirmado para controle de prazos`
    *   Como Fazer: `GET /sales/{id} e consultar o campo "approved_date"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


12. **Verificar detalhes de frete e envio**
    *   Objetivo: `Obter informações sobre método de entrega e valor do frete`
    *   Como Fazer: `GET /sales/{id} e verificar o objeto "shipping"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


13. **Consultar impostos aplicados na venda**
    *   Objetivo: `Verificar taxa e valor total de impostos para fins contábeis`
    *   Como Fazer: `GET /sales/{id} e verificar campos "payment.sale_tax_rate" e "payment.sale_tax_amount"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


14. **Verificar se uma venda foi reembolsada**
    *   Objetivo: `Confirmar se e quando houve reembolso de uma compra`
    *   Como Fazer: `GET /sales/{id} e verificar o campo "refunded_at" (null se não reembolsado)`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


15. **Obter referência curta da venda para identificação rápida**
    *   Objetivo: `Usar código de referência curto em comunicações com cliente`
    *   Como Fazer: `GET /sales/{id} e usar o valor do campo "reference"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


16. **Verificar se a compra foi realizada com 1-click**
    *   Objetivo: `Identificar vendas feitas através de compra rápida com 1-click`
    *   Como Fazer: `GET /sales/{id} e verificar o valor booleano do campo "is_one_click"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


17. **Comparar valores brutos e líquidos para análise de taxas**
    *   Objetivo: `Analisar diferença entre valor cobrado e valor líquido recebido`
    *   Como Fazer: `GET /sales/{id} e comparar "payment.charge_amount" com "payment.net_amount"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


18. **Obter dados de CPF/documento para emissão de nota fiscal**
    *   Objetivo: `Acessar CPF do cliente para emissão de documentos fiscais`
    *   Como Fazer: `GET /sales/{id} e verificar campo "customer.cpf"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


19. **Verificar tipo da venda para categorização interna**
    *   Objetivo: `Identificar o tipo de venda para classificação em relatórios`
    *   Como Fazer: `GET /sales/{id} e verificar campo "sale_type" e "type"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


20. **Obter informações de moeda para conversões financeiras**
    *   Objetivo: `Identificar moedas utilizadas na transação para processamento contábil`
    *   Como Fazer: `GET /sales/{id} e verificar "currency", "payment.charge_currency" e "payment.settlement_currency"`
    *(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 10. Notas Adicionais


> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas dos endpoints.


* **Formato de Valores Monetários:** `Todos os valores monetários são representados como inteiros em centavos. Por exemplo, R$ 103,88 é representado como 10388.`


* **Múltiplas Moedas:** `A API permite transações em múltiplas moedas. Observe os campos de moeda correspondentes para cada valor monetário.`


* **Segurança e Privacidade:** `Dados sensíveis como CPF e informações de cartão possuem acesso restrito conforme políticas de privacidade.`


* **Valores Nulos:** `Campos que não se aplicam à transação específica são retornados como null.`


* **Compatibilidade:** `Este endpoint segue o padrão de versionamento da API (v1). Mudanças na estrutura serão comunicadas previamente.`


* **Documentação Adicional:** `Para detalhes completos sobre todos os status possíveis e outros campos, consulte a documentação de referência.`


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)


> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.


```json
{
  "doc_id": "kiwify_sales_001",
  "api_provider": "Kiwify",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Consultar Venda", "Get Sale"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Venda", "Cliente", "Produto", "Pagamento", "Afiliado"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["e-commerce", "vendas", "pagamentos"],
  "db_relations": { 
    "tables": ["sales", "customers", "products", "payments"], 
    "schemas": ["public", "kiwify"] 
  },
  "related_concepts": ["pagamento", "cliente", "produto", "afiliado", "comissão"],
  "question_embeddings": [
    "Como consultar os detalhes de uma venda específica na Kiwify?",
    "Qual o formato da resposta ao consultar uma venda na API da Kiwify?",
    "Quais são os campos retornados ao consultar uma venda?",
    "Como verificar o status de pagamento de uma venda?",
    "Como obter informações de cliente em uma venda na Kiwify?"
  ],
  "reasoning_pathways": ["conditional", "sequential"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "API Key"],
  "typical_integration_points": ["ERP", "Sistemas financeiros", "CRM", "Dashboards analíticos"],
  "common_error_patterns": ["ID inválido", "Venda não encontrada", "Autenticação falhou"]
}
```


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 12. Checklist de Implementação (Opcional)


> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação dos endpoints.


- [ ] Autenticação
  - [ ] Implementar mecanismo de obtenção do token OAuth
  - [ ] Armazenar ID da conta Kiwify de forma segura
  - [ ] Configurar renovação automática do token expirado


- [ ] Tratamento de Erros (4xx, 5xx)
  - [ ] Implementar handlers para "404 Not Found" (venda inexistente)
  - [ ] Adicionar tratamento para "401 Unauthorized" (token inválido)
  - [ ] Implementar logging detalhado para debug


- [ ] Retries (429, 5xx)
  - [ ] Implementar backoff exponencial
  - [ ] Definir máximo de 3 tentativas para erros de servidor
  - [ ] Adicionar jitter para evitar sincronização de retentativas


- [ ] Validação de Entrada
  - [ ] Validar formato UUID do ID da venda
  - [ ] Verificar presença e formato do token antes de enviar
  - [ ] Garantir que o ID da conta Kiwify está presente


- [ ] Mapeamento de Resposta
  - [ ] Converter timestamps para formato de data local
  - [ ] Mapear valores monetários de centavos para decimais
  - [ ] Implementar tratamento para campos opcionais ou nulos


- [ ] Logs & Monitoramento
  - [ ] Registrar tempo de resposta de cada chamada
  - [ ] Monitorar taxa de erros 404 (vendas não encontradas)
  - [ ] Implementar rastreamento de requisições (request_id)


- [ ] Cache
  - [ ] Implementar cache local com TTL de 5 minutos para consultas frequentes
  - [ ] Definir estratégia de invalidação para atualizações de vendas
  - [ ] Incluir mecanismo para forçar refresh do cache quando necessário


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
---


## 13. Glossário de Termos Técnicos


> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados na documentação.


| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Venda`                   | `Transação comercial que representa a aquisição de um produto ou serviço por um cliente na plataforma Kiwify` |
| `Token de Autenticação`   | `Credencial de segurança temporária usada para autorizar requisições à API da Kiwify` |
| `x-kiwify-account-id`     | `Identificador único da conta Kiwify, enviado como cabeçalho nas requisições` |
| `Coprodutor`              | `Parceiro que participa da divisão de receita de uma venda, representado no campo revenue_partners` |
| `Afiliado`                | `Promotor que recebe comissão por direcionar clientes para realizar uma compra` |
| `One-Click`               | `Método de compra rápida onde informações de pagamento já estão salvas, facilitando transações subsequentes` |
| `net_amount`              | `Valor líquido da venda após a dedução de taxas, impostos e comissões` |
| `charge_amount`           | `Valor total cobrado do cliente, incluindo o produto, frete e taxas` |
| `Parâmetros UTM`          | `Marcadores utilizados para rastrear a origem do tráfego que resultou em uma venda` |
| `ISO 8601`                | `Padrão internacional para representação de datas e horas, usado nos campos de timestamp da API` |


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*
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


*(Ref: Kiwify Get Sale, ID kiwify_getsale_001)*