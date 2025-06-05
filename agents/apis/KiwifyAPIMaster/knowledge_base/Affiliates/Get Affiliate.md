# API Kiwify - Afiliados - Consultar Afiliado (Get Affiliate)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Afiliados - Consultar Afiliado (Get Affiliate)`   |
| **Identificador Interno** | `kiwify_aff_001`                                                |
| **Título Curto (Ref.)**   | `Kiwify Get Affiliate`                                          |
| **Versão do Documento**   | `1.0.0`                                                         |
| **Data de Criação**       | `2025-04-15`                                                    |
| **Última Atualização**    | `2025-04-15`                                                    |
| **Autor/Responsável**     | `Equipe de Documentação`                                        |
| **Fonte Original**        | `https://docs.kiwify.com.br/api-reference/affiliates/single`    |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/affiliates/single`    |
| **Status do Documento**   | `Em Uso`                                                        |
| **Ambiente de Referência**| `Produção`                                                      |
| **Idioma Original**       | `Português (BR)`                                                |
| **Formato de Datas (API)**| `ISO 8601`                                                      |




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 2. Contexto




> **Resumo:** Este endpoint permite a recuperação de informações detalhadas de um afiliado específico em plataformas de marketing digital e vendas de produtos.




Este endpoint fornece acesso detalhado às informações de um afiliado específico na plataforma Kiwify, facilitando a integração com sistemas de CRM, dashboards analíticos e ferramentas de gestão de relacionamento. A API permite que desenvolvedores acessem detalhes como nome, email, informações fiscais e configurações de comissão do afiliado. Este documento refere-se ao ID Interno: kiwify_aff_001.




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 3. Visão Geral da API/Endpoint(s)




> **Resumo:** Visão geral do endpoint de consulta de afiliados, que permite recuperar informações detalhadas de um afiliado específico.




Este endpoint permite a consulta dos detalhes completos de um afiliado específico, utilizando seu identificador único (affiliate_id) como parâmetro de busca. O endpoint retorna informações de identificação pessoal, detalhes de contato, configurações de comissão e relacionamentos com produtos, permitindo a visualização completa dos dados do afiliado para análise, integração ou validação.




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 4. Detalhes Técnicos




> **Resumo:** Especificações técnicas detalhadas do endpoint de consulta de afiliado, incluindo URL, método HTTP e requisitos de autenticação.




### `Endpoint 1: /affiliates/{id}`




*   **Endpoint URL:** `https://public-api.kiwify.com/v1/affiliates/{id}`
*   **Método HTTP:** `GET`
*   **Autenticação:** `Requer o cabeçalho 'Authorization' com Bearer Token obtido via OAuth 2.0 e o cabeçalho 'x-kiwify-account-id' com a chave da API.`




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 5. Parâmetros de Entrada




> **Resumo:** Detalhamento de todos os parâmetros que podem ser enviados nas requisições ao endpoint de consulta de afiliado.




### `Endpoint 1: /affiliates/{id}` (`Path Parameters`)




| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `id` (Path)        | Identificador único do afiliado a ser consultado. | string | Sim | ex: "c52ccea4-2b5a-4d03-b53a-d9dc96756fc0" |




### `Endpoint 1: /affiliates/{id}` (`Header Parameters`)




| Parâmetro          | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :----------------- | :-------- | :--- | :----------- | :-------------- |
| `Authorization`    | Token de acesso obtido através do fluxo OAuth 2.0. | string | Sim | ex: "Bearer eyJhbGci..." |
| `x-kiwify-account-id` | Chave da API que identifica a conta Kiwify. | string | Sim | ex: "acc_abc123" |




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)




> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint de consulta de afiliado nas respostas bem-sucedidas.




### `Endpoint 1: /affiliates/{id}`




#### 6.1.1 Estrutura Geral




| Campo              | Descrição | Tipo   |
| :----------------- | :-------- | :----- |
| `affiliate_id`     | Identificador único do afiliado. | string |
| `name`             | Nome completo do afiliado. | string |
| `email`            | Endereço de email do afiliado. | string |
| `company_name`     | Nome da empresa do afiliado, quando aplicável. | string |
| `director_cpf`     | CPF do diretor da empresa afiliada. | string |
| `company_cnpj`     | CNPJ da empresa afiliada, quando aplicável. | string |
| `product`          | Objeto contendo informações do produto associado ao afiliado. | object |
| `commission`       | Valor da comissão configurada para o afiliado, em centavos. | number |
| `status`           | Status atual do afiliado na plataforma. | string |
| `created_at`       | Data e hora de criação do registro do afiliado. | string (ISO 8601) |




#### 6.1.2 Detalhes do Objeto `product`




| Campo Aninhado     | Descrição | Tipo | Notas |
| :----------------- | :-------- | :--- | :---- |
| `id`               | Identificador único do produto. | string | ex: "aaa86f40-d7ae-11ed-acc6-e1c45591a30e" |
| `name`             | Nome do produto associado ao afiliado. | string | ex: "My Product" |




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 7. Exemplos de Requisição e Resposta




> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint de consulta de afiliado.




### `Endpoint 1: /affiliates/{id}`




#### 7.1.1 Exemplo de Requisição (cURL)




```bash
curl --request GET \
  --url https://public-api.kiwify.com/v1/affiliates/c52ccea4-2b5a-4d03-b53a-d9dc96756fc0 \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  --header 'x-kiwify-account-id: acc_28a9d8f53b7e'
```




#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)




```json
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
```




#### 7.1.3 Exemplo de Resposta (JSON - Erro)




```json
{
  "error": {
    "code": "affiliate_not_found",
    "message": "O afiliado solicitado não foi encontrado",
    "request_id": "req_58f7d2c9a14b"
  }
}
```




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 8. Códigos de Status e Tratamento de Erros




> **Resumo:** Descrição completa dos códigos de status HTTP retornados pelo endpoint de consulta de afiliado e como gerenciar erros.




| Status Code               | Descrição Geral                                    |
| :------------------------ | :------------------------------------------------- |
| `200 OK`                  | Sucesso. A requisição foi processada e os detalhes do afiliado foram retornados. |
| `400 Bad Request`         | Erro na requisição. Parâmetros ausentes ou inválidos. |
| `401 Unauthorized`        | Falha na autenticação. Token inválido ou expirado. |
| `403 Forbidden`           | Sem permissão. A conta não tem acesso a este recurso. |
| `404 Not Found`           | Afiliado não encontrado com o ID especificado. |
| `429 Too Many Requests`   | Rate Limit excedido. Aguarde antes de fazer novas solicitações. |
| `500 Internal Server Error`| Erro no servidor da API. Contate o suporte se persistir. |




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)




> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint de consulta de afiliado.




1.  **Endpoint 1: Verificar dados cadastrais de um afiliado específico**
    *   Objetivo: `Recuperar informações de identificação e contato de um afiliado para validação`
    *   Como Fazer: `GET /affiliates/{id} onde {id} é o identificador único do afiliado`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




2.  **Endpoint 1: Consultar taxa de comissão configurada para um afiliado**
    *   Objetivo: `Verificar qual o percentual ou valor fixo de comissão definido para o afiliado`
    *   Como Fazer: `GET /affiliates/{id} e analisar o campo "commission" na resposta`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




3.  **Endpoint 1: Verificar qual produto está associado ao afiliado**
    *   Objetivo: `Identificar qual produto específico o afiliado está autorizado a promover`
    *   Como Fazer: `GET /affiliates/{id} e examinar o objeto "product" na resposta`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




4.  **Endpoint 1: Consultar status atual do afiliado**
    *   Objetivo: `Verificar se o afiliado está ativo, pendente, suspenso ou em outro estado`
    *   Como Fazer: `GET /affiliates/{id} e analisar o campo "status" na resposta`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




5.  **Endpoint 1: Recuperar dados fiscais de um afiliado para fins contábeis**
    *   Objetivo: `Obter CNPJ e CPF do afiliado para emissão de documentos fiscais`
    *   Como Fazer: `GET /affiliates/{id} e verificar os campos "company_cnpj" e "director_cpf"`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




6.  **Endpoint 1: Verificar quando um afiliado foi cadastrado no sistema**
    *   Objetivo: `Determinar a data exata em que o afiliado foi registrado na plataforma`
    *   Como Fazer: `GET /affiliates/{id} e analisar o campo "created_at" na resposta`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




7.  **Endpoint 1: Exportar dados de um afiliado para um CRM externo**
    *   Objetivo: `Integrar informações do afiliado com um sistema de CRM de terceiros`
    *   Como Fazer: `GET /affiliates/{id} e mapear os campos retornados para o formato do CRM`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




8.  **Endpoint 1: Sincronizar informações de contato do afiliado**
    *   Objetivo: `Manter um sistema externo atualizado com os dados de contato mais recentes`
    *   Como Fazer: `GET /affiliates/{id} periodicamente e atualizar o sistema externo`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




9.  **Endpoint 1: Verificar detalhes completos após receber notificação de webhook**
    *   Objetivo: `Obter dados completos do afiliado após receber um evento de atualização`
    *   Como Fazer: `GET /affiliates/{id} quando um webhook notificar mudanças no afiliado`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




10. **Endpoint 1: Validar existência de um afiliado antes de atribuir uma venda**
    *   Objetivo: `Confirmar que o afiliado ainda existe e está ativo antes de registrar comissão`
    *   Como Fazer: `GET /affiliates/{id} e verificar se o status é "active"`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




11. **Endpoint 1: Construir painel administrativo com dados de afiliados**
    *   Objetivo: `Exibir informações detalhadas de cada afiliado em um dashboard personalizado`
    *   Como Fazer: `GET /affiliates/{id} para cada afiliado a ser exibido no painel`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




12. **Endpoint 1: Verificar dados para geração de contrato de afiliação**
    *   Objetivo: `Coletar informações necessárias para gerar um contrato legal de afiliação`
    *   Como Fazer: `GET /affiliates/{id} e extrair nome, empresa, CPF/CNPJ e demais dados relevantes`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




13. **Endpoint 1: Confirmar associação entre afiliado e produto específico**
    *   Objetivo: `Validar se o afiliado está autorizado a promover um produto em particular`
    *   Como Fazer: `GET /affiliates/{id} e comparar product.id com o ID do produto em questão`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




14. **Endpoint 1: Auditar informações de afiliados para conformidade legal**
    *   Objetivo: `Verificar dados para garantir conformidade com requisitos regulatórios`
    *   Como Fazer: `GET /affiliates/{id} para cada afiliado envolvido no processo de auditoria`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




15. **Endpoint 1: Recuperar email do afiliado para comunicação direta**
    *   Objetivo: `Obter endereço de email atual para envio de comunicados ou relatórios`
    *   Como Fazer: `GET /affiliates/{id} e extrair o campo "email" da resposta`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




16. **Endpoint 1: Verificar dados para cálculo de impostos sobre comissões**
    *   Objetivo: `Obter informações fiscais necessárias para calcular retenções de impostos`
    *   Como Fazer: `GET /affiliates/{id} e analisar os campos com dados fiscais (CNPJ/CPF)`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




17. **Endpoint 1: Integrar dados do afiliado com sistema de pagamentos**
    *   Objetivo: `Sincronizar informações do afiliado com uma plataforma de processamento de pagamentos`
    *   Como Fazer: `GET /affiliates/{id} e utilizar os dados para configurar destinatário de pagamentos`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




18. **Endpoint 1: Validar nome da empresa do afiliado para emissão de documentos**
    *   Objetivo: `Confirmar o nome correto da empresa para inclusão em relatórios e documentos oficiais`
    *   Como Fazer: `GET /affiliates/{id} e extrair o campo "company_name"`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




19. **Endpoint 1: Recuperar detalhes para personalização de portal do afiliado**
    *   Objetivo: `Obter dados para customizar interface de usuário baseada no perfil do afiliado`
    *   Como Fazer: `GET /affiliates/{id} e utilizar nome, produto associado e outros dados para personalização`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




20. **Endpoint 1: Verificar consistência de dados após migração de sistema**
    *   Objetivo: `Comparar dados do afiliado entre sistemas para garantir integridade após migração`
    *   Como Fazer: `GET /affiliates/{id} e comparar com os dados armazenados no sistema legado`
    *(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 10. Notas Adicionais




> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint de consulta de afiliado.




*   **Privacidade de Dados:** `Este endpoint retorna dados pessoais e fiscais de afiliados (CPF, CNPJ, email). Garanta que sua aplicação processe esses dados de acordo com a LGPD e outras regulamentações de privacidade aplicáveis.`




*   **Formatos de Comissão:** `O valor no campo "commission" é expresso em centavos. Para obter o valor em reais, divida por 100. Por exemplo, 4600 representa R$ 46,00.`




*   **Campos Vazios:** `Campos como "company_cnpj" podem estar vazios ("") quando não aplicáveis ao tipo de afiliado. Sua aplicação deve lidar adequadamente com esses casos.`




*   **Data de Criação:** `O campo "created_at" segue o formato ISO 8601 completo com timezone UTC. Certifique-se de converter para o fuso horário local se necessário para exibição.`




*   **Cache:** `As respostas deste endpoint podem ser cacheadas por curtos períodos (1-5 minutos) para reduzir chamadas à API, desde que sua aplicação possa tolerar dados ligeiramente desatualizados.`




*   **Integração com Webhooks:** `Para um sistema mais eficiente, considere usar os webhooks da Kiwify para receber notificações de alterações nos afiliados, e então use este endpoint apenas para obter os detalhes completos atualizados.`




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)




> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.




```json
{
  "doc_id": "kiwify_aff_001",
  "api_provider": "Kiwify",
  "api_product_area": "Afiliados",
  "endpoint_focus": ["Consultar Afiliado", "Obter Detalhes de Afiliado"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "Medium",
  "business_impact": "Médio",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Afiliado", "Produto"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["afiliados", "marketing digital", "comissões"],
  "db_relations": { 
    "tables": ["affiliates", "products"], 
    "schemas": ["public", "kiwify"] 
  },
  "related_concepts": ["programa de afiliados", "comissão", "marketing de afiliados", "produtos digitais"],
  "question_embeddings": [
    "Como consultar os dados de um afiliado na Kiwify?",
    "Qual o formato dos dados de comissão de afiliados na API da Kiwify?",
    "Como verificar o status de um afiliado na plataforma Kiwify?",
    "Quais campos fiscais são retornados na consulta de afiliados?",
    "Como integrar dados de afiliados da Kiwify com sistemas externos?"
  ],
  "reasoning_pathways": ["conditional", "sequential"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "API Key"],
  "typical_integration_points": ["CRM", "Sistema de Pagamentos", "Dashboard"],
  "common_error_patterns": ["affiliate_not_found", "invalid_authorization"]
}
```




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 12. Checklist de Implementação (Opcional)




> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação do endpoint de consulta de afiliado.




- [ ] Autenticação
  - [ ] Implementar mecanismo de obtenção do token OAuth
  - [ ] Configurar renovação automática do token expirado
  - [ ] Gerenciar de forma segura a chave da API (x-kiwify-account-id)




- [ ] Tratamento de Erros (4xx, 5xx)
  - [ ] Implementar handlers para 404 (afiliado não encontrado)
  - [ ] Adicionar logging detalhado para debug
  - [ ] Apresentar mensagens de erro amigáveis ao usuário final




- [ ] Retries (429, 5xx)
  - [ ] Implementar backoff exponencial
  - [ ] Definir número máximo de tentativas
  - [ ] Adicionar jitter para evitar sincronização de retentativas




- [ ] Validação de Entrada
  - [ ] Validar formato do ID do afiliado antes da requisição
  - [ ] Verificar presença dos cabeçalhos obrigatórios
  - [ ] Sanitizar dados de entrada para evitar injeção




- [ ] Mapeamento de Resposta
  - [ ] Converter formato de data para padrão da aplicação
  - [ ] Mapear campos para modelos internos
  - [ ] Formatar valor de comissão de centavos para formato de exibição




- [ ] Logs & Monitoramento
  - [ ] Registrar tempo de resposta de cada chamada
  - [ ] Monitorar taxa de erros
  - [ ] Implementar rastreamento de requisições (request_id)




- [ ] Cache
  - [ ] Implementar cache para resultados frequentes
  - [ ] Definir estratégias de invalidação
  - [ ] Respeitar cabeçalhos Cache-Control




- [ ] Testes (Casos normais, Edge-cases)
  - [ ] Criar testes unitários para mappers
  - [ ] Implementar testes de integração com mock
  - [ ] Verificar cenários de erro e exceção




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
---


## 13. Glossário de Termos Técnicos




> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados na documentação.




| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `Afiliado`                | `Pessoa ou empresa registrada para promover e vender produtos de terceiros na plataforma, recebendo comissão pelas vendas realizadas` |
| `Token de Autenticação`   | `Credencial de segurança temporária usada para autorizar requisições à API Kiwify` |
| `Comissão`                | `Valor ou percentual a ser pago ao afiliado por cada venda realizada através de sua indicação` |
| `Produto`                 | `Item digital ou serviço disponibilizado para venda na plataforma Kiwify` |
| `CNPJ`                    | `Cadastro Nacional da Pessoa Jurídica, registro de empresas brasileiras` |
| `CPF`                     | `Cadastro de Pessoas Físicas, registro de identificação fiscal de cidadãos brasileiros` |
| `Status do Afiliado`      | `Estado atual do afiliado na plataforma (ativo, pendente, suspenso, etc.)` |
| `OAuth 2.0`               | `Protocolo de autorização que permite que aplicações terceiras acessem recursos em nome de um usuário` |
| `Bearer Token`            | `Tipo de token de acesso utilizado no header Authorization para autenticar requisições` |
| `ISO 8601`                | `Padrão internacional para representação de datas e horas (YYYY-MM-DDTHH:MM:SSZ)` |




*(Ref: Kiwify Get Affiliate, ID kiwify_getaffiliate_001)*
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




**(FIM DO TEMPLATE PADRÃO)**