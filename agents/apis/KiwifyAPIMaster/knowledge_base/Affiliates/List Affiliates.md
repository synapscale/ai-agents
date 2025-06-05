# API Kiwify - Afiliados - Listar Afiliados (List Affiliates)


# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Afiliados - Listar Afiliados (List Affiliates)` |
| **Identificador Interno** | `kiwify_affil_001`                   |
| **Título Curto (Ref.)**   | `Kiwify List Affiliates`           |
| **Versão do Documento**   | `1.0.0`                                |
| **Data de Criação**       | `2025-04-15`                                                  |
| **Última Atualização**    | `2025-04-15`                                                  |
| **Autor/Responsável**     | `Equipe de Documentação de API`                                    |
| **Fonte Original**        | `https://docs.kiwify.com.br/api-reference/affiliates/list`  |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/affiliates/list` |
| **Status do Documento**   | `Em Uso`                              |
| **Ambiente de Referência**| `Produção`                                |
| **Idioma Original**       | `Português (BR)`                                  |
| **Formato de Datas (API)**| `ISO 8601 (YYYY-MM-DDTHH:MM:SS.sssZ)` |


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 2. Contexto


> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint de listagem de afiliados da Kiwify.


Este endpoint permite obter uma lista completa de todos os afiliados cadastrados na plataforma Kiwify, incluindo seus dados pessoais, informações da empresa, detalhes de produtos associados e valores de comissão. O recurso é essencial para gestão de programas de afiliados, análise de desempenho e integração com sistemas de marketing ou CRM. O endpoint suporta paginação e filtragem para facilitar a navegação em grandes conjuntos de dados.


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 3. Visão Geral da API/Endpoint(s)


> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint de listagem de afiliados.


O endpoint de Listar Afiliados fornece acesso aos dados completos de todos os afiliados cadastrados na plataforma Kiwify. Este recurso permite:
- Recuperar informações detalhadas de cada afiliado, incluindo seus dados de contato
- Visualizar produtos associados a cada afiliado
- Consultar valores de comissão configurados
- Filtrar afiliados por status, produto específico ou termo de busca
- Navegar através de resultados paginados para gerenciar grandes volumes de dados


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 4. Detalhes Técnicos


> **Resumo:** Especificações técnicas detalhadas do endpoint, incluindo URL, método HTTP e requisitos de autenticação.


### Endpoint 1: /affiliates


* **Endpoint URL:** `https://public-api.kiwify.com/v1/affiliates`
* **Método HTTP:** `GET`
* **Autenticação:** 
  * Bearer Token no cabeçalho `Authorization: Bearer <token>`
  * ID da conta no cabeçalho `x-kiwify-account-id: <api-key>`


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 5. Parâmetros de Entrada


> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados nas requisições ao endpoint de listagem de afiliados.


### Endpoint 1: /affiliates (Query Parameters)


| Parâmetro        | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :--------------- | :-------- | :--- | :----------- | :-------------- |
| `page_size`      | Número de registros por página | string | Não | Padrão: 10 |
| `page_number`    | Número da página solicitada | string | Não | Padrão: 1 |
| `status`         | Filtro de afiliados pelo status | string | Não | Ex: "active", "pending" |
| `product_id`     | Filtro de afiliados pelo ID do produto | string | Não | Ex: "aaa86f40-d7ae-11ed-acc6-e1c45591a30e" |
| `search`         | Termo de busca para filtrar afiliados | string | Não | Busca por nome ou email |


### Cabeçalhos Obrigatórios


| Parâmetro            | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :------------------- | :-------- | :--- | :----------- | :-------------- |
| `Authorization`      | Token de acesso OAuth 2.0 | string | Sim | Format: "Bearer {token}" |
| `x-kiwify-account-id`| ID da conta Kiwify | string | Sim | Identifica a conta do usuário |


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)


> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint de listagem de afiliados.


### Endpoint 1: /affiliates


#### 6.1.1 Estrutura Geral


| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `pagination`  | Objeto contendo informações de paginação | object |
| `data`        | Array contendo a lista de afiliados | array |


#### 6.1.2 Detalhes do Objeto `pagination`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `count`           | Número total de afiliados disponíveis | number | Total de registros |
| `page_number`     | Número da página atual | number | Começa em 1 |
| `page_size`       | Número de itens por página | number | Quantidade de registros por página |


#### 6.1.3 Detalhes do Array `data` (objetos afiliados)


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `affiliate_id`    | ID único do afiliado | string | Format: UUID |
| `name`            | Nome do afiliado | string | Nome completo |
| `email`           | Email do afiliado | string | Endereço de contato |
| `company_name`    | Nome da empresa do afiliado | string | Pode ser igual ao nome pessoal |
| `director_cpf`    | CPF do diretor da empresa afiliada | string | Formato: números sem formatação |
| `company_cnpj`    | CNPJ da empresa afiliada | string | Pode estar vazio |
| `product`         | Objeto com informações do produto | object | Ver detalhes abaixo |
| `commission`      | Valor de comissão do afiliado | number | Em centavos (4600 = R$ 46,00) |
| `status`          | Status atual do afiliado | string | "active", "pending", etc. |
| `created_at`      | Data de criação do registro | string | Formato ISO 8601 |


#### 6.1.4 Detalhes do Objeto `product`


| Campo Aninhado    | Descrição | Tipo | Notas |
| :---------------- | :-------- | :--- | :---- |
| `id`              | ID único do produto | string | Format: UUID |
| `name`            | Nome do produto | string | Nome do produto associado ao afiliado |


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 7. Exemplos de Requisição e Resposta


> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint de listagem de afiliados.


### Endpoint 1: /affiliates


#### 7.1.1 Exemplo de Requisição (cURL)


```bash
curl --request GET \
  --url 'https://public-api.kiwify.com/v1/affiliates?page_size=10&page_number=1&status=active' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  --header 'x-kiwify-account-id: 5f9b2a1c-3e5d-4f8a-b7c6-9d1a2b3c4d5e'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 200)


```json
{
  "pagination": {
    "count": 10,
    "page_number": 1,
    "page_size": 10
  },
  "data": [
    {
      "affiliate_id": "c52ccea4-2b5a-4d03-b53a-d9dc96756fc0",
      "name": "MY Affiliate",
      "email": "myaffiliate@mail.com",
      "company_name": "MY Affiliate",
      "director_cpf": "99999999999",
      "company_cnpj": "",
      "product": {
        "id": "aaa86f40-d7ae-11ed-acc6-e1c45591a30e",
        "name": "My Product"
      },
      "commission": 4600,
      "status": "active",
      "created_at": "2023-07-24T15:56:26.189Z"
    }
  ]
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro)


```json
{
  "error": {
    "code": "unauthorized",
    "message": "Credenciais de autenticação inválidas ou ausentes",
    "request_id": "req_7f8e9d6c5b4a"
  }
}
```


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 8. Códigos de Status e Tratamento de Erros


> **Resumo:** Descrição completa dos códigos de status HTTP retornados pelo endpoint e como gerenciar erros.


| Status Code               | Descrição Geral                                    |
| :------------------------ | :------------------------------------------------- |
| `200 OK`                  | Sucesso. A requisição foi processada e a lista de afiliados foi retornada. |
| `400 Bad Request`         | Erro na requisição. Parâmetros inválidos ou mal formatados. |
| `401 Unauthorized`        | Falha na autenticação. Token inválido ou expirado. |
| `403 Forbidden`           | Sem permissão. O usuário autenticado não tem acesso a este recurso. |
| `404 Not Found`           | Recurso não encontrado. Endpoint incorreto ou ID inexistente. |
| `429 Too Many Requests`   | Rate Limit excedido. Muitas requisições em curto período. |
| `500 Internal Server Error`| Erro no servidor da API. Problema interno da Kiwify. |


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)


> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint de listagem de afiliados.


1. **Listar todos os afiliados ativos**
   * Objetivo: `Recuperar apenas os afiliados que estão com status ativo no sistema`
   * Como Fazer: `GET /affiliates?status=active`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


2. **Buscar afiliados de um produto específico**
   * Objetivo: `Localizar todos os afiliados associados a um produto particular`
   * Como Fazer: `GET /affiliates?product_id=aaa86f40-d7ae-11ed-acc6-e1c45591a30e`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


3. **Encontrar afiliados por termo de busca**
   * Objetivo: `Localizar afiliados cujo nome ou email contenha um termo específico`
   * Como Fazer: `GET /affiliates?search=marketing`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


4. **Paginar resultados de afiliados**
   * Objetivo: `Recuperar um conjunto grande de afiliados dividido em páginas gerenciáveis`
   * Como Fazer: `GET /affiliates?page_size=20&page_number=2`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


5. **Combinar múltiplos filtros para afiliados**
   * Objetivo: `Encontrar afiliados que atendam a múltiplos critérios simultaneamente`
   * Como Fazer: `GET /affiliates?status=active&product_id=aaa86f40-d7ae-11ed-acc6-e1c45591a30e`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


6. **Listar todos os afiliados pendentes**
   * Objetivo: `Recuperar afiliados com status pendente que requerem aprovação`
   * Como Fazer: `GET /affiliates?status=pending`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


7. **Obter primeira página com tamanho personalizado**
   * Objetivo: `Recuperar os primeiros N afiliados com tamanho de página específico`
   * Como Fazer: `GET /affiliates?page_size=50&page_number=1`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


8. **Encontrar afiliados por nome específico**
   * Objetivo: `Localizar afiliados que contenham um nome específico`
   * Como Fazer: `GET /affiliates?search=João Silva`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


9. **Listar afiliados organizados por produto e status**
   * Objetivo: `Obter afiliados de um produto específico com status determinado`
   * Como Fazer: `GET /affiliates?product_id=aaa86f40-d7ae-11ed-acc6-e1c45591a30e&status=active`
   *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


10. **Buscar afiliados por domínio de email**
    * Objetivo: `Encontrar afiliados que usam um domínio de email específico`
    * Como Fazer: `GET /affiliates?search=@empresa.com.br`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


11. **Visualizar todos os afiliados em blocos pequenos**
    * Objetivo: `Obter afiliados em pequenos conjuntos para processamento leve`
    * Como Fazer: `GET /affiliates?page_size=5&page_number=1 (incrementando page_number)`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


12. **Encontrar afiliados recém-cadastrados**
    * Objetivo: `Localizar os afiliados mais recentes através de paginação ordenada`
    * Como Fazer: `GET /affiliates?page_size=10&page_number=1 (assumindo ordenação padrão por created_at desc)`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


13. **Verificar total de afiliados no sistema**
    * Objetivo: `Obter a contagem total de afiliados disponíveis`
    * Como Fazer: `GET /affiliates?page_size=1&page_number=1 (verificar pagination.count na resposta)`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


14. **Filtrar afiliados inativos para reativação**
    * Objetivo: `Encontrar afiliados com status inativo para campanha de reativação`
    * Como Fazer: `GET /affiliates?status=inactive`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


15. **Buscar afiliados pessoas jurídicas (com CNPJ)**
    * Objetivo: `Encontrar afiliados que são empresas com CNPJ cadastrado`
    * Como Fazer: `GET /affiliates?search=CNPJ (ou filtro específico se disponível)`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


16. **Navegar por todas as páginas de resultados**
    * Objetivo: `Percorrer sistematicamente todas as páginas de resultados de afiliados`
    * Como Fazer: `GET /affiliates?page_size=100&page_number=1, depois 2, 3... até pagination.count`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


17. **Encontrar afiliados para múltiplos produtos**
    * Objetivo: `Obter sequencialmente afiliados de diferentes produtos`
    * Como Fazer: `GET /affiliates?product_id=produto1, depois product_id=produto2`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


18. **Verificar existência de um afiliado específico**
    * Objetivo: `Confirmar se um determinado email está cadastrado como afiliado`
    * Como Fazer: `GET /affiliates?search=email@especifico.com`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


19. **Obter afiliados com maior comissão**
    * Objetivo: `Identificar afiliados com valores de comissão mais altos`
    * Como Fazer: `GET /affiliates (e ordenar os resultados pelo campo commission)`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


20. **Listar afiliados para exportação de dados**
    * Objetivo: `Recuperar todos os afiliados em lotes grandes para exportação`
    * Como Fazer: `GET /affiliates?page_size=100&page_number=N (iterando até obter todos)`
    *(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 10. Notas Adicionais


> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint de listagem de afiliados.


* **Rate Limits:** `A documentação oficial não especifica limites de taxa para este endpoint. Recomenda-se implementar backoff exponencial para retentativas em caso de erros 429.`


* **Paginação:** `O endpoint suporta paginação através dos parâmetros page_size e page_number. O valor máximo de page_size não é documentado, mas recomenda-se usar valores entre 10 e 100 para melhor desempenho.`


* **Formatos de Data:** `Todas as datas são retornadas no formato ISO 8601 (YYYY-MM-DDTHH:MM:SS.sssZ).`


* **Valores de Comissão:** `Os valores de comissão são retornados em centavos. Por exemplo, 4600 representa R$ 46,00.`


* **Filtros Combinados:** `Múltiplos filtros (status, product_id, search) podem ser utilizados simultaneamente para refinar os resultados.`


* **Campos Sensíveis:** `O endpoint retorna dados pessoais como CPF e CNPJ que devem ser tratados conforme a LGPD e outras regulamentações de privacidade aplicáveis.`


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)


> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.


```json
{
  "doc_id": "kiwify_affil_001",
  "api_provider": "Kiwify",
  "api_product_area": "Afiliados",
  "endpoint_focus": ["Listar Afiliados"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "Medium",
  "business_impact": "Médio",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Afiliados", "Produtos"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["afiliados", "marketing", "comissões"],
  "db_relations": { 
    "tables": ["affiliates", "products"], 
    "schemas": ["public"] 
  },
  "related_concepts": ["programa de afiliados", "comissões", "marketing", "produtos"],
  "question_embeddings": [
    "Como listar todos os afiliados da minha conta Kiwify?",
    "Como filtrar afiliados por produto específico?",
    "Qual formato de dados é retornado ao listar afiliados?",
    "Como paginar resultados ao consultar afiliados?",
    "Como obter afiliados com status específico na Kiwify?"
  ],
  "reasoning_pathways": ["conditional", "sequential"],
  "typical_usage_frequency": "Média",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "x-kiwify-account-id"],
  "typical_integration_points": ["CRM", "Sistemas de Marketing", "Dashboards de Afiliados"],
  "common_error_patterns": ["authentication_failure", "invalid_parameters", "rate_limit_exceeded"]
}
```


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 12. Checklist de Implementação (Opcional)


> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação do endpoint de listagem de afiliados.


- [ ] Autenticação
  - [ ] Implementar mecanismo de obtenção do token OAuth
  - [ ] Configurar renovação automática do token expirado
  - [ ] Gerenciar o cabeçalho x-kiwify-account-id


- [ ] Tratamento de Erros (4xx, 5xx)
  - [ ] Implementar handlers para cada código de erro relevante
  - [ ] Adicionar logging detalhado para debug
  - [ ] Apresentar mensagens de erro amigáveis ao usuário final


- [ ] Retries (429, 5xx)
  - [ ] Implementar backoff exponencial
  - [ ] Definir número máximo de tentativas
  - [ ] Adicionar jitter para evitar sincronização de retentativas


- [ ] Paginação
  - [ ] Implementar suporte a parâmetros page_size e page_number
  - [ ] Armazenar estado de paginação para iteração completa
  - [ ] Gerenciar fim de resultados (verificar pagination.count)


- [ ] Validação de Entrada
  - [ ] Validar formatos dos parâmetros de filtro
  - [ ] Verificar valores permitidos para status
  - [ ] Tratar campos obrigatórios vs. opcionais


- [ ] Mapeamento de Resposta
  - [ ] Converter datas para formato padrão da aplicação
  - [ ] Mapear valores de comissão de centavos para decimal
  - [ ] Implementar modelo de dados para afiliados


- [ ] Logs & Monitoramento
  - [ ] Registrar tempo de resposta de cada chamada
  - [ ] Monitorar taxa de erros
  - [ ] Implementar rastreamento de requisições (request_id)


- [ ] Cache
  - [ ] Implementar cache para resultados frequentes
  - [ ] Definir tempo de expiração apropriado
  - [ ] Implementar invalidação de cache em operações de escrita


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 13. Glossário de Termos Técnicos


> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados na documentação.


| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Afiliado`                | `Pessoa ou empresa que promove produtos de terceiros e recebe comissão por vendas geradas` |
| `Token de Autenticação`   | `Credencial de segurança temporária usada para autorizar requisições à API da Kiwify` |
| `Rate Limit`              | `Número máximo de requisições permitidas em um período de tempo específico` |
| `Paginação`               | `Técnica para dividir conjuntos grandes de resultados em páginas gerenciáveis` |
| `Status do Afiliado`      | `Estado atual do afiliado no sistema (active, pending, etc.)` |
| `Comissão`                | `Valor ou percentual que o afiliado recebe por cada venda realizada` |
| `CPF`                     | `Cadastro de Pessoas Físicas - documento de identificação fiscal de pessoas físicas no Brasil` |
| `CNPJ`                    | `Cadastro Nacional de Pessoa Jurídica - documento de identificação fiscal de empresas no Brasil` |
| `UUID`                    | `Identificador Único Universal - formato de ID utilizado pela Kiwify para identificação de recursos` |
| `ISO 8601`                | `Padrão internacional para representação de datas e horas` |


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---


## 14. Observações Finais sobre Formatação


> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.


*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados e comparativos.
*   Use blocos de código (``` ```) com indicação de linguagem para exemplos de código e JSON.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa.
*   Formate nomes de parâmetros, campos e valores de exemplo com backticks (`exemplo`).
*   **Crucial:** Inclua `(Ref: [TITULO_CURTO], ID [ID_INTERNO])` no final de **CADA SEÇÃO PRINCIPAL (##)** e opcionalmente em subitens/chunks.
*   Mantenha os resumos de seção concisos (1-2 linhas) e informativos.
*   Use listas e bullets para informações sequenciais ou enumeradas.
*   Evite abreviações não explicadas ou jargão não definido no documento.


*(Ref: Kiwify List Affiliates, ID kiwify_listaffiliates_001)*
---