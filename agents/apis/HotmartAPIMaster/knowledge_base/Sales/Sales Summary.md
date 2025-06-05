# API Hotmart - Vendas - Obter Sumário de Vendas (Sales Summary)


## 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Vendas - Obter Sumário de Vendas (Sales Summary) |
| **Identificador Interno** | hotmart_sales_001                                               |
| **Título Curto (Ref.)**   | Hotmart Sales Summary                                          |
| **Versão do Documento**   | 1.1.0                                                          |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação de APIs                                 |
| **Fonte Original**        | Documentação Oficial Hotmart                                   |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/v1/sales/sales-summary/ |
| **Status do Documento**   | Em Uso                                                         |
| **Ambiente de Referência**| Produção                                                       |
| **Idioma Original**       | Português (BR)                                                 |
| **Formato de Datas (API)**| Timestamp Unix (milissegundos)                                 |
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 2. Contexto
O endpoint de Sumário de Vendas permite obter os valores de comissões totalizados por moeda, oferecendo uma visão consolidada das transações comerciais realizadas na plataforma Hotmart. Este endpoint é particularmente útil para análises financeiras, relatórios gerenciais e acompanhamento de vendas em diferentes moedas. Por padrão, apenas transações com status "APPROVED" e "COMPLETE" são consideradas, a menos que filtros específicos de status (`transaction_status`) ou transação (`transaction`) sejam aplicados. Este endpoint faz parte do módulo de Vendas da API Payments da Hotmart (ID Interno: hotmart_sales_001).
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 3. Visão Geral da API/Endpoint(s)
Este endpoint GET (`/sales/summary`) fornece um resumo totalizado das transações de vendas, agregando e agrupando comissões por moeda. O recurso permite análises detalhadas através de diversos filtros como produto, período, status da transação, tipo de pagamento, afiliado, oferta, ou origem da venda. Os resultados são apresentados como um array de objetos, cada um representando uma moeda diferente com seu respectivo valor total e quantidade de transações. O endpoint suporta paginação completa para lidar eficientemente com grandes volumes de dados, permitindo a navegação através de tokens de página.
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 4. Detalhes Técnicos
### Endpoint: /sales/summary
*   **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/sales/summary`
*   **Método HTTP:** `GET`
*   **Autenticação:** `Bearer Token` no cabeçalho `Authorization`. O token deve ter as permissões adequadas para acessar dados de vendas e comissões.
*   **Content-Type:** `application/json` para o cabeçalho `Accept`
*   **Versão da API:** `v1`
*   **Base URL:** `https://developers.hotmart.com/payments/api`
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 5. Parâmetros de Entrada
### Endpoint: /sales/summary (Query Parameters)
| Parâmetro          | Descrição | Tipo | Notas / Exemplo |
| :----------------- | :-------- | :--- | :-------------- |
| `transaction`      | Código único de referência para uma transação específica. Filtra o sumário para incluir apenas esta transação. Útil para verificar uma venda individual. | string | Formato alfanumérico. Ex: `HP17716038716369` |
| `transaction_status` | Filtra as transações pelo status da compra. Se este parâmetro e `transaction` não forem informados, o padrão é retornar apenas `APPROVED` e `COMPLETE`. Os valores são case-sensitive e devem ser enviados exatamente como documentados. Veja a lista completa de valores possíveis abaixo. | string | Ex: `APPROVED`, `CANCELLED`, `REFUNDED` |
| `max_results`      | Número máximo de itens (sumários por moeda) a serem retornados por página. Usado para paginação. O valor padrão é 30 itens e o máximo permitido é 100. Valores maiores serão limitados automaticamente. | integer | Valores entre 1 e 100. Ex: `50` |
| `page_token`       | Token opaco utilizado para obter a próxima página de resultados ou a página anterior. Obtido dos campos `next_page_token` ou `prev_page_token` da resposta anterior. Não deve ser modificado ou gerado manualmente. | string | Ex: `CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA` |
| `product_id`       | ID numérico do produto vendido. Filtra o sumário para incluir apenas vendas deste produto. Permite analisar o desempenho de um produto específico. | integer | Número inteiro positivo. Ex: `1234567` |
| `start_date`       | Data inicial do período para o filtro, em formato timestamp Unix (milissegundos). Inclui transações a partir desta data/hora. Não pode ser futuro. | long | Ex: `1678848000000` (15/Mar/2023 00:00:00 UTC) |
| `end_date`         | Data final do período para o filtro, em formato timestamp Unix (milissegundos). Inclui transações até esta data/hora. Deve ser maior que `start_date`. | long | Ex: `1678934399000` (15/Mar/2023 23:59:59 UTC) |
| `sales_source`     | Código SRC (parâmetro de URL) utilizado no link da página de pagamento para identificar a origem da venda. Filtra vendas por canal ou campanha específica. | string | Alfanumérico. Ex: `facebook_ads`, `email_campaign` |
| `affiliate_name`   | Nome da pessoa Afiliada responsável pela venda. Filtra vendas atribuídas a este afiliado específico. Útil para analisar desempenho de afiliados. | string | Sensível a acentos/capitalização. Ex: `João Silva` |
| `payment_type`     | Tipo de pagamento utilizado pela pessoa compradora. Filtra por método de pagamento. Os valores são case-sensitive. Veja a lista completa de valores possíveis abaixo. | string | Ex: `CREDIT_CARD`, `PIX`, `BILLET` |
| `offer_code`       | Código da oferta específica do produto vendido. Filtra vendas associadas a esta oferta. Útil para analisar desempenho de diferentes ofertas de um mesmo produto. | string | Alfanumérico. Ex: `BLACK_FRIDAY_2023` |


**Valores possíveis para `transaction_status`:**
- `APPROVED`: Compra aprovada, pagamento confirmado, mas ainda em processamento.
- `BLOCKED`: Compra bloqueada por questões de segurança ou compliance.
- `CANCELLED`: Compra cancelada pelo cliente ou pelo produtor.
- `CHARGEBACK`: Compra contestada pelo cliente junto à operadora do cartão (chargeback).
- `COMPLETE`: Compra totalmente processada e finalizada com sucesso.
- `EXPIRED`: Compra expirada por falta de pagamento dentro do prazo.
- `NO_FUNDS`: Compra sem fundos suficientes para processamento.
- `OVERDUE`: Compra em atraso (pagamento não realizado na data esperada).
- `PARTIALLY_REFUNDED`: Compra parcialmente reembolsada ao cliente.
- `PRE_ORDER`: Pré-compra (pagamento confirmado para produto ainda não disponível).
- `PRINTED_BILLET`: Boleto impresso, mas ainda não pago.
- `PROCESSING_TRANSACTION`: Transação em processamento, aguardando confirmação.
- `PROTESTED`: Compra protestada por questões legais ou disputas.
- `REFUNDED`: Compra totalmente reembolsada ao cliente.
- `STARTED`: Compra iniciada, mas ainda não finalizada pelo cliente.
- `UNDER_ANALISYS`: Compra sob análise de risco ou fraude.
- `WAITING_PAYMENT`: Aguardando pagamento (boleto gerado, PIX aguardando, etc).


**Valores possíveis para `payment_type`:**
- `BILLET`: Boleto bancário brasileiro.
- `CASH_PAYMENT`: Pagamento em dinheiro (ex: OXXO México, Baloto Colômbia).
- `CREDIT_CARD`: Cartão de crédito (todas as bandeiras).
- `DIRECT_BANK_TRANSFER`: Transferência bancária direta (ex: TEF, DOC, TED).
- `DIRECT_DEBIT`: Débito direto em conta bancária.
- `FINANCED_BILLET`: Boleto financiado por terceiros.
- `FINANCED_INSTALLMENT`: Parcelamento financiado por terceiros.
- `GOOGLE_PAY`: Pagamento via carteira digital Google Pay.
- `HOTCARD`: Cartão digital Hotmart (quando aplicável).
- `HYBRID`: Pagamento realizado combinando múltiplos métodos.
- `MANUAL_TRANSFER`: Transferência manual confirmada pelo produtor.
- `PAYPAL`: Pagamento via PayPal em moeda local.
- `PAYPAL_INTERNACIONAL`: PayPal em transações internacionais/cross-border.
- `PICPAY`: Pagamento via carteira digital PicPay (Brasil).
- `PIX`: Pagamento via PIX (sistema brasileiro de pagamentos instantâneos).
- `SAMSUNG_PAY`: Pagamento via carteira digital Samsung Pay.
- `WALLET`: Saldo em carteira digital Hotmart.
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Endpoint: /sales/summary
#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   | Notas |
| :------------ | :-------- | :----- | :---- |
| `items`       | Lista contendo os objetos de sumário, um para cada moeda encontrada nas transações filtradas. A ordem não é garantida e pode variar. | array | Pode ser vazia (`[]`) se não houver resultados para os filtros aplicados. |
| `page_info`   | Objeto contendo informações sobre a paginação dos resultados. Essencial para implementar navegação entre páginas. | object | Sempre presente, mesmo se `items` for vazio. |


#### 6.1.2 Detalhes do Objeto `items` (Array de Objetos)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `total_items`       | Quantidade total de transações (comissões) que foram somadas para gerar o valor total nesta moeda específica, considerando os filtros aplicados. Representa o número de vendas, não o número de produtos vendidos. | integer | Sempre positivo. Ex: `15` significa 15 transações nesta moeda. |
| `total_value`       | Objeto contendo o valor monetário total das comissões e a moeda correspondente. | object | Nunca será nulo. Representa o somatório financeiro. |


#### 6.1.3 Detalhes do Objeto `total_value` (Dentro de `items`)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `value`             | Valor numérico total das comissões no período/filtros para esta moeda. Representa o montante financeiro somado. | float | Ex: `1500.75`. Pode ter até 2 casas decimais. |
| `currency_code`     | Código da moeda no padrão ISO 4217. Identifica a moeda dos valores apresentados. | string | Ex: `"BRL"` (Real Brasileiro), `"USD"` (Dólar Americano), `"EUR"` (Euro) |


#### 6.1.4 Detalhes do Objeto `page_info`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `total_results`     | Quantidade total de *sumários por moeda* que a consulta inteira retornaria, desconsiderando a paginação. Indica quantos tipos diferentes de moeda existem no resultado completo. | integer | Sempre presente. Ex: `3` indica resultados em 3 moedas diferentes no total. |
| `next_page_token`   | Token opaco que deve ser enviado no parâmetro `page_token` da próxima requisição para obter a página seguinte de resultados. Não deve ser decodificado ou modificado. | string | **Ausente** se esta for a última página (não há mais resultados). |
| `prev_page_token`   | Token opaco que deve ser enviado no parâmetro `page_token` da próxima requisição para obter a página anterior de resultados. Não deve ser decodificado ou modificado. | string | **Ausente** se esta for a primeira página. |
| `results_per_page`  | Quantidade de itens (sumários por moeda) retornados *nesta página específica*. Corresponde ao `max_results` enviado na requisição ou ao padrão da API. | integer | Sempre presente. Será menor ou igual ao `max_results` solicitado. |
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 7. Exemplos de Requisição e Resposta
### Endpoint: /sales/summary
#### 7.1.1 Exemplo de Requisição (cURL - Filtrando por produto e período)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/sales/summary?product_id=1234567&start_date=1672531200000&end_date=1675209599000' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer SEU_ACCESS_TOKEN'
```


#### 7.1.2 Exemplo de Requisição (cURL - Filtrando por produto e tipo de pagamento)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/sales/summary?product_id=1234567&payment_type=CREDIT_CARD' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer SEU_ACCESS_TOKEN'
```


#### 7.1.3 Exemplo de Resposta (JSON - Sucesso 200 - Múltiplas Moedas)
```json
{
  "items": [
    {
      "total_items": 15,
      "total_value": {
        "value": 1250.50,
        "currency_code": "BRL"
      }
    },
    {
      "total_items": 5,
      "total_value": {
        "value": 350.00,
        "currency_code": "USD"
      }
    }
  ],
  "page_info": {
    "total_results": 2,
    "results_per_page": 10
  }
}
```


#### 7.1.4 Exemplo de Resposta (JSON - Sucesso 200 - Com Paginação)
```json
{
  "items": [
    {
      "total_items": 120,
      "total_value": {
        "value": 5250.75,
        "currency_code": "BRL"
      }
    },
    {
      "total_items": 85,
      "total_value": {
        "value": 2780.50,
        "currency_code": "USD"
      }
    }
  ],
  "page_info": {
    "total_results": 4,
    "next_page_token": "CiAKGjBpNDd2Nmp2Zml2cXRwYjBpOXA5cGdtbzAShAPYAd54AQ",
    "results_per_page": 2
  }
}
```


#### 7.1.5 Exemplo de Resposta (JSON - Sucesso 200 - Sem Resultados)
```json
{
  "items": [],
  "page_info": {
    "total_results": 0,
    "results_per_page": 10
  }
}
```


#### 7.1.6 Exemplo de Resposta (JSON - Erro 400 - Parâmetro Inválido)
```json
{
  "error": "invalid_parameter",
  "error_description": "The parameter 'start_date' has an invalid format. Expected timestamp in milliseconds."
}
```


#### 7.1.7 Exemplo de Resposta (JSON - Erro 401 - Não Autenticado)
```json
{
  "error": "invalid_token",
  "error_description": "The access token is invalid or has expired."
}
```


#### 7.1.8 Exemplo de Resposta (JSON - Erro 403 - Sem Permissão)
```json
{
  "error": "insufficient_permissions",
  "error_description": "You don't have permission to access sales data for this product."
}
```
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              | Notas Específicas / Causas Comuns |
| :--------------------- | :----------------------------------------------------------- | :-------------------------------- |
| `200 OK`               | Sucesso. A resposta contém o sumário de vendas solicitado. O array `items` pode estar vazio se nenhum resultado corresponder aos filtros. | Mesmo com resultados vazios, o código 200 é retornado quando a requisição é válida. |
| `400 Bad Request`      | Erro na requisição devido a parâmetros inválidos ou formato incorreto. | Causas comuns: Timestamp `start_date`/`end_date` em formato não numérico; `product_id` não numérico; `transaction_status` ou `payment_type` com valor não suportado; `end_date` menor que `start_date`; `max_results` menor que 1. |
| `401 Unauthorized`     | Falha na autenticação. O Bearer Token está ausente, inválido ou expirado. | Verifique se o token foi corretamente gerado, não expirou, e está sendo enviado no formato correto: `Authorization: Bearer SEU_ACCESS_TOKEN`. |
| `403 Forbidden`        | Autenticado com sucesso, mas sem permissão para acessar este recurso ou os dados solicitados. | O usuário associado ao token não tem permissões suficientes para acessar dados de vendas do produto especificado. Verifique se o produto pertence à conta associada ao token. |
| `404 Not Found`        | Endpoint não encontrado ou recurso específico inexistente. | Verifique a URL base e o caminho do endpoint. Pode ocorrer se a versão da API (v1) estiver incorreta ou se o recurso específico foi descontinuado. |
| `429 Too Many Requests`| Limite de requisições (Rate Limit) excedido. O cliente deve aguardar antes de fazer novas requisições. | O cabeçalho `Retry-After` pode indicar quantos segundos esperar antes de tentar novamente. Implemente backoff exponencial para mitigar este erro. |
| `500 Internal Server Error` | Erro inesperado no servidor da API Hotmart. Não é um problema do cliente ou da requisição. | Não altere sua requisição. Tente novamente após alguns minutos. Se persistir, verifique o status da API (status.hotmart.com) ou contate o suporte. |
| `503 Service Unavailable` | Servidor temporariamente indisponível devido a manutenção programada ou sobrecarga. | Recomenda-se aguardar alguns minutos e tentar novamente. O cabeçalho `Retry-After` pode indicar quando o serviço estará disponível novamente. |
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1.  **Obter sumário total de vendas de um produto específico**
    *   Objetivo: Visualizar o valor total e quantidade de vendas para um produto específico em todas as moedas
    *   Como Fazer: `GET /sales/summary?product_id=1234567`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
2.  **Analisar vendas de Janeiro/2023**
    *   Objetivo: Obter o sumário das transações dentro de um mês específico
    *   Como Fazer: `GET /sales/summary?start_date=1672531200000&end_date=1675209599000` (1/Jan a 31/Jan/2023)
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
3.  **Verificar total de vendas por cartão de crédito**
    *   Objetivo: Analisar o volume de vendas realizadas especificamente com cartão de crédito
    *   Como Fazer: `GET /sales/summary?payment_type=CREDIT_CARD`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
4.  **Obter sumário apenas de vendas Aprovadas**
    *   Objetivo: Filtrar o sumário para mostrar apenas transações aprovadas pela operadora
    *   Como Fazer: `GET /sales/summary?transaction_status=APPROVED`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
5.  **Obter sumário apenas de vendas Completas**
    *   Objetivo: Visualizar apenas transações que atingiram o status final de completadas
    *   Como Fazer: `GET /sales/summary?transaction_status=COMPLETE`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
6.  **Analisar total de vendas Canceladas**
    *   Objetivo: Verificar o impacto financeiro dos cancelamentos nas vendas
    *   Como Fazer: `GET /sales/summary?transaction_status=CANCELLED`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
7.  **Monitorar valor total de Chargebacks**
    *   Objetivo: Avaliar o impacto financeiro de chargebacks nas vendas
    *   Como Fazer: `GET /sales/summary?transaction_status=CHARGEBACK`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
8.  **Verificar desempenho de vendas de um Afiliado específico**
    *   Objetivo: Analisar o volume de vendas gerado por um afiliado particular
    *   Como Fazer: `GET /sales/summary?affiliate_name=Nome%20do%20Afiliado`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
9.  **Analisar vendas originadas por uma campanha de marketing**
    *   Objetivo: Medir o desempenho de uma campanha específica através do código SRC
    *   Como Fazer: `GET /sales/summary?sales_source=facebook_campaign_2023`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
10. **Verificar total de vendas por Boleto**
    *   Objetivo: Analisar o volume de vendas realizadas via boleto bancário
    *   Como Fazer: `GET /sales/summary?payment_type=BILLET`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
11. **Analisar total de vendas por PIX**
    *   Objetivo: Medir a adoção e o volume de vendas realizadas via PIX (pagamento instantâneo brasileiro)
    *   Como Fazer: `GET /sales/summary?payment_type=PIX`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
12. **Verificar desempenho de uma Oferta específica**
    *   Objetivo: Analisar o sucesso de uma oferta específica de produto
    *   Como Fazer: `GET /sales/summary?offer_code=BLACK_FRIDAY_2023`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
13. **Monitorar valor total de vendas Aguardando Pagamento**
    *   Objetivo: Verificar o volume financeiro de vendas pendentes de pagamento
    *   Como Fazer: `GET /sales/summary?transaction_status=WAITING_PAYMENT`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
14. **Analisar valor total de vendas Expiradas**
    *   Objetivo: Verificar oportunidades perdidas devido a expiração de pagamentos
    *   Como Fazer: `GET /sales/summary?transaction_status=EXPIRED`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
15. **Verificar valor total de Reembolsos completos**
    *   Objetivo: Medir o impacto financeiro de reembolsos totais nas vendas
    *   Como Fazer: `GET /sales/summary?transaction_status=REFUNDED`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
16. **Monitorar valor total de Reembolsos Parciais**
    *   Objetivo: Analisar o impacto financeiro de reembolsos parciais nas vendas
    *   Como Fazer: `GET /sales/summary?transaction_status=PARTIALLY_REFUNDED`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
17. **Analisar vendas via PayPal**
    *   Objetivo: Verificar o volume de transações processadas via PayPal
    *   Como Fazer: `GET /sales/summary?payment_type=PAYPAL`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
18. **Combinar múltiplos filtros para análise detalhada**
    *   Objetivo: Analisar vendas de um produto específico, via cartão de crédito, em Janeiro/2023
    *   Como Fazer: `GET /sales/summary?product_id=1234567&payment_type=CREDIT_CARD&start_date=1672531200000&end_date=1675209599000`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
19. **Verificar vendas Aprovadas por PIX**
    *   Objetivo: Analisar especificamente transações aprovadas feitas via PIX
    *   Como Fazer: `GET /sales/summary?transaction_status=APPROVED&payment_type=PIX`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
    
20. **Implementar paginação para análise completa**
    *   Objetivo: Navegar por todos os resultados quando há muitas moedas diferentes
    *   Como Fazer: Primeira chamada: `GET /sales/summary?max_results=50`, depois usar o `next_page_token` retornado: `GET /sales/summary?max_results=50&page_token=CiAKGjBpNDd2Nmp2...`
    *(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 10. Notas Adicionais
*   **Paginação:** O endpoint implementa paginação baseada em tokens (opaco) para lidar eficientemente com grandes volumes de dados. O número padrão de itens por página é 30, mas pode ser ajustado com `max_results` (até 100). Use `next_page_token` da resposta para obter a próxima página de resultados. A paginação ocorre sobre as diferentes moedas encontradas, não sobre as transações individuais que são agregadas.


*   **Filtros de Status Padrão:** Por padrão, apenas transações com status `APPROVED` e `COMPLETE` são consideradas, a menos que `transaction` ou `transaction_status` sejam especificados. Isto significa que o comportamento padrão exclui transações canceladas, reembolsadas, em análise, etc.


*   **Moedas:** O resultado é agrupado por moeda (`currency_code`), apresentando um objeto separado para cada moeda diferente encontrada nas transações correspondentes aos filtros. Isso permite analisar vendas em diferentes mercados ou regiões separadamente.


*   **Período de Dados:** Por razões de desempenho, é recomendável especificar filtros de data (`start_date` e `end_date`) para períodos não muito extensos, preferencialmente até 31 dias. Consultas para períodos muito longos podem resultar em tempos de resposta maiores.


*   **Case Sensitivity:** Parâmetros como `transaction_status`, `payment_type` e `affiliate_name` são sensíveis a maiúsculas e minúsculas (case-sensitive). Certifique-se de usar os valores exatamente como documentados.


*   **Rate Limits:** A API Hotmart implementa limites de requisição para proteger a infraestrutura. As limitações específicas para este endpoint são de 120 requisições por minuto por token de acesso. Se exceder este limite, o erro `429 Too Many Requests` será retornado e o cabeçalho `Retry-After` indicará quantos segundos esperar.


*   **Caching:** Para otimizar o desempenho, considere implementar cache client-side para requisições frequentes com os mesmos parâmetros. Resultados para períodos históricos (dados de dias/meses anteriores) raramente mudam e podem ser armazenados em cache por períodos mais longos.


*   **Fusos Horários:** Todos os timestamps (`start_date`, `end_date`) são interpretados em UTC. Certifique-se de fazer a conversão adequada do fuso horário local para UTC antes de enviar estes parâmetros.
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sales_001",
  "api_provider": "Hotmart",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Obter Sumário de Vendas", "Totalizar Comissões por Moeda", "Filtrar Vendas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Financial",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Sumário de Vendas", "Comissões", "Transações", "Pagamentos", "Produtos", "Afiliados", "Ofertas", "Moedas"],
  "context_level": ["intermediate"],
  "topic_cluster": ["vendas", "financeiro", "comissões", "relatórios", "api", "agregação"],
  "db_relations": { "tables": ["sales", "transactions", "commissions", "currencies", "products", "affiliates"], "schemas": ["payments_reporting", "sales_analytics"] },
  "related_concepts": ["transações", "pagamentos", "comissões", "moedas", "paginação", "filtros", "reporting api", "timestamp unix", "análise financeira", "conversão"],
  "question_embeddings": [
    "Como obter o sumário de vendas na API Hotmart?",
    "Qual endpoint da Hotmart retorna o total de comissões por moeda?",
    "Como filtrar vendas por tipo de pagamento na API Hotmart?",
    "Como verificar comissões por moeda na API da Hotmart?",
    "Como analisar vendas de um afiliado específico via API?",
    "Como usar a paginação no endpoint de sumário de vendas da Hotmart?",
    "Quais status de transação posso filtrar no sumário de vendas?",
    "Como obter o sumário de vendas de um produto específico em um período?",
    "Como verificar vendas feitas por PIX na API Hotmart?",
    "Como filtrar vendas por origem (source) na API Hotmart?",
    "Qual é o formato de data aceito no endpoint de sumário de vendas?",
    "Como verificar o total de reembolsos via API Hotmart?"
  ],
  "reasoning_pathways": ["filtering", "pagination", "aggregation", "time-series analysis", "financial reporting", "performance analysis"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```


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
*(Ref: Hotmart Sales Summary, ID hotmart_salessummary_001)*