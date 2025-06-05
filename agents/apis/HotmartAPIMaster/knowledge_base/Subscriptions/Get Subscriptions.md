# API Hotmart - Assinaturas - Get Subscriptions   


## 1. Título e Identificação


| Campo                     | Valor                                                                 |
| :------------------------ | :-------------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Assinaturas - Get Subscriptions                       |
| **Identificador Interno** | `hotmart_subscriptions_001`                                         |
| **Título Curto (Ref.)**   | Hotmart Get Subscriptions                                           |
| **Versão do Documento**   | 1.1.0 (Atualizado com correções)                                     |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Integração                                                |
| **Fonte Original**        | [Hotmart API Documentation](https://developers.hotmart.com/docs/pt-BR/v1/subscription/get-subscribers/) |
| **URL de Referência**     | https://developers.hotmart.com/payments/api/v1/subscriptions       |
| **Status do Documento**   | Em Uso                                                               |
| **Ambiente de Referência**| Produção                                                              |
| **Idioma Original**       | Português (BR)                                                      |
| **Formato de Datas (API)**| Timestamp (ms)                                                      |


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 2. Contexto


Este documento descreve a API para obter assinaturas na área de Assinaturas do provedor Hotmart. O endpoint "Obter Assinaturas" fornece informações detalhadas sobre as assinaturas e assinantes, permitindo gerenciar e monitorar status, planos associados e transações. O ID Interno deste documento é: `hotmart_subscriptions_001`.


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 3. Visão Geral da API/Endpoint(s)


Esta API permite:
*   Listar assinaturas ativas, inativas, canceladas ou atrasadas.
*   Filtrar assinaturas por critérios como ID do produto, nome do plano, data de início e status.
*   Obter detalhes de cada assinatura, incluindo informações do assinante, plano e transação.


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 4. Detalhes Técnicos


### Endpoint: `/subscriptions`


*   **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/subscriptions`
*   **Método HTTP:** `GET`
*   **Autenticação:** `Authorization: Bearer :access_token` (enviado no header)


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 5. Parâmetros de Entrada


| Parâmetro              | Descrição                                                                 | Tipo     | Notas/Exemplo                                                                 |
| :--------------------- | :-------------------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------- |
| `max_results`        | Número máximo de itens por página                                        | integer  | Ex: `10`                                                                      |
| `page_token`         | Cursor para paginação                                                     | string   | Ex: `05b60506b659c1c6e728db93eada6271e3adcfb4edf507b679874458e31577b3`     |
| `product_id`         | ID do produto de assinatura                                             | integer  | Ex: `123456`                                                                  |
| `plan`               | Nome do plano de assinatura                                            | string   | Ex: `Plano Mensal`                                                            |
| `plan_id`            | ID do plano de assinatura                                              | string   | Ex: `726420`                                                                   |
| `accession_date`     | Data de início da assinatura em milissegundos                          | long     | Ex: `1577847600`                                                               |
| `end_accession_date` | Data de término da assinatura em milissegundos                          | long     | Ex: `1641005999`                                                                |
| `status`             | Status da assinatura                                                   | string   | Valores: `ACTIVE`, `INACTIVE`, `DELAYED`, `CANCELLED_BY_CUSTOMER`, `CANCELLED_BY_SELLER`, `CANCELLED_BY_ADMIN`, `STARTED`, `OVERDUE` |
| `subscriber_code`   | Código exclusivo do assinante                                          | string   | Ex: `ABC12DEF`                                                                  |
| `subscriber_email`  | Email do assinante                                                     | string   | Ex: `assinante@email.com.br`                                                   |
| `transaction`       | Identificador único da transação                                       | string   | Ex: `HP17715690036014`                                                            |
| `trial`              | Indica se a assinatura tem período de teste                             | boolean  | Ex: `true` ou `false`                                                            |
| `cancelation_date`   | Data de cancelamento da assinatura em milissegundos                    | long     | Ex: `1641005999`                                                                |
| `end_cancelation_date`| Data limite para cancelamentos em milissegundos                        | long     | Ex: `1641005999`                                                                |
| `date_next_charge`   | Data do próximo pagamento em milissegundos                            | long     | Ex: `1580558059`                                                                |
| `end_date_next_charge`| Data limite para o próximo pagamento em milissegundos                | long     | Ex: `1580558059`                                                                |


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)


### Estrutura Geral


| Campo               | Descrição                                                                 | Tipo       |
| :------------------ | :-------------------------------------------------------------------------- | :--------- |
| `subscriber_code`  | Código exclusivo do assinante                                             | string     |
| `subscription_id` | ID da assinatura                                                          | integer    |
| `status`           | Status da assinatura                                                     | string     |
| `accession_date`   | Data de início da assinatura                                            | long       |
| `end_accession_date`| Data de término da assinatura                                           | long       |
| `request_date`     | Data da criação da assinatura                                           | long       |
| `date_next_charge`  | Data do próximo pagamento                                               | long       |
| `trial`            | Indica se a assinatura tem período de teste                             | boolean    |
| `transaction`      | Identificador único da transação                                         | string     |
| `plan`             | Detalhes do plano                                                       | object     |
| `product`          | Detalhes do produto                                                     | object     |
| `price`            | Preço da assinatura                                                      | object     |
| `subscriber`       | Detalhes do assinante                                                   | object     |
| `page_info`        | Informações de paginação                                                 | object     |


### Detalhes do Objeto `plan`


| Campo               | Descrição                                                                 | Tipo       |
| :------------------ | :-------------------------------------------------------------------------- | :--------- |
| `name`             | Nome do plano                                                            | string     |
| `id`               | ID do plano                                                              | integer    |
| `recurrency_period`| Periodicidade de cobrança                                                | integer    |
| `max_charge_cycles` | Número máximo de cobranças                                               | integer    |


### Detalhes do Objeto `product`


| Campo               | Descrição                                                                 | Tipo       |
| :------------------ | :-------------------------------------------------------------------------- | :--------- |
| `id`               | ID do produto                                                            | integer    |
| `name`             | Nome do produto                                                           | string     |
| `ucode`            | Identificação externa do produto                                           | string     |


### Detalhes do Objeto `price`


| Campo               | Descrição                                                                 | Tipo       |
| :------------------ | :-------------------------------------------------------------------------- | :--------- |
| `value`            | Valor do preço                                                            | float      |
| `currency_code`   | Código da moeda                                                           | string     |


### Detalhes do Objeto `subscriber`


| Campo               | Descrição                                                                 | Tipo       |
| :------------------ | :-------------------------------------------------------------------------- | :--------- |
| `name`             | Nome do assinante                                                         | string     |
| `email`            | Email do assinante                                                        | string     |
| `ucode`            | Identificação externa do assinante                                         | string     |


### Detalhes do Objeto `page_info`


| Campo                      | Descrição                                                                 | Tipo       |
| :------------------------- | :-------------------------------------------------------------------------- | :--------- |
| `total_results`           | Total de itens na lista                                                  | integer    |
| `next_page_token`         | Token para a próxima página                                             | string     |
| `prev_page_token`         | Token para a página anterior                                             | string     |
| `results_per_page`        | Número de itens por página                                               | integer    |


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 7. Exemplos de Requisição e Resposta


### Exemplo de Requisição (cURL)


```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/subscriptions?status=ACTIVE&max_results=10' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json'
```


### Exemplo de Resposta (JSON - Sucesso 2xx)


```json
{
  "items": [
    {
      "subscriber_code": "ABC12DEF",
      "subscription_id": 123456,
      "status": "ACTIVE",
      "accession_date": 1577847600,
      "end_accession_date": 1641005999,
      "request_date": 1577847600,
      "date_next_charge": 1580558059,
      "trial": false,
      "transaction": "HP16616613605324",
      "plan": {
        "name": "Plano Mensal",
        "id": 726420,
        "recurrency_period": 30,
        "max_charge_cycles": 6
      },
      "product": {
        "id": 123456,
        "name": "Produto de Assinatura",
        "ucode": "12a34bcd-56e7-4847-fg89-h1i23j4567l8"
      },
      "price": {
        "value": 123.45,
        "currency_code": "BRL"
      },
      "subscriber": {
        "name": "Nome do Assinante",
        "email": "assinante@email.com.br",
        "ucode": "10a98bcd-76e5-4321-fg09-h8i76j5432l1"
      }
    }
  ],
  "page_info": {
    "total_results": 30,
    "next_page_token": "05b60506b659c1c6e728db93eada6271e3adcfb4edf507b679874458e31577b3",
    "prev_page_token": "cf1fg8bd082e2864069035c057eca0bac7eb5d604719c5a76e80f0933f49c217",
    "results_per_page": 10
  }
}
```


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 8. Códigos de Status e Tratamento de Erros


| Status Code            | Descrição                                                                 |
| :--------------------- | :-------------------------------------------------------------------------- |
| `200 OK`               | Requisição realizada com sucesso.                                         |
| `400 Bad Request`     | Erro na requisição (parâmetros, formato).                                   |
| `401 Unauthorized`    | Falha na autenticação.                                                   |
| `404 Not Found`        | Recurso não encontrado.                                                  |
| `429 Too Many Requests`| Limite de requisições excedido.                                            |
| `500 Internal Server Error` | Erro interno no servidor da API.                                      |


### Exemplo de Resposta de Erro


**401 - Unauthorized:**
```json
{
  "error": "invalid_token",
  "error_description": "Token de acesso inválido ou expirado."
}
```


**404 - Not Found:**
```json
{
  "error": "resource_not_found",
  "error_description": "Recurso não encontrado."
}
```


**500 - Internal Server Error:**
```json
{
  "error": "INTERNAL_SERVER_ERROR",
  "error_description": "Erro interno no servidor."
}
```


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 9. Casos de Uso Comuns (20 Exemplos Específicos)


1.  **Listar todas as assinaturas ativas**
    *   Objetivo: Obter uma lista de todas as assinaturas que estão ativas.
    *   Como Fazer: Utilizar o parâmetro `status=ACTIVE` na requisição.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
2.  **Filtrar assinaturas por ID do produto**
    *   Objetivo: Obter assinaturas associadas a um produto específico.
    *   Como Fazer: Utilizar o parâmetro `product_id={id_do_produto}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
3.  **Obter detalhes de uma assinatura específica**
    *   Objetivo: Visualizar informações detalhadas de uma assinatura.
    *   Como Fazer: Utilizar o parâmetro `subscriber_code={codigo_do_assinante}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
4.  **Listar assinaturas com período de teste**
    *   Objetivo: Filtrar assinaturas que incluem um período de teste.
    *   Como Fazer: Utilizar o parâmetro `trial=true`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
5.  **Obter assinaturas canceladas pelo cliente**
    *   Objetivo: Listar assinaturas canceladas pelo cliente.
    *   Como Fazer: Utilizar o parâmetro `status=CANCELLED_BY_CUSTOMER`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
6.  **Filtrar assinaturas por data de início**
    *   Objetivo: Obter assinaturas iniciadas após uma data específica.
    *   Como Fazer: Utilizar o parâmetro `accession_date={data_em_milissegundos}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
7.  **Listar assinaturas próximas de vencer**
    *   Objetivo: Identificar assinaturas com data de cobrança próxima.
    *   Como Fazer: Utilizar o parâmetro `date_next_charge` com uma faixa de datas.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
8.  **Obter assinaturas de um plano específico**
    *   Objetivo: Filtrar assinaturas baseadas no nome do plano.
    *   Como Fazer: Utilizar o parâmetro `plan={nome_do_plano}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
9.  **Gerenciar a paginação de resultados**
    *   Objetivo: Navegar entre as páginas de resultados.
    *   Como Fazer: Utilizar os parâmetros `page_token` e `max_results`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
10. **Atualizar lista de assinaturas**
    *   Objetivo: Atualizar a lista de assinaturas para refletir as mais recentes.
    *   Como Fazer: Realizar uma nova requisição sem parâmetros de filtro.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
11. **Filtrar assinaturas por email do assinante**
    *   Objetivo: Encontrar assinaturas associadas a um email específico.
    *   Como Fazer: Utilizar o parâmetro `subscriber_email={email}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
12. **Listar assinaturas em período de teste**
    *   Objetivo: Identificar todas as assinaturas atualmente em período de teste.
    *   Como Fazer: Utilizar o parâmetro `trial=true`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
13. **Obter histórico de assinaturas canceladas**
    *   Objetivo: Listar todas as assinaturas que foram canceladas.
    *   Como Fazer: Utilizar o parâmetro `status=CANCELLED_BY_SELLER`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
14. **Filtrar assinaturas por data de término**
    *   Objetivo: Obter assinaturas que terminarão após uma data específica.
    *   Como Fazer: Utilizar o parâmetro `end_accession_date={data_em_milissegundos}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
15. **Gerenciar assinantes inativos**
    *   Objetivo: Listar assinantes que estão inativos.
    *   Como Fazer: Utilizar o parâmetro `status=INACTIVE`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
16. **Obter assinaturas com transações específicas**
    *   Objetivo: Filtrar assinaturas baseadas em um identificador de transação.
    *   Como Fazer: Utilizar o parâmetro `transaction={id_da_transacao}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
17. **Listar assinaturas atrasadas**
    *   Objetivo: Identificar assinaturas que estão atrasadas.
    *   Como Fazer: Utilizar o parâmetro `status=OVERDUE`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
18. **Filtrar assinaturas por código do assinante**
    *   Objetivo: Encontrar uma assinatura específica usando o código do assinante.
    *   Como Fazer: Utilizar o parâmetro `subscriber_code={codigo}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
19. **Obter assinaturas com cobrança recorrente**
    *   Objetivo: Listar assinaturas que têm cobrança recorrente.
    *   Como Fazer: Utilizar o parâmetro `max_charge_cycles={numero_de_cobranças}`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*
20. **Gerenciar limites de requisições**
    *   Objetivo: Monitorar e gerenciar o número de requisições para evitar o erro 429.
    *   Como Fazer: Implementar lógica de retry com backoff para lidar com o erro `Too Many Requests`.
    *(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 10. Notas Adicionais


*   **Rate Limits:** A API pode ter limites de requisições por minuto. É recomendável implementar retry com backoff para lidar com o erro 429.
*   **Paginação:** Use os parâmetros `max_results` e `page_token` para navegar pelos resultados.
*   **Autenticação:** Certifique-se de que o token de acesso (`:access_token`) está válido e possui as permissões necessárias.
*   **Filtros Combinados:** Combine vários parâmetros para refinar os resultados, por exemplo, filtar por status e data de início simultaneamente.


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 11. Metadados Internos (Para Indexação e RAG)


```json
{
  "doc_id": "hotmart_subscriptions_001",
  "api_provider": "Hotmart",
  "api_product_area": "Assinaturas",
  "endpoint_focus": ["Listar Assinaturas", "Filtrar Assinaturas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII", // Atualizado pois contém dados de assinantes
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Assinaturas", "Assinantes", "Planos", "Transações"],
  "context_level": ["intermediate"],
  "topic_cluster": ["Assinaturas", "Gerenciamento de Assinantes", "Pagamentos"],
  "db_relations": { "tables": [], "schemas": [] },
  "related_concepts": ["Pagamento Recorrente", "Gerenciamento de Clientes", "Análise de Assinaturas", "Churn Rate"],
  "question_embeddings": [
    "Como listar todas as assinaturas ativas da Hotmart?",
    "Como filtrar assinaturas da Hotmart por ID do produto?",
    "Como obter detalhes de uma assinatura específica na Hotmart usando a API?",
    "Quais são os possíveis status de uma assinatura na Hotmart?",
    "Como paginar os resultados da API de assinaturas da Hotmart?"
  ],
  "reasoning_pathways": ["Filtragem", "Listagem", "Detalhamento", "Paginação"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 12. Checklist de Implementação (Opcional)


- [ ] Autenticação
- [ ] Tratamento de Erros (4xx, 5xx)
- [ ] Retries (429, 5xx)
- [ ] Paginação
- [ ] Validação de Entrada
- [ ] Mapeamento de Resposta
- [ ] Logs & Monitoramento
- [ ] Cache
- [ ] Testes (Casos normais, Edge-cases)
- [ ] Rate Limits


*(Ref: Hotmart Get Subscriptions, ID hotmart_getsubscriptions_001)*


## 13. Observações Finais sobre Formatação


*   Use headings (`#`, `##`, `###`) para estruturação clara.
*   Utilize tabelas Markdown para apresentar informações em formato tabular.
*   Inclua blocos de código (```bash, ```json) para exemplos.
*   Mantenha a linguagem clara e objetiva.
*   **Importante:** Inclua `(Ref: Hotmart Get Subscriptions, ID hotmart_subscriptions_001)` no final de cada seção principal e item de lista significativo (como Casos de Uso).


*(FIM DO TEMPLATE PADRÃO)*