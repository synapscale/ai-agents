# API Kiwify - Produtos - Consultar Produto (Get Product)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Produtos - Consultar Produto (Get Product)` |
| **Identificador Interno** | `kiwify_prod_001`                   |
| **Título Curto (Ref.)**   | `Kiwify Get Product`           |
| **Versão do Documento**   | `1.0.2`                                |
| **Data de Criação**       | `2025-04-10`                                                  |
| **Última Atualização**    | `2025-04-11`                                                  |
| **Autor/Responsável**     | `Equipe de Documentação Técnica`                                    |
| **Fonte Original**        | `https://docs.kiwify.com.br/api-reference/products/single`  |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/products/single` |
| **Status do Documento**   | `Em Uso`                              |
| **Ambiente de Referência**| `Produção, Sandbox`                                |
| **Idioma Original**       | `Português (BR)`                                  |
| **Formato de Datas (API)**| `ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)` |




*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 2. Contexto


> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint de consulta de produtos da Kiwify.


O endpoint de Consultar Produto permite que aplicações integradas com a API da Kiwify acessem informações detalhadas de um produto específico utilizando seu identificador único (`id`). Este endpoint é essencial para plataformas que precisam obter dados completos sobre produtos, incluindo preços, status, configurações de eventos, assinaturas e parceiros de receita. As informações recuperadas são fundamentais para apresentação de catálogos, integrações de e-commerce e gestão de produtos em sistemas externos. O ID interno deste documento é `kiwify_prod_001`.


Este endpoint é particularmente útil para sincronização de dados entre a Kiwify e sistemas externos, seja para exibição em landing pages, integração com sistemas ERP, ou para alimentar dashboards administrativos. Ele fornece uma visão completa e atualizada de um produto específico, permitindo que sistemas integrados sejam mantidos sincronizados com informações precisas da plataforma Kiwify.


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 3. Visão Geral da API/Endpoint(s)


> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint coberto neste documento.


O endpoint `GET /v1/products/{id}` oferece acesso de leitura completo às informações de um produto específico na plataforma Kiwify. Através dele, é possível recuperar todos os atributos de um produto, incluindo seus links de acesso, informações de preço, configurações de eventos, lotes, assinaturas, bumps (ofertas especiais) e parceiros de receita. Este endpoint é parte do grupo de APIs de Produtos da Kiwify, que permite a gestão e consulta do catálogo de produtos de uma conta.


O endpoint retorna dados detalhados em formato JSON, permitindo que os integradores acessem todas as propriedades configuradas para o produto, independentemente do seu tipo (digital, físico, evento). A resposta inclui não apenas atributos básicos como nome e preço, mas também estruturas complexas como configurações específicas de eventos, detalhes de lotes de ingressos, e informações de parceiros de receita.


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 4. Detalhes Técnicos


> **Resumo:** Especificações técnicas detalhadas do endpoint, incluindo URL, método HTTP e requisitos de autenticação.


### `Endpoint: /products/{id}`


*   **Endpoint URL:** `https://public-api.kiwify.com/v1/products/{id}`
*   **Método HTTP:** `GET`
*   **Autenticação:** OAuth 2.0 - Bearer Token + API Key
    *   Cabeçalho `Authorization`: `Bearer {SEU_TOKEN_OAUTH}`
    *   Cabeçalho `x-kiwify-account-id`: `{SEU_ACCOUNT_ID}`
*   **Content-Type:** `application/json` (para resposta)
*   **Versão da API:** `v1`
*   **Protocolo:** `HTTPS` (obrigatório, requisições HTTP não são aceitas)


O token de acesso OAuth 2.0 deve ser obtido previamente através do fluxo de autenticação da Kiwify. O cabeçalho `x-kiwify-account-id` identifica a conta Kiwify específica para a qual a requisição é realizada, permitindo o acesso apenas aos produtos vinculados a essa conta.


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 5. Parâmetros de Entrada


> **Resumo:** Detalhamento de todos os parâmetros que devem ser enviados nas requisições ao endpoint de consulta de produtos.


### `Endpoint: /products/{id}`


#### 5.1 Parâmetros de Caminho (Path Parameters)


| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `id`               | Identificador único do produto a ser consultado | string (UUID) | Sim | Ex: `20072760-3699-11ee-b627-87e13b212de8` |


#### 5.2 Cabeçalhos (Headers)


| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `Authorization`    | Token de acesso OAuth 2.0 prefixado com "Bearer " | string | Sim | Ex: `Bearer eyJhbGciOiJIUzI1NiIsInR5...` |
| `x-kiwify-account-id` | Identificador único da conta Kiwify | string | Sim | Ex: `XvS0qfkdzCZTg8z` |
| `Accept`           | Tipo de conteúdo aceito na resposta | string | Não | Default: `application/json` |
| `Content-Type`     | Tipo de conteúdo da requisição | string | Não | Default: `application/json` |


#### 5.3 Parâmetros de Consulta (Query Parameters)


Este endpoint não aceita parâmetros de consulta específicos para filtrar os resultados, pois retorna um único recurso identificado pelo ID.


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)


> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint de consulta de produtos em respostas bem-sucedidas (200 OK).


### `Endpoint: /products/{id}`


#### 6.1 Estrutura Geral da Resposta


| Campo             | Descrição | Tipo   | Notas |
| :---------------- | :-------- | :----- | :---- |
| `id`              | Identificador único do produto | string (UUID) | Ex: `20072760-3699-11ee-b627-87e13b212de8` |
| `store_id`        | Identificador da loja associada ao produto | string | Ex: `XvS0qfkdzCZTg8z` |
| `name`            | Nome do produto | string | Ex: `Curso de Marketing Digital` |
| `type`            | Tipo do produto | string | Valores possíveis: `membership`, `physical`, `event` |
| `created_at`      | Data e hora de criação do produto | string (ISO 8601) | Ex: `2023-08-09T09:42:59.074Z` |
| `price`           | Preço base do produto em centavos | number | Ex: `500` (equivale a R$ 5,00) |
| `affiliate_enabled` | Indica se o programa de afiliados está habilitado | boolean | `true` ou `false` |
| `status`          | Status atual do produto | string | Valores possíveis: `active`, `inactive`, `draft` |
| `payment_type`    | Tipo de cobrança principal | string | Valores possíveis: `charge` (cobrança única), `subscription` |
| `shipping_options`| Lista de opções de frete (para produtos físicos) | array de objetos | Ver Seção 6.2 |
| `links`           | Lista de links associados ao produto (checkout, etc.) | array de objetos | Ver Seção 6.3 |
| `bumps`           | Lista de ofertas especiais (bumps) | array de objetos | Ver Seção 6.4 |
| `offers`          | Lista de ofertas associadas ao produto | array de objetos | Ver Seção 6.5 |
| `event_settings`  | Configurações específicas para produtos do tipo `event` | objeto ou null | Ver Seção 6.6 |
| `event_batches`   | Lista de lotes de ingressos para produtos do tipo `event` | array de objetos | Ver Seção 6.7 |
| `subscriptions`   | Lista de planos de assinatura associados | array de objetos | Ver Seção 6.8 |
| `revenue_partners`| Lista de parceiros de receita associados | array de objetos | Ver Seção 6.9 |


#### 6.2 Detalhes do Objeto `shipping_options`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | Identificador único da opção de frete | string (UUID) | Ex: `928b5935-a3d9-4f21-879d-f46c1b30d9f0` |
| `name`            | Nome da opção de frete | string | Ex: `Frete Gratis`, `PAC`, `SEDEX` |
| `price`           | Preço do frete em centavos | number | Ex: `0` para frete grátis, `1500` para R$ 15,00 |


#### 6.3 Detalhes do Objeto `links`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | Identificador único do link | string | Formato curto, ex: `KMgND1r` |
| `custom_name`     | Nome personalizado do link (se definido) | string ou null | Ex: `link-principal`, `checkout-promocional` |
| `status`          | Status do link | string | Valores possíveis: `active`, `inactive` |
| `is_sales_page`   | Indica se este link é a página de vendas principal | boolean | `true` ou `false` |


#### 6.4 Detalhes do Objeto `bumps`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | Identificador único do bump | string (UUID) | Ex: `9811cdd9-45e9-456d-8c3b-114a7cf6fa33` |
| `color`           | Cor associada ao bump (hexadecimal) | string | Ex: `#f7f7f7`, `#ff0000` |
| `link`            | Objeto contendo detalhes do link do produto ofertado no bump | objeto | Estrutura idêntica à Seção 6.3 |
| `properties`      | Propriedades adicionais do bump (se houver) | objeto ou null | Contém campos como `action_call`, `oto_description`, `oto_headline`, `show_product_image`, etc. |


#### 6.5 Detalhes do Objeto `offers`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | Identificador único da oferta | string (UUID) | |
| `name`            | Nome da oferta | string | Ex: `Pacote Premium`, `Oferta Especial` |
| `price`           | Preço da oferta em centavos | number | Ex: `9900` para R$ 99,00 |
| `active`          | Indica se a oferta está ativa | boolean | `true` ou `false` |


#### 6.6 Detalhes do Objeto `event_settings`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `address`         | Endereço do evento | objeto | Contém informações de localização |
| `  route`         | Rua/Logradouro do evento | string | Ex: `Av. Paulista, 1000` |
| `  administrative_area_level_2` | Cidade do evento | string | Ex: `São Paulo` |
| `  administrative_area_level_1` | Estado do evento | string | Ex: `SP` |
| `  country`       | País do evento | string | Ex: `Brasil` |
| `  postal_code`   | CEP do local do evento | string | Ex: `01310-100` |
| `  latitude`      | Latitude da localização | number | Ex: `-23.5505` |
| `  longitude`     | Longitude da localização | number | Ex: `-46.6333` |
| `enable_handtags` | Habilita etiquetas de mão | boolean | `true` ou `false` |
| `handtag_code_type` | Tipo de código da etiqueta | string | Ex: `qrcode`, `barcode` |
| `handtag_auto_print` | Impressão automática de etiqueta | boolean | `true` ou `false` |
| `description_enabled` | Exibição de descrição habilitada | boolean | `true` ou `false` |
| `collect_phone`   | Requer coleta de telefone na inscrição | boolean | `true` ou `false` |
| `collect_cpf`     | Requer coleta de CPF na inscrição | boolean | `true` ou `false` |
| `start_date`      | Data e hora de início do evento | string (ISO 8601) | Ex: `2023-12-15T09:00:00Z` |
| `end_date`        | Data e hora de término do evento | string (ISO 8601) | Ex: `2023-12-15T18:00:00Z` |
| `sale_start_at`   | Data e hora de início das vendas | string (ISO 8601) | Ex: `2023-11-01T00:00:00Z` |
| `sale_end_at`     | Data e hora de término das vendas | string (ISO 8601) | Ex: `2023-12-14T23:59:59Z` |


#### 6.7 Detalhes do Objeto `event_batches`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | Identificador único do lote | string (UUID) | |
| `name`            | Nome do lote | string | Ex: `Lote 1`, `Pré-venda`, `Lote Promocional` |
| `max_tickets`     | Número máximo de ingressos neste lote | number | Ex: `100`, `500` |
| `available_tickets`| Número de ingressos ainda disponíveis | number | Deve ser ≤ `max_tickets` |
| `issued_tickets`  | Número de ingressos emitidos | number | |
| `sold_tickets`    | Número de ingressos vendidos neste lote | number | |
| `created_at`      | Data de criação do lote | string (ISO 8601) | |
| `updated_at`      | Data da última atualização do lote | string (ISO 8601) | |


#### 6.8 Detalhes do Objeto `subscriptions`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | Identificador único do plano de assinatura | string (UUID) | |
| `name`            | Nome do plano | string | Ex: `Mensal`, `Anual`, `Premium Trimestral` |
| `description`     | Descrição detalhada do plano | string ou null | |
| `price`           | Preço da recorrência em centavos | number | Ex: `4990` para R$ 49,90 |
| `frequency`       | Frequência da cobrança | string | Valores possíveis: `monthly`, `bimonthly`, `quarterly`, `semiannual`, `yearly` |
| `installments`    | Número de parcelas (se aplicável) | number | Ex: `1`, `3`, `12` |
| `qty_charges`     | Quantidade total de cobranças (se limitado) | number | Ex: `12` para assinatura de 1 ano com cobranças mensais |
| `trial_days`      | Número de dias de teste gratuito | number | Ex: `0`, `7`, `14`, `30` |
| `setup_fee`       | Taxa de adesão em centavos | number | Ex: `9900` para R$ 99,00 |
| `setup_fee_enabled`| Indica se a taxa de adesão está habilitada | boolean | `true` ou `false` |


#### 6.9 Detalhes do Objeto `revenue_partners`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `account_id`      | ID da conta Kiwify do parceiro | string | |
| `legal_name`      | Nome legal/Razão Social do parceiro | string | |
| `status`          | Status da parceria | string | Valores possíveis: `active`, `inactive`, `pending` |
| `document_id`     | Documento de identificação do parceiro (CPF/CNPJ) | string | Formato: apenas números |
| `percentage`      | Percentual da receita destinado ao parceiro | number | Ex: `10` para 10%, `30` para 30% |
| `split_invoices`  | Indica se as faturas são divididas automaticamente | boolean | `true` ou `false` |
| `start_date`      | Data de início da parceria | string (ISO 8601) | |
| `end_date`        | Data de término da parceria (se aplicável) | string (ISO 8601) ou null | |


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 7. Exemplos de Requisição e Resposta


> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint de consulta de produtos.


### `Endpoint: /products/{id}`


#### 7.1 Exemplo de Requisição (cURL)


```bash
curl --request GET \
  --url https://public-api.kiwify.com/v1/products/20072760-3699-11ee-b627-87e13b212de8 \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  --header 'x-kiwify-account-id: XvS0qfkdzCZTg8z' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json'
```


#### 7.2 Exemplo de Requisição (JavaScript/Fetch)


```javascript
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
    'x-kiwify-account-id': 'XvS0qfkdzCZTg8z',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};


fetch('https://public-api.kiwify.com/v1/products/20072760-3699-11ee-b627-87e13b212de8', options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```


#### 7.3 Exemplo de Resposta (JSON - Sucesso 200 OK)


```json
{
  "id": "20072760-3699-11ee-b627-87e13b212de8",
  "store_id": "XvS0qfkdzCZTg8z",
  "name": "pix test",
  "type": "membership",
  "created_at": "2023-08-09T09:42:59.074Z",
  "price": 500,
  "affiliate_enabled": false,
  "status": "active",
  "payment_type": "charge",
  "shipping_options": [
    {
      "id": "928b5935-a3d9-4f21-879d-f46c1b30d9f0",
      "name": "Frete Gratis",
      "price": 0
    }
  ],
  "links": [
    {
      "id": "KMgND1r",
      "custom_name": null,
      "status": "active",
      "is_sales_page": false
    }
  ],
  "bumps": [
    {
      "id": "9811cdd9-45e9-456d-8c3b-114a7cf6fa33",
      "color": "#f7f7f7",
      "link": {
        "id": "AbDFGi0",
        "custom_name": null,
        "status": "active",
        "is_sales_page": false
      },
      "properties": {
        "action_call": "Adicione este produto especial ao seu pedido",
        "oto_description": "Descrição detalhada da oferta especial",
        "oto_headline": "Oferta exclusiva para você",
        "color": "#f7f7f7",
        "show_product_image": true
      }
    }
  ],
  "offers": [],
  "event_settings": null,
  "event_batches": [],
  "subscriptions": [],
  "revenue_partners": []
}
```


#### 7.4 Exemplo de Resposta (JSON - Erro 404 Not Found)


```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Product not found.",
    "details": {
       "resource_id": "20072760-3699-11ee-b627-87e13b212de9"
    },
    "request_id": "req_kiwify_ab12cd34"
  }
}
```


#### 7.5 Exemplo de Resposta (JSON - Erro 401 Unauthorized)


```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Invalid or expired token.",
    "request_id": "req_kiwify_ef56gh78"
  }
}
```


#### 7.6 Exemplo de Resposta (JSON - Erro 403 Forbidden)


```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have permission to access this resource.",
    "details": {
      "resource_type": "product",
      "resource_id": "20072760-3699-11ee-b627-87e13b212de8"
    },
    "request_id": "req_kiwify_ij90kl12"
  }
}
```


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 8. Códigos de Status e Tratamento de Erros


> **Resumo:** Descrição dos códigos de status HTTP mais comuns retornados pelo endpoint e estratégias de gerenciamento de erros.


| Status Code               | Descrição Geral                                    | Ação Recomendada | Retriável? |
| :------------------------ | :------------------------------------------------- | :--------------- | :--------- |
| `200 OK`                  | Sucesso. Os dados do produto foram retornados no corpo da resposta. | Processar os dados recebidos. | - |
| `400 Bad Request`         | Erro na requisição. Pode ser um ID mal formatado ou parâmetro inválido. | Verificar o formato do ID e a estrutura da requisição. | Não |
| `401 Unauthorized`        | Falha na autenticação. Token `Authorization` inválido, expirado ou ausente, ou `x-kiwify-account-id` inválido/ausente. | Obter um novo token de acesso e tentar novamente. | Sim, após obter novo token |
| `403 Forbidden`           | Acesso negado. As credenciais são válidas, mas não têm permissão para acessar este produto específico. | Verificar as permissões da conta associada às credenciais. | Não |
| `404 Not Found`           | Recurso não encontrado. O `id` do produto fornecido não existe ou foi excluído. | Verificar se o `id` do produto está correto. | Não |
| `429 Too Many Requests`   | Limite de requisições (Rate Limit) excedido. | Implementar espera (backoff) antes de tentar novamente. Verificar cabeçalhos `Retry-After` e `X-RateLimit-*` na resposta. | Sim, após período de espera |
| `500 Internal Server Error`| Erro inesperado no servidor da Kiwify. | Tentar novamente após um intervalo (30s+). Se o erro persistir, contatar o suporte da Kiwify. | Sim, com backoff |
| `503 Service Unavailable` | Servidor temporariamente indisponível ou em manutenção. | Tentar novamente após um intervalo maior (1min+). | Sim, com backoff |


### 8.1 Formato das Respostas de Erro


As respostas de erro da API Kiwify seguem uma estrutura consistente que permite identificar o problema e obter referências para depuração:


```json
{
  "error": {
    "code": "ERRO_CODE_SPECIFIC",
    "message": "Mensagem descritiva sobre o erro",
    "details": {
      // Objeto opcional com detalhes específicos do erro
    },
    "request_id": "identificador_único_da_requisição"
  }
}
```


### 8.2 Códigos de Erro Comuns


| Código de Erro           | Descrição                                         | Status HTTP |
| :----------------------- | :------------------------------------------------ | :---------- |
| `RESOURCE_NOT_FOUND`     | O recurso especificado (produto) não foi encontrado | 404 |
| `UNAUTHORIZED`           | Falha na autenticação, token inválido ou expirado | 401 |
| `FORBIDDEN`              | Sem permissão para acessar o recurso              | 403 |
| `RATE_LIMIT_EXCEEDED`    | Limite de requisições excedido                    | 429 |
| `INVALID_REQUEST`        | Requisição mal formada ou com parâmetros inválidos | 400 |
| `INTERNAL_SERVER_ERROR`  | Erro interno no servidor da Kiwify                | 500 |


### 8.3 Estratégia de Retentativas Recomendada


Para os erros retriáveis (429, 500, 503), recomenda-se:


1. **Backoff Exponencial:** Comece com um intervalo de 1 segundo e duplique a cada tentativa
2. **Jitter Aleatório:** Adicione uma variação aleatória (±10-25%) ao tempo de espera para evitar sincronização de requisições
3. **Máximo de Tentativas:** Limite a 5-8 tentativas antes de falhar definitivamente
4. **Respeito ao Retry-After:** Se o cabeçalho `Retry-After` estiver presente, priorize este valor sobre o cálculo de backoff


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)


> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint de consulta de produtos.


1.  **Exibir detalhes completos de um produto em uma página de detalhes**
    *   Objetivo: `Mostrar todas as informações disponíveis de um produto para o usuário visualizar`
    *   Como Fazer: `GET /v1/products/{id} onde {id} é o identificador do produto a ser exibido`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


2.  **Verificar se um produto está ativo antes de apresentá-lo em catálogo**
    *   Objetivo: `Confirmar que o produto pode ser exibido aos clientes por estar com status "active"`
    *   Como Fazer: `GET /v1/products/{id} e verificar se o campo status é igual a "active"`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


3.  **Obter links de checkout para direcionar clientes**
    *   Objetivo: `Recuperar as URLs corretas dos links (array links) para direcionar os compradores ao processo de pagamento`
    *   Como Fazer: `GET /v1/products/{id}, extrair os objetos do array links e construir URLs de checkout com o formato https://kiwify.com.br/LINK_ID`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


4.  **Recuperar preço atual do produto para atualização em sistema integrado**
    *   Objetivo: `Sincronizar o valor do produto (campo price) em um sistema de terceiros com o valor na Kiwify`
    *   Como Fazer: `GET /v1/products/{id}, capturar o campo price e dividir por 100 para obter o valor em Reais/Dólares`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


5.  **Identificar opções de frete disponíveis para um produto físico**
    *   Objetivo: `Listar as opções de entrega (array shipping_options) e seus respectivos custos para apresentar ao cliente`
    *   Como Fazer: `GET /v1/products/{id} e iterar pelo array shipping_options, extraindo id, name e price de cada opção`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


6.  **Verificar se um produto permite programa de afiliados**
    *   Objetivo: `Determinar se é possível ativar comissões para afiliados neste produto (campo affiliate_enabled)`
    *   Como Fazer: `GET /v1/products/{id} e verificar se affiliate_enabled é true`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


7.  **Acessar detalhes dos parceiros de receita associados ao produto**
    *   Objetivo: `Identificar como a receita do produto é compartilhada (array revenue_partners)`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array revenue_partners para extrair account_id, legal_name e percentage de cada parceiro`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


8.  **Recuperar informações de assinaturas disponíveis para um produto**
    *   Objetivo: `Listar os planos de assinatura (array subscriptions) oferecidos para este produto`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array subscriptions para extrair name, price, frequency e trial_days de cada plano`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


9.  **Verificar configurações de evento de um produto tipo `event`**
    *   Objetivo: `Obter detalhes como data, horário e localização de um evento (objeto event_settings)`
    *   Como Fazer: `GET /v1/products/{id}, verificar se type é "event" e extrair start_date, end_date e address do objeto event_settings`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


10. **Consultar disponibilidade de ingressos nos lotes de um evento**
    *   Objetivo: `Determinar quantos ingressos ainda estão disponíveis (campo available_tickets) em cada lote (array event_batches)`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array event_batches e extrair name e available_tickets de cada lote`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


11. **Identificar bumps (ofertas especiais) associados ao produto**
    *   Objetivo: `Encontrar ofertas complementares (array bumps) que podem ser apresentadas durante o checkout`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array bumps, extraindo id e analisando properties (action_call, oto_headline) e link de cada bump`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


12. **Verificar o tipo de produto (`type`) para tratamento específico**
    *   Objetivo: `Adaptar a interface ou processamento baseado no tipo do produto (physical, membership, event)`
    *   Como Fazer: `GET /v1/products/{id}, verificar o valor do campo type e implementar lógica condicional baseada no resultado`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


13. **Recuperar data de criação (`created_at`) para auditoria ou ordenação**
    *   Objetivo: `Registrar quando o produto foi criado ou ordenar produtos cronologicamente`
    *   Como Fazer: `GET /v1/products/{id}, extrair o campo created_at e converter para o formato de data desejado`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


14. **Identificar a página de vendas principal associada ao produto**
    *   Objetivo: `Encontrar o link que está marcado como página de vendas (is_sales_page = true)`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array links e filtrar itens onde is_sales_page é true`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


15. **Verificar o tipo de pagamento (`payment_type`) principal do produto**
    *   Objetivo: `Determinar se o produto é de cobrança única ("charge") ou assinatura ("subscription")`
    *   Como Fazer: `GET /v1/products/{id} e analisar o campo payment_type para implementar comportamentos específicos de pagamento`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


16. **Consultar ofertas (`offers`) específicas associadas ao produto**
    *   Objetivo: `Recuperar informações sobre ofertas especiais ou promocionais ativas (array offers)`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array offers, filtrando onde active é true, e extrair name e price`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


17. **Verificar requisitos de coleta de informações em eventos (`event_settings`)**
    *   Objetivo: `Identificar se dados como telefone (collect_phone) ou CPF (collect_cpf) são necessários para inscrição`
    *   Como Fazer: `GET /v1/products/{id}, verificar os campos collect_phone e collect_cpf no objeto event_settings`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


18. **Obter localização geográfica (`latitude`, `longitude`) de um evento**
    *   Objetivo: `Acessar coordenadas precisas do endereço do evento para exibição em mapa interativo`
    *   Como Fazer: `GET /v1/products/{id}, extrair latitude e longitude do objeto event_settings.address para usar em serviços de mapas`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


19. **Verificar período de vendas (`sale_start_at`, `sale_end_at`) de um evento**
    *   Objetivo: `Determinar se um evento está atualmente com vendas abertas (comparar datas em event_settings)`
    *   Como Fazer: `GET /v1/products/{id}, extrair sale_start_at e sale_end_at de event_settings e compará-los com a data atual`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


20. **Identificar se um produto de assinatura (`subscriptions`) possui período de teste (`trial_days`)**
    *   Objetivo: `Verificar se existe e qual a duração do teste gratuito para planos de assinatura`
    *   Como Fazer: `GET /v1/products/{id}, iterar pelo array subscriptions, verificar quais têm trial_days > 0 e destacar esta informação`
    *(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 10. Notas Adicionais


> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint de consulta de produtos.


*   **Valores Monetários:** Todos os campos de preço (`price`, `setup_fee`, etc.) são retornados como **inteiros representando centavos**. Para obter o valor na moeda local (ex: Reais, Dólares), divida o valor por 100. Por exemplo, `price: 500` representa R$ 5,00.


*   **Tipos de Produto:** O campo `type` indica a natureza do produto e determina quais campos adicionais são relevantes:
    * `membership`: Produto digital (infoproduto, curso, etc.)
    * `physical`: Produto físico (campos `shipping_options` serão relevantes)
    * `event`: Evento presencial ou online (campos `event_settings` e `event_batches` serão relevantes)


*   **Respostas Condicionais:** Dependendo do tipo e configuração do produto, alguns arrays ou objetos podem estar vazios ou nulos:
    * Arrays vazios (`[]`): `subscriptions`, `revenue_partners`, `offers`, `bumps`, `event_batches`, `shipping_options`
    * Objeto nulo (`null`): `event_settings` (para produtos não-evento)
    * Campos nulos (`null`): `custom_name`, `end_date`, `properties`, entre outros


*   **Rate Limits:** A API Kiwify implementa limites de requisição. Para este endpoint específico:
    * Limite padrão: 60 requisições por minuto por token de API
    * Cabeçalhos de resposta incluem: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
    * Quando excedido, retorna status 429 com cabeçalho `Retry-After` indicando segundos de espera


*   **Cache:** As respostas podem ser armazenadas em cache por até 5 minutos para otimizar performance. Para forçar dados atualizados, utilize o cabeçalho `Cache-Control: no-cache`.


*   **Links e URLs:** Os IDs de link (`links[].id`, `bumps[].link.id`) são identificadores curtos. Para criar a URL completa, utilize o formato:
    * `https://kiwify.com.br/{link_id}` (Ex: `https://kiwify.com.br/KMgND1r`)


*   **Datas e Horários:** Todos os campos de data/hora seguem o padrão ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) e são retornados em UTC. Faça a conversão para o fuso horário local conforme necessário na sua aplicação.


*   **Valores de Status:** Os campos de status (`status`, `links[].status`, etc.) seguem padrões consistentes:
    * Produto: `active`, `inactive`, `draft`
    * Link: `active`, `inactive`
    * Parceiro: `active`, `inactive`, `pending`


*   **Compatibilidade Futura:** Este endpoint pode receber novos campos no futuro sem que isso quebre integrações existentes. Sua implementação deve ignorar graciosamente campos desconhecidos.


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)


> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.


```json
{
  "doc_id": "kiwify_prod_001",
  "api_provider": "Kiwify",
  "api_product_area": "Produtos",
  "endpoint_focus": ["Consultar Produto", "Obter Detalhes de Produto", "Get Product by ID"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Confidential",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Produto", "Loja", "Link", "Bump", "Oferta", "Assinatura", "Evento", "LoteEvento", "ParceiroReceita", "OpcaoFrete"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["e-commerce", "infoprodutos", "gestao_produtos", "eventos", "assinaturas", "api_integracao"],
  "db_relations": {
    "tables": ["products", "stores", "product_links", "product_bumps", "product_offers", "subscriptions", "events", "event_batches", "revenue_partners", "shipping_options"],
    "schemas": ["public", "billing", "events"]
  },
  "related_concepts": ["checkout", "pagamento online", "catalogo de produtos", "afiliados", "order bump", "gestao de eventos", "planos recorrentes", "split de pagamento"],
  "question_embeddings": [
    "Como faço para obter os dados de um produto específico na Kiwify via API?",
    "Qual endpoint da Kiwify retorna detalhes de um produto pelo ID?",
    "Como verificar o preço e status de um produto Kiwify?",
    "Quais informações a API da Kiwify fornece sobre um produto?",
    "Como listar os links de checkout de um produto Kiwify?",
    "É possível ver os planos de assinatura de um produto pela API Kiwify?",
    "Como consultar informações de um evento (local, data) pela API Kiwify?",
    "Qual formato devo usar para obter dados de um produto da Kiwify?",
    "Como verificar se um produto Kiwify permite programa de afiliados?",
    "Onde encontro o preço de um produto na resposta da API Kiwify?"
  ],
  "reasoning_pathways": ["retrieval", "conditional_logic", "data_extraction", "url_construction", "date_comparison"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "API Key Header (x-kiwify-account-id)"],
  "typical_integration_points": ["Plataforma E-commerce", "Sistema ERP", "Dashboard Personalizado", "Ferramenta de Automação de Marketing", "Aplicativo Mobile", "Sistema de Controle de Eventos"],
  "common_error_patterns": ["RESOURCE_NOT_FOUND (404)", "UNAUTHORIZED (401)", "FORBIDDEN (403)", "RATE_LIMIT_EXCEEDED (429)"]
}
```


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 12. Checklist de Implementação (Opcional)


> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação da consulta de produtos.


- [ ] **Autenticação**
  - [ ] Implementar fluxo OAuth 2.0 para obter `Bearer Token`
  - [ ] Armazenar e fornecer `x-kiwify-account-id` no cabeçalho
  - [ ] Implementar lógica de renovação de token (refresh token)
  - [ ] Armazenar credenciais de forma segura (não em código-fonte)


- [ ] **Construção da Requisição**
  - [ ] Validar formato do `id` do produto (UUID) antes de chamar a API
  - [ ] Montar URL corretamente: `https://public-api.kiwify.com/v1/products/{id}`
  - [ ] Incluir cabeçalhos `Authorization` e `x-kiwify-account-id`
  - [ ] Adicionar cabeçalhos opcionais relevantes (`Accept`, `Content-Type`)


- [ ] **Tratamento de Resposta (Sucesso - 200 OK)**
  - [ ] Mapear JSON de resposta para objeto/estrutura de dados interna
  - [ ] Converter valores monetários (dividir por 100)
  - [ ] Tratar arrays vazios (`[]`) e objetos/campos `null`
  - [ ] Verificar o campo `type` para processamento condicional
  - [ ] Construir URLs completas a partir dos IDs de links


- [ ] **Tratamento de Erros (4xx, 5xx)**
  - [ ] Implementar handlers específicos para `401`, `403`, `404`
  - [ ] Extrair `error.code`, `error.message` e `error.request_id` para logging
  - [ ] Implementar lógica de retentativa com backoff exponencial para `429`, `500`, `503`
  - [ ] Respeitar cabeçalho `Retry-After` quando presente
  - [ ] Adicionar logging detalhado para erros, incluindo `request_id`


- [ ] **Otimização**
  - [ ] Implementar cache local para respostas (TTL: 5 minutos)
  - [ ] Monitorar uso de rate limits via cabeçalhos `X-RateLimit-*`
  - [ ] Invalidar cache se houver suspeita de atualização do produto
  - [ ] Usar compressão HTTP (cabeçalho `Accept-Encoding: gzip, deflate`)


- [ ] **Validação e Testes**
  - [ ] Criar testes unitários para o mapeamento da resposta
  - [ ] Implementar testes de integração cobrindo sucesso e erros comuns
  - [ ] Testar com diferentes tipos de produtos (membership, physical, event)
  - [ ] Verificar manipulação correta de datas ISO 8601
  - [ ] Testar cenários de timeout e falhas de rede


- [ ] **Logging e Monitoring**
  - [ ] Registrar `request_id` para todas as chamadas (sucesso e erro)
  - [ ] Implementar métricas de performance (tempo de resposta)
  - [ ] Monitorar taxa de erros por tipo (401, 403, 404, 429, 5xx)
  - [ ] Criar alertas para falhas recorrentes ou aumentos na taxa de erro


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 13. Glossário de Termos Técnicos


> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados nesta documentação.


| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Produto`                 | Entidade principal que representa um item vendável na plataforma Kiwify (digital, físico, evento, etc.). |
| `ID (Produto)`            | Identificador único universal (UUID) de um produto na Kiwify. |
| `UUID`                    | Formato de identificador único universal (Universally Unique Identifier) usado para IDs de produtos e outras entidades. |
| `Bearer Token`            | Credencial de segurança (token) usada no cabeçalho `Authorization` para autenticação OAuth 2.0. |
| `x-kiwify-account-id`     | Cabeçalho HTTP obrigatório contendo o identificador único da conta Kiwify que realiza a requisição. |
| `Membership`              | Tipo de produto digital (infoproduto, curso, área de membros) na plataforma Kiwify. |
| `Bump`                    | Oferta complementar apresentada durante o processo de checkout para aumentar o valor do pedido. |
| `Link`                    | URL única que direciona o cliente para uma página específica relacionada ao produto (checkout, página de vendas). |
| `Assinatura`              | Plano de pagamento recorrente associado a um produto, com cobrança periódica (mensal, anual, etc.). |
| `Lote de Evento`          | Subdivisão de ingressos para um evento, geralmente com preço ou quantidade limitada específica. |
| `Parceiro de Receita`     | Conta Kiwify configurada para receber uma porcentagem da receita das vendas de um produto (split de pagamento). |
| `ISO 8601`                | Padrão internacional para representação de datas e horas (formato YYYY-MM-DDTHH:MM:SSZ). |
| `Backoff Exponencial`     | Estratégia de retentativa onde o tempo de espera entre tentativas aumenta exponencialmente após falhas. |
| `Rate Limit`              | Limite no número de requisições que podem ser feitas à API em um determinado período de tempo. |
| `Trial`                   | Período de teste gratuito oferecido antes do início da cobrança em um plano de assinatura. |
| `Setup Fee`               | Taxa única de adesão cobrada no início de um plano de assinatura, além das cobranças recorrentes. |
| `Centavos`                | Unidade básica dos valores monetários na API. Todos os preços são expressos em centavos (100 = R$ 1,00). |
| `Webhook`                 | Mecanismo de notificação onde a Kiwify envia requisições HTTP para uma URL configurada quando eventos ocorrem. |
| `OAuth 2.0`               | Protocolo de autorização utilizado pela API Kiwify para autenticação segura. |
| `Frete`                   | Opção de envio disponível para produtos físicos, configurada através de `shipping_options`. |


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---


## 14. Observações Finais sobre Formatação


> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.


*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados e comparativos.
*   Use blocos de código (``` ```) com indicação de linguagem (`bash`, `json`) para exemplos.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa.
*   Formate nomes de parâmetros (`id`), campos (`price`), valores (`active`) e cabeçalhos (`Authorization`) com backticks (` `).
*   **Crucial:** Inclua a tag `(Ref: [TITULO_CURTO], ID [ID_INTERNO])` no final de **CADA SEÇÃO PRINCIPAL (##)**.
*   Mantenha os resumos de seção (`> **Resumo:** ...`) concisos (1-2 linhas) e informativos.
*   Use listas (`*`, `-`) e bullets para informações sequenciais ou enumeradas (como no Checklist e Casos de Uso).
*   Defina termos técnicos e abreviações no Glossário (Seção 13) ou na primeira ocorrência.
*   Seja consistente na terminologia em todo o documento.
*   Organize informações do mais geral para o mais específico dentro de cada seção.
*   Utilize exemplos concretos e práticos para ilustrar conceitos.
*   Mantenha o foco no endpoint específico sendo documentado.


*(Ref: Kiwify Get Product, ID kiwify_getproducts_001)*
---