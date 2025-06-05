#  API Hotmart - Geral - Códigos de Resposta HTTP (HTTP Response Codes)


# 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Geral - Códigos de Resposta HTTP (HTTP Response Codes) |
| **Identificador Interno** | hotmart_gen_001                                                |
| **Título Curto (Ref.)**   | Hotmart HTTP Codes                                             |
| **Versão do Documento**   | 1.0.0                                                          |
| **Data de Criação**       | 2025-04-22                                                     |
| **Última Atualização**    | 2025-04-22                                                     |
| **Autor/Responsável**     | Equipe de Documentação                                         |
| **Fonte Original**        | https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/ |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/ |
| **Status do Documento**   | Em Uso                                                         |
| **Ambiente de Referência**| Produção                                                       |
| **Idioma Original**       | Português (BR)                                                 |
| **Formato de Datas (API)**| Não especificado                                               |
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 2. Contexto
Os códigos de resposta HTTP da API Hotmart são essenciais para identificar o sucesso ou falha de cada requisição feita à plataforma. Este documento apresenta os diferentes códigos de status, suas explicações e os tipos de erros retornados, ajudando desenvolvedores a diagnosticar problemas em suas integrações com a Hotmart. Compreender estes códigos é fundamental para criar integrações robustas que saibam lidar apropriadamente com diferentes cenários de resposta, desde o sucesso até falhas temporárias ou permanentes. Estas informações são aplicáveis a todos os endpoints da API Hotmart, independente da funcionalidade específica.
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 3. Visão Geral da API/Endpoint(s)
A API da Hotmart utiliza o padrão de códigos de resposta HTTP para comunicar o resultado das operações. Além do código de status, a API fornece objetos JSON com detalhes sobre erros, incluindo tipo de erro, descrição e link para documentação adicional. Os códigos 2xx indicam sucesso, 4xx indicam erros do cliente, e 5xx indicam problemas com os serviços da Hotmart.


Este documento abrange todos os códigos de resposta possíveis ao interagir com qualquer endpoint da API Hotmart. O conhecimento destes códigos e seus significados é crucial para implementar uma integração robusta que saiba interpretar corretamente as respostas da API e tomar as ações apropriadas para cada cenário.
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 4. Detalhes Técnicos
### Códigos de Resposta HTTP
* **Endpoint URL:** Aplica-se a todos os endpoints da API Hotmart
* **Método HTTP:** Todos (GET, POST, PUT, DELETE, etc.)
* **Autenticação:** OAuth 2.0 (mencionado indiretamente nos erros 401)
* **Formato de Resposta:** JSON para detalhes de erro
* **Comportamento de Timeout:** 30 segundos (conforme indicado no erro 502)
* **Aplicação:** Comum a todas as operações da API Hotmart
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 5. Parâmetros de Entrada
Não aplicável - este documento descreve os códigos de resposta e estruturas de erro que se aplicam a todas as chamadas da API Hotmart, independentemente dos parâmetros de entrada específicos de cada endpoint.
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Estrutura Geral de Erro
| Campo         | Descrição | Tipo   | Notas |
| :------------ | :-------- | :----- | :---- |
| `error`       | O tipo de erro retornado. Indica a categoria específica do problema encontrado. | string | Valores possíveis incluem: invalid_token, token_expired, unauthorized, unauthorized_client, invalid_parameter, invalid_value_parameter, invalid_value_headers, not_found, too_many_requests, internal_server_error. Cada valor tem significado específico relacionado ao código HTTP. |
| `error_description` | Uma mensagem de fácil entendimento que fornece mais detalhes sobre o erro. | string | Inclui informações específicas sobre o problema, como "Full authentication is required to access this resource" para erros de autenticação. |
| `error_uri`   | Um link para a documentação onde poderá encontrar mais sobre o código de erro recebido. | string | Normalmente aponta para a documentação oficial da Hotmart: https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/ |
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 7. Exemplos de Requisição e Resposta
### Exemplo de Erro 401 (Unauthorized)
#### 7.1.1 Exemplo de Resposta (JSON - Erro 401)
```json
{
  "error": "unauthorized",
  "error_description": "Full authentication is required to access this resource.",
  "error_uri": "https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/"
}
```


### Exemplo de Erro 400 (Bad Request)
#### 7.2.1 Exemplo de Resposta (JSON - Erro 400)
```json
{
  "error": "invalid_parameter",
  "error_description": "The parameter 'start_date' is required for this request.",
  "error_uri": "https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/"
}
```


### Exemplo de Erro 429 (Too Many Requests)
#### 7.3.1 Exemplo de Resposta (JSON - Erro 429)
```json
{
  "error": "too_many_requests",
  "error_description": "Rate limit exceeded. Please wait before making additional requests.",
  "error_uri": "https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/"
}
```


### Exemplo de Erro 500 (Internal Server Error)
#### 7.4.1 Exemplo de Resposta (JSON - Erro 500)
```json
{
  "error": "internal_server_error",
  "error_description": "An unexpected error occurred while processing your request.",
  "error_uri": "https://developers.hotmart.com/docs/pt-BR/start/http-response-codes/"
}
```
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              |
| :--------------------- | :----------------------------------------------------------- |
| `200 OK`               | Código de sucesso. Tudo ocorreu como planejado. A resposta conterá os dados solicitados conforme documentado para o endpoint específico. |
| `201 Created`          | Similar ao 200, porém se refere a um retorno quando um novo recurso foi criado com sucesso. Normalmente retornado após operações POST bem-sucedidas que criam entidades. |
| `400 Bad Request`      | A requisição contém parâmetros inválidos ou mal formatados. Verifique os dados enviados e corrija conforme necessário. |
| `401 Unauthorized`     | Falha na autenticação ou token expirado. Verifique se o token foi enviado corretamente e se ainda é válido. |
| `403 Forbidden`        | O usuário não possui permissões para o recurso solicitado, mesmo com autenticação válida. Verifique as permissões da sua aplicação. |
| `404 Not Found`        | A URL requisitada não foi encontrada. Verifique se o endpoint está correto ou se o recurso específico existe. |
| `429 Too Many Requests`| Muitas requisições foram feitas em um curto período de tempo. Implemente rate limiting e retries com back-off exponencial. |
| `500 Internal Server Error` | Ocorreu um erro interno não esperado no servidor da Hotmart. A falha não está relacionada com sua requisição. |
| `502 Bad Gateway`      | A requisição excedeu o tempo limite de processamento (30s). Tente otimizar sua consulta reduzindo o período de dados ou adicionando filtros. |
| `503 Service Unavailable` | API indisponível para todos os usuários temporariamente. Um problema sistêmico está afetando a API. Tente novamente mais tarde. |


### Detalhamento dos Erros 400 (Bad Request)
| Tipo de Erro            | Descrição                                              |
| :---------------------- | :----------------------------------------------------- |
| `invalid_parameter`     | A requisição enviada está de alguma forma inválida. Um ou mais parâmetros obrigatórios podem estar faltando ou ter formato incorreto. |
| `invalid_value_parameter` | A requisição enviada está com o valor da queryString de alguma forma inválida. Verifique o formato e as restrições de valores para parâmetros de URL. |
| `invalid_value_headers` | A requisição enviada está com o valor do header de alguma forma inválida. Revise os headers HTTP, especialmente os relacionados à autenticação e formato de conteúdo. |
| `invalid_token`         | O valor do parâmetro page_token está inválido na requisição enviada. Este erro específico refere-se a problemas com tokens de paginação, não de autenticação. |


### Detalhamento dos Erros 401 (Unauthorized)
| Tipo de Erro            | Descrição                                              |
| :---------------------- | :----------------------------------------------------- |
| `unauthorized`          | É necessário estar autenticado para prosseguir com a requisição. Ocorre quando o token de acesso não foi passado ou há problemas no nome do parâmetro no Header. Verifique se está usando o header "Authorization" com o formato correto. |
| `token_expired`         | O token de acesso passado como parâmetro expirou. É necessário solicitar um novo token de acesso usando o fluxo de refresh token ou reautenticação. |
| `invalid_token`         | O token de acesso passado como parâmetro está inválido. Pode indicar um token malformado, revogado, ou que não foi gerado pela Hotmart. |


### Detalhamento dos Erros 403 (Forbidden)
| Tipo de Erro            | Descrição                                              |
| :---------------------- | :----------------------------------------------------- |
| `unauthorized_client`   | O usuário não possui permissões para prosseguir com a requisição. A autenticação foi bem-sucedida, mas o usuário ou aplicação não tem autorização para o recurso específico. Verifique os escopos (scopes) do token e as permissões concedidas. |


### Detalhamento dos Erros 404 (Not Found)
| Tipo de Erro            | Descrição                                              |
| :---------------------- | :----------------------------------------------------- |
| `not_found`             | A URL requisitada não foi encontrada e está de alguma forma inválida. Verifique o endpoint, parâmetros de path, e se o recurso específico (como ID de produto) existe no sistema. |


### Detalhamento dos Erros 429 (Too Many Requests)
| Tipo de Erro            | Descrição                                              |
| :---------------------- | :----------------------------------------------------- |
| `too_many_requests`     | Muitas requisições foram feitas em curto período. A API Hotmart implementa limites de taxa (rate limits) para garantir a estabilidade do serviço. Consulte a documentação específica sobre Rate Limit para entender os limites aplicáveis aos diferentes endpoints. |


### Detalhamento dos Erros 500, 502, 503 (Server Errors)
| Status Code             | Tipo de Erro             | Descrição                 |
| :---------------------- | :----------------------- | :------------------------ |
| `500`                   | `internal_server_error`  | Ocorreu algum erro interno não esperado. Este é um problema no lado do servidor da Hotmart e não está relacionado com a sua requisição. Recomenda-se implementar retry com back-off exponencial para estes casos. |
| `502`                   | `internal_server_error`  | A requisição demorou mais de 30 segundos para ser processada e foi encerrada pelo servidor. Indica uma consulta que está levando tempo excessivo, geralmente por processar muitos dados. Recomenda-se revisar datas consultadas e/ou usar outros filtros para reduzir o volume de dados. |
| `503`                   | `internal_server_error`  | API indisponível para todos os usuários. Indica um problema sistêmico que está afetando a API como um todo. Tente novamente mais tarde, pois a equipe da Hotmart estará trabalhando para restabelecer o serviço. |
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1. **Verificar autenticação válida antes de fazer requisições**
   * Objetivo: Garantir que o token de acesso esteja válido e ativo
   * Como Fazer: Implementar tratamento específico para respostas 401 com `token_expired` ou `invalid_token`, solicitando automaticamente novo token quando necessário
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


2. **Diagnosticar problemas de permissão**
   * Objetivo: Identificar quando o usuário não tem acesso ao recurso específico solicitado
   * Como Fazer: Verificar resposta 403 com `unauthorized_client` e informar ao usuário quais permissões estão faltando para acessar o recurso
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


3. **Lidar com parâmetros de entrada inválidos**
   * Objetivo: Corrigir parâmetros enviados incorretamente antes de fazer novas tentativas
   * Como Fazer: Analisar resposta 400 com `invalid_parameter`, determinar qual parâmetro específico está causando o erro a partir de `error_description` e corrigi-lo
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


4. **Otimizar consultas que ultrapassam timeout**
   * Objetivo: Reduzir tempo de processamento de consultas longas que retornam erro 502
   * Como Fazer: Ao receber 502, ajustar os filtros de data para períodos menores (ex: dividir consulta de 1 ano em 12 consultas mensais) ou adicionar filtros adicionais para reduzir o volume de dados
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


5. **Implementar retry automático para erros de servidor**
   * Objetivo: Aumentar resiliência da integração frente a falhas temporárias da API
   * Como Fazer: Implementar retry com backoff exponencial para códigos 500 e 503, começando com 1 segundo e duplicando a cada tentativa, com máximo de 5 retentativas
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


6. **Respeitar os limites de taxa (rate limits)**
   * Objetivo: Evitar bloqueios temporários por excesso de requisições (429)
   * Como Fazer: Ao receber 429, implementar espera progressiva antes de novas tentativas e distribuir requisições ao longo do tempo para evitar picos de uso
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


7. **Identificar URLs incorretas**
   * Objetivo: Detectar chamadas a endpoints inexistentes para correção rápida
   * Como Fazer: Verificar resposta 404 com `not_found`, conferir a URL usada com a documentação oficial e garantir que parâmetros de path estejam corretos
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


8. **Renovar tokens expirados**
   * Objetivo: Manter a integração funcionando sem interrupções quando tokens expirarem
   * Como Fazer: Ao receber 401 com `token_expired`, usar o refresh token para solicitar novo token de acesso automaticamente, sem interromper o fluxo da aplicação
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


9. **Validar headers de requisição**
   * Objetivo: Garantir que headers estejam formatados corretamente para evitar erros 400
   * Como Fazer: Analisar resposta 400 com `invalid_value_headers`, verificar especialmente o formato do header Authorization (Bearer token) e Content-Type (application/json)
   *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


10. **Confirmar criação de recursos**
    * Objetivo: Verificar se um novo recurso foi criado com sucesso na plataforma Hotmart
    * Como Fazer: Observar resposta 201 (Created) após operações POST e capturar o identificador do recurso criado na resposta para referência futura
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


11. **Capturar erros de paginação**
    * Objetivo: Corrigir problemas específicos com tokens de paginação em listagens
    * Como Fazer: Verificar resposta 400 com `invalid_token` relacionado a page_token, reiniciar a paginação do início ou ajustar a lógica de armazenamento do token de página
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


12. **Monitorar disponibilidade da API**
    * Objetivo: Detectar quando a API está completamente indisponível para todos os usuários
    * Como Fazer: Identificar respostas 503, configurar alertas para a equipe técnica e pausar operações automatizadas até normalização do serviço
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


13. **Depurar problemas de queryString**
    * Objetivo: Corrigir parâmetros de URL mal formatados que resultam em erro 400
    * Como Fazer: Analisar resposta 400 com `invalid_value_parameter`, verificar a codificação URL de caracteres especiais e o formato dos parâmetros de data, numéricos ou enumerações
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


14. **Verificar configuração correta de autenticação**
    * Objetivo: Garantir que o token esteja sendo enviado no header correto e formato adequado
    * Como Fazer: Ao receber 401 com `unauthorized`, verificar implementação do header Authentication, confirmando uso do formato "Bearer [token]" com espaço após "Bearer"
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


15. **Logging detalhado de erros**
    * Objetivo: Manter histórico completo de problemas para análise e resolução sistemática
    * Como Fazer: Registrar `error`, `error_description` e `error_uri` de todas as respostas de erro, junto com timestamps, endpoint chamado e parâmetros enviados (sanitizados de dados sensíveis)
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


16. **Implementar circuit breaker para proteção da aplicação**
    * Objetivo: Evitar sobrecarga em caso de falha generalizada da API Hotmart
    * Como Fazer: Monitorar frequência de erros 5xx e pausar automaticamente as requisições por 5-15 minutos se mais de 50% das chamadas falhar em um período de 1 minuto
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


17. **Acessar documentação de erros específicos**
    * Objetivo: Obter mais informações detalhadas sobre um erro específico da documentação oficial
    * Como Fazer: Utilizar o `error_uri` retornado na resposta de erro para acessar diretamente a página da documentação relevante para aquele erro específico
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


18. **Distinguir entre diferentes tipos de problemas de servidor**
    * Objetivo: Adotar estratégias específicas para cada tipo de erro de servidor (5xx)
    * Como Fazer: Implementar lógicas distintas para cada código: 500 (retry simples), 502 (otimização de consulta) e 503 (espera mais longa antes de retry)
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


19. **Validar requisições antes de enviar**
    * Objetivo: Reduzir erros 400 implementando validação prévia no cliente
    * Como Fazer: Criar validadores locais para todos os parâmetros de requisição, verificando formatos, intervalos de valores e restrições documentadas antes de enviar à API
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*


20. **Ajustar timeout do cliente para consultas pesadas**
    * Objetivo: Evitar que o cliente encerre a conexão antes do servidor processar completamente a requisição
    * Como Fazer: Configurar timeout do cliente HTTP para pelo menos 35 segundos (superior ao limite do servidor de 30s indicado no erro 502) para garantir que você receba a resposta de timeout do servidor
    *(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 10. Notas Adicionais
* **Rate Limits:** A documentação menciona limites de taxa ao explicar o erro 429, mas não fornece detalhes específicos sobre quais são esses limites. Consulte a documentação específica sobre Rate Limit para mais informações sobre limites por minuto/hora/dia e por endpoint.


* **Timeout de Requisição:** As requisições têm um limite fixo de 30 segundos para processamento, após o qual retornam erro 502. Este é um limite não negociável da plataforma Hotmart.


* **Estratégia para Consultas Lentas:** Para consultas que resultam em timeout (502), recomenda-se:
  - Reduzir o intervalo de datas consultado (dividir em múltiplas requisições menores)
  - Adicionar filtros específicos para reduzir o volume de dados processados
  - Verificar se está solicitando apenas os campos necessários, se a API oferecer essa opção


* **Códigos de Erro Consistentes:** A Hotmart mantém uma estrutura de erro consistente entre todos seus endpoints, o que facilita a implementação de tratamento de erros genérico na sua aplicação.


* **Comportamento com Erros 5xx:** Para erros 5xx (servidor), a melhor prática é implementar uma estratégia de retry com back-off exponencial, começando com 1-2 segundos e aumentando progressivamente o tempo entre tentativas.


* **Monitoramento:** É recomendável implementar monitoramento ativo dos padrões de erro da sua integração, especialmente para identificar aumentos na taxa de erros 5xx que possam indicar problemas mais amplos na API da Hotmart.
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_gen_001",
  "api_provider": "Hotmart",
  "api_product_area": "General",
  "endpoint_focus": ["HTTP Response Codes", "Error Handling"],
  "version_api_endpoint": "N/A",
  "data_sensitivity": "Public",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["HTTPResponse", "ErrorCodes", "Authentication", "RateLimit"],
  "context_level": ["foundational"],
  "topic_cluster": ["error_handling", "authentication", "api_basics", "integration_patterns"],
  "db_relations": { "tables": [], "schemas": [] },
  "related_concepts": ["OAuth", "Authentication", "Rate Limiting", "API Integration", "Circuit Breaker", "Exponential Backoff"],
  "question_embeddings": [
    "Quais são os códigos de erro da API Hotmart?",
    "O que significa o erro 401 na API Hotmart?",
    "Como lidar com timeout na API Hotmart?",
    "O que fazer quando recebo erro 429 na Hotmart?",
    "Como implementar retry para erros 5xx na API Hotmart?",
    "Como renovar um token expirado na Hotmart?",
    "Qual o significado de internal_server_error na Hotmart?",
    "Quanto tempo esperar entre retries na API Hotmart?"
  ],
  "reasoning_pathways": ["diagnostic", "troubleshooting", "integration", "error_prevention", "resilience_patterns"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*
---
## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação (Token Bearer)
- [ ]  Tratamento de Erros (4xx, 5xx)
- [ ] Retries (429, 5xx)
- [ ]  Paginação
- [ ]  Validação de Entrada
- [ ]  Mapeamento de Resposta
- [ ] Logs & Monitoramento
- [ ] Cache
- [ ]  Testes (Casos normais, Edge-cases)
- [ ]  Rate Limits
*(Ref: Hotmart HTTP Codes, ID hotmart_responsecodes_001)*