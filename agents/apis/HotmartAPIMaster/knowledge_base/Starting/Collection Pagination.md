# API Hotmart - Paginação - Acessar Coleções Paginadas (Collection Pagination)


## 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Paginação - Acessar Coleções Paginadas (Collection Pagination) |
| **Identificador Interno** | hotmart_pag_001                           |
| **Título Curto (Ref.)**   | Hotmart Pagination                 |
| **Versão do Documento**   | 1.1.0                                     |
| **Data de Criação**       | 2025-04-22                                                  |
| **Última Atualização**    | 2025-04-22                                                  |
| **Autor/Responsável**     | Equipe de Documentação                                    |
| **Fonte Original**        | https://developers.hotmart.com/docs/pt-BR/start/pagination/  |
| **URL de Referência**     | https://developers.hotmart.com/payments/api/v1/subscriptions (Exemplo de endpoint que usa paginação) |
| **Status do Documento**   | Em Uso                              |
| **Ambiente de Referência**| Produção                                |
| **Idioma Original**       | Português (BR)                                  |
| **Formato de Datas (API)**| ISO 8601 |
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 2. Contexto
Este documento descreve o mecanismo padrão de paginação da API Hotmart, essencial para acessar grandes conjuntos de dados (como vendas, assinaturas, etc.) de forma eficiente e controlada, evitando timeouts e sobrecarga. A paginação baseada em cursor é implementada em diversos endpoints da API que retornam listas, permitindo que os desenvolvedores processem grandes volumes de dados em partes gerenciáveis. ID Interno: hotmart_pag_001.
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 3. Visão Geral da API/Endpoint(s)
A API de paginação da Hotmart fornece uma estrutura consistente para navegar por grandes coleções de dados. Utilizando um sistema de paginação baseado em cursor (tokens opacos), permite recuperar dados em partes, com controle sobre o tamanho das páginas (`max_results`). Este mecanismo garante maior estabilidade na navegação, mesmo que novos dados sejam inseridos entre as chamadas. Ele é aplicado em múltiplos endpoints da API Hotmart que retornam listas de recursos.


Exemplos de endpoints que utilizam este padrão de paginação:
*   `GET /payments/api/v1/sales` - Lista de vendas
*   `GET /payments/api/v1/subscriptions` - Lista de assinaturas
*   `GET /club/api/v1/subscribers` - Lista de assinantes
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 4. Detalhes Técnicos
### Padrão Geral de Paginação (Aplicável a Vários Endpoints)
*   **Endpoint URL Base (Exemplo: Subscrições):** `https://developers.hotmart.com/payments/api/v1/subscriptions`
*   **Método HTTP:** `GET` (para a maioria dos endpoints de listagem)
*   **Autenticação:** Bearer Token (OAuth 2.0) - Requer um token de acesso válido no header `Authorization`.
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 5. Parâmetros de Entrada
Os parâmetros de paginação são enviados como **Query Parameters** na URL da requisição.


### Parâmetros Comuns de Paginação
| Parâmetro          | Descrição | Tipo | Notas / Exemplo |
| :----------------- | :-------- | :--- | :-------------- |
| `max_results`      | Define o número máximo de itens que devem ser retornados por página. Cada endpoint possui um valor padrão e um limite máximo permitido. Se um valor maior que o limite for enviado, a API retornará o máximo permitido. Utilizando um valor maior para este parâmetro ajuda a reduzir o número total de chamadas à API, mas pode aumentar o tempo de resposta de cada chamada individual. | Integer | `?max_results=50` - Solicita 50 itens por página, mas o endpoint pode retornar menos se o máximo permitido for menor. |
| `page_token`       | Token opaco que representa a página específica a ser recuperada (seja a próxima ou a anterior). Este token é obtido a partir dos campos `next_page_token` ou `prev_page_token` da resposta de uma chamada anterior. Não deve ser modificado ou gerado pelo cliente, pois contém informações específicas de posicionamento encriptadas. Para a primeira página, este parâmetro não é enviado ou pode ser enviado como vazio. | String | `?page_token=eyJwYWdlIjoyLCJyb3dzIjoxMH0=` - Token obtido de uma resposta anterior, geralmente codificado em Base64. |
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Estrutura Geral de Respostas Paginadas
A estrutura de resposta para endpoints que suportam paginação geralmente segue este padrão:


#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `items`       | Array contendo a coleção de itens da página atual. O tipo e a estrutura dos objetos dentro deste array dependem do endpoint específico que foi chamado (ex: objetos de assinatura, objetos de venda). Este array pode estar vazio se não houver resultados para os filtros aplicados, ou pode conter menos itens que o solicitado se estiver na última página da coleção. | Array |
| `page_info`   | Objeto contendo metadados sobre a paginação atual. Este objeto está sempre presente na resposta, mesmo quando o array `items` está vazio, e fornece as informações necessárias para navegar entre as páginas. | Object |


#### 6.1.2 Detalhes do Objeto `page_info`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `total_results`     | Número total de itens existentes na coleção completa, desconsiderando a paginação. Este valor permite calcular o número total de páginas e implementar indicadores de progresso como "Página 2 de 10" ou "Mostrando 1-20 de 143 resultados". **Importante:** Este campo pode não ser retornado em todos os endpoints, principalmente aqueles que lidam com grandes volumes de dados onde o cálculo do total seria custoso. | Integer | Ex: `143` - Indica que existem 143 itens no total na coleção completa. |
| `next_page_token`   | Token opaco que serve como referência para requisitar a *próxima* página da lista. Deve ser usado diretamente no parâmetro `page_token` da próxima requisição, sem modificações. Este campo estará **ausente** ou será `null` na resposta da última página, o que pode ser usado como condição de parada em loops automáticos de processamento. | String | Ex: `"eyJwYWdlIjozLCJyb3dzIjoxMH0="` - Token codificado que aponta para a próxima página. |
| `prev_page_token`   | Token opaco que serve como referência para requisitar a página *anterior* da lista. Deve ser usado diretamente no parâmetro `page_token` da requisição para voltar uma página. Este campo estará **ausente** ou será `null` na resposta da primeira página, o que permite determinar se o usuário já está no início da coleção. | String | Ex: `"eyJwYWdlIjoxLCJyb3dzIjoxMH0="` - Token codificado que aponta para a página anterior. |
| `results_per_page`  | Indica a quantidade de itens efetivamente retornados na página *atual* (ou seja, o tamanho do array `items`). Este valor será igual ou menor que o `max_results` solicitado, limitado ao máximo permitido pelo endpoint específico. Em casos de última página, pode ser menor que o `max_results` solicitado. | Integer | Ex: `10` - Indica que há 10 itens no array `items` da resposta atual. |
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 7. Exemplos de Requisição e Resposta
### Exemplo: Listando Assinaturas (Segunda Página)


#### 7.1.1 Exemplo de Requisição (cURL)
```bash
# Supondo que o next_page_token da primeira página foi "eyJwYWdlIjoyLCJyb3dzIjoxMH0="
# E queremos limitar a 20 resultados por página (se permitido pelo endpoint)
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/subscriptions?max_results=20&page_token=eyJwYWdlIjoyLCJyb3dzIjoxMH0=' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer seu_token_de_acesso'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
{
  "items": [
    // Array de objetos de assinatura (até 20, conforme max_results e limite do endpoint)
    {
      "id": "subscription_123",
      "subscriber_name": "João Silva",
      "product_id": "product_456",
      "status": "ACTIVE",
      "created_date": "2023-01-15T14:30:00Z",
      "payment_method": "CREDIT_CARD",
      "recurrency_period": "MONTHLY"
      // ... outros campos da assinatura
    },
    {
      "id": "subscription_124",
      "subscriber_name": "Maria Souza",
      "product_id": "product_789",
      "status": "ACTIVE",
      "created_date": "2023-01-16T09:45:00Z",
      "payment_method": "BOLETO",
      "recurrency_period": "YEARLY"
      // ... outros campos da assinatura
    }
    // ... mais itens (até 20 no total)
  ],
  "page_info": {
    // (Opcional) Total de resultados na coleção inteira
    "total_results": 143,
    // Token para buscar a próxima página (se houver)
    "next_page_token": "eyJwYWdlIjozLCJyb3dzIjoxMH0=",
    // Token para buscar a página anterior
    "prev_page_token": "eyJwYWdlIjoxLCJyb3dzIjoxMH0=",
    // Quantidade de itens efetivamente retornados nesta página
    "results_per_page": 20 // Ou o máximo permitido, se 20 for maior
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro 429 Rate Limit)
```json
{
  "error": "too_many_requests",
  "error_description": "Rate limit exceeded. Try again later.",
  "timestamp": "2023-08-15T14:30:45.123Z",
  "status": 429,
  "path": "/payments/api/v1/subscriptions"
  // Os campos exatos podem variar dependendo da implementação
}
```
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              | Notas Adicionais |
| :--------------------- | :----------------------------------------------------------- | :--------------- |
| `200 OK`               | Sucesso. Retorna a coleção paginada de recursos no corpo da resposta. O array `items` pode estar vazio se nenhum resultado corresponder aos filtros aplicados, mas o objeto `page_info` estará presente. | A resposta de sucesso inclui os headers de rate limit que devem ser monitorados para evitar erros 429 em iterações subsequentes. |
| `400 Bad Request`      | Erro na requisição, como um `page_token` inválido, expirado, ou formato incorreto de `max_results` (ex: valor não numérico). | O corpo da resposta geralmente contém um JSON com detalhes específicos do erro, incluindo mensagem e possíveis soluções. |
| `401 Unauthorized`     | Falha na autenticação. Token de acesso (Bearer) ausente, inválido ou expirado. | Verificar a validade do token e o processo de autenticação. Pode ser necessário obter um novo token de acesso. |
| `403 Forbidden`        | Autenticado com sucesso, mas sem permissão para acessar o recurso específico ou visualizar determinados dados. | Verificar as permissões associadas ao token e à conta. Alguns dados podem requerer permissões específicas. |
| `404 Not Found`        | O endpoint solicitado não existe ou o recurso específico (se aplicável, como um filtro por ID) não foi encontrado. | Verificar cuidadosamente a URL do endpoint e os parâmetros de filtro utilizados. |
| `429 Too Many Requests`| Rate Limit excedido. O cliente fez muitas requisições em um curto período. Limite padrão de 500 chamadas/minuto. | Os headers da resposta contêm informações cruciais: `RateLimit-Remaining` (chamadas restantes) e `RateLimit-Reset` (segundos até reset). Implementar backoff exponencial e monitoramento de limites. |
| `500 Internal Server Error` | Erro inesperado no servidor da API Hotmart. | Este é um erro do lado do servidor, não do cliente. Tentar novamente após alguns segundos. Se persistir, contatar o suporte Hotmart com detalhes da requisição. |
| `503 Service Unavailable` | Serviço temporariamente indisponível, possivelmente devido a manutenção ou sobrecarga. | Implementar retry com backoff exponencial. Verificar status.hotmart.com para informações sobre possíveis incidentes. |
| `504 Gateway Timeout`  | O servidor da API não conseguiu responder dentro do tempo limite, possivelmente devido a uma consulta complexa ou grande volume de dados. | Considerar reduzir o `max_results` ou simplificar filtros. Tentar novamente com backoff. |
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1.  **Listar primeira página de assinaturas**
    * Objetivo: Recuperar os primeiros resultados das assinaturas ativas
    * Como Fazer: `GET /payments/api/v1/subscriptions` sem `page_token` e possivelmente com filtro `status=ACTIVE`
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


2.  **Navegar para a próxima página de assinaturas**
    * Objetivo: Avançar para a página seguinte na listagem de assinaturas
    * Como Fazer: Extrair `next_page_token` da resposta anterior e enviar como parâmetro `page_token` na próxima chamada
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


3.  **Voltar para a página anterior de assinaturas**
    * Objetivo: Retornar à página previamente visualizada na navegação
    * Como Fazer: Utilizar o `prev_page_token` da resposta atual como parâmetro `page_token` na nova chamada
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


4.  **Aumentar o número de resultados por página para reduzir chamadas**
    * Objetivo: Obter mais registros em cada chamada para processar menos requisições no total
    * Como Fazer: Adicionar `?max_results=100` (ou valor máximo permitido) à URL da requisição
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


5.  **Verificar se há mais páginas disponíveis após a atual**
    * Objetivo: Determinar programaticamente se existem mais registros após a página atual
    * Como Fazer: Verificar se o campo `next_page_token` existe e não é nulo/vazio na resposta
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


6.  **Consultar o total de registros disponíveis para exibir progresso**
    * Objetivo: Exibir ao usuário informações como "Mostrando 1-20 de 143 resultados"
    * Como Fazer: Verificar o campo `total_results` no objeto `page_info` (quando disponível)
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


7.  **Listar primeira página de vendas filtradas por produto**
    * Objetivo: Obter os primeiros registros de vendas de um produto específico
    * Como Fazer: Chamar `GET /payments/api/v1/sales?product_id=12345` sem `page_token`
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


8.  **Navegar para a próxima página de vendas mantendo filtros**
    * Objetivo: Avançar na paginação de vendas mantendo os filtros aplicados
    * Como Fazer: Utilizar o `next_page_token` retornado na resposta, mantendo os mesmos parâmetros de filtro originais
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


9.  **Otimizar chamadas à API ao processar grande volume histórico**
    * Objetivo: Minimizar o número de requisições ao processar todo o histórico de vendas
    * Como Fazer: Configurar `max_results` com o valor máximo permitido e implementar processamento em lote dos resultados
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


10. **Implementar sistema de navegação por páginas em interface web**
    * Objetivo: Criar interface com botões "Próxima" e "Anterior" para usuário navegar entre páginas
    * Como Fazer: Armazenar `next_page_token` e `prev_page_token` para habilitar/desabilitar botões de navegação conforme disponibilidade
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


11. **Listar primeira página de assinantes do clube com filtro de status**
    * Objetivo: Obter os primeiros registros de assinantes ativos do clube
    * Como Fazer: Chamar `GET /club/api/v1/subscribers?status=ACTIVE` sem `page_token`
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


12. **Verificar se está na primeira página para controle de navegação**
    * Objetivo: Desabilitar botão "Anterior" quando estiver na primeira página
    * Como Fazer: Verificar a ausência do campo `prev_page_token` na resposta (será null ou ausente)
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


13. **Verificar se está na última página para controle de navegação**
    * Objetivo: Desabilitar botão "Próxima" quando estiver na última página disponível
    * Como Fazer: Verificar a ausência do campo `next_page_token` na resposta (será null ou ausente)
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


14. **Calcular o número total de páginas para exibir navegação numerada**
    * Objetivo: Mostrar controle de páginas do tipo "1 2 3 ... 15" em interface de usuário
    * Como Fazer: Se `total_results` estiver disponível, calcular `Math.ceil(total_results / results_per_page)`
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


15. **Verificar a quantidade de itens na página atual para controle de exibição**
    * Objetivo: Saber exatamente quantos itens foram retornados para processamento ou exibição
    * Como Fazer: Verificar o campo `results_per_page` no `page_info` ou contar elementos no array `items`
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


16. **Processar todas as páginas de resultados automaticamente**
    * Objetivo: Iterar por todas as páginas disponíveis em um processo automatizado (ETL, relatório completo)
    * Como Fazer: Implementar loop que continua chamando a API com `next_page_token` enquanto ele estiver presente nas respostas
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


17. **Respeitar rate limits ao processar múltiplas páginas sequencialmente**
    * Objetivo: Evitar erros 429 (Too Many Requests) ao processar grande volume de dados
    * Como Fazer: Monitorar os headers `RateLimit-Remaining` e `RateLimit-Reset`, implementar atrasos adaptativos entre chamadas
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


18. **Listar histórico de assinaturas de um cliente específico com paginação**
    * Objetivo: Obter todas as assinaturas de um cliente específico em formato paginado
    * Como Fazer: Chamar endpoint com filtro de email ou ID de cliente e processar paginação normalmente
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


19. **Salvar token de página para retomar processamento interrompido**
    * Objetivo: Criar checkpoint para permitir continuação do processamento em caso de falha ou pausa
    * Como Fazer: Armazenar último `next_page_token` processado em banco de dados ou arquivo de estado
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


20. **Combinar paginação com filtros de período para relatórios mensais**
    * Objetivo: Gerar relatório de vendas do mês anterior com todos os dados paginados
    * Como Fazer: Incluir parâmetros de data `start_date=2023-04-01&end_date=2023-04-30` junto com parâmetros de paginação
    *(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 10. Notas Adicionais
*   **Rate Limits:** A API Hotmart tem um limite padrão de 500 chamadas por minuto (incluindo leitura e escrita). As respostas incluem headers relacionados ao rate limit que são essenciais para gerenciar o consumo:
    * `RateLimit-Limit`: Número total de chamadas permitidas por janela de tempo
    * `RateLimit-Remaining`: Total de requisições disponíveis na janela atual
    * `RateLimit-Reset`: Tempo restante em segundos para redefinição do limite
    * `X-RateLimit-Limit-Minute`: Chamadas permitidas por minuto
    * `X-RateLimit-Remaining-Minute`: Total de requisições restantes no minuto atual
    
    Quando implementar processos que iterem por várias páginas, monitore estes headers e implemente atrasos adaptativos para evitar atingir o limite.


*   **Consistência da Paginação:** A implementação de paginação baseada em cursor (page_token) é projetada para manter a consistência mesmo quando novos itens são adicionados durante a navegação. Porém, em sistemas de alta escrita, é teoricamente possível que alguns itens sejam duplicados ou omitidos entre páginas se ocorrerem mudanças significativas nos dados subjacentes. Para operações críticas que exigem consistência absoluta, considere usar identificadores únicos para detectar possíveis duplicações.


*   **Expiração de Tokens:** Os tokens de paginação (`next_page_token` e `prev_page_token`) podem ter um tempo de validade limitado. Se armazenar estes tokens para uso posterior (ex: em sessões longas de usuário), implemente tratamento para possíveis erros 400 (Bad Request) caso o token expire, reiniciando a paginação do início.


*   **Disponibilidade de Campos:** O campo `total_results` não é garantido em todos os endpoints, especialmente aqueles que lidam com grandes volumes de dados onde calcular o total seria custoso. Verifique sua presença antes de utilizá-lo em cálculos ou exibições.


*   **Tamanho Máximo de Página:** Cada endpoint define seu próprio limite máximo para o parâmetro `max_results`. Alguns podem permitir até 100 itens por página, enquanto outros podem limitar a 20 ou 50. Consulte a documentação específica de cada endpoint ou teste valores diferentes para determinar o máximo permitido.


*   **Desempenho vs. Volume:** Valores maiores de `max_results` reduzem o número total de chamadas necessárias para processar uma coleção completa, mas podem aumentar o tempo de resposta individual de cada chamada e o consumo de memória. Para conjuntos muito grandes, encontre um equilíbrio entre tamanho da página e número de requisições.
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_pag_001",
  "api_provider": "Hotmart",
  "api_product_area": "Paginação",
  "endpoint_focus": ["Listar Coleções", "Navegar Páginas", "Gerenciar Grandes Volumes de Dados"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Varies by Endpoint (PII, Financial possible)",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Coleções", "Paginação", "Tokens", "Rate Limits", "Resultados"],
  "context_level": ["intermediate"],
  "topic_cluster": ["API Integration", "Pagination Patterns", "Data Retrieval", "API Best Practices"],
  "db_relations": { "tables": [], "schemas": [] },
  "related_concepts": ["Cursor Pagination", "Rate Limiting", "Collection Iteration", "API Throttling", "Idempotency", "Backoff Strategy", "Token-Based Navigation", "Large Dataset Processing"],
  "question_embeddings": [
    "Como implementar paginação na API Hotmart?",
    "Qual é o limite de taxa da API Hotmart?",
    "Como obter a próxima página de resultados na Hotmart API?",
    "Como saber o total de resultados em uma lista paginada da Hotmart?",
    "Como lidar com o erro 429 (Too Many Requests) na API Hotmart?",
    "Qual a diferença entre next_page_token e prev_page_token?",
    "Como definir quantos itens por página quero na API Hotmart?",
    "O que fazer quando o token de paginação é inválido?",
    "Como saber se estou na última página de resultados?",
    "Como implementar botões de navegação entre páginas?"
  ],
  "reasoning_pathways": ["if-then", "process", "looping", "pagination", "error-handling"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*


---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação (Bearer Token)
- [ ] Tratamento de Erros (4xx, 5xx, especificamente 429)
- [ ] Retries (Necessário para 429, 5xx)
- [ ] Paginação (Implementação de `page_token` e `max_results`)
- [ ]  Validação de Entrada (Verificar formato dos tokens e valores numéricos para max_results)
- [ ]  Mapeamento de Resposta (Extrair `items`, `next_page_token`, `prev_page_token`)
- [ ]  Logs & Monitoramento (Monitorar Rate Limits e erros)
- [ ]  Cache (Opcional: armazenar resultados temporariamente para reduzir chamadas)
- [ ]  Testes (Casos: primeira página, páginas intermediárias, última página, página única, erro 429)
- [ ]  Rate Limits (Implementar respeito aos headers e backoff)
*(Ref: Hotmart Pagination, ID hotmart_collectionpagination_001)*