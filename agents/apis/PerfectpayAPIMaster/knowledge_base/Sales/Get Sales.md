# API PerfectPay - Vendas - Consultar Vendas (Get Sales)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API PerfectPay - Vendas - Consultar Vendas (Get Sales)`          |
| **Identificador Interno** | `perfectpay_sales_001`                                          |
| **Título Curto (Ref.)**   | `PerfectPay Get Sales`                                          |
| **Versão do Documento**   | `1.0.0`                                                         |
| **Data de Criação**       | `2025-04-27`                                                    |
| **Última Atualização**    | `2025-04-27`                                                    |
| **Autor/Responsável**     | `Equipe de Documentação / IA`                                   |
| **Fonte Original**        | `https://support.perfectpay.com.br/doc/perfect-pay/perfectpay-api/vendas` |
| **URL de Referência**     | `https://app.perfectpay.com.br/api/v1/sales/get`                |
| **Status do Documento**   | `Em Uso`                                                        |
| **Ambiente de Referência**| `Produção`                                                      |
| **Idioma Original**       | `Português (BR)`                                                |
| **Formato de Datas (API)**| `Entrada: YYYY-MM-DD, Saída: YYYY-MM-DD HH:MM:SS`              |


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 2. Contexto
> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint `Get Sales` da API PerfectPay.


O endpoint `Get Sales` (`perfectpay_sales_001`) é utilizado para consultar vendas na plataforma PerfectPay. Ele permite recuperar informações detalhadas de transações comerciais, oferecendo diversos filtros como datas de venda, datas de aprovação, status e identificadores específicos (ex: `transaction_token`). Este endpoint é fundamental para integração de sistemas de gestão (ERP, CRM), geração de relatórios financeiros e operacionais, e análise de desempenho de vendas.


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 3. Visão Geral da API/Endpoint(s)
> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint `Get Sales`.


Este documento cobre o endpoint `POST /api/v1/sales/get`. Ele permite obter uma lista paginada de vendas com dados completos, incluindo informações de produtos, planos, clientes, comissões, notas fiscais e metadados de marketing. A API suporta filtros por período (venda/aprovação), múltiplos status de venda e identificadores únicos de transação, além de oferecer paginação para lidar com grandes volumes de dados.


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 4. Detalhes Técnicos
> **Resumo:** Especificações técnicas detalhadas do endpoint, incluindo URL, método HTTP e requisitos de autenticação.


### `Endpoint: /api/v1/sales/get`


*   **Endpoint URL:** `https://app.perfectpay.com.br/api/v1/sales/get`
*   **Método HTTP:** `POST`
*   **Autenticação:** `Bearer Token`. Requer um token de acesso válido no cabeçalho `Authorization`. Ex: `Authorization: Bearer {SEU_TOKEN}`.


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 5. Parâmetros de Entrada
> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados no corpo (body) da requisição POST.


### `Endpoint: /api/v1/sales/get` (`Body Parameters`)


| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo / Valores Possíveis |
| :----------------- | :-------- | :--- | :----------- | :---------------------------------- |
| `start_date_sale`  | Data inicial da venda (inclusiva) | string | Não | Formato: `YYYY-MM-DD`. Ex: `"2023-01-01"` |
| `end_date_sale`    | Data final da venda (inclusiva) | string | Não | Formato: `YYYY-MM-DD`. Ex: `"2023-01-31"` |
| `start_date_approved` | Data inicial de aprovação da venda (inclusiva) | string | Não | Formato: `YYYY-MM-DD`. |
| `end_date_approved`| Data final de aprovação da venda (inclusiva) | string | Não | Formato: `YYYY-MM-DD`. |
| `sale_status`      | Filtra por um ou mais status da venda. | array (de inteiros) | Não | Veja a lista de valores possíveis abaixo. Ex: `[1, 2]` |
| `transaction_token`| Identificador único da venda (transação). | string | Não | Ex: `"CPTFB5RR2MNGGF"` |
| `page`             | Número da página para paginação dos resultados. | integer | Não | Padrão: `1`. Ex: `1` |


**Valores Possíveis para `sale_status`:**
*   `1`: Pendente
*   `2`: Aprovado
*   `3`: Processando
*   `4`: Mediação
*   `5`: Rejeitado
*   `6`: Cancelado
*   `7`: Devolvido
*   `8`: Autorizado
*   `9`: Cobrado de volta (Chargeback)
*   `10`: Completo
*   `11`: Erro de Checkout
*   `12`: Pré-checkout
*   `13`: Expirado
*   `16`: Revisão


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint na resposta bem-sucedida (200 OK).


### `Endpoint: /api/v1/sales/get`


#### 6.1.1 Estrutura Geral da Resposta


A resposta é um objeto JSON contendo a chave `sales`.


| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `sales`       | Objeto principal contendo os dados das vendas e informações de paginação. | object |


#### 6.1.2 Detalhes do Objeto `sales`


| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `sales.data`        | Array contendo os objetos de cada venda encontrada. | array | Se nenhuma venda for encontrada, será um array vazio `[]`. |
| `sales.current_page` | Número da página atual retornada. | integer | |
| `sales.current_items_count` | Quantidade de itens (vendas) na página atual. | integer | |
| `sales.total_pages` | Número total de páginas disponíveis para a consulta. | integer | |
| `sales.total_items` | Número total de itens (vendas) encontrados que correspondem aos filtros aplicados. | integer | |


#### 6.1.3 Detalhes de cada Objeto de Venda dentro de `sales.data`


| Campo               | Descrição | Tipo | Notas / Valores Possíveis |
| :------------------ | :-------- | :--- | :------------------------ |
| `product_code`      | Código do Produto. | string | Ex: `"PPBP2A04"` |
| `product_name`      | Nome do Produto. | string | Ex: `"Herus Caps"` |
| `transaction_token` | Identificador único da venda. | string | Ex: `"CPTFB5RR2MNGGF"` |
| `value`             | Valor total da Venda (incluindo frete, se aplicável). | decimal (string) | Ex: `"385.00"` |
| `unit_value`        | Valor unitário do Produto. | decimal (string) | Ex: `"77.00"` |
| `shipping_amount`   | Valor do frete. | decimal (string) | Ex: `"0.00"` |
| `plan`              | Array com informações do Plano associado (se houver). | array (de objetos) | Veja detalhes abaixo. |
| `customer`          | Array com informações do Cliente. | array (de objetos) | Veja detalhes abaixo. |
| `commissions`       | Array com informações de Comissão (se houver). | array (de objetos) | Veja detalhes abaixo. |
| `metadata`          | Objeto com metadados de marketing (UTMs, etc.). | object | Veja detalhes abaixo. |
| `total_invoices`    | Número total de notas fiscais associadas à venda. | integer | Ex: `2` |
| `invoices`          | Array com informações das Notas Fiscais (se houver). | array (de objetos) | Veja detalhes abaixo. |
| `sale_status`       | Status atual da venda. | string | Ex: `"approved"`, `"pending"`, `"refunded"`, etc. |
| `payment_type`      | Tipo de pagamento utilizado. | integer | `1`: Cartão de crédito, `2`: Boleto, `3`: PayPal, `5`: Gratuito, `6`: Cartão (Upsell), `7`: Pix |
| `date_created`      | Data e hora da criação da venda. | string | Formato: `YYYY-MM-DD HH:MM:SS`. Ex: `"2019-02-19 13:31:28"` |
| `date_approved`     | Data e hora da aprovação da venda (se aplicável). | string | Formato: `YYYY-MM-DD HH:MM:SS`. Ex: `"2019-02-19 13:32:09"` |


#### 6.1.4 Detalhes do Objeto `plan` (dentro de `sales.data`)


| Campo Aninhado | Descrição | Tipo |
| :------------- | :-------- | :--- |
| `plan_name`    | Nome do Plano. | string |
| `plan_code`    | Código do Plano. | string |
| `quantity`     | Quantidade de produtos no plano. | integer |


#### 6.1.5 Detalhes do Objeto `customer` (dentro de `sales.data`)


| Campo Aninhado           | Descrição | Tipo | Notas / Valores Possíveis |
| :----------------------- | :-------- | :--- | :------------------------ |
| `full_name`              | Nome completo do cliente. | string | |
| `email`                  | Email do cliente. | string | |
| `identification_type`    | Tipo de identificação. | string | `CPF`, `CNPJ`, `ESTRANGEIRO` (Mapeado de: `1`, `2`, `3`) |
| `identification_number`  | Número do documento. | string | |
| `phone`                  | Número de telefone. | string | |
| `zip_code`               | CEP. | string | |
| `street_name`            | Nome da rua. | string | |
| `street_number`          | Número do endereço. | integer / null | |
| `complement`             | Complemento do endereço. | string / null | |
| `district`               | Bairro. | string | |
| `city`                   | Cidade. | string | |
| `state`                  | Estado (UF). | string | |
| `country`                | País (Código ISO). | string | Ex: `"BR"` |


#### 6.1.6 Detalhes do Objeto `commissions` (dentro de `sales.data`)


| Campo Aninhado     | Descrição | Tipo | Notas / Valores Possíveis |
| :----------------- | :-------- | :--- | :------------------------ |
| `affiliation_name` | Nome do afiliado/produtor/parceiro. | string | |
| `affiliation_type` | Tipo de afiliado. | integer | `1`: Produtor, `2`: Co-Produtor, `3`: Gerente de Afiliados, `4`: Parceiro, `5`: Afiliado |
| `value`            | Valor da comissão. | decimal | |
| `commission`       | Percentual ou valor fixo da comissão. | decimal | |
| `commission_type`  | Tipo de comissão. | integer | `1`: Valor Fixo (R$), `2`: Percentual (%) |


#### 6.1.7 Detalhes do Objeto `metadata` (dentro de `sales.data`)


| Campo Aninhado  | Descrição | Tipo |
| :-------------- | :-------- | :--- |
| `src`           | Origem (SRC). | string / null |
| `utm_source`    | UTM Source. | string / null |
| `utm_medium`    | UTM Medium. | string / null |
| `utm_campaign`  | UTM Campaign. | string / null |
| `utm_term`      | UTM Term. | string / null |
| `utm_content`   | UTM Content. | string / null |
| `utm_perfect`   | UTM Perfect (parâmetro específico PerfectPay). | string / null |


#### 6.1.8 Detalhes do Objeto `invoices` (dentro de `sales.data`)


| Campo Aninhado           | Descrição | Tipo |
| :----------------------- | :-------- | :--- |
| `external_id`            | Código externo da NF. | string / null |
| `logistic_id`            | Código da logística associado à NF. | string / null |
| `fiscal_number`          | Número da nota fiscal. | integer / null |
| `fiscal_access_key`      | Chave de acesso da NF-e. | string / null |
| `fiscal_pdf`             | URL do PDF da nota fiscal. | string / null |
| `fiscal_xml`             | URL do XML da nota fiscal. | string / null |
| `fiscal_status`          | Status da nota fiscal (conforme sistema de logística/emissão). | string / null |
| `fiscal_date_emission`   | Data de emissão da nota fiscal. | string / null | Formato: `YYYY-MM-DD HH:MM:SS` |


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 7. Exemplos de Requisição e Resposta
> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint `Get Sales`.


### `Endpoint: /api/v1/sales/get`


#### 7.1.1 Exemplo de Requisição (cURL)


```bash
curl --location --request POST 'https://app.perfectpay.com.br/api/v1/sales/get' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {SEU_TOKEN}' \
--data-raw '{
  "start_date_sale": "2023-01-01",
  "end_date_sale": "2023-01-31",
  "sale_status": [2],
  "page": 1
}'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 200 OK)


```json
{
  "sales": {
    "data": [
      {
        "product_code": "PPBP2A04",
        "product_name": "Herus Caps",
        "transaction_token": "CPTFB5RR2MNGGF",
        "value": "385.00",
        "unit_value": "77.00",
        "shipping_amount": "0.00",
        "plan": [
          {
            "plan_name": "Herus Caps | 5 Potes",
            "plan_code": "UUTGG9Q9R",
            "quantity": 5
          }
        ],
        "customer": [
          {
            "full_name": "Example Name",
            "email": "examplename5@gmail.com",
            "identification_type": "CPF",
            "identification_number": "54645896548",
            "phone": "(55) 94548-4767",
            "zip_code": "34578-888",
            "street_name": "Rua Example",
            "street_number": null,
            "complement": null,
            "district": "Centro",
            "city": "Example City",
            "state": "RS",
            "country": "BR"
          }
        ],
        "commissions": [
          {
            "affiliation_name": "Affiliate Example",
            "affiliation_type": 5,
            "value": 144.51,
            "commission": 40.00,
            "commission_type": 1
          },
          {
            "affiliation_name": "Affiliate Example2",
            "affiliation_type": 1,
            "value": 216.77,
            "commission": 100.00,
            "commission_type": 1
          }
        ],
        "metadata": {
          "src": null,
          "utm_source": "teste",
          "utm_medium": "medio",
          "utm_campaign": "campaign",
          "utm_term": null,
          "utm_content": null,
          "utm_perfect": null
        },
        "total_invoices": 2,
        "invoices": [
          {
            "external_id": null,
            "logistic_id": null,
            "fiscal_number": 123,
            "fiscal_access_key": "456",
            "fiscal_pdf": "http://pdf",
            "fiscal_xml": "http://xml",
            "fiscal_status": "Autorizada",
            "fiscal_date_emission": "2019-05-02 00:00:00"
          },
          {
            "external_id": null,
            "logistic_id": null,
            "fiscal_number": 123,
            "fiscal_access_key": "456",
            "fiscal_pdf": "http://pdf",
            "fiscal_xml": "http://xml",
            "fiscal_status": "Autorizada",
            "fiscal_date_emission": "2019-05-02 00:00:00"
          }
        ],
        "sale_status": "approved",
        "payment_type": 1,
        "date_created": "2019-02-19 13:31:28",
        "date_approved": "2019-02-19 13:32:09"
      }
    ],
    "current_page": 1,
    "current_items_count": 1,
    "total_pages": 1,
    "total_items": 1
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro 401 Unauthorized)


```json
{
  "error": {
    "code": "unauthorized",
    "message": "Token de autenticação inválido ou ausente."
  }
}
```


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 8. Códigos de Status e Tratamento de Erros
> **Resumo:** Descrição dos códigos de status HTTP comuns retornados pelo endpoint e como interpretar erros.


| Status Code               | Descrição Geral                                              | Ação Recomendada |
| :------------------------ | :----------------------------------------------------------- | :--------------- |
| `200 OK`                  | Sucesso. A requisição foi processada e os dados solicitados (ou um array vazio se nada for encontrado) estão no corpo da resposta. | Processar os dados em `sales.data`. |
| `400 Bad Request`         | Erro na requisição devido a parâmetros inválidos, formato incorreto (ex: data inválida) ou falta de campos obrigatórios (se houver). | Verificar os parâmetros enviados na requisição e corrigir. Consultar a mensagem de erro para detalhes. |
| `401 Unauthorized`        | Falha na autenticação. O token Bearer está ausente, inválido ou expirado. | Verificar se o cabeçalho `Authorization` está correto e se o token é válido e não expirado. Obter um novo token se necessário. |
| `403 Forbidden`           | Acesso negado. O token de autenticação é válido, mas não possui permissão para acessar este recurso ou os dados solicitados. | Verificar as permissões associadas ao token/usuário. Contatar o suporte PerfectPay se acreditar que deveria ter acesso. |
| `404 Not Found`           | Endpoint não encontrado. (Menos provável para este endpoint específico, mas possível se a URL base mudar). | Verificar a URL do endpoint. |
| `429 Too Many Requests`   | Limite de taxa de requisições (Rate Limit) excedido. | Reduzir a frequência das requisições. Implementar backoff exponencial antes de tentar novamente. Verificar os cabeçalhos de Rate Limit na resposta (se disponíveis). |
| `500 Internal Server Error`| Ocorreu um erro inesperado no servidor da PerfectPay. | Tentar novamente após alguns instantes. Se o erro persistir, contatar o suporte da PerfectPay com detalhes da requisição (incluindo `request_id`, se disponível). |
| `503 Service Unavailable` | O serviço está temporariamente indisponível (manutenção, sobrecarga). | Tentar novamente mais tarde. |


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)
> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint `Get Sales`.


1.  **Obter vendas de um período específico**
    *   Objetivo: Recuperar todas as vendas realizadas em janeiro de 2023.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "start_date_sale": "2023-01-01", "end_date_sale": "2023-01-31" }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


2.  **Consultar vendas aprovadas**
    *   Objetivo: Listar apenas vendas com status "Aprovado".
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [2] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


3.  **Buscar uma venda específica pelo token**
    *   Objetivo: Localizar detalhes de uma transação específica.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "transaction_token": "CPTFB5RR2MNGGF" }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


4.  **Verificar vendas pendentes**
    *   Objetivo: Identificar todas as vendas com status "Pendente".
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [1] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


5.  **Consultar vendas aprovadas em um período específico**
    *   Objetivo: Obter vendas aprovadas em fevereiro de 2023.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "start_date_approved": "2023-02-01", "end_date_approved": "2023-02-28", "sale_status": [2] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


6.  **Acessar a segunda página de resultados de vendas aprovadas**
    *   Objetivo: Navegar para a próxima página em resultados paginados de vendas aprovadas.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [2], "page": 2 }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


7.  **Verificar vendas canceladas**
    *   Objetivo: Listar apenas vendas com status "Cancelado".
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [6] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


8.  **Consultar vendas rejeitadas**
    *   Objetivo: Identificar todas as vendas com status "Rejeitado".
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [5] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


9.  **Consultar vendas aprovadas e completas simultaneamente**
    *   Objetivo: Obter vendas com status "Aprovado" ou "Completo" em uma única consulta.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [2, 10] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


10. **Verificar vendas com status de mediação**
    *   Objetivo: Listar vendas que estão em processo de mediação.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [4] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


11. **Consultar vendas realizadas hoje**
    *   Objetivo: Obter vendas criadas no dia atual.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "start_date_sale": "YYYY-MM-DD", "end_date_sale": "YYYY-MM-DD" }` (Substituir YYYY-MM-DD pela data atual).
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


12. **Verificar vendas com chargeback**
    *   Objetivo: Identificar vendas que sofreram chargeback ("Cobrado de volta").
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [9] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


13. **Consultar vendas devolvidas (reembolsadas)**
    *   Objetivo: Listar vendas que foram reembolsadas ao cliente.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [7] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


14. **Obter vendas com erros de checkout**
    *   Objetivo: Identificar transações que falharam durante o checkout.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [11] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


15. **Verificar vendas expiradas**
    *   Objetivo: Listar vendas que expiraram sem conclusão (ex: boleto não pago).
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [13] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


16. **Consultar vendas em revisão**
    *   Objetivo: Identificar transações que estão em processo de revisão manual ou automática.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [16] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


17. **Verificar vendas autorizadas (pré-aprovação)**
    *   Objetivo: Listar vendas que foram autorizadas pelo gateway, mas aguardam confirmação/captura.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [8] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


18. **Consultar vendas em processamento**
    *   Objetivo: Identificar transações que estão sendo processadas (status intermediário).
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [3] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


19. **Obter vendas completas (status final positivo)**
    *   Objetivo: Listar vendas que atingiram o status final "Completo".
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [10] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


20. **Consultar vendas em pré-checkout (carrinho abandonado, etc.)**
    *   Objetivo: Identificar interações que chegaram à fase de pré-checkout mas não foram concluídas.
    *   Como Fazer: `POST /api/v1/sales/get` com body: `{ "sale_status": [12] }`
    *(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 10. Notas Adicionais
> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint.


*   **Formato de Datas:** Datas nos parâmetros de entrada (`start_date_sale`, `end_date_sale`, etc.) devem usar o formato `YYYY-MM-DD`. Datas nos parâmetros de saída (`date_created`, `date_approved`, etc.) são retornadas no formato `YYYY-MM-DD HH:MM:SS`.


*   **Paginação:** Os resultados são sempre paginados. Utilize o parâmetro `page` para navegar entre as páginas. A resposta inclui `current_page`, `total_pages`, `current_items_count`, e `total_items` para auxiliar na gestão da paginação. Não há informação sobre o limite de itens por página na documentação original.


*   **Status da Venda:** O parâmetro `sale_status` aceita um array de inteiros, permitindo filtrar por múltiplos status simultaneamente. A resposta retorna o status como uma string descritiva (ex: `"approved"`).


*   **Rate Limits:** A documentação original não especifica limites de taxa de requisição (Rate Limits). É recomendado monitorar os cabeçalhos de resposta (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`) ou consultar a documentação geral da PerfectPay API para obter essa informação. Implemente tratamento para o código `429 Too Many Requests`.


*   **Obrigatoriedade de Parâmetros:** Embora a tabela marque todos os parâmetros como "Não Obrigatório", enviar uma requisição sem filtros pode retornar um volume muito grande de dados. É recomendado usar filtros de data (`start_date_sale`/`end_date_sale` ou `start_date_approved`/`end_date_approved`) para limitar o escopo da consulta.


*   **Consistência de Dados:** Certifique-se de que os dados de `customer`, `commissions`, `invoices`, etc., sejam interpretados corretamente, pois são retornados como arrays de objetos (mesmo que contenham apenas um elemento, como no exemplo).


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)
> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.


```json
{
  "doc_id": "perfectpay_sales_001",
  "api_provider": "PerfectPay",
  "api_product_area": "Vendas",
  "endpoint_focus": [
    "Consultar Vendas",
    "Filtrar Vendas por Data",
    "Filtrar Vendas por Status",
    "Buscar Venda por Token",
    "Listar Transações Pagas",
    "Obter Dados de Clientes de Vendas",
    "Obter Dados de Comissões",
    "Paginação de Vendas"
  ],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Financial",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": [
    "Venda",
    "Transação",
    "Cliente",
    "Produto",
    "Plano",
    "Comissão",
    "Nota Fiscal",
    "Pagamento"
  ],
  "context_level": [
    "intermediate"
  ],
  "topic_cluster": [
    "e-commerce",
    "plataforma de pagamentos",
    "gestão de vendas",
    "relatórios financeiros",
    "api de pagamentos",
    "afiliados"
  ],
  "db_relations": {
    "tables": [
      "sales",
      "transactions",
      "customers",
      "products",
      "plans",
      "commissions",
      "invoices",
      "payments"
    ],
    "schemas": []
  },
  "related_concepts": [
    "status de pagamento",
    "token de transação",
    "filtro de data",
    "paginaçao API",
    "comissionamento de afiliados",
    "dados do cliente",
    "nota fiscal eletrônica",
    "webhook de vendas"
  ],
  "question_embeddings": [
    "Como consultar vendas na API da PerfectPay?",
    "Qual endpoint usar para buscar vendas por período na PerfectPay?",
    "Como filtrar vendas por status (aprovado, pendente, cancelado) na PerfectPay?",
    "É possível buscar uma venda específica pelo transaction_token na API PerfectPay?",
    "Como obter os dados do cliente associado a uma venda na PerfectPay?",
    "Como listar as comissões de uma venda via API PerfectPay?",
    "Como funciona a paginação no endpoint de consulta de vendas da PerfectPay?",
    "Quais são os possíveis status de venda retornados pela API PerfectPay?",
    "Como obter vendas aprovadas entre duas datas específicas na PerfectPay?"
  ],
  "reasoning_pathways": [
    "query-filter",
    "data-retrieval",
    "status-lookup",
    "pagination-handling",
    "entity-relationship-extraction"
  ],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": [
    "Bearer Token"
  ],
  "typical_integration_points": [
    "Sistema ERP",
    "Sistema CRM",
    "Plataforma de BI",
    "Dashboard Financeiro",
    "Sistema de Gestão de Afiliados"
  ],
  "common_error_patterns": [
    "Invalid date format",
    "Invalid sale status code",
    "Missing or invalid authentication token",
    "Rate limit exceeded"
  ]
}
```


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 12. Checklist de Implementação (Opcional)
> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação da integração com o endpoint `Get Sales`.


- [ ] **Autenticação**
  - [ ] Implementar obtenção segura e armazenamento do Bearer Token
  - [ ] Incluir o token no cabeçalho `Authorization` de cada requisição
  - [ ] Implementar lógica de renovação de token (se aplicável)


- [ ] **Construção da Requisição**
  - [ ] Montar o corpo JSON da requisição `POST` com os filtros desejados
  - [ ] Validar formato das datas (`YYYY-MM-DD`) antes de enviar
  - [ ] Usar os códigos numéricos corretos para `sale_status`


- [ ] **Tratamento de Resposta**
  - [ ] Processar a resposta JSON bem-sucedida (`200 OK`)
  - [ ] Extrair dados do array `sales.data`
  - [ ] Mapear campos da resposta para modelos internos da aplicação
  - [ ] Lidar corretamente com campos que podem ser `null`


- [ ] **Paginação**
  - [ ] Implementar lógica para iterar pelas páginas usando o parâmetro `page`
  - [ ] Utilizar `total_pages` e `total_items` para controlar o loop de paginação
  - [ ] Considerar o limite de itens por página para otimizar chamadas


- [ ] **Tratamento de Erros**
  - [ ] Implementar handlers para códigos de erro `400`, `401`, `403`, `429`, `500`, `503`
  - [ ] Implementar lógica de retentativas com backoff exponencial para erros `429` e `5xx`
  - [ ] Registrar erros detalhadamente para depuração


- [ ] **Validação e Robustez**
  - [ ] Validar os dados recebidos (tipos, formatos esperados)
  - [ ] Lidar com respostas vazias (`sales.data` como `[]`) sem gerar erros


- [ ] **Monitoramento e Logs**
  - [ ] Registrar tempo de resposta de cada chamada
  - [ ] Monitorar taxa de erros (`4xx`, `5xx`)
  - [ ] Implementar rastreamento de requisições (request_id)


- [ ] **Otimização (Opcional)**
  - [ ] Implementar cache para consultas frequentes (se aplicável)
  - [ ] Definir estratégias de invalidação de cache


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 13. Glossário de Termos Técnicos
> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados nesta documentação específica.


| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Venda (Sale)`            | Representa uma transação comercial registrada na plataforma PerfectPay. |
| `Token de Transação`      | Identificador único alfanumérico (`transaction_token`) para cada venda/transação. |
| `Status da Venda`         | Estado atual do ciclo de vida da venda (Pendente, Aprovado, Cancelado, etc.). |
| `Paginação`               | Técnica para dividir grandes conjuntos de resultados (vendas) em páginas menores e gerenciáveis. |
| `Bearer Token`            | Credencial de segurança temporária usada no cabeçalho `Authorization` para autenticar requisições à API. |
| `Endpoint`                | URL específica (`/api/v1/sales/get`) que aceita requisições para realizar uma operação (consultar vendas). |
| `Rate Limit`              | Número máximo de requisições permitidas à API em um determinado período de tempo. |
| `Webhook`                 | Mecanismo (não descrito neste endpoint) onde a API notificaria um sistema externo sobre eventos (ex: nova venda). |
| `Parâmetro de Entrada`    | Dado enviado na requisição (neste caso, no corpo JSON) para filtrar ou controlar a operação da API. |
| `Parâmetro de Saída`      | Dado retornado na resposta da API contendo as informações solicitadas. |
| `JSON`                    | (JavaScript Object Notation) Formato padrão de troca de dados usado por esta API. |
| `cURL`                    | Ferramenta de linha de comando usada para fazer requisições HTTP (usada nos exemplos). |
| `Decimal (string)`        | Tipo de dado usado para valores monetários, retornado como string para evitar problemas de precisão. |


*(Ref: PerfectPay Get Sales, ID perfectpay_getsales_001)*
---


## 14. Observações Finais sobre Formatação
> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.


*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados (parâmetros, códigos de status, glossário).
*   Use blocos de código (``` ```) com indicação de linguagem (`bash`, `json`) para exemplos.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa.
*   Formate nomes de parâmetros, campos e valores de exemplo com backticks (`` `exemplo` ``).
*   **Crucial:** Inclua `(Ref: [TITULO_CURTO], ID [ID_INTERNO])` no final de **CADA SEÇÃO PRINCIPAL (##)**.
*   Mantenha os resumos de seção (`> **Resumo:** ...`) concisos (1-2 linhas) e informativos.
*   Use listas e bullets para informações sequenciais ou enumeradas (como nos Casos de Uso e Checklist).


**(FIM DO TEMPLATE PADRÃO)**