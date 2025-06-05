# API Hotmart - Vendas - Detalhamento de Preços de Venda (Sales Price Details)


## 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Vendas - Detalhamento de Preços de Venda (Sales Price Details) |
| **Identificador Interno** | hotmart_sales_001                                               |
| **Título Curto (Ref.)**   | Hotmart Sales Price Details                                     |
| **Versão do Documento**   | 1.0.0                                                           |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação                                          |
| **Fonte Original**        | https://developers.hotmart.com/docs/pt-BR/v1/sales/sales-price-details/ |
| **URL de Referência**     | https://developers.hotmart.com/payments/api/v1/sales/price/details |
| **Status do Documento**   | Em Uso                                                          |
| **Ambiente de Referência**| Produção                                                        |
| **Idioma Original**       | Português (BR)                                                  |
| **Formato de Datas (API)**| Timestamp (ms) desde 1970-01-01 00:00:00 UTC                    |


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 2. Contexto
Este endpoint permite consultar o detalhamento dos valores de uma compra na plataforma Hotmart, fornecendo informações detalhadas como valor total, valor base para comissão, impostos, cupons de desconto, entre outros. É um recurso fundamental para análise financeira e conciliação de vendas. Por padrão, sem filtros específicos, são retornados apenas vendas com status "APPROVED" e "COMPLETE". Esse tipo de informação é essencial para produtores, afiliados e integradores que precisam acompanhar detalhadamente os aspectos financeiros das transações.


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 3. Visão Geral da API/Endpoint(s)
O endpoint de Detalhamento de Preços de Vendas permite obter informações financeiras detalhadas sobre transações realizadas na plataforma Hotmart. É possível filtrar as transações por diversos parâmetros como status da transação, tipo de pagamento, e período específico. Este endpoint fornece dados cruciais como valores base, impostos, taxas aplicadas, informações de cupons, taxas de conversão de moeda e detalhes de paginação para grandes volumes de dados. É uma ferramenta essencial para relatórios financeiros, conciliação contábil e análise de desempenho de vendas.


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 4. Detalhes Técnicos
### Endpoint de Detalhamento de Preços de Venda
* **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/sales/price/details`
* **Método HTTP:** `GET`
* **Autenticação:** Bearer Token (Authorization: Bearer :access_token)
* **Cabeçalhos Requeridos:** 
  * `Content-Type: application/json`
  * `Authorization: Bearer :access_token`


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 5. Parâmetros de Entrada
### Endpoint de Detalhamento de Preços de Venda (Query Parameters)


**Nota:** Se os parâmetros `transaction` ou `transaction_status` não forem informados, a API retornará por padrão apenas transações com status "APPROVED" e "COMPLETE".


| Parâmetro          | Descrição | Tipo | Notas / Exemplo |
| :----------------- | :-------- | :--- | :-------------- |
| `transaction`      | Código único de referência para uma transação. Identifica uma venda específica na plataforma Hotmart. Cada transação possui um código único que começa com "HP" seguido de 14 dígitos. | string | Ex: `HP17715690036014` |
| `transaction_status` | Filtra as transações pelo seu status atual no sistema. Este parâmetro permite visualizar transações em diferentes estágios do ciclo de vida do pagamento. | string | Valores possíveis: `STARTED` (Transação iniciada pelo comprador), `COMPLETE` (Transação completamente processada), `PRINTED_BILLET` (Boleto foi gerado e impresso), `WAITING_PAYMENT` (Sistema aguardando confirmação de pagamento), `APPROVED` (Pagamento aprovado pela operadora/processadora), `UNDER_ANALISYS` (Pagamento em análise de risco/fraude), `CANCELLED` (Transação cancelada), `PROTESTED` (Transação protestada pelo comprador), `REFUNDED` (Valor reembolsado ao comprador), `CHARGEBACK` (Estorno solicitado pelo comprador junto à operadora), `BLOCKED` (Transação bloqueada por regras de segurança), `OVERDUE` (Pagamento não realizado no prazo), `EXPIRED` (Prazo para pagamento expirado), `PARTIALLY_REFUNDED` (Parte do valor foi reembolsado). |
| `payment_type`     | Filtra as transações pelo método de pagamento utilizado pelo comprador. Este parâmetro permite analisar comportamentos de compra e preferências de pagamento por segmento. | string | Valores possíveis: `BILLET` (Pagamento por boleto bancário), `CASH_PAYMENT` (Pagamento em dinheiro), `CREDIT_CARD` (Pagamento por cartão de crédito), `DIRECT_BANK_TRANSFER` (Transferência bancária direta), `DIRECT_DEBIT` (Débito direto em conta), `FINANCED_BILLET` (Boleto financiado), `FINANCED_INSTALLMENT` (Parcelamento financiado), `GOOGLE_PAY` (Pagamento via Google Pay), `HOTCARD` (Pagamento via cartão proprietário Hotmart), `HYBRID` (Combinação de diferentes métodos de pagamento), `MANUAL_TRANSFER` (Transferência manual registrada no sistema), `PAYPAL` (Pagamento via PayPal nacional), `PAYPAL_INTERNACIONAL` (Pagamento via PayPal internacional), `PICPAY` (Pagamento via PicPay), `PIX` (Pagamento via PIX), `SAMSUNG_PAY` (Pagamento via Samsung Pay), `WALLET` (Pagamento via carteiras digitais). |
| `max_results`      | Define o número máximo de itens (transações) que devem ser retornados em uma única página de resultados. Este parâmetro é essencial para gerenciar grandes volumes de dados, evitando sobrecarga no processamento de respostas extensas. | integer | Ex: `50` (retorna até 50 transações na resposta). Se não informado, utiliza o valor padrão definido pela API. |
| `page_token`       | Token de cursor que indica a partir de qual ponto da lista total de resultados a página atual deve começar. Este valor é obtido da resposta anterior através dos campos `next_page_token` ou `prev_page_token`. Fundamental para navegação entre páginas em conjuntos grandes de dados. | string | Ex: `eyJyb3dzIjoxMCwicGFnZSI6Mn0=` (token codificado em base64 que aponta para um ponto específico na lista de resultados) |
| `product_id`       | Filtra as transações para retornar apenas aquelas relacionadas a um produto específico, identificado pelo seu ID único na plataforma Hotmart. Permite análise de vendas por produto. | integer | Ex: `8547854` (ID numérico de 7 dígitos que identifica unicamente um produto) |
| `start_date`       | Data e hora inicial do período para o filtro de transações. A data deve ser fornecida em milissegundos desde a época Unix (1970-01-01 00:00:00 UTC). Este parâmetro é usado em conjunto com `end_date` para definir um intervalo temporal para a consulta. | long | Ex: `1609459200000` (Representa 2021-01-01 00:00:00 UTC). Utilizado para análises em períodos específicos como meses, trimestres ou anos. |
| `end_date`         | Data e hora final do período para o filtro de transações. A data deve ser fornecida em milissegundos desde a época Unix (1970-01-01 00:00:00 UTC). Este parâmetro delimita o fim do intervalo temporal da consulta. | long | Ex: `1612137599000` (Representa 2021-01-31 23:59:59 UTC). Para análises diárias, recomenda-se definir o valor para 23:59:59 do dia em questão. |


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Endpoint de Detalhamento de Preços de Venda
#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `items`       | Lista contendo todas as transações retornadas que atendem aos critérios de filtro. Cada elemento representa uma transação individual com seus detalhes financeiros. | array  |
| `page_info`   | Objeto contendo informações sobre a paginação dos resultados, incluindo tokens para navegação entre páginas e estatísticas da consulta. | object |


#### 6.1.2 Detalhes do Objeto `items` (elementos do array)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `transaction`       | Código único de referência para uma transação na plataforma Hotmart. Identificador primário de uma venda. | string | Ex: `HP17715690036014`. Sempre começa com "HP" seguido de 14 caracteres numéricos. |
| `product`           | Objeto contendo informações sobre o produto vendido na transação. | object | Contém identificação e nome do produto associado à venda. |
| `product.id`        | Identificador único (ID) do produto vendido na plataforma Hotmart. | integer | Número de 7 dígitos que identifica unicamente um produto. Ex: `8547854` |
| `product.name`      | Nome do produto conforme cadastrado na plataforma. | string | Nome comercial do produto visível para os compradores. Ex: `"Curso de Marketing Digital"` |
| `base`              | Objeto contendo o valor base utilizado para cálculos de comissionamento e divisões de receita. Este é o valor antes de aplicação de impostos ou taxas adicionais. | object | Fundamental para cálculos de comissões para afiliados e produtores. |
| `base.value`        | Valor numérico base da transação, utilizado como referência para divisões de receita. | number | Ex: `930.00` (valor em unidades monetárias, com precisão de duas casas decimais) |
| `base.currency_code`| Código da moeda do valor base, no formato padrão internacional de três letras (ISO 4217). | string | Ex: `MXN` (Peso Mexicano), `BRL` (Real Brasileiro), `USD` (Dólar Americano) |
| `total`             | Objeto contendo o preço total cobrado do cliente, incluindo o valor base, impostos (VAT) e eventuais juros de parcelamento. | object | Representa o valor efetivamente pago pelo cliente. |
| `total.value`       | Valor numérico total da transação, incluindo todas as taxas e impostos aplicáveis. | number | Ex: `486.25` (valor em unidades monetárias, com precisão de duas casas decimais) |
| `total.currency_code`| Código da moeda do valor total, no formato padrão internacional de três letras (ISO 4217). | string | Ex: `MXN` (Peso Mexicano), `BRL` (Real Brasileiro), `USD` (Dólar Americano) |
| `vat`               | Objeto contendo informações sobre o imposto sobre valor agregado (Value Added Tax) aplicado à transação. | object | Relevante principalmente para transações internacionais ou sujeitas a regimes tributários específicos. |
| `vat.value`         | Valor numérico do imposto cobrado sobre a transação. | number | Ex: `193.25` (valor em unidades monetárias, com precisão de duas casas decimais) |
| `vat.currency_code` | Código da moeda do valor de imposto, no formato padrão internacional de três letras (ISO 4217). | string | Ex: `BRL` (Real Brasileiro) - Pode ser diferente da moeda do valor base em transações internacionais. |
| `fee`               | Objeto contendo informações sobre valores de juros cobrados em compras parceladas ou taxas adicionais aplicáveis. | object | Representa custos financeiros adicionais aplicados à transação. |
| `fee.value`         | Valor numérico dos juros ou taxas adicionais cobradas na transação. | number | Ex: `55.00` (valor em unidades monetárias, com precisão de duas casas decimais) |
| `fee.currency_code` | Código da moeda dos juros, no formato padrão internacional de três letras (ISO 4217). | string | Ex: `USD` (Dólar Americano) - Pode ser diferente da moeda do valor base. |
| `coupon`            | Objeto contendo informações sobre cupom de desconto aplicado à transação, se houver. | object | Presente apenas quando um cupom foi utilizado na compra. |
| `coupon.code`       | Código identificador do cupom aplicado na transação. | string | Ex: `coupon1` - Código alfanumérico que identifica unicamente o cupom. |
| `coupon.value`      | Valor ou percentual de desconto aplicado pelo cupom na transação. | number | Ex: `22.9` - Representa o valor absoluto ou percentual do desconto. |
| `real_conversion_rate`| Taxa de conversão utilizada para converter o valor original da oferta no valor pago pelo comprador em sua moeda local. Importante para transações internacionais. | number | Ex: `708.75` - Representa a taxa de conversão aplicada. Multiplicar o valor na moeda original por esta taxa resulta no valor na moeda local. |


#### 6.1.3 Detalhes do Objeto `page_info`
| Campo Aninhado           | Descrição | Tipo | Notas |
| :----------------------- | :-------- | :--- | :---- |
| `total_results`          | Número total de itens na lista completa de resultados, desconsiderando a paginação. Indica o tamanho total do conjunto de dados que atende aos critérios de filtro. | integer | Ex: `14` - Indica que existem 14 transações no total que atendem aos critérios. |
| `next_page_token`        | Token de referência para a próxima página de resultados. Este valor deve ser utilizado no parâmetro `page_token` para obter a próxima página. | string | Ex: `eyJyb3dzIjoxMCwicGFnZSI6Mn0=` - Token codificado em base64. Ausente quando não há mais páginas disponíveis. |
| `prev_page_token`        | Token de referência para a página anterior de resultados. Este valor deve ser utilizado no parâmetro `page_token` para obter a página anterior. | string | Ex: `eyJyb3dzIjoxMCwicGFnZSI6MX0=` - Token codificado em base64. Ausente na primeira página. |
| `results_per_page`       | Quantidade de itens presentes na página atual. Pode ser menor que `max_results` se for a última página ou se houver menos resultados que o solicitado. | integer | Ex: `10` - Indica que a página atual contém 10 transações. |


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 7. Exemplos de Requisição e Resposta
### Endpoint de Detalhamento de Preços de Venda
#### 7.1.1 Exemplo de Requisição (cURL)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/sales/price/details?transaction_status=CANCELLED&payment_type=CREDIT_CARD' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer :access_token'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
{
  "items": [
    {
      "transaction": "HP14916251567230",
      "product": {
        "id": 8547854,
        "name": "product1"
      },
      "base": {
        "value": 930,
        "currency_code": "MXN"
      },
      "total": {
        "value": 486.25,
        "currency_code": "MXN"
      },
      "vat": {
        "value": 193.25,
        "currency_code": "BRL"
      },
      "fee": {
        "value": 55,
        "currency_code": "USD"
      },
      "coupon": {
        "code": "coupon1",
        "value": 22.9
      },
      "real_conversion_rate": 708.75
    }
  ],
  "page_info": {
    "total_results": 14,
    "next_page_token": "eyJyb3dzIjoxMCwicGFnZSI6Mn0=",
    "results_per_page": 10
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro)
```json
{
  "code": "UNAUTHORIZED",
  "message": "Authentication failed. Please check your access token."
}
```


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              |
| :--------------------- | :----------------------------------------------------------- |
| `200 OK`               | Sucesso na requisição. Os dados solicitados foram encontrados e retornados corretamente. |
| `400 Bad Request`      | Erro nos parâmetros da requisição. Verifique o formato e os valores dos parâmetros enviados, especialmente datas e IDs. |
| `401 Unauthorized`     | Falha na autenticação. O token de acesso é inválido, expirou ou não foi fornecido corretamente no header Authorization. |
| `403 Forbidden`        | Não possui permissão para acessar o recurso. O token é válido, mas não tem permissões suficientes para acessar estes dados. |
| `404 Not Found`        | Recurso não encontrado. Os parâmetros fornecidos não correspondem a nenhuma transação existente ou acessível. |
| `429 Too Many Requests`| Limite de requisições excedido. A API possui limites de requisições por intervalo de tempo que foram ultrapassados. |
| `500 Internal Server Error` | Erro interno no servidor. Problema no processamento da requisição no lado do servidor Hotmart. |


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1. **Consultar detalhes de uma transação específica**
   * Objetivo: Verificar os valores exatos de uma venda individual para conciliação financeira
   * Como Fazer: Utilize o parâmetro `transaction` com o código da transação (ex: ?transaction=HP17715690036014)
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


2. **Listar todas as vendas canceladas**
   * Objetivo: Auditar transações canceladas para análise de padrões e motivos de cancelamento
   * Como Fazer: Defina `transaction_status=CANCELLED` na requisição
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


3. **Verificar vendas realizadas via cartão de crédito**
   * Objetivo: Analisar vendas por método de pagamento específico para estratégias de conversão
   * Como Fazer: Utilize `payment_type=CREDIT_CARD` na requisição
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


4. **Consultar vendas de um produto específico**
   * Objetivo: Avaliar o desempenho financeiro de um produto individual na plataforma
   * Como Fazer: Forneça o `product_id` do produto desejado (ex: ?product_id=8547854)
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


5. **Listar vendas aprovadas em um período específico**
   * Objetivo: Analisar vendas em uma janela temporal específica para relatórios mensais
   * Como Fazer: Combine `transaction_status=APPROVED` com `start_date` e `end_date` em milissegundos
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


6. **Auditar reembolsos emitidos**
   * Objetivo: Verificar todos os reembolsos realizados para análise financeira e de satisfação
   * Como Fazer: Use `transaction_status=REFUNDED` para listar todas as transações reembolsadas
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


7. **Consultar chargebacks recebidos**
   * Objetivo: Analisar chargebacks para gestão de risco e identificação de fraudes potenciais
   * Como Fazer: Defina `transaction_status=CHARGEBACK` na requisição
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


8. **Verificar vendas via PIX**
   * Objetivo: Analisar adoção de pagamento via PIX e sua contribuição para as vendas totais
   * Como Fazer: Use `payment_type=PIX` para filtrar apenas pagamentos realizados via PIX
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


9. **Consultar vendas com pagamento via boleto**
   * Objetivo: Verificar vendas realizadas via boleto bancário e taxa de conversão deste método
   * Como Fazer: Configure `payment_type=BILLET` na requisição
   *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


10. **Listar transações completas do último mês**
    * Objetivo: Gerar relatório mensal de vendas concluídas para fechamento contábil
    * Como Fazer: Combine `transaction_status=COMPLETE` com datas do mês anterior em `start_date` e `end_date`
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


11. **Consultar vendas internacionais via PayPal**
    * Objetivo: Analisar penetração em mercados internacionais e taxas de conversão específicas
    * Como Fazer: Use `payment_type=PAYPAL_INTERNACIONAL` na requisição
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


12. **Verificar vendas com aplicação de cupom de desconto**
    * Objetivo: Avaliar efetividade de campanhas com cupom e impacto nos valores base de comissão
    * Como Fazer: Filtrar resultados e analisar o campo `coupon` nas respostas para transações com cupons aplicados
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


13. **Analisar impostos pagos (VAT) por região**
    * Objetivo: Realizar avaliação tributária por localidade para planejamento fiscal
    * Como Fazer: Obtenha dados de múltiplas transações e agrupe por região, analisando o campo `vat` nas respostas
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


14. **Consultar vendas parceladas com juros**
    * Objetivo: Avaliar o impacto financeiro de parcelamentos na receita e fluxo de caixa
    * Como Fazer: Filtrar resultados e analisar transações onde o campo `fee` tem valor maior que zero
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


15. **Verificar vendas em processamento/análise**
    * Objetivo: Monitorar vendas pendentes de aprovação para projeções de receita
    * Como Fazer: Use `transaction_status=UNDER_ANALISYS` para listar transações em análise
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


16. **Consultar vendas com boletos impressos mas não pagos**
    * Objetivo: Realizar follow-up com potenciais clientes para aumentar conversão
    * Como Fazer: Defina `transaction_status=PRINTED_BILLET` para transações com boleto emitido
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


17. **Listar vendas vencidas ou expiradas**
    * Objetivo: Limpar pipeline de vendas e identificar oportunidades perdidas
    * Como Fazer: Use `transaction_status=OVERDUE` ou `transaction_status=EXPIRED` para filtrar transações não concluídas
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


18. **Verificar vendas via carteiras digitais**
    * Objetivo: Analisar tendências de pagamentos digitais e otimizar opções de checkout
    * Como Fazer: Use `payment_type=WALLET` ou tipos específicos como `GOOGLE_PAY` ou `SAMSUNG_PAY`
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


19. **Consultar vendas com pagamento híbrido**
    * Objetivo: Analisar vendas com múltiplos métodos de pagamento para entender padrões de compra complexos
    * Como Fazer: Use `payment_type=HYBRID` para identificar transações com pagamentos combinados
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


20. **Analisar taxas de conversão de moeda em vendas internacionais**
    * Objetivo: Avaliar impacto cambial nas vendas e otimizar precificação internacional
    * Como Fazer: Obtenha dados de múltiplas transações internacionais e analise o campo `real_conversion_rate` nas respostas
    *(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 10. Notas Adicionais
* **Filtros padrão:** Se os parâmetros `transaction` ou `transaction_status` não forem informados, serão retornados apenas os status "APPROVED" e "COMPLETE". Isto é importante para relatórios padrão que normalmente focam em vendas concluídas com sucesso.


* **Paginação:** Para conjuntos de dados grandes, utilize os parâmetros `max_results` para definir o tamanho da página e `page_token` para navegar entre páginas. Os tokens para próxima e página anterior estão disponíveis no objeto `page_info` da resposta.


* **Formato de Datas:** Todas as datas na API são representadas em milissegundos desde 1970-01-01 00:00:00 UTC (timestamp Unix em milissegundos). Para converter datas entre formatos, utilize bibliotecas de manipulação de data disponíveis na linguagem de programação que estiver utilizando.


* **Moedas:** Os valores monetários são sempre acompanhados de seu código de moeda (`currency_code`) no formato ISO 4217 de três letras. Note que diferentes componentes do preço (base, vat, fee) podem estar em moedas diferentes, especialmente em transações internacionais.


* **Recomendação de uso:** Para análises em tempo real de vendas, considere programar consultas periódicas ao endpoint para atualização de painéis e relatórios de gestão.


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sales_001",
  "api_provider": "Hotmart",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Consultar Detalhamento de Preços", "Análise Financeira de Vendas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Financial",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Transação", "Produto", "Pagamento", "Preço", "Imposto", "Cupom", "Taxa de Conversão"],
  "context_level": ["intermediate", "advanced"],
  "topic_cluster": ["e-commerce", "payments", "financial_analysis", "sales_reporting"],
  "db_relations": { 
    "tables": ["transactions", "products", "payments", "coupons", "tax_rates"], 
    "schemas": ["sales", "financial"]
  },
  "related_concepts": [
    "comissão", 
    "impostos", 
    "descontos", 
    "conversão monetária", 
    "métodos de pagamento", 
    "ciclo de vida da transação", 
    "relatórios financeiros"
  ],
  "question_embeddings": [
    "Como consultar detalhes de preço de uma venda específica na Hotmart?",
    "Quais tipos de pagamento posso filtrar no endpoint de detalhes de preço?",
    "Como obter informações sobre impostos (VAT) nas vendas da Hotmart?",
    "Como filtrar vendas canceladas na API da Hotmart?",
    "Como funcionam as taxas de conversão de moeda nas vendas internacionais da Hotmart?"
  ],
  "reasoning_pathways": [
    "análise financeira", 
    "auditoria de vendas", 
    "conciliação contábil", 
    "avaliação de desempenho de produtos",
    "análise de métodos de pagamento",
    "otimização de campanhas com cupom"
  ],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*


---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação via Bearer Token
- [ ] Tratamento de Erros (4xx, 5xx)
- [ ] Retries (429, 5xx) com backoff exponencial
- [ ] Paginação (usando max_results e page_token)
- [ ] Validação de Entrada (filtros e parâmetros)
- [ ] Mapeamento de Resposta para modelo de dados interno
- [ ] Logs & Monitoramento de chamadas à API
- [ ] Cache para requisições frequentes (TTL: 5-15 minutos)
- [ ] Testes (Casos normais, Edge-cases, filtros variados)
- [ ] Verificação de Rate Limits da API
- [ ] Formatação e conversão de datas (timestamps)
- [ ] Tratamento de valores monetários e múltiplas moedas
- [ ] Implementação de timeout adequado (10-30 segundos)
- [ ] Documentação de uso interno


*(Ref: Hotmart Sales Price Details, ID hotmart_salespricedetails_001)*