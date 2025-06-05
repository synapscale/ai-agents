# API PerfectPay - Assinaturas - Obter Assinaturas




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


> **Resumo:** Metadados essenciais que identificam e contextualizam este documento de API.


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API PerfectPay - Assinaturas - Obter Informações de Assinaturas |
| **Identificador Interno** | `perfectpay_sub_001`                                            |
| **Título Curto (Ref.)**   | `PerfectPay Get Subscriptions`                                  |
| **Versão do Documento**   | `1.0.0`                                                         |
| **Data de Criação**       | `2025-04-27`                                                    |
| **Última Atualização**    | `2025-04-27`                                                    |
| **Autor/Responsável**     | `Equipe de Documentação`                                        |
| **Fonte Original**        | `https://support.perfectpay.com.br/doc/perfect-pay/perfectpay-api/assinatura` |
| **URL de Referência**     | `https://app.perfectpay.com.br/api/v1/subscriptions/get`        |
| **Status do Documento**   | `Em Uso`                                                        |
| **Ambiente de Referência**| `Produção`                                                      |
| **Idioma Original**       | `Português (BR)`                                                |
| **Formato de Datas (API)**| `Date (YYYY-MM-DD)`                                             |


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 2. Contexto


> **Resumo:** Descreve o propósito e o cenário de uso do endpoint de consulta de assinaturas da PerfectPay.


Este endpoint (`perfectpay_sub_001`) é utilizado para obter informações detalhadas sobre assinaturas de usuários na plataforma PerfectPay. Seu principal propósito é permitir a consulta e filtragem de dados de assinaturas com base em critérios como status (`subscription_status_enum`), tipo de recorrência (`recurrent_type_enum`) e email do cliente (`customer_email`). É fundamental para integrações que necessitam monitorar, analisar ou gerenciar o ciclo de vida de assinaturas recorrentes.


A API é particularmente útil para:
- Sistemas de gestão financeira que precisam acompanhar assinaturas ativas e canceladas
- Ferramentas de análise de churn que monitoram cancelamentos
- Dashboards administrativos que exibem visões consolidadas de assinaturas
- Integrações com CRMs que necessitam de dados atualizados sobre o status das assinaturas dos clientes


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 3. Visão Geral da API/Endpoint(s)


> **Resumo:** Apresenta uma visão de alto nível da funcionalidade do endpoint de obtenção de assinaturas.


Este documento cobre um único endpoint (`POST /api/v1/subscriptions/get`) que permite consultar dados de assinaturas existentes no sistema PerfectPay. A consulta é feita via `POST`, enviando filtros opcionais no corpo da requisição. A resposta inclui uma lista paginada de assinaturas que correspondem aos filtros, contendo detalhes sobre status, recorrência, datas, valores, cliente, produto e plano associados.


O endpoint foi projetado para fornecer uma interface unificada para todas as necessidades de consulta de assinaturas, suportando:
- Filtragem por múltiplos critérios (status, tipo de recorrência, email)
- Paginação para conjuntos grandes de resultados
- Dados completos sobre cada assinatura em um único formato de resposta


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 4. Detalhes Técnicos


> **Resumo:** Especificações técnicas essenciais para interagir com o endpoint.


### `Endpoint: /api/v1/subscriptions/get`


*   **Endpoint URL:** `https://app.perfectpay.com.br/api/v1/subscriptions/get`
*   **Método HTTP:** `POST`
*   **Autenticação:** `Bearer Token`. Incluir o cabeçalho `Authorization: Bearer "TOKEN_API_GERADO_NA_PAY"`.
*   **Content-Type:** `application/json`
*   **Accept:** `application/json`
*   **Codificação de Caracteres:** `UTF-8`
*   **Timeout Recomendado:** `30 segundos` (não especificado oficialmente, mas recomendado)


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 5. Parâmetros de Entrada


> **Resumo:** Detalhamento dos parâmetros aceitos no corpo (body) da requisição POST para filtrar as assinaturas.


### `Endpoint: /api/v1/subscriptions/get` (`Body Parameters`)


| Parâmetro                 | Descrição | Tipo | Obrigatório? | Notas / Valores Possíveis |
| :------------------------ | :-------- | :--- | :----------- | :------------------------ |
| `subscription_status_enum`| Status da assinatura para filtro. | Integer | Não | `1`: Período de teste<br>`2`: Ativa<br>`3`: Cancelada<br>`4`: Aguardando pagamento |
| `recurrent_type_enum`     | Tipo de recorrência da assinatura. | Integer | Não | `1`: 7 dias<br>`2`: 15 dias<br>`3`: Mensal<br>`4`: Trimestral<br>`5`: Semestral<br>`6`: Anual |
| `customer_email`          | Email do cliente para filtro. | String | Não | Ex: `emaildocliente@gmail.com` |
| `page`                    | Número da página para paginação dos resultados. | Integer | Não | Padrão: 1. Usado para navegar por conjuntos grandes de resultados. |


**Notas sobre Filtragem:**
- Todos os parâmetros são opcionais. Se nenhum for fornecido, o endpoint retornará todas as assinaturas (paginadas).
- Filtros múltiplos atuam como condição "E" lógica (ex: status=2 E email=xyz@exemplo.com).
- Os valores fornecidos para `subscription_status_enum` e `recurrent_type_enum` devem ser os números inteiros correspondentes, não os textos descritivos.


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)


> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint em caso de sucesso (200 OK).


### `Endpoint: /api/v1/subscriptions/get`


#### 6.1.1 Estrutura Geral da Resposta


| Campo             | Descrição | Tipo   |
| :---------------- | :-------- | :----- |
| `subscriptions`   | Objeto raiz contendo os dados das assinaturas e informações de paginação. | Object |


#### 6.1.2 Detalhes do Objeto `subscriptions`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `data`                | Array contendo os objetos de cada assinatura encontrada. | Array | Pode ser um array vazio se nenhuma assinatura corresponder aos filtros. |
| `current_page`        | Número da página atual retornada. | Integer | Corresponde ao parâmetro `page` enviado ou 1 se não especificado. |
| `current_items_count` | Quantidade de assinaturas retornadas na página atual. | Integer | Útil para determinar se a página está completa. |
| `total_pages`         | Número total de páginas disponíveis para os filtros aplicados. | Integer | Use para determinar quando parar a paginação. |
| `total_items`         | Número total de assinaturas encontradas para os filtros aplicados. | Integer | O número total de resultados disponíveis em todas as páginas. |


#### 6.1.3 Detalhes do Objeto de Assinatura (dentro do array `data`)


| Campo Aninhado             | Descrição | Tipo | Notas |
| :------------------------- | :-------- | :--- | :---- |
| `id`                       | Identificador único da assinatura. | Integer | Pode ser usado para referência em outras operações. |
| `recurrent_type_enum`      | Descrição textual do tipo de recorrência. | String | Ex: `"7 Dias"`, `"15 Dias"`, `"Mensal"`, `"Trimestral"`, `"Semestral"`, `"Anual"` |
| `installments`             | Número de prestações (geralmente `1` para assinaturas). | Integer | Para assinaturas recorrentes, normalmente será 1. |
| `start_date_recurrent`     | Data de início da assinatura. | Date | Formato `YYYY-MM-DD`. Indica quando a assinatura foi criada. |
| `end_date_recurrent`       | Data de término da assinatura (se aplicável). | Date | Formato `YYYY-MM-DD`. Pode ser `null` para assinaturas sem data de término definida. |
| `next_date_recurrent`      | Data da próxima cobrança agendada. | Date | Formato `YYYY-MM-DD`. Indica quando ocorrerá a próxima renovação. |
| `canceled_date`            | Data em que a assinatura foi cancelada (se aplicável). | Date | Formato `YYYY-MM-DD`. `null` se a assinatura estiver ativa. |
| `charges_made`             | Quantidade de cobranças já realizadas nesta assinatura. | Integer | Útil para análise de ciclo de vida do cliente. |
| `subscription_status_enum` | Descrição textual do status atual da assinatura. | String | `"Período de teste"`, `"Ativa"`, `"Cancelada"`, `"Aguardando pagamento"` |
| `subscription_status_detail`| Detalhe adicional sobre o status. | String | Ex: `"active"`, `"cancelled_by_customer"`, `"cancelled_billing_error"`, `"trial"`, `"awaiting_payment"` etc. |
| `payment_type_enum`        | Código numérico do tipo de pagamento principal associado. | Integer | `1`: Cartão de Crédito, `2`: Boleto, `3`: PayPal, `4`: Cartão Recorrente, etc. |
| `customer`                 | Objeto contendo informações do cliente. | Object | Ver detalhes abaixo. |
| `product`                  | Objeto contendo informações do produto associado. | Object | Ver detalhes abaixo. |
| `plan`                     | Objeto contendo informações do plano associado. | Object | Ver detalhes abaixo. |
| `subscription_amount`      | Valor da assinatura formatado em Reais. | String | Ex: `"R$ 5,00"` (nota: é uma string formatada, não um valor numérico). |


#### 6.1.4 Detalhes do Objeto `customer`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `email`               | E-mail do cliente. | String | Corresponde ao endereço de email cadastrado pelo cliente. |
| `full_name`           | Nome completo do cliente. | String | Nome conforme fornecido pelo cliente no cadastro. |


#### 6.1.5 Detalhes do Objeto `product`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `name`                | Nome do produto principal da assinatura. | String | Identifica o produto ou serviço assinado. |


#### 6.1.6 Detalhes do Objeto `plan`


| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `name`                | Nome do plano específico da assinatura. | String | Pode ser `null` se não houver um plano específico associado. |


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 7. Exemplos de Requisição e Resposta


> **Resumo:** Exemplos práticos de como chamar o endpoint e o formato esperado da resposta.


### `Endpoint: /api/v1/subscriptions/get`


#### 7.1.1 Exemplo de Requisição (cURL - Filtrando por Status e Email)


```bash
curl -X POST "https://app.perfectpay.com.br/api/v1/subscriptions/get" \
  -H "Authorization: Bearer {TOKEN_API_GERADO_NA_PAY}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "subscription_status_enum": 3,
    "customer_email": "wilsiinups@gmail.com"
  }'
```


#### 7.1.2 Exemplo de Requisição (PHP - Filtrando por Status e Email)


```php
<?php
$sendData = [
    "subscription_status_enum" => 3, // Filtrar por Cancelada
    "customer_email"           => "wilsiinups@gmail.com",
];


$ch = curl_init();


curl_setopt($ch, CURLOPT_URL, 'https://app.perfectpay.com.br/api/v1/subscriptions/get');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($sendData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Accept: application/json',
    'Authorization: Bearer "TOKEN_API_GERADO_NA_PAY"', // Substitua pelo seu token real
]);


$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);


echo "HTTP Code: " . $httpCode . "\n";
echo "Response Body: " . $response . "\n";


// Decodificar a resposta JSON
$responseData = json_decode($response, true);
// Agora você pode acessar os dados, ex: $responseData['subscriptions']['data']
?>
```


#### 7.1.3 Exemplo de Resposta (JSON - Sucesso 200 OK)


```json
{
  "subscriptions": {
    "data": [
      {
        "id": 2,
        "recurrent_type_enum": "15 Dias",
        "installments": 1,
        "start_date_recurrent": "2019-07-05",
        "end_date_recurrent": null,
        "next_date_recurrent": "2019-07-22",
        "canceled_date": "2019-07-09",
        "charges_made": 3,
        "subscription_status_enum": "Cancelada",
        "subscription_status_detail": "cancelled_billing_error",
        "payment_type_enum": 1,
        "customer": {
          "email": "wilsiinups@gmail.com",
          "full_name": "Cliente Teste"
        },
        "product": {
          "name": "Teste Recorrente"
        },
        "plan": {
          "name": "Produto Caps | 4 Potes"
        },
        "subscription_amount": "R$ 5,00"
      }
    ],
    "current_page": 1,
    "current_items_count": 1,
    "total_pages": 1,
    "total_items": 1
  }
}
```


#### 7.1.4 Exemplo de Requisição (cURL - Listando Todas as Assinaturas Ativas, Página 1)


```bash
curl -X POST "https://app.perfectpay.com.br/api/v1/subscriptions/get" \
  -H "Authorization: Bearer {TOKEN_API_GERADO_NA_PAY}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "subscription_status_enum": 2,
    "page": 1
  }'
```


#### 7.1.5 Exemplo de Resposta (JSON - Múltiplas Assinaturas, Paginação)


```json
{
  "subscriptions": {
    "data": [
      {
        "id": 1965,
        "recurrent_type_enum": "7 Dias",
        "installments": 1,
        "start_date_recurrent": "2019-11-05",
        "end_date_recurrent": null,
        "next_date_recurrent": "2019-12-11",
        "canceled_date": null,
        "charges_made": 4,
        "subscription_status_enum": "Ativa",
        "subscription_status_detail": "active",
        "payment_type_enum": 1,
        "customer": {
          "email": "sememail@gmail.com",
          "full_name": "Cliente Full Name"
        },
        "product": {
          "name": "Teste Recorrente"
        },
        "plan": {
          "name": null
        },
        "subscription_amount": "R$ 5,00"
      },
      {
        "id": 1966,
        "recurrent_type_enum": "Mensal",
        "installments": 1,
        "start_date_recurrent": "2019-11-10",
        "end_date_recurrent": null,
        "next_date_recurrent": "2019-12-10",
        "canceled_date": null,
        "charges_made": 1,
        "subscription_status_enum": "Ativa",
        "subscription_status_detail": "active",
        "payment_type_enum": 1,
        "customer": {
          "email": "outro@email.com",
          "full_name": "Outro Cliente"
        },
        "product": {
          "name": "Produto Mensal"
        },
        "plan": {
          "name": "Plano Básico"
        },
        "subscription_amount": "R$ 29,90"
      }
    ],
    "current_page": 1,
    "current_items_count": 2,
    "total_pages": 3,
    "total_items": 6
  }
}
```


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 8. Códigos de Status e Tratamento de Erros


> **Resumo:** Descrição dos códigos de status HTTP retornados e possíveis causas de erro.


| Status Code               | Descrição Geral                                              | Possíveis Causas / Ações Recomendadas |
| :------------------------ | :----------------------------------------------------------- | :------------------------------------ |
| `200 OK`                  | Sucesso. A requisição foi processada e os dados retornados no corpo. | N/A |
| `400 Bad Request`         | Erro na requisição. | Verificar se o JSON enviado é válido e se os parâmetros (`subscription_status_enum`, `recurrent_type_enum`, `page`) estão nos formatos corretos (Integer). |
| `401 Unauthorized`        | Falha na autenticação. | Verificar se o `Bearer Token` está correto, válido e incluído no cabeçalho `Authorization`. |
| `404 Not Found`           | Endpoint não encontrado. | Verificar se a URL `https://app.perfectpay.com.br/api/v1/subscriptions/get` está correta. |
| `405 Method Not Allowed`  | Método HTTP incorreto. | Certificar-se de que está usando o método `POST`. |
| `429 Too Many Requests`   | Limite de requisições excedido. | Implementar backoff exponencial e tentar novamente mais tarde. |
| `500 Internal Server Error`| Erro inesperado no servidor da PerfectPay. | Tentar novamente mais tarde. Se o erro persistir, contatar o suporte da PerfectPay. |
| `503 Service Unavailable` | Serviço temporariamente indisponível. | Aguardar e tentar novamente mais tarde. |


**Exemplo de Resposta de Erro (401 Unauthorized):**


```json
{
  "error": {
    "code": "invalid_token",
    "message": "Token de acesso inválido ou expirado"
  }
}
```


**Exemplo de Resposta de Erro (400 Bad Request):**


```json
{
  "error": {
    "code": "invalid_parameter",
    "message": "Parâmetro 'subscription_status_enum' deve ser um número inteiro"
  }
}
```


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)


> **Resumo:** Lista abrangente de 20 exemplos práticos de como utilizar o endpoint para diferentes necessidades.


1.  **Listar todas as assinaturas ativas**
    *   Objetivo: `Obter uma lista de todas as assinaturas com status "Ativa"`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 2}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


2.  **Listar assinaturas canceladas**
    *   Objetivo: `Obter uma lista de todas as assinaturas com status "Cancelada"`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 3}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


3.  **Verificar assinaturas em período de teste**
    *   Objetivo: `Identificar assinaturas que ainda estão na fase de teste gratuito`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 1}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


4.  **Verificar assinaturas aguardando pagamento**
    *   Objetivo: `Listar assinaturas que estão pendentes de pagamento para ativação ou renovação`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 4}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


5.  **Buscar assinaturas de um cliente específico pelo email**
    *   Objetivo: `Encontrar todas as assinaturas associadas a um determinado endereço de email`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"customer_email": "cliente.exemplo@email.com"}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


6.  **Listar todas as assinaturas com recorrência mensal**
    *   Objetivo: `Encontrar todas as assinaturas configuradas com ciclo de cobrança mensal`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"recurrent_type_enum": 3}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


7.  **Listar todas as assinaturas com recorrência anual**
    *   Objetivo: `Identificar todas as assinaturas configuradas com ciclo de cobrança anual`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"recurrent_type_enum": 6}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


8.  **Buscar assinaturas semanais que estão ativas**
    *   Objetivo: `Encontrar assinaturas ativas que possuem um ciclo de cobrança de 7 dias`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"recurrent_type_enum": 1, "subscription_status_enum": 2}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


9.  **Identificar assinaturas canceladas devido a erro na cobrança**
    *   Objetivo: `Analisar falhas de pagamento que resultaram em cancelamentos automáticos`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 3}` e filtrar a resposta pelo campo `subscription_status_detail` igual a `"cancelled_billing_error"`.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


10. **Identificar assinaturas canceladas pelo próprio cliente**
    *   Objetivo: `Analisar cancelamentos iniciados voluntariamente pelos clientes`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 3}` e filtrar a resposta pelo campo `subscription_status_detail` igual a `"cancelled_by_customer"`.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


11. **Navegar para a segunda página de resultados de assinaturas ativas**
    *   Objetivo: `Obter o próximo conjunto de assinaturas ativas quando a primeira página está cheia`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 2, "page": 2}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


12. **Listar assinaturas ativas de um cliente específico**
    *   Objetivo: `Verificar quais assinaturas um cliente específico possui que estão atualmente ativas`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"customer_email": "cliente.exemplo@email.com", "subscription_status_enum": 2}`
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


13. **Identificar assinaturas ativas com próxima cobrança nos próximos 7 dias**
    *   Objetivo: `Antecipar renovações ou possíveis problemas de pagamento`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 2}` e filtrar a resposta pelo campo `next_date_recurrent` dentro do intervalo desejado.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


14. **Verificar o número de cobranças já realizadas para assinaturas canceladas**
    *   Objetivo: `Analisar o tempo de vida médio das assinaturas antes do cancelamento`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 3}` e analisar o campo `charges_made` na resposta.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


15. **Identificar clientes que cancelaram assinaturas mensais no último mês**
    *   Objetivo: `Analisar churn recente para assinaturas mensais`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 3, "recurrent_type_enum": 3}` e filtrar a resposta pelo campo `canceled_date` dentro do último mês.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


16. **Listar assinaturas canceladas que tiveram mais de 3 cobranças realizadas**
    *   Objetivo: `Identificar clientes que permaneceram por um tempo razoável antes de cancelar`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 3}` e filtrar a resposta onde `charges_made > 3`.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


17. **Contar quantas assinaturas ativas cada cliente possui**
    *   Objetivo: `Identificar clientes com múltiplos produtos ou serviços ativos`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 2}`, obter todos os resultados (usando paginação) e agrupar/contar pelo `customer.email` na aplicação cliente.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


18. **Gerar um relatório de distribuição de assinaturas por tipo de recorrência**
    *   Objetivo: `Entender quais são os planos de recorrência mais populares`
    *   Como Fazer: `POST /api/v1/subscriptions/get` (sem filtro de recorrência), obter todos os resultados e contar a ocorrência de cada valor em `recurrent_type_enum` na aplicação cliente.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


19. **Identificar assinaturas ativas sem data de término definida (contínuas)**
    *   Objetivo: `Localizar assinaturas que renovarão indefinidamente até o cancelamento`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 2}` e filtrar a resposta onde `end_date_recurrent` é `null`.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


20. **Calcular o valor total mensal recorrente (MRR) das assinaturas ativas**
    *   Objetivo: `Estimar a receita recorrente mensal com base nas assinaturas ativas`
    *   Como Fazer: `POST /api/v1/subscriptions/get` com body `{"subscription_status_enum": 2}`, obter todos os resultados, normalizar os valores de `subscription_amount` para mensais (considerando `recurrent_type_enum`) e somá-los na aplicação cliente.
    *(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 10. Notas Adicionais


> **Resumo:** Informações complementares importantes sobre o comportamento e limitações do endpoint.


*   **Rate Limits:** A documentação oficial da PerfectPay não especifica limites de requisição (Rate Limits) para este endpoint. Recomenda-se monitorar respostas `429 Too Many Requests` e implementar backoff exponencial se necessário.


*   **Paginação:** O endpoint utiliza paginação baseada no parâmetro `page`. É essencial verificar os campos `total_pages` e `current_page` na resposta para iterar corretamente por todos os resultados quando `total_items` for grande. O número de itens por página não é explicitamente configurável e parece ser um padrão interno da API.


*   **Formatos de Data:** As datas nos parâmetros de saída (`start_date_recurrent`, `end_date_recurrent`, `next_date_recurrent`, `canceled_date`) são retornadas no formato `YYYY-MM-DD`.


*   **Valores Monetários:** O campo `subscription_amount` é retornado como uma string já formatada (`"R$ X,XX"`). Para cálculos, será necessário parsear esta string para um formato numérico removendo o prefixo "R$ " e convertendo a vírgula para ponto decimal.


*   **Filtragem Combinada:** É possível combinar múltiplos filtros na requisição (ex: `subscription_status_enum` e `customer_email`) para refinar a busca.


*   **Consistência de Dados:** A atualização dos status e datas pode ter um pequeno delay em relação aos eventos reais na plataforma.


*   **Idempotência:** O endpoint é idempotente para consultas - a mesma requisição retornará os mesmos resultados, dado que o estado das assinaturas não tenha mudado entre as chamadas.


*   **Tipo de Conteúdo:** Tanto a requisição quanto a resposta utilizam o formato JSON. Certifique-se de incluir o cabeçalho `Content-Type: application/json`.


*   **Informações de Disponibilidade:** A API está disponível 24/7, mas pode haver janelas de manutenção ocasionais não documentadas.


*   **Ordenação:** Os resultados são ordenados internamente pelo sistema. A API não oferece parâmetros para controlar a ordenação.


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 11. Metadados Internos (Para Indexação e RAG)


> **Resumo:** Metadados estruturados em JSON para otimizar a indexação e recuperação por sistemas RAG.


```json
{
  "doc_id": "perfectpay_sub_001",
  "api_provider": "PerfectPay",
  "api_product_area": "Assinaturas",
  "endpoint_focus": ["Obter Informações de Assinaturas", "Filtrar Assinaturas", "Listar Assinaturas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Assinatura", "Cliente", "Produto", "Plano", "Pagamento Recorrente", "Status Assinatura"],
  "context_level": ["intermediate"],
  "topic_cluster": ["pagamentos", "assinaturas", "gestão de clientes", "recorrência", "api perfectpay"],
  "db_relations": {
    "tables": ["subscriptions", "customers", "products", "plans", "subscription_charges"],
    "schemas": ["production"]
  },
  "related_concepts": ["pagamento recorrente", "ciclo de cobrança", "churn", "MRR", "status de assinatura", "filtro de dados", "paginação API"],
  "question_embeddings": [
    "Como listar assinaturas ativas na PerfectPay via API?",
    "Como filtrar assinaturas por email do cliente na PerfectPay?",
    "Qual endpoint usar para buscar assinaturas canceladas na PerfectPay?",
    "Como obter a data da próxima cobrança de uma assinatura PerfectPay?",
    "A API da PerfectPay permite filtrar assinaturas por tipo de recorrência?",
    "Como paginar os resultados da API de assinaturas da PerfectPay?",
    "Quais são os status possíveis para uma assinatura na PerfectPay (API)?",
    "Como saber se uma assinatura PerfectPay foi cancelada por erro de cobrança?",
    "É possível buscar assinaturas por período de teste na API da PerfectPay?"
  ],
  "reasoning_pathways": ["filtering", "retrieval", "status_check", "pagination_handling", "data_extraction"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Unknown",
  "authentication_requirements": ["Bearer Token"],
  "typical_integration_points": ["CRM", "Plataforma E-commerce", "Sistema de BI", "Painel de Controle Interno"],
  "common_error_patterns": ["Invalid Bearer Token (401)", "Incorrect parameter format (400)"]
}
```


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 12. Checklist de Implementação (Opcional)


> **Resumo:** Lista verificável de aspectos técnicos a considerar ao implementar a integração com este endpoint.


- [ ] Autenticação
  - [ ] Implementar mecanismo de obtenção e armazenamento seguro do `Bearer Token`.
  - [ ] Tratar erro `401 Unauthorized` (token inválido/expirado).
  - [ ] Implementar renovação automática do token quando necessário.


- [ ] Tratamento de Erros (4xx, 5xx)
  - [ ] Implementar handlers para códigos `400`, `401`, `404`, `500`.
  - [ ] Adicionar logging detalhado para debug de requisições falhas.
  - [ ] Apresentar mensagens de erro amigáveis ao usuário final.


- [ ] Retries (429, 5xx)
  - [ ] Implementar backoff exponencial para `5xx` e `429` (se ocorrer).
  - [ ] Definir número máximo de tentativas (recomendado: 3-5).
  - [ ] Adicionar jitter para evitar sincronização de retentativas.


- [ ] Paginação
  - [ ] Implementar lógica para usar o parâmetro `page`.
  - [ ] Verificar `total_pages` e `current_page` para iterar por todos os resultados.
  - [ ] Gerenciar o caso de `total_items` ser zero.


- [ ] Validação de Entrada
  - [ ] Garantir que os parâmetros de filtro (`subscription_status_enum`, `recurrent_type_enum`, `page`) sejam enviados como Integers.
  - [ ] Validar formato do `customer_email` antes de enviar (opcional).
  - [ ] Tratar campos obrigatórios vs. opcionais.


- [ ] Mapeamento de Resposta
  - [ ] Parsear corretamente a estrutura JSON da resposta.
  - [ ] Converter/Parsear `subscription_amount` (String "R$ X,XX") para numérico, se necessário para cálculos.
  - [ ] Tratar campos que podem ser `null` (ex: `canceled_date`, `end_date_recurrent`, `plan.name`).


- [ ] Logs & Monitoramento
  - [ ] Registrar requisições e respostas (sucesso/falha).
  - [ ] Monitorar taxa de erros `4xx`/`5xx`.
  - [ ] Implementar rastreamento de requisições (request_id).


- [ ] Cache (Opcional)
  - [ ] Considerar cache local se as mesmas consultas forem feitas frequentemente.
  - [ ] Definir estratégias de invalidação de cache.
  - [ ] Respeitar cabeçalhos Cache-Control (se implementados futuramente).


- [ ] Testes
  - [ ] Criar testes unitários para mapeamento de resposta.
  - [ ] Implementar testes de integração cobrindo filtros, paginação e erros.
  - [ ] Verificar cenários de erro e exceção.


- [ ] Performance
  - [ ] Monitorar tempo de resposta.
  - [ ] Otimizar consultas com filtros apropriados.
  - [ ] Avaliar impacto de paginação em lotes.


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*


---


## 13. Glossário de Termos Técnicos


> **Resumo:** Definições claras dos principais termos técnicos utilizados neste documento.


| Termo                      | Definição                                                                                                |
| :------------------------- | :------------------------------------------------------------------------------------------------------- |
| `Assinatura`               | Representa um acordo de pagamento recorrente entre um cliente e um vendedor para acesso a um produto/serviço. |
| `Bearer Token`             | Credencial de segurança (token) enviada no cabeçalho `Authorization` para autenticar requisições à API.     |
| `Endpoint`                 | URL específica (`/api/v1/subscriptions/get`) onde a API recebe requisições para uma funcionalidade.       |
| `Paginação`                | Técnica usada pela API para dividir grandes conjuntos de resultados (assinaturas) em páginas menores (`page`). |
| `Recorrência`              | Frequência com que uma assinatura é cobrada (ex: Mensal, Anual). Definido por `recurrent_type_enum`.       |
| `Status da Assinatura`     | Estado atual da assinatura no seu ciclo de vida (ex: Ativa, Cancelada). Definido por `subscription_status_enum`. |
| `JSON (JavaScript Object Notation)` | Formato leve de troca de dados usado no corpo das requisições e respostas da API.                   |
| `POST`                     | Método HTTP usado por este endpoint para enviar dados (filtros) no corpo da requisição.                   |
| `cURL`                     | Ferramenta de linha de comando para transferir dados com URLs, usada aqui para exemplificar requisições API. |
| `API (Application Programming Interface)` | Conjunto de regras e protocolos que permite a comunicação entre diferentes sistemas de software. |
| `MRR (Monthly Recurring Revenue)` | Receita recorrente mensal, calculada com base nas assinaturas ativas e seus valores normalizados para ciclo mensal. |
| `Churn`                    | Taxa de cancelamento de assinaturas em um determinado período, importante para análise de retenção.       |
| `Idempotência`             | Propriedade onde múltiplas requisições idênticas têm o mesmo efeito que uma única requisição.             |
| `Rate Limit`               | Número máximo de requisições permitidas em um determinado período de tempo para evitar sobrecarga da API. |
| `Backoff Exponencial`      | Estratégia de retentativa onde o intervalo entre tentativas aumenta exponencialmente após falhas.         |
| `Webhook`                  | Mecanismo de notificação onde a API envia dados para uma URL configurada quando ocorrem eventos específicos. |
| `PII (Personally Identifiable Information)` | Dados pessoais que podem identificar um indivíduo, como email e nome completo.              |


*(Ref: PerfectPay Get Subscriptions, ID perfectpay_subscriptions_001)*