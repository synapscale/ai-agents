# API Hotmart - Pagamentos - Consultar Comissões de Vendas (Sales Commissions)


## 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Pagamentos - Consultar Comissões de Vendas (Sales Commissions) |
| **Identificador Interno** | hotmart_pay_001                                                |
| **Título Curto (Ref.)**   | Hotmart Comissões de Vendas                                     |
| **Versão do Documento**   | 1.0.0                                                          |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação                                          |
| **Fonte Original**        | Documentação Hotmart Developers                                 |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/v1/sales/sales-commissions/ |
| **Status do Documento**   | Em Uso                                                          |
| **Ambiente de Referência**| Produção                                                        |
| **Idioma Original**       | Português (BR)                                                  |
| **Formato de Datas (API)**| Timestamp (ms)                                                  |
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 2. Contexto
Este endpoint permite a consulta das informações de comissões pagas aos diversos participantes de uma venda na plataforma Hotmart, incluindo produtores, co-produtores, afiliados e add-ons. Útil para análise financeira, contabilidade e verificação de desempenho de vendas. Uma limitação importante é que se os filtros de transação ou status de transação não forem informados, o endpoint retornará apenas transações com status "APPROVED" e "COMPLETE".
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 3. Visão Geral da API/Endpoint(s)
Este endpoint fornece dados detalhados sobre comissões de vendas, incluindo valores em moeda, percentuais e identificação dos participantes comissionados. Permite filtrar por transação específica, status de transação, produto, período de datas e tipo de comissionamento.
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 4. Detalhes Técnicos
### Consultar Comissões de Vendas
* **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/sales/commissions`
* **Método HTTP:** `GET`
* **Autenticação:** Bearer Token no cabeçalho: `Authorization: Bearer :access_token`
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 5. Parâmetros de Entrada
### Consultar Comissões de Vendas (Query Parameters)


| Parâmetro          | Descrição | Tipo | Notas / Exemplo |
| :----------------- | :-------- | :--- | :-------------- |
| `transaction`      | Código único de referência para uma transação específica da Hotmart. | string | **Opcional.** Usado para filtrar os resultados para uma única transação. Ex: `HP17715690036014` |
| `transaction_status` | Filtra as transações pelo seu status atual. | string | **Opcional.** Se este parâmetro e `transaction` forem omitidos, a API retornará **apenas** status `APPROVED` e `COMPLETE`. Valores possíveis: `APPROVED`, `BLOCKED`, `CANCELLED`, `CHARGEBACK`, `COMPLETE`, `EXPIRED`, `NO_FUNDS`, `OVERDUE`, `PARTIALLY_REFUNDED`, `PRE_ORDER`, `PRINTED_BILLET`, `PROCESSING_TRANSACTION`, `PROTESTED`, `REFUNDED`, `STARTED`, `UNDER_ANALISYS`, `WAITING_PAYMENT`. |
| `max_results`      | Define o número máximo de itens (transações) que devem ser retornados em uma única página de resultados. | integer | **Opcional.** Útil para controlar o volume de dados por requisição. A API pode ter um limite máximo superior próprio (ex: 100), mesmo que um valor maior seja solicitado. Se omitido, um valor padrão da API será usado. |
| `page_token`       | Um token opaco fornecido pela API na resposta anterior (`next_page_token` ou `prev_page_token`) para navegar pela lista de resultados paginada. | string | **Opcional.** Essencial para buscar páginas subsequentes ou anteriores quando o total de resultados excede `max_results`. Não envie na primeira requisição. |
| `product_id`       | Identificador numérico único (ID) de um produto específico na Hotmart. | string | **Opcional.** Filtra as comissões relacionadas apenas a vendas deste produto específico. Geralmente um número de 7 dígitos. |
| `start_date`       | Data inicial do período para filtrar as transações, representada como timestamp Unix em **milissegundos** desde a época (1970-01-01 00:00:00 UTC). | long | **Opcional.** Usado para definir o limite inferior do intervalo de datas. **Deve ser usado em conjunto com `end_date`**. Ex: `1640995200000` (01/Jan/2022 00:00:00 UTC). |
| `end_date`         | Data final do período para filtrar as transações, representada como timestamp Unix em **milissegundos** desde a época (1970-01-01 00:00:00 UTC). | long | **Opcional.** Usado para definir o limite superior do intervalo de datas. **Deve ser usado em conjunto com `start_date`**. Ex: `1643673599999` (31/Jan/2022 23:59:59 UTC). |
| `commission_as`    | Filtra as comissões baseado no papel que o usuário autenticado (dono do token) teve na venda. | string | **Opcional.** Permite ver apenas as vendas onde você atuou como Produtor, Co-produtor ou Afiliado. Valores possíveis: `PRODUCER`, `COPRODUCER`, `AFFILIATE`. |
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Consultar Comissões de Vendas
#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `items`       | Array contendo os detalhes de cada transação e suas respectivas comissões que correspondem aos filtros aplicados na requisição. | array (de objetos) |
| `page_info`   | Objeto contendo metadados sobre a paginação dos resultados, essencial para navegar por grandes conjuntos de dados. | object |


#### 6.1.2 Detalhes do Objeto `items` (Cada elemento do Array `items`)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `transaction`       | Código único de identificação da transação na Hotmart. | string | Formato geralmente iniciado por "HP" seguido de números. Ex: `HP12345678901234` |
| `product`           | Objeto contendo informações básicas do produto associado à transação. | object | Contém os campos `name` e `id`. |
| `product.name`      | Nome comercial do produto vendido. | string | Ex: "Curso de Marketing Digital Avançado" |
| `product.id`        | Identificador numérico único do produto na Hotmart. | integer | Ex: `123456` |
| `exchange_rate_currency_payout` | Taxa de câmbio utilizada pela Hotmart para converter o valor original da compra (sem impostos) para a moeda na qual a comissão bruta (`commissions.commission.value`) é paga. | float | Retorna `1.0` se a moeda da compra e da comissão forem a mesma. Útil para entender conversões em vendas internacionais. |
| `commissions`       | Array contendo um objeto para cada participante que foi comissionado nesta transação específica. Pode incluir Produtor, Co-produtor(es), Afiliado(s) e Addon(s). | array (de objetos) |


#### 6.1.3 Detalhes do Objeto `commissions` (Cada elemento do Array `commissions`)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `commission`        | Objeto detalhando o valor monetário específico desta parcela da comissão. | object | Contém `currency_value` e `value`. |
| `commission.currency_value` | Código da moeda (padrão ISO 4217 de 3 letras) na qual o `value` da comissão está expresso. | string | Ex: `BRL`, `USD`, `EUR`, `MXN`. |
| `commission.value`  | O valor numérico bruto da comissão para este participante específico, na moeda indicada por `currency_value`. | float | Representa o valor antes de possíveis taxas ou impostos da Hotmart. Ex: `95.00` |
| `user`              | Objeto identificando o usuário Hotmart que recebeu esta comissão específica. | object | Contém `ucode` e `name`. |
| `user.ucode`        | Identificador único universal (UUID) do usuário Hotmart que recebeu a comissão. | string | Formato UUID. Ex: `1c2fbe3a-e4cb-56ec-b7e8-b9c0f1a234f4` |
| `user.name`         | Nome do usuário Hotmart que recebeu a comissão. | string | Ex: "Nome Sobrenome do Produtor" |
| `source`            | Indica o papel ou a origem da comissão para este participante na venda. | string | Valores possíveis: `PRODUCER` (Produtor principal), `COPRODUCER` (Co-produtor), `AFFILIATE` (Afiliado), `ADDON` (Comissão de produto adicional/Order Bump). |


#### 6.1.4 Detalhes do Objeto `page_info`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `total_results`     | Número total de registros (transações) que correspondem aos critérios de filtro aplicados, independentemente da paginação. | integer | Indica o tamanho total do conjunto de dados. |
| `next_page_token`   | Token opaco que deve ser enviado no parâmetro `page_token` da *próxima* requisição GET para obter a página seguinte de resultados. | string | **Ausente** na resposta se esta for a última página de resultados. |
| `prev_page_token`   | Token opaco que deve ser enviado no parâmetro `page_token` da *próxima* requisição GET para obter a página anterior de resultados. | string | **Ausente** na resposta se esta for a primeira página de resultados. |
| `results_per_page`  | Número de resultados (transações) efetivamente retornados *nesta* página específica. | integer | Geralmente igual ao `max_results` solicitado, exceto possivelmente na última página, onde pode ser menor. |
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 7. Exemplos de Requisição e Resposta
### Consultar Comissões de Vendas
#### 7.1.1 Exemplo de Requisição (cURL)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/sales/commissions?product_id=123456' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer :access_token'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
{
  "items": [
    {
      "transaction": "HP12345678901234",
      "product": {
        "name": "Product Test",
        "id": 123456
      },
      "exchange_rate_currency_payout": 0.001334,
      "commissions": [
        {
          "commission": {
            "currency_value": "USD",
            "value": 95.00
          },
          "user": {
            "ucode": "1c2fbe3a-e4cb-56ec-b7e8-b9c0f1a234f4",
            "name": "Name User Producer Test"
          },
          "source": "PRODUCER"
        },
        {
          "commission": {
            "currency_value": "USD",
            "value": 4.35
          },
          "user": {
            "ucode": "1c2fbe3a-e4cb-56ec-b7e8-b9c0f1a234f5",
            "name": "Name User Coproducer Test"
          },
          "source": "COPRODUCER"
        },
        {
          "commission": {
            "currency_value": "USD",
            "value": 0.65
          },
          "user": {
            "ucode": "1c2fbe3a-e4cb-56ec-b7e8-b9c0f1a234f6",
            "name": "Name User Addon Test"
          },
          "source": "ADDON"
        }
      ]
    }
  ],
  "page_info": {
    "total_results": 10,
    "results_per_page": 10
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro)
```json
{
  "code": "BAD_REQUEST",
  "message": "Invalid parameter: Invalid transaction status",
  "details": [
    {
      "field": "transaction_status",
      "value": "INVALID_STATUS",
      "issue": "invalid_value"
    }
  ]
}
```
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              | Notas Adicionais |
| :--------------------- | :----------------------------------------------------------- | :--------------- |
| `200 OK`               | Sucesso. A requisição foi processada corretamente e os dados de comissões (se houver) estão no corpo da resposta. | Mesmo que não existam comissões correspondentes aos filtros, a API retornará 200 OK com um array `items` vazio. |
| `400 Bad Request`      | Erro na requisição. Geralmente devido a parâmetros inválidos (formato, tipo, valor) ou combinações incorretas de filtros. | Verifique o corpo da resposta para detalhes específicos do erro. Comuns: formato inválido de data, status de transação inválido, ID de produto mal-formatado. |
| `401 Unauthorized`     | Falha na autenticação. O `access_token` fornecido é inválido, expirado ou ausente. | Garanta que o token Bearer está correto e válido no cabeçalho `Authorization`. Tokens geralmente expiram após algumas horas. |
| `403 Forbidden`        | Acesso negado. O token é válido, mas o usuário autenticado não tem permissão para acessar os dados solicitados (ex: comissões de outro usuário). | Verifique as permissões associadas ao token. Requer permissões específicas para acessar dados de comissões. |
| `404 Not Found`        | Recurso não encontrado. Pode indicar que a URL do endpoint está incorreta ou, em alguns casos, que um recurso específico filtrado (como uma `transaction`) não existe. | Verifique a URL e os identificadores usados nos filtros. Diferencia-se de um array vazio (200 OK), que indica ausência de resultados para filtros válidos. |
| `429 Too Many Requests`| Limite de taxa (Rate Limit) excedido. Muitas requisições foram feitas em um curto período. | Implemente backoff exponencial antes de tentar novamente. Respeite os cabeçalhos de rate limiting, como `X-RateLimit-Remaining` e `X-RateLimit-Reset`, se fornecidos. |
| `500 Internal Server Error` | Erro inesperado no servidor da API Hotmart. | Tente novamente mais tarde com backoff. Se persistir, pode ser um problema na plataforma Hotmart - registre logs detalhados e entre em contato com o suporte. |
| `503 Service Unavailable` | Serviço temporariamente indisponível, possivelmente devido a manutenção ou carga excessiva. | Implemente retry com backoff exponencial. Verifique o status da plataforma Hotmart. |


*Nota: A API Hotmart fornece detalhes valiosos no corpo da resposta em caso de erro. O campo `details` geralmente contém informações específicas sobre campos problemáticos, valores inválidos e o tipo de problema, facilitando a correção do erro. Sempre analise esta resposta ao depurar problemas.*
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1. **Consultar todas as comissões de um produto específico**
   * Objetivo: Obter dados de comissões para análise financeira de um produto
   * Como Fazer: Enviar requisição GET com `product_id=123456`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


2. **Verificar comissões recebidas como produtor**
   * Objetivo: Analisar apenas comissões onde o usuário é o produtor
   * Como Fazer: Adicionar parâmetro `commission_as=PRODUCER`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


3. **Consultar comissões de afiliados para um produto**
   * Objetivo: Analisar performance dos afiliados de um produto
   * Como Fazer: Combinar `product_id=123456` com `commission_as=AFFILIATE`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


4. **Verificar comissões de transação específica**
   * Objetivo: Auditar os valores de comissão de uma venda específica
   * Como Fazer: Usar parâmetro `transaction=HP12345678901234`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


5. **Filtrar comissões por período específico**
   * Objetivo: Analisar comissões dentro de um intervalo de datas para relatório mensal
   * Como Fazer: Definir `start_date=1640995200000` e `end_date=1643673600000` (Jan/2022)
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


6. **Consultar apenas comissões de vendas aprovadas**
   * Objetivo: Analisar apenas comissões confirmadas
   * Como Fazer: Adicionar `transaction_status=APPROVED`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


7. **Verificar comissões de vendas canceladas**
   * Objetivo: Auditar comissões de vendas que foram canceladas
   * Como Fazer: Utilizar `transaction_status=CANCELLED`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


8. **Analisar comissões de vendas com chargeback**
   * Objetivo: Identificar impacto financeiro de chargebacks nas comissões
   * Como Fazer: Filtrar com `transaction_status=CHARGEBACK`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


9. **Consultar comissões de co-produtores por produto**
   * Objetivo: Análise de desempenho de co-produtores para um produto específico
   * Como Fazer: Combinar `product_id=123456` e `commission_as=COPRODUCER`
   *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


10. **Limitar resultados por página para melhor performance**
    * Objetivo: Otimizar carregamento em aplicações com muitos dados
    * Como Fazer: Definir `max_results=50` para limitar resultados
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


11. **Navegar entre páginas de resultados**
    * Objetivo: Acessar mais resultados além da primeira página
    * Como Fazer: Usar o `next_page_token` retornado na resposta anterior no parâmetro `page_token`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


12. **Comparar comissões entre dois produtos**
    * Objetivo: Analisar diferenças de desempenho entre produtos
    * Como Fazer: Realizar duas requisições separadas com diferentes `product_id`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


13. **Verificar comissões pendentes (aguardando pagamento)**
    * Objetivo: Prever receita futura de comissões
    * Como Fazer: Filtrar com `transaction_status=WAITING_PAYMENT`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


14. **Analisar comissões de vendas reembolsadas**
    * Objetivo: Avaliar impacto financeiro de reembolsos
    * Como Fazer: Utilizar `transaction_status=REFUNDED`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


15. **Verificar comissões parcialmente reembolsadas**
    * Objetivo: Analisar ajustes em comissões após reembolsos parciais
    * Como Fazer: Filtrar com `transaction_status=PARTIALLY_REFUNDED`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


16. **Consultar comissões de add-ons para produto específico**
    * Objetivo: Analisar desempenho de serviços adicionais vinculados ao produto
    * Como Fazer: Filtrar por `product_id` e analisar comissões com `source=ADDON` no resultado
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


17. **Auditar taxa de câmbio aplicada às comissões**
    * Objetivo: Verificar valores de conversão aplicados em comissões internacionais
    * Como Fazer: Analisar o campo `exchange_rate_currency_payout` nos resultados
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


18. **Gerar relatório trimestral de comissões**
    * Objetivo: Criar relatório financeiro para um trimestre específico
    * Como Fazer: Definir `start_date` e `end_date` correspondentes ao trimestre (ex: 01/Jan a 31/Mar)
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


19. **Verificar comissões bloqueadas**
    * Objetivo: Identificar comissões retidas para análise ou verificação
    * Como Fazer: Filtrar com `transaction_status=BLOCKED`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*


20. **Analisar comissões de transações expiradas**
    * Objetivo: Avaliar receita perdida por expiração de transações
    * Como Fazer: Utilizar `transaction_status=EXPIRED`
    *(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 10. Notas Adicionais
*   **Filtros Padrão:** Se os filtros `transaction` ou `transaction_status` **não forem informados**, o endpoint retornará por padrão **apenas** transações com status `APPROVED` e `COMPLETE`. Para ver outros status, você deve especificá-los explicitamente.
*   **Paginação:** A navegação entre páginas é feita usando os tokens (`next_page_token`, `prev_page_token`) retornados no objeto `page_info`. Nunca tente construir ou manipular estes tokens manualmente - eles são opacos e específicos da API Hotmart.
*   **Limites de Resultados:** Use `max_results` para controlar o tamanho da página. A API tem um limite máximo que será respeitado mesmo se você solicitar mais. Se não especificado, a API usará um valor padrão (geralmente entre 10-50 itens).
*   **Filtros de Data:** Os parâmetros `start_date` e `end_date` devem ser fornecidos em **milissegundos** (timestamp Unix) e **devem ser usados juntos** para definir um intervalo de tempo válido. O intervalo máximo permitido não é especificado na documentação, mas é recomendável usar períodos de até 90 dias para evitar timeouts ou limitações.
*   **Identificadores:** O `ucode` do usuário é um UUID, enquanto o `product_id` é um inteiro (mas deve ser passado como string nos parâmetros). O `transaction` é uma string alfanumérica geralmente iniciada por "HP".
*   **Valores Monetários:** Os valores de comissão (`commission.value`) são retornados na moeda especificada por `commission.currency_value`. A taxa de câmbio (`exchange_rate_currency_payout`) ajuda a entender conversões em transações internacionais.
*   **Composição de Comissões:** Uma única transação (venda) pode ter múltiplas comissões distribuídas entre diferentes participantes (`PRODUCER`, `COPRODUCER`, `AFFILIATE`, `ADDON`). O array `commissions` contém todas essas divisões.
*   **Cache de Resultados:** Recomenda-se implementar cache do lado do cliente para resultados frequentemente consultados, especialmente para períodos históricos que não mudam. Isso ajuda a respeitar os rate limits e melhora o desempenho.
*   **Tratamento de Erros:** Implemente retry com backoff exponencial para erros 429, 500 e 503. Registre detalhadamente erros 400 para depuração de parâmetros inválidos.
*   **Segurança:** O token de acesso usado para autenticação contém permissões sensíveis. Nunca exponha este token em código-fonte, logs ou URLs acessíveis ao público.
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_pay_001",
  "api_provider": "Hotmart",
  "api_product_area": "Pagamentos",
  "endpoint_focus": ["Consultar Comissões", "Listar Transações com Comissões"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Financial",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Comissões", "Transações", "Produtos", "Participantes"],
  "context_level": ["intermediate"],
  "topic_cluster": ["pagamentos", "comissões", "vendas", "afiliados", "marketplace"],
  "db_relations": { 
    "tables": ["transactions", "commissions", "users", "products"], 
    "schemas": ["sales", "payments"] 
  },
  "related_concepts": ["affiliate marketing", "revenue share", "sales tracking", "commission splits", "payout tracking"],
  "question_embeddings": [
    "Como consultar comissões de vendas na Hotmart?",
    "Quais tipos de participantes recebem comissões?",
    "Como filtrar comissões por status de transação?",
    "Como verificar comissões de afiliados?",
    "Como analisar comissões por período específico?",
    "Como implementar paginação nos resultados de comissões?",
    "Quais status de transação posso filtrar na API de comissões?"
  ],
  "reasoning_pathways": ["transactional", "financial-analysis", "payment-tracking", "commission-calculation", "affiliate-performance"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*
---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação com token Bearer
- [ ] Tratamento de Erros (4xx, 5xx)
- [ ] Implementação de retry com backoff exponencial
- [ ] Implementação de paginação completa (next/prev)
- [ ] Validação de parâmetros de entrada
- [ ] Conversão adequada de timestamps para datas
- [ ] Mapeamento correto dos campos de resposta
- [ ] Logs & Monitoramento
- [ ] Cache de resultados frequentes
- [ ] Testes de diferentes status de transação
- [ ] Testes com diferentes tipos de comissionamento
- [ ] Implementação de filtros por data
- [ ] Tratamento para casos sem dados retornados
- [ ] Gerenciamento seguro do token de autenticação
- [ ] Alertas para erros recorrentes
- [ ] Controle de uso dentro de rate limits
*(Ref: Hotmart Comissões de Vendas, ID hotmart_salescommissions_001)*