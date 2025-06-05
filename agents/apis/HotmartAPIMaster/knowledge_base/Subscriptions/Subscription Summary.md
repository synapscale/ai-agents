# API Hotmart - Assinaturas - Obter Sumário de Assinaturas (Subscription Summary)


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Assinaturas - Obter Sumário de Assinaturas (Subscription Summary) |
| **Identificador Interno** | hotmart_sub_001                                               |
| **Título Curto (Ref.)**   | Hotmart Get Subscription Summary                                |
| **Versão do Documento**   | 1.1.0                                                |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação                                          |
| **Fonte Original**        | Documentação Hotmart API                                        |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/v1/subscription/get-subscription-summary/ |
| **Status do Documento**   | Em Uso                                                          |
| **Ambiente de Referência**| Produção                                                        |
| **Idioma Original**       | Português (BR)                                                  |
| **Formato de Datas (API)**| Timestamp (milissegundos desde 1970-01-01 00:00:00 UTC)         |
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 2. Contexto
Este endpoint (`hotmart_sub_001`) fornece uma visão geral agregada do status atual de Assinaturas, Smart Installments e Smart Recovery na plataforma Hotmart. Ele detalha a situação da última recorrência e fornece informações que podem ser usadas para ações de retenção de clientes. **Importante:** Os dados retornados por este endpoint possuem uma **defasagem de até 24 horas**. Para informações em tempo real, deve-se utilizar o endpoint específico de "Obter Assinaturas". O endpoint abrange os três tipos de cobrança recorrente: Assinaturas padrão (acesso contínuo a produtos), Smart Installments (parcelamento em mercados específicos) e Smart Recovery (recuperação de vendas recusadas por saldo insuficiente).
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 3. Visão Geral da API/Endpoint(s)
O endpoint de Sumário de Assinaturas permite consultar, de forma paginada, informações consolidadas sobre as assinaturas vinculadas à conta. Retorna dados como status atual, tempo de vida, detalhes do plano, produto, oferta, informações da última recorrência (incluindo status e tipo de cobrança) e dados básicos do assinante. É ideal para análises de coorte, relatórios gerenciais e identificação de tendências ou grupos de assinantes que precisam de atenção especial (ex: em atraso, cancelados recentemente), ciente da defasagem de 24h. Os resultados podem ser filtrados por diversos parâmetros como produto, período de adesão ou código de assinante específico.
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 4. Detalhes Técnicos
### Endpoint de Sumário de Assinaturas
*   **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/subscriptions/summary`
*   **Método HTTP:** `GET`
*   **Autenticação:** Bearer Token. Requer um token de acesso válido no cabeçalho HTTP: `Authorization: Bearer :access_token`
*   **Content-Type:** `application/json` (para o cabeçalho da requisição)
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 5. Parâmetros de Entrada (Query Parameters)
| Parâmetro          | Descrição Detalhada | Tipo | Notas / Exemplo |
| :----------------- | :------------------ | :--- | :-------------- |
| `max_results`      | Define o número máximo de itens (assinaturas) a serem retornados por página. Se não informado, o sistema usará um valor padrão. Permite controlar o volume de dados retornados em cada chamada. | integer | O valor padrão e o máximo permitido variam conforme a API. Recomendado: entre 50 e 500. Ex: `max_results=500` |
| `page_token`       | Cursor utilizado para navegar entre as páginas de resultados. Permite percorrer conjuntos grandes de dados através de múltiplas chamadas, formando uma sequência ordenada. | string | Use o valor de `next_page_token` ou `prev_page_token` da resposta anterior para requisitar a página seguinte ou anterior. Ex: `page_token=05b60506b659c1c6e728db93eada6271e3adcfb4edf507b679874458e31577b3` |
| `product_id`       | Filtra as assinaturas para retornar apenas aquelas associadas a um produto específico. Útil para análises por produto ou para reduzir o volume de dados retornados. | integer | Deve ser o ID numérico (7 dígitos) do produto na Hotmart. Ex: `product_id=1234567` |
| `subscriber_code`  | Filtra para retornar a assinatura associada a um código de assinante específico. Ideal para consultas pontuais quando se conhece o código. | string | Código alfanumérico único que identifica a relação Assinatura-Assinante. Um mesmo comprador terá códigos diferentes para cada produto assinado. Ex: `subscriber_code=ABC12DEF` |
| `accession_date`   | Filtra assinaturas cuja data de adesão (início) seja igual ou posterior a esta data. Permite limitar a consulta a assinaturas criadas a partir de determinado momento. | long | Formato: Timestamp em milissegundos desde a época Unix (1970-01-01 00:00:00 UTC). **Padrão:** Data atual menos 30 dias, se não informado. Ex: `accession_date=1682910000000` (01/05/2023) |
| `end_accession_date` | Filtra assinaturas cuja data de adesão seja anterior a esta data. Usado em conjunto com `accession_date` para definir um intervalo temporal preciso. | long | Formato: Timestamp em milissegundos desde a época Unix UTC. Deve ser maior que `accession_date` para formar um intervalo válido. Ex: `end_accession_date=1696374925000` (03/10/2023) |
| `date_next_charge` | Filtra assinaturas com base na data da próxima cobrança agendada. Para assinaturas canceladas, este parâmetro considerará a última data de acesso. | long | Formato: Timestamp em milissegundos desde a época Unix UTC. **Padrão:** Data atual, se não informado. Útil para identificar assinaturas com renovação próxima. Ex: `date_next_charge=1700000000000` (14/11/2023) |
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Endpoint de Sumário de Assinaturas
#### 6.1.1 Estrutura Geral
| Campo         | Descrição Detalhada | Tipo   |
| :------------ | :------------------ | :----- |
| `items`       | Array contendo os objetos de sumário de cada assinatura encontrada, conforme os filtros aplicados. Pode ser vazio se nenhuma assinatura corresponder aos critérios. | array (object) |
| `page_info`   | Objeto contendo informações sobre a paginação dos resultados, incluindo tokens para navegação entre páginas e contagens. | object |


#### 6.1.2 Detalhes do Objeto `items` (cada elemento do array)
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `subscriber_code`   | Código alfanumérico único que identifica esta assinatura específica para este assinante. Um mesmo comprador terá códigos diferentes se assinar produtos distintos. | string | Uso: Identificação unívoca da relação assinante-assinatura. Ex: "ABC12DEF" |
| `subscription_id`   | Identificador numérico único da assinatura na plataforma Hotmart. Usado para referência interna do sistema. | integer | Ex: 1223334 |
| `status`            | Status atual da assinatura, indicando sua situação operacional. | string | Valores possíveis: `ACTIVE` (Ativa, em uso normal), `INACTIVE` (Inativa, ex: aguardando pagamento inicial), `DELAYED` (Atrasada, com pagamento pendente), `CANCELLED_BY_CUSTOMER` (Cancelada pelo Cliente), `CANCELLED_BY_SELLER` (Cancelada pelo Vendedor), `CANCELLED_BY_ADMIN` (Cancelada pelo Admin Hotmart), `STARTED` (Iniciada, ex: em período de trial), `OVERDUE` (Vencida, período de pagamento expirado). |
| `lifetime`          | Tempo de vida da assinatura em dias, calculado desde a data de adesão (`accession_date`). | integer | O cálculo depende do `status`: Para `ACTIVE`/`DELAYED`: dias até data atual; Para `INACTIVE`/`STARTED`: 0 dias; Para status `CANCELLED_*`: dias até a data do cancelamento; Para `OVERDUE`: dias até a data do vencimento. Ex: 200 |
| `accession_date`    | Data e hora em que o acesso ao conteúdo da assinatura foi liberado inicialmente (data de adesão). | integer (long) | Formato: Timestamp em milissegundos (UTC). Ex: 1694113403000 (07/09/2023) |
| `end_accession_date`| Data e hora em que o assinante solicitou o cancelamento da assinatura. Presente apenas em assinaturas canceladas. | integer (long) | Formato: Timestamp em milissegundos (UTC). Será nulo para assinaturas não canceladas. Ex: 1694113503000 (07/09/2023) |
| `trial`             | Indica se a assinatura possui ou possuiu um período de teste (trial). | boolean | `true` se a assinatura incluiu período de trial, `false` se foi iniciada diretamente com pagamento. |
| `plan`              | Objeto contendo detalhes do plano associado à assinatura na última recorrência. | object | Ver Seção 6.1.3 para detalhamento dos campos. |
| `product`           | Objeto contendo detalhes do produto associado à assinatura. | object | Ver Seção 6.1.4 para detalhamento dos campos. |
| `offer`             | Objeto contendo detalhes da oferta associada à assinatura na última recorrência. | object | Ver Seção 6.1.5 para detalhamento dos campos. |
| `last_recurrency`   | Objeto contendo informações detalhadas sobre a última recorrência processada para esta assinatura. | object | Ver Seção 6.1.6 para detalhamento dos campos. |
| `unpaid_recurrencies` | Array de objetos listando as recorrências desta assinatura que não foram pagas. | array (object) | Pode estar vazio se não houver recorrências não pagas. Ver Seção 6.1.7 para detalhamento dos campos. |
| `subscriber`        | Objeto contendo informações básicas do assinante. | object | Ver Seção 6.1.8 para detalhamento dos campos. |


#### 6.1.3 Detalhes do Objeto `plan`
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `name`              | Nome do plano que estava vigente na última recorrência. Pode ser diferente do plano original se o assinante o trocou após a adesão. | string | Ex: "Plano Premium Mensal", "Plano Gold Anual" |
| `recurrency_period` | Duração, em dias, do período de recorrência do plano vigente na última cobrança. Define o intervalo entre cobranças sucessivas. | integer | Valores comuns: 30 (mensal), 90 (trimestral), 180 (semestral), 365 (anual). Ex: 180 |


#### 6.1.4 Detalhes do Objeto `product`
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `id`                | Identificador numérico único do produto na Hotmart. | integer | Normalmente um número de 7 dígitos que identifica o produto no ecossistema Hotmart. Ex: 12345 |
| `name`              | Nome do produto de assinatura, conforme cadastrado na plataforma Hotmart. | string | Nome comercial do produto visível para clientes e gestores. Ex: "Curso de Marketing Digital Avançado" |


#### 6.1.5 Detalhes do Objeto `offer`
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `code`              | Código identificador da oferta (preço/condições) que estava vigente na última recorrência. Pode mudar se o assinante alterou o plano/oferta após a adesão inicial. | string | Código alfanumérico único da oferta no sistema Hotmart. Ex: "o1c97lta" |


#### 6.1.6 Detalhes do Objeto `last_recurrency`
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `number`            | Número sequencial da última recorrência processada (contagem de períodos/cobranças da assinatura). | integer | Se `STARTED` ou `INACTIVE`, será 1. Se `CANCELLED` ou `OVERDUE`, é a recorrência final. Se `ACTIVE` ou `DELAYED`, é a recorrência atual. Ex: 2 |
| `request_date`      | Data e hora em que a última recorrência se iniciou (início do período de utilização do serviço). Para assinaturas vigentes, corresponde à primeira transação de cobrança da recorrência atual. | integer (long) | Formato: Timestamp em milissegundos (UTC). Ex: 1694113403000 (07/09/2023) |
| `status`            | Status do pagamento da última recorrência, indicando se foi bem-sucedido ou qual o problema encontrado. | string | Valores possíveis: `PAID` (Paga com sucesso), `NOT_PAID` (Pagamento não realizado ou falhou), `REFUNDED` (Valor reembolsado ao cliente), `CHARGEBACK` (Pagamento contestado pelo cliente junto à operadora de cartão), `CLAIMED` (Em processo de disputa/contestação). Ex: "NOT_PAID" |
| `transaction_number`| Quantidade de transações de cobrança (tentativas) realizadas para esta última recorrência. Valor maior que 1 indica múltiplas tentativas de cobrança. | integer | Útil para identificar assinaturas com dificuldades de pagamento. Ex: 1 |
| `billing_type`      | Indica o tipo específico de cobrança recorrente aplicada a esta assinatura. Cada assinatura só pode ter um tipo. | string | Valores possíveis: `SUBSCRIPTION` (Assinatura padrão, originada de oferta de produto de assinatura), `SMART_INSTALLMENT` (Parcelamento Inteligente, permite parcelamento em países sem suporte nativo), `SMART_RECOVERY` (Recuperação Inteligente, criada a partir de venda recusada por saldo insuficiente). Ex: "SMART_INSTALLMENT" |


#### 6.1.7 Detalhes do Objeto `unpaid_recurrencies` (cada elemento do array)
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `number`            | Número sequencial da recorrência que não foi paga. Identifica precisamente qual período/cobrança está pendente. | integer | Corresponde ao número da recorrência na sequência temporal da assinatura. Ex: 2 |
| `charge_date`       | Data e hora em que a cobrança desta recorrência não paga foi tentada. | integer (long) | Formato: Timestamp em milissegundos (UTC). Útil para estratégias de recobrança. Ex: 1694113403000 (07/09/2023) |


#### 6.1.8 Detalhes do Objeto `subscriber`
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `name`              | Nome completo do assinante (comprador), conforme registrado na plataforma Hotmart. | string | Pode conter primeiro nome e sobrenome. Ex: "John Doe" |
| `id`                | Identificador numérico único do usuário comprador na plataforma Hotmart. | integer | Este ID é único para cada usuário na plataforma, independentemente de quantos produtos assine. Ex: 12345 |
| `email`             | Endereço de e-mail do assinante, usado para comunicações e identificação. | string | Formato de email padrão. Ex: "john.doe@email.com" |


#### 6.1.9 Detalhes do Objeto `page_info`
| Campo Aninhado      | Descrição Detalhada | Tipo | Notas |
| :------------------ | :------------------ | :--- | :---- |
| `next_page_token`   | Token (cursor) para requisitar a próxima página de resultados. | string | **Ausente** se esta for a última página de resultados. Use este valor no parâmetro `page_token` da próxima requisição GET. Ex: "05b60506b659c1c6e728db93eada6271e3adcfb4edf507b679874458e31577b3" |
| `prev_page_token`   | Token (cursor) para requisitar a página anterior de resultados. | string | **Ausente** se esta for a primeira página de resultados. Use este valor no parâmetro `page_token` da próxima requisição GET. Ex: "cf1fg8bd082e2864069035c057eca0bac7eb5d604719c5a76e80f0933f49c217" |
| `results_per_page`  | Número de itens (assinaturas) retornados nesta página específica. | integer | Pode ser menor que o `max_results` solicitado se for a última página ou se houver poucos resultados. Ex: 100 |
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 7. Exemplos de Requisição e Resposta
### Endpoint de Sumário de Assinaturas
#### 7.1.1 Exemplo de Requisição (cURL)
```bash
# Exemplo buscando assinaturas de um produto específico, com adesão entre duas datas, máximo 100 por página
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/subscriptions/summary?product_id=1234567&accession_date=1682910000000&end_accession_date=1696374925000&max_results=100' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer SEU_ACCESS_TOKEN_AQUI'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 200 OK)
```json
{
  "items": [
    {
      "subscriber_code": "ABC12DEF",
      "subscription_id": 1223334,
      "status": "ACTIVE",
      "lifetime": 200,
      "accession_date": 1694113403000,
      "end_accession_date": null,
      "trial": true,
      "plan": {
        "name": "Plano Gold Anual",
        "recurrency_period": 365
      },
      "product": {
        "name": "Acesso VIP Plataforma",
        "id": 1234567
      },
      "offer": {
        "code": "oferta_anual_vip"
      },
      "last_recurrency": {
        "number": 1,
        "request_date": 1694113403000,
        "status": "PAID",
        "transaction_number": 1,
        "billing_type": "SUBSCRIPTION"
      },
      "unpaid_recurrencies": [],
      "subscriber": {
        "name": "Maria Silva",
        "id": 98765,
        "email": "maria.silva@email.com"
      }
    },
    {
      "subscriber_code": "XYZ98ABC",
      "subscription_id": 7654321,
      "status": "DELAYED",
      "lifetime": 45,
      "accession_date": 1691607803000,
      "end_accession_date": null,
      "trial": false,
      "plan": {
        "name": "Plano Mensal Básico",
        "recurrency_period": 30
      },
      "product": {
        "name": "Acesso VIP Plataforma",
        "id": 1234567
      },
      "offer": {
        "code": "oferta_mensal_basica"
      },
      "last_recurrency": {
        "number": 2,
        "request_date": 1694199803000,
        "status": "NOT_PAID",
        "transaction_number": 3,
        "billing_type": "SUBSCRIPTION"
      },
      "unpaid_recurrencies": [
        {
          "number": 2,
          "charge_date": 1694199803000
        }
      ],
      "subscriber": {
        "name": "João Santos",
        "id": 87654,
        "email": "joao.santos@email.com"
      }
    }
  ],
  "page_info": {
    "results_per_page": 2,
    "next_page_token": "abcdef123456789abcdef123456789abcdef123456789abcdef123456789abcd",
    "prev_page_token": null
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro 401 Unauthorized)
```json
{
  "code": "UNAUTHORIZED",
  "message": "Authentication failed. Please check your credentials and try again."
}
```
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral Provável | Notas |
| :--------------------- | :----------------------- | :---- |
| `200 OK`               | Requisição bem-sucedida. A resposta contém os dados solicitados (pode ser uma lista vazia se nenhum item corresponder aos filtros). | É o único código de sucesso retornado por este endpoint. |
| `400 Bad Request`      | Erro na requisição do cliente. Pode ser devido a parâmetros inválidos (formato, tipo, valor), ausência de parâmetros obrigatórios (se houver, embora todos aqui sejam opcionais), ou sintaxe incorreta. | Verifique especialmente o formato dos timestamps (milissegundos), intervalos de datas e tipos de dados numéricos. |
| `401 Unauthorized`     | Falha na autenticação. O `access_token` fornecido no cabeçalho `Authorization` está ausente, inválido, expirado ou não tem permissão para acessar este recurso. | Regenere o token de acesso e verifique se está sendo enviado corretamente no formato `Bearer TOKEN`. |
| `403 Forbidden`        | Acesso negado. O token é válido, mas a conta associada não tem permissão para realizar esta operação específica. | Verificar se a conta possui permissões para consultar assinaturas ou se há restrições no ambiente. |
| `404 Not Found`        | O endpoint solicitado (`/payments/api/v1/subscriptions/summary`) não foi encontrado. Geralmente indica um erro na URL base ou no caminho do endpoint. | Confirmar a URL completa, incluindo o domínio e caminho do endpoint. |
| `429 Too Many Requests`| Limite de taxa (Rate Limit) excedido. Muitas requisições foram feitas em um curto período. | Implementar estratégia de backoff exponencial e aguardar antes de tentar novamente. |
| `500 Internal Server Error` | Erro inesperado no servidor da Hotmart ao processar a requisição. | Tente novamente mais tarde. Se o erro persistir, abra um ticket com o suporte Hotmart incluindo detalhes da requisição (sem dados sensíveis). |
| `503 Service Unavailable`| O serviço está temporariamente indisponível, possivelmente por manutenção programada ou sobrecarga. | Tente novamente após alguns minutos. Consulte status.hotmart.com para verificar incidentes conhecidos. |


*(Nota: A documentação original não detalha códigos de erro específicos. A lista acima representa códigos HTTP comuns e suas interpretações prováveis neste contexto.)*
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1.  **Obter todos os assinantes ATIVOS de um produto específico:**
    *   Objetivo: Listar assinantes ativos para análise de base ou comunicação.
    *   Como Fazer: Use `product_id={ID_PRODUTO}`. Filtre a resposta pelo campo `status` igual a `"ACTIVE"`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
2.  **Identificar assinaturas em ATRASO (DELAYED) para recuperação:**
    *   Objetivo: Encontrar assinaturas com pagamento pendente para ações de retenção/cobrança.
    *   Como Fazer: Requisite os dados (possivelmente filtrando por produto) e filtre a resposta pelo campo `status` igual a `"DELAYED"`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
3.  **Verificar assinaturas CANCELADAS nos últimos 30 dias:**
    *   Objetivo: Analisar taxa de churn recente e motivos (se possível inferir).
    *   Como Fazer: Use `accession_date` (para limitar o volume inicial, opcional) e `end_accession_date` para filtrar o período de *cancelamento*. Filtre a resposta por `status` contendo `"CANCELLED_"`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
4.  **Avaliar conversão pós-TRIAL:**
    *   Objetivo: Analisar quantos usuários que iniciaram com trial se tornaram pagantes.
    *   Como Fazer: Requisite assinaturas (filtrando por produto/data, se necessário). Analise itens com `trial=true` e verifique seus `status` atuais (ex: `ACTIVE`, `CANCELLED_`).
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
5.  **Identificar assinantes de LONGO PRAZO (ex: > 1 ano):**
    *   Objetivo: Reconhecer clientes fiéis para ações de engajamento ou programas VIP.
    *   Como Fazer: Requisite os dados e filtre a resposta por `lifetime > 365`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
6.  **Localizar assinaturas com RECORRÊNCIAS NÃO PAGAS:**
    *   Objetivo: Identificar assinaturas com histórico de falha de pagamento para análise.
    *   Como Fazer: Requisite os dados e filtre a resposta verificando se o array `unpaid_recurrencies` não está vazio.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
7.  **Consultar o SUMÁRIO de uma assinatura específica pelo CÓDIGO:**
    *   Objetivo: Obter rapidamente o status e detalhes de uma assinatura conhecida.
    *   Como Fazer: Use o parâmetro `subscriber_code={CODIGO_ASSINANTE}` na requisição.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
8.  **Listar assinaturas por DATA DE PRÓXIMA COBRANÇA:**
    *   Objetivo: Identificar assinaturas com renovação próxima (ex: para comunicação prévia).
    *   Como Fazer: Use o parâmetro `date_next_charge` para definir um intervalo de datas de próxima cobrança.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
9.  **Analisar distribuição de TIPOS DE COBRANÇA (Billing Type):**
    *   Objetivo: Entender a proporção entre Assinaturas, Smart Installments e Smart Recovery.
    *   Como Fazer: Requisite os dados e agrupe/conte os resultados pelo campo `last_recurrency.billing_type`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
10. **Identificar assinaturas CANCELADAS PELO VENDEDOR:**
    *   Objetivo: Avaliar cancelamentos iniciados internamente.
    *   Como Fazer: Requisite os dados e filtre a resposta por `status` igual a `"CANCELLED_BY_SELLER"`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
11. **Comparar retenção entre diferentes PLANOS:**
    *   Objetivo: Analisar qual plano tem melhor desempenho em termos de retenção.
    *   Como Fazer: Requisite dados (possivelmente por produto) e agrupe por `plan.name`, analisando a distribuição de `status` (ativos vs. cancelados) para cada plano.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
12. **Verificar assinaturas com MÚLTIPLAS TENTATIVAS na última recorrência:**
    *   Objetivo: Identificar assinaturas que exigiram mais de uma tentativa de cobrança recentemente.
    *   Como Fazer: Requisite os dados e filtre a resposta por `last_recurrency.transaction_number > 1`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
13. **Calcular TEMPO MÉDIO DE VIDA (Lifetime) das assinaturas canceladas:**
    *   Objetivo: Entender a duração média da relação com o cliente antes do cancelamento.
    *   Como Fazer: Requisite os dados, filtre por `status` contendo `"CANCELLED_"`, e calcule a média do campo `lifetime`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
14. **Identificar OFERTAS com maior número de assinantes ativos:**
    *   Objetivo: Determinar quais ofertas geram mais assinantes pagantes.
    *   Como Fazer: Requisite os dados, filtre por `status="ACTIVE"`, e agrupe/conte por `offer.code`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
15. **Monitorar STATUS DE PAGAMENTO da última recorrência (NOT_PAID):**
    *   Objetivo: Focar em assinaturas cuja última tentativa de pagamento falhou.
    *   Como Fazer: Requisite os dados e filtre a resposta por `last_recurrency.status` igual a `"NOT_PAID"`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
16. **Listar assinaturas criadas (ADESÃO) em um intervalo específico:**
    *   Objetivo: Analisar o volume de novas assinaturas em um período.
    *   Como Fazer: Use os parâmetros `accession_date` e `end_accession_date` para definir o intervalo de datas de adesão desejado.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
17. **Identificar assinaturas com PERÍODO DE RECORRÊNCIA mais longo (ex: anual):**
    *   Objetivo: Analisar a preferência por planos de maior duração.
    *   Como Fazer: Requisite os dados e analise/filtre pelo valor de `plan.recurrency_period` (ex: `plan.recurrency_period >= 365`).
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
18. **Exportar lista de EMAILS de assinantes ativos para comunicação:**
    *   Objetivo: Obter contatos para campanhas (respeitando LGPD/GDPR).
    *   Como Fazer: Requisite os dados, filtre por `status="ACTIVE"`, e extraia o campo `subscriber.email` de cada item.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
19. **Analisar taxa de assinaturas VENCIDAS (OVERDUE):**
    *   Objetivo: Avaliar o impacto de assinaturas que passaram do prazo de pagamento sem cancelamento formal.
    *   Como Fazer: Requisite os dados e calcule a proporção de itens com `status="OVERDUE"` em relação ao total.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
20. **Verificar distribuição de assinaturas ativas por PRODUTO:**
    *   Objetivo: Identificar quais produtos concentram a maior base de assinantes ativos.
    *   Como Fazer: Requisite os dados (sem filtro de produto), filtre por `status="ACTIVE"`, e agrupe/conte por `product.id` ou `product.name`.
    *(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 10. Notas Adicionais
*   **DEFASAGEM DE DADOS (CRÍTICO):** Lembre-se sempre que os dados retornados por este endpoint **NÃO SÃO EM TEMPO REAL**. Eles podem ter **até 24 horas de atraso**. Para operações que exigem dados instantâneos (ex: verificar acesso imediato), use outros endpoints da API Hotmart.
*   **Paginação:** A API utiliza paginação baseada em cursor (`page_token`). É essencial implementar a lógica de paginação para recuperar todos os resultados se o volume for grande. Verifique sempre a presença de `next_page_token` na resposta e faça chamadas subsequentes até que ele não seja mais retornado (última página).
*   **Tipos de Cobrança:** O campo `last_recurrency.billing_type` é crucial para distinguir entre assinaturas padrão (`SUBSCRIPTION`), parcelamentos (`SMART_INSTALLMENT`) e recuperações de vendas (`SMART_RECOVERY`). Cada identificador de venda recorrente só pode estar associado a um destes tipos.
*   **Cálculo de Lifetime:** A interpretação do campo `lifetime` depende diretamente do `status` atual da assinatura. Para status `ACTIVE`/`DELAYED` é contabilizado até a data atual; para `INACTIVE`/`STARTED` o valor será zero; para status de cancelamento (`CANCELLED_*`) é contado até a data do cancelamento; para `OVERDUE` é até a data de vencimento.
*   **Rate Limits:** Embora não explicitamente documentado na fonte original, espere limites de taxa (rate limits). Implemente tratamento adequado (ex: backoff exponencial) para o código de status `429 Too Many Requests` e limite o número de requisições simultâneas.
*   **Filtros Complementares:** Alguns filtros mais complexos (ex: por status específico) precisam ser aplicados após receber a resposta, já que não são suportados como parâmetros de consulta. Considere implementar uma camada de filtros em memória para otimizar análises recorrentes.
*   **Fusos Horários:** Todos os timestamps são fornecidos em UTC (milissegundos desde a época). Lembre-se de fazer as conversões necessárias ao apresentar datas e horas para usuários em diferentes fusos horários.
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sub_001",
  "api_provider": "Hotmart",
  "api_product_area": "Assinaturas",
  "endpoint_focus": ["Consultar Sumário de Assinaturas", "Listar Assinaturas", "Analisar Status de Assinaturas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Assinatura", "Assinante", "Produto", "Plano", "Oferta", "Recorrência", "Pagamento"],
  "context_level": ["intermediate"],
  "topic_cluster": ["pagamentos", "assinaturas", "recorrência", "gestão de clientes", "relatórios"],
  "db_relations": {
    "tables": ["subscriptions", "subscribers", "products", "plans", "offers", "recurrencies", "transactions"],
    "schemas": ["payments_api", "customer_data"]
  },
  "related_concepts": ["Cobrança Recorrente", "Churn Rate", "Customer Lifetime Value (CLV)", "Smart Installment", "Smart Recovery", "Retenção de Clientes", "Paginação API", "Timestamp Unix"],
  "question_embeddings": [
    "Como obter um resumo das minhas assinaturas na Hotmart?",
    "Qual API da Hotmart lista assinaturas com status e última recorrência?",
    "Como verificar assinaturas canceladas ou atrasadas na Hotmart via API?",
    "O que significa o status DELAYED ou OVERDUE em assinaturas Hotmart?",
    "Como filtrar assinaturas Hotmart por produto ou data de adesão?",
    "Qual a diferença entre Assinatura, Smart Installment e Smart Recovery na API Hotmart?",
    "Como usar a paginação (page_token) na API de sumário de assinaturas Hotmart?",
    "Os dados da API de sumário de assinaturas Hotmart são em tempo real?"
  ],
  "reasoning_pathways": ["status-analysis", "payment-history-check", "churn-calculation-support", "cohort-analysis-support", "filtering-pagination"],
  "typical_usage_frequency": "Média/Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*


---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação: Implementar obtenção e uso seguro do Bearer Token.
- [ ] Tratamento de Datas: Converter/validar timestamps em milissegundos (UTC) nos parâmetros de entrada.
- [ ] Paginação: Implementar loop para seguir `next_page_token` até que seja nulo, tratando `prev_page_token` se necessário.
- [ ] Tratamento de Erros: Implementar lógica para tratar códigos 4xx/5xx (especialmente 401, 429, 500). Incluir retentativas com backoff para 429/5xx.
- [ ] Validação de Entrada: Validar tipos e formatos dos parâmetros opcionais antes da chamada.
- [ ] Mapeamento de Resposta: Mapear a estrutura JSON para objetos/estruturas de dados internas.
- [ ] Logs & Monitoramento: Registrar chamadas, sucessos, falhas e latência.
- [ ] Cache: Considerar cache **ciente da defasagem de 24h**. Cache de curta duração pode ser útil para evitar chamadas repetidas idênticas em um curto espaço de tempo.
- [ ] Testes: Cobrir cenários com e sem filtros, paginação, diferentes status, dados vazios, erros esperados.
- [ ] Consciência da Defasagem: Garantir que a aplicação ou usuário final esteja ciente da defasagem de 24h dos dados.
*(Ref: Hotmart Get Subscription Summary, ID hotmart_subscriptionsummary_001)*