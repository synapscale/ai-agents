# API Kiwify - Contas - Consultar Detalhes da Conta (Account Details)




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | `API Kiwify - Contas - Consultar Detalhes da Conta (Account Details)` |
| **Identificador Interno** | `kiwify_acc_001`                   |
| **Título Curto (Ref.)**   | `Kiwify Account Details`           |
| **Versão do Documento**   | `1.0.2`                                |
| **Data de Criação**       | `2025-04-11`                                                  |
| **Última Atualização**    | `2025-04-11`                                                  |
| **Autor/Responsável**     | `Equipe de Documentação Técnica`                                    |
| **Fonte Original**        | `https://docs.kiwify.com.br/api-reference/account/account-details`  |
| **URL de Referência**     | `https://docs.kiwify.com.br/api-reference/account/account-details` |
| **Status do Documento**   | `Em Uso`                              |
| **Ambiente de Referência**| `Produção`                                |
| **Idioma Original**       | `Português (BR)`                                  |
| **Formato de Datas (API)**| `ISO 8601 (YYYY-MM-DDTHH:MM:SS.mmmZ)` |




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 2. Contexto




> **Resumo:** Esta seção descreve o propósito e o contexto mais amplo do endpoint de consulta de detalhes da conta dentro do ecossistema Kiwify.




Este endpoint (`/v1/account-details`) é fundamental para integrações com a plataforma Kiwify, pois permite obter informações detalhadas sobre uma conta específica. Ele serve como base para verificar dados cadastrais, validar informações fiscais, e entender a estrutura de entidades legais associadas a uma conta. O acesso a esses detalhes é crucial para sistemas externos que precisam sincronizar dados, realizar verificações de compliance, ou apresentar informações consolidadas da conta Kiwify. 


As informações retornadas incluem dados sensíveis como CPF e CNPJ, o que torna este endpoint particularmente importante do ponto de vista de segurança e conformidade com regulamentações como a LGPD. Sistemas integrados podem usar esses dados para validar a identidade da conta, configurar recebimentos via PIX, ou sincronizar informações de contato e fiscais com sistemas ERP, CRM ou de faturamento.




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 3. Visão Geral da API/Endpoint(s)




> **Resumo:** Visão de alto nível sobre a funcionalidade e escopo do endpoint de consulta de detalhes da conta.




O endpoint `GET /v1/account-details` fornece uma visão completa dos dados cadastrais de uma conta específica na plataforma Kiwify. Ele retorna informações como o identificador único da conta (`id`), nome da empresa (`company_name`), documentos fiscais do diretor (`director_cpf`) e da empresa (`company_cnpj`), além de uma lista detalhada das entidades legais (`legal_entities`) associadas, incluindo seus próprios identificadores, status, dados fiscais e chave PIX.


Este endpoint é exclusivamente para leitura (método GET) e não modifica nenhum dado no sistema. Ele requer autenticação OAuth 2.0 e exige que o solicitante especifique qual conta está consultando através do cabeçalho personalizado `x-kiwify-account-id`. As respostas são sempre em formato JSON com estrutura consistente, tornando simples a integração com sistemas de terceiros.




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 4. Detalhes Técnicos




> **Resumo:** Especificações técnicas detalhadas do endpoint, incluindo URL, método HTTP e requisitos de autenticação.




### Endpoint: `/v1/account-details`




*   **Endpoint URL:** `https://public-api.kiwify.com/v1/account-details`
*   **Método HTTP:** `GET`
*   **Autenticação:** Requer um token de acesso OAuth 2.0 válido no cabeçalho `Authorization` (formato `Bearer {token}`) e o identificador da conta alvo no cabeçalho `x-kiwify-account-id`.
*   **Tipo de Conteúdo:** Aceita e retorna conteúdo no formato `application/json`.
*   **Codificação:** UTF-8
*   **Versão da API:** v1




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 5. Parâmetros de Entrada




> **Resumo:** Detalhamento de todos os parâmetros que devem ser enviados nas requisições ao endpoint (neste caso, cabeçalhos).




### Endpoint: `/v1/account-details` (Headers)




| Parâmetro           | Descrição | Tipo | Obrigatório? | Notas / Exemplo |
| :------------------ | :-------- | :--- | :----------- | :-------------- |
| `Authorization`     | Token de acesso OAuth 2.0 obtido no processo de autorização. | string | Sim | Deve seguir o formato `Bearer {SEU_TOKEN}`. Ex: `Bearer eyJhbGciOi...` |
| `x-kiwify-account-id` | Identificador único da conta Kiwify cujos detalhes serão consultados. | string | Sim | Ex: `XvS0qfkdzCZTg8z` |
| `Content-Type`      | Tipo de conteúdo da requisição. | string | Não (padrão) | Use `application/json` |
| `Accept`            | Formato de resposta desejado. | string | Não (padrão) | Use `application/json` |




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 6. Parâmetros de Saída (Estrutura da Resposta JSON)




> **Resumo:** Documentação completa da estrutura de dados retornada pelo endpoint em respostas bem-sucedidas (200 OK).




### Endpoint: `/v1/account-details`




#### 6.1.1 Estrutura Geral da Resposta




| Campo             | Descrição | Tipo   | Notas |
| :---------------- | :-------- | :----- | :---- |
| `id`              | Identificador único da conta consultada. | string | Identificador alfanumérico da conta Kiwify. |
| `company_name`    | Nome da empresa associada à conta principal. | string | Nome oficial da empresa como registrado na plataforma. |
| `director_cpf`    | CPF (sem formatação) do diretor ou responsável pela conta. | string | Apenas dígitos, sem pontos ou traços. |
| `company_cnpj`    | CNPJ (sem formatação) da empresa associada à conta principal. | string | Apenas dígitos, sem pontos, traços ou barra. Pode ser vazio se não aplicável/cadastrado. |
| `legal_entities`  | Array contendo objetos que representam as entidades legais associadas à conta. | array (de objetos) | Pode conter zero ou mais entidades legais. Veja detalhes abaixo. |




#### 6.1.2 Detalhes do Objeto `legal_entities` (dentro do array)




| Campo Aninhado        | Descrição | Tipo | Notas |
| :-------------------- | :-------- | :--- | :---- |
| `id`                  | Identificador único (UUID) da entidade legal. | string | Formato UUID padrão (36 caracteres, incluindo hifens). |
| `active`              | Indica se a entidade legal está ativa (`true`) ou inativa (`false`). | boolean | Entidades inativas (`false`) não devem ser usadas para transações. |
| `company_name`        | Nome da empresa registrada para esta entidade legal. | string | Pode ser diferente do nome da conta principal. |
| `director_cpf`        | CPF (sem formatação) do diretor associado a esta entidade legal. | string | Apenas dígitos, sem pontos ou traços. Pode ser diferente do CPF da conta principal. |
| `company_cnpj`        | CNPJ (sem formatação) da empresa para esta entidade legal. | string | Apenas dígitos, sem formatação. Pode ser vazio se a entidade for baseada apenas em CPF. |
| `pix_key`             | Chave PIX registrada para esta entidade legal. | string | Pode ser um email, telefone, CPF, CNPJ ou chave aleatória. |
| `created_at`          | Data e hora de criação do registro da entidade legal. | string | Formato ISO 8601 (UTC). Ex: `2023-05-31T12:23:59.746Z` |
| `updated_at`          | Data e hora da última atualização do registro da entidade legal. | string | Formato ISO 8601 (UTC). Ex: `2023-09-27T18:10:37.697Z` |




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 7. Exemplos de Requisição e Resposta




> **Resumo:** Exemplos práticos e completos de como construir requisições e interpretar respostas para o endpoint `/v1/account-details`.




### Endpoint: `/v1/account-details`




#### 7.1.1 Exemplo de Requisição (cURL)




```bash
# Substitua {SEU_TOKEN} pelo seu token Bearer válido
# Substitua {ID_DA_CONTA} pelo ID da conta alvo
curl --request GET \
  --url https://public-api.kiwify.com/v1/account-details \
  --header 'Authorization: Bearer {SEU_TOKEN}' \
  --header 'x-kiwify-account-id: {ID_DA_CONTA}' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json'
```




#### 7.1.2 Exemplo de Requisição (JavaScript/Fetch)




```javascript
// Substitua os valores das variáveis pelo seu token e ID da conta
const token = 'seu_token_oauth';
const accountId = 'id_da_conta_kiwify';


fetch('https://public-api.kiwify.com/v1/account-details', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`,
    'x-kiwify-account-id': accountId,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }
  return response.json();
})
.then(data => console.log(data))
.catch(error => console.error('Erro na requisição:', error));
```




#### 7.1.3 Exemplo de Resposta (JSON - Sucesso 200 OK)




```json
{
  "id": "XvS0qfkdzCZTg8z",
  "company_name": "Minha Empresa Fantástica LTDA",
  "director_cpf": "11122233344",
  "company_cnpj": "12345678000199",
  "legal_entities": [
    {
      "id": "d644de3d-9a02-46b1-aed4-72785fe8828f",
      "active": true,
      "company_name": "Minha Empresa Fantástica LTDA",
      "director_cpf": "11122233344",
      "company_cnpj": "12345678000199",
      "pix_key": "chave.pix@email.com",
      "created_at": "2023-05-31T12:23:59.746Z",
      "updated_at": "2023-09-27T18:10:37.697Z"
    },
    {
      "id": "a1b2c3d4-e5f6-7890-1234-56789abcdef0",
      "active": false,
      "company_name": "Outra Filial Inativa",
      "director_cpf": "99988877766",
      "company_cnpj": "",
      "pix_key": "99988877766",
      "created_at": "2022-11-15T10:00:00.000Z",
      "updated_at": "2023-01-20T15:30:00.000Z"
    }
  ]
}
```




#### 7.1.4 Exemplo de Resposta (JSON - Erro 401 Unauthorized)




```json
{
  "error": {
    "code": "unauthorized",
    "message": "Token de acesso inválido ou expirado.",
    "request_id": "req_kwi_abc123xyz789"
  }
}
```




#### 7.1.5 Exemplo de Resposta (JSON - Erro 404 Not Found)




```json
{
  "error": {
    "code": "account_not_found",
    "message": "A conta especificada não foi encontrada.",
    "request_id": "req_kwi_def456uvw321"
  }
}
```




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 8. Códigos de Status e Tratamento de Erros




> **Resumo:** Descrição completa dos códigos de status HTTP retornados pelo endpoint e como gerenciar erros comuns.




| Status Code               | Descrição Geral                                    | Ação Recomendada | Exemplo de Resposta |
| :------------------------ | :------------------------------------------------- | :--------------- | :------------------ |
| `200 OK`                  | Sucesso. A requisição foi processada com sucesso e os detalhes da conta foram retornados no corpo da resposta. | Processar os dados retornados conforme necessário. | Ver exemplo 7.1.3 |
| `400 Bad Request`         | Erro na requisição. Geralmente indica um problema com os cabeçalhos enviados (formato inválido). | Verificar a formatação dos cabeçalhos `Authorization` e `x-kiwify-account-id`. | `{"error":{"code":"invalid_request","message":"Formato de cabeçalho inválido","request_id":"req_..."}}` |
| `401 Unauthorized`        | Falha na autenticação. O token `Bearer` fornecido é inválido, expirado ou ausente. | Obter um novo token de acesso válido e reenviar a requisição. | Ver exemplo 7.1.4 |
| `403 Forbidden`           | Sem permissão. O token é válido, mas não tem autorização para acessar os detalhes da conta especificada no `x-kiwify-account-id`. | Verificar se o token possui os escopos necessários e se a conta está correta. | `{"error":{"code":"permission_denied","message":"Sem permissão para acessar esta conta","request_id":"req_..."}}` |
| `404 Not Found`           | Conta não encontrada. O ID de conta fornecido no cabeçalho `x-kiwify-account-id` não corresponde a nenhuma conta existente. | Verificar se o ID da conta está correto. | Ver exemplo 7.1.5 |
| `429 Too Many Requests`   | Limite de taxa (Rate Limit) excedido. Muitas requisições foram feitas em um curto período. | Implementar backoff exponencial e tentar novamente após o período indicado no cabeçalho `Retry-After` (se presente). | `{"error":{"code":"rate_limit_exceeded","message":"Excedeu o limite de requisições. Tente novamente em N segundos.","request_id":"req_..."}}` |
| `500 Internal Server Error`| Erro inesperado no servidor da Kiwify durante o processamento da requisição. | Tentar novamente após alguns instantes. Se o erro persistir, contatar o suporte da Kiwify. | `{"error":{"code":"internal_error","message":"Ocorreu um erro interno. Nossa equipe foi notificada.","request_id":"req_..."}}` |
| `503 Service Unavailable` | O serviço está temporariamente indisponível (manutenção, sobrecarga). | Tentar novamente mais tarde, preferencialmente com backoff exponencial. | `{"error":{"code":"service_unavailable","message":"Serviço temporariamente indisponível. Tente novamente mais tarde.","request_id":"req_..."}}` |




### Estratégia Recomendada para Tratamento de Erros


1. **Para erros 4xx (exceto 429)**:
   - Registre detalhes do erro incluindo o `request_id` para referência futura
   - Interrompa as tentativas após algumas falhas consecutivas (não é provável que se resolva automaticamente)
   - Para 401, tente renovar o token e repetir a requisição uma vez


2. **Para erros 429**:
   - Implemente backoff exponencial começando com 1 segundo
   - Respeite o cabeçalho `Retry-After` se disponível
   - Adicione um pequeno jitter (variação aleatória) para evitar sincronização em sistemas distribuídos


3. **Para erros 5xx**:
   - Implemente backoff exponencial com jitter
   - Limite o total de tentativas (ex: máximo 5 tentativas)
   - Considere implementar um mecanismo de circuit breaker para falhas persistentes




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 9. Casos de Uso Comuns (20 Exemplos Específicos)




> **Resumo:** Lista abrangente de 20 casos de uso reais e específicos que demonstram aplicações práticas do endpoint `/v1/account-details`.




1.  **Exibir dados da conta em um painel administrativo interno.**
    *   Objetivo: `Mostrar nome da empresa, CPF/CNPJ principal para o administrador da integração.`
    *   Como Fazer: `GET /v1/account-details e usar os campos id, company_name, director_cpf, company_cnpj.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


2.  **Validar se uma conta Kiwify existe antes de outras operações.**
    *   Objetivo: `Confirmar a existência de uma conta pelo seu ID antes de tentar criar recursos associados a ela.`
    *   Como Fazer: `GET /v1/account-details com o x-kiwify-account-id. Um status 200 confirma a existência.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


3.  **Listar todas as entidades legais de uma conta.**
    *   Objetivo: `Obter a lista completa de CNPJs ou CPFs associados a uma conta para fins fiscais ou de configuração.`
    *   Como Fazer: `GET /v1/account-details e iterar sobre o array legal_entities.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


4.  **Filtrar entidades legais ativas para processamento de pagamentos.**
    *   Objetivo: `Identificar quais entidades legais estão habilitadas a receber pagamentos.`
    *   Como Fazer: `GET /v1/account-details, iterar legal_entities e selecionar aquelas com active: true.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


5.  **Recuperar a chave PIX de uma entidade legal específica.**
    *   Objetivo: `Obter a chave PIX associada a um CNPJ/CPF específico dentro da conta para configurar pagamentos.`
    *   Como Fazer: `GET /v1/account-details, encontrar a entidade legal desejada no array legal_entities (pelo CNPJ/CPF ou ID) e extrair o campo pix_key.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


6.  **Sincronizar dados cadastrais com um sistema CRM ou ERP.**
    *   Objetivo: `Manter os dados da conta Kiwify (nome, documentos) atualizados em um sistema externo.`
    *   Como Fazer: `GET /v1/account-details periodicamente e atualizar os registros correspondentes no CRM/ERP.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


7.  **Verificar a data da última atualização de uma entidade legal.**
    *   Objetivo: `Determinar se houve mudanças recentes nos dados de uma entidade legal específica para acionar atualizações.`
    *   Como Fazer: `GET /v1/account-details, localizar a entidade legal desejada e verificar o valor de updated_at.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


8.  **Auditar quais entidades legais estão inativas.**
    *   Objetivo: `Identificar entidades legais que foram desativadas na plataforma Kiwify.`
    *   Como Fazer: `GET /v1/account-details, iterar legal_entities e selecionar aquelas com active: false.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


9.  **Obter o ID (UUID) de uma entidade legal para usar em outras chamadas API.**
    *   Objetivo: `Recuperar o identificador único de uma entidade legal baseado no seu CNPJ/CPF para referenciá-la em outras APIs Kiwify.`
    *   Como Fazer: `GET /v1/account-details, encontrar a entidade pelo CNPJ/CPF e extrair seu campo id.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


10. **Validar o CPF do diretor para conformidade (KYC).**
    *   Objetivo: `Verificar se o CPF do diretor principal da conta está preenchido e corresponde ao esperado para processos de Know Your Customer.`
    *   Como Fazer: `GET /v1/account-details e verificar o campo director_cpf, validando o formato e a consistência com outros sistemas.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


11. **Contar o número de entidades legais associadas a uma conta.**
    *   Objetivo: `Saber quantas entidades legais (CNPJs/CPFs) estão vinculadas a uma conta para fins de relatórios ou limites.`
    *   Como Fazer: `GET /v1/account-details e obter o tamanho (length) do array legal_entities retornado.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


12. **Verificar se uma conta possui CNPJ principal cadastrado.**
    *   Objetivo: `Determinar se a conta principal está configurada como Pessoa Jurídica para requisitos fiscais específicos.`
    *   Como Fazer: `GET /v1/account-details e verificar se o campo company_cnpj não está vazio ("").`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


13. **Preparar dados para emissão de relatórios fiscais e contábeis.**
    *   Objetivo: `Coletar nomes, CPFs e CNPJs associados à conta para inclusão em relatórios fiscais obrigatórios.`
    *   Como Fazer: `GET /v1/account-details e extrair os dados relevantes de company_name, director_cpf, company_cnpj e do array legal_entities.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


14. **Identificar entidades legais criadas recentemente.**
    *   Objetivo: `Monitorar a adição de novas entidades legais a uma conta nas últimas 24 horas ou outro período definido.`
    *   Como Fazer: `GET /v1/account-details, iterar legal_entities e verificar o campo created_at comparando com a data atual menos o período desejado.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


15. **Confirmar se uma chave PIX específica está cadastrada na conta.**
    *   Objetivo: `Verificar se uma determinada chave PIX já está associada a alguma entidade legal da conta antes de associá-la a outra.`
    *   Como Fazer: `GET /v1/account-details, iterar legal_entities e procurar pela chave PIX específica no campo pix_key de cada entidade.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


16. **Obter dados para pré-preencher formulários de configuração.**
    *   Objetivo: `Usar os dados da conta Kiwify para facilitar o preenchimento de formulários em um sistema integrado, evitando que o usuário precise digitar novamente.`
    *   Como Fazer: `GET /v1/account-details e usar os campos retornados como valores padrão em formulários de cadastro ou configuração.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


17. **Verificar se existem entidades legais sem CNPJ cadastrado.**
    *   Objetivo: `Identificar entidades legais que podem precisar completar o cadastro fiscal para conformidade ou funcionalidades adicionais.`
    *   Como Fazer: `GET /v1/account-details, iterar legal_entities e verificar quais têm o campo company_cnpj vazio ("").`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


18. **Mapear IDs de contas Kiwify para nomes de empresas em sistemas integrados.**
    *   Objetivo: `Criar uma referência entre o ID técnico da conta e o nome da empresa para exibição amigável em interfaces de usuário de sistemas integrados.`
    *   Como Fazer: `GET /v1/account-details para um ID específico e armazenar a relação id -> company_name em seu sistema.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


19. **Auditar consistência de dados entre conta principal e entidades legais.**
    *   Objetivo: `Verificar se o nome da empresa, CPF ou CNPJ da conta principal corresponde a pelo menos uma entidade legal ativa, identificando possíveis inconsistências.`
    *   Como Fazer: `GET /v1/account-details e comparar os campos do nível raiz (company_name, director_cpf, company_cnpj) com os mesmos campos das entidades ativas no array legal_entities.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*


20. **Validar permissões do token de API e testar a configuração inicial da integração.**
    *   Objetivo: `Confirmar que o token de API utilizado tem permissão para ler os detalhes da conta especificada como parte do processo de setup ou troubleshooting da integração.`
    *   Como Fazer: `Realizar uma chamada GET /v1/account-details e verificar o status da resposta. Um status 200 indica configuração correta, enquanto 401/403 indicam problemas de permissão/autenticação.`
    *(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 10. Notas Adicionais




> **Resumo:** Informações complementares importantes sobre aspectos operacionais, limitações e considerações específicas do endpoint `/v1/account-details`.




*   **Sensibilidade dos Dados (PII):** Este endpoint retorna dados pessoais e fiscais sensíveis (Nome, CPF, CNPJ, Chave PIX). É **crucial** que a aplicação que consome esta API implemente medidas rigorosas de segurança para proteger esses dados, em conformidade com a LGPD (Lei Geral de Proteção de Dados) e outras regulamentações de privacidade aplicáveis. O acesso a esses dados deve ser restrito, registrado (log) e o armazenamento deve ser seguro ou temporário.


*   **Rate Limits:** A documentação oficial não especifica limites de taxa explícitos para este endpoint. Recomenda-se implementar estratégias defensivas assumindo um limite conservador (ex: 60 requisições por minuto) e incluir lógica de retry com backoff exponencial caso receba erros 429 (Too Many Requests).


*   **Consistência e Atualização de Dados:** Os dados retornados refletem o estado da conta no momento da consulta. Alterações realizadas na plataforma Kiwify podem levar alguns instantes (geralmente segundos, mas em alguns casos até minutos) para serem refletidas na API. Para dados críticos, considere implementar verificações periódicas ao invés de assumir imutabilidade.


*   **Campos Opcionais/Vazios:** Campos como `company_cnpj` nas entidades legais podem retornar uma string vazia (`""`) se não estiverem preenchidos na plataforma. A aplicação cliente deve ser capaz de lidar adequadamente com esses casos e não assumir que todos os campos terão valores.


*   **Entidades Legais Inativas:** Entidades com `active: false` são mantidas no array `legal_entities` por questões históricas, mas não devem ser utilizadas para operações ativas como processamento de pagamentos. Sempre verifique o status `active` antes de utilizar uma entidade legal para transações.


*   **Formato de Datas:** Todas as datas são retornadas em formato ISO 8601 com timezone UTC (indicado pelo `Z` no final). Ao processar esses dados, certifique-se de tratá-los adequadamente como UTC ou converter para o timezone local conforme necessário.


*   **Versionamento API:** Este endpoint pertence à versão `v1` da API pública da Kiwify. Embora não haja um roadmap público para descontinuação, é recomendável acompanhar a documentação oficial para notificações sobre futuras versões ou mudanças.


*   **Requisitos de Compatibilidade:** O endpoint é compatível com todas as principais linguagens e frameworks que suportam requisições HTTP/HTTPS. Para integrações robustas, utilize bibliotecas client HTTP que suportem timeouts adequados, retries automáticos e tratamento de erros.




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 11. Metadados Internos (Para Indexação e RAG)




> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.




```json
{
  "doc_id": "kiwify_acc_001",
  "api_provider": "Kiwify",
  "api_product_area": "Contas",
  "endpoint_focus": ["Consultar Detalhes da Conta"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Baixa",
  "key_entities_handled": ["Conta Kiwify", "Entidade Legal", "Empresa", "CPF", "CNPJ", "PIX Key"],
  "context_level": ["foundational", "intermediate"],
  "topic_cluster": ["kiwify", "api", "contas", "detalhes", "cadastro", "fiscal"],
  "db_relations": {
    "tables": ["accounts", "legal_entities", "users"],
    "schemas": ["platform_core"]
  },
  "related_concepts": ["OAuth 2.0", "Autenticação API", "Dados Cadastrais", "Entidades Legais", "Compliance Fiscal", "PII", "LGPD", "Rate Limiting"],
  "question_embeddings": [
    "Como obter os detalhes de uma conta na Kiwify via API?",
    "Qual endpoint da API Kiwify retorna o CNPJ e CPF de uma conta?",
    "Como listar as entidades legais associadas a uma conta Kiwify?",
    "Qual a estrutura JSON da resposta da API de detalhes da conta Kiwify?",
    "Quais cabeçalhos são necessários para chamar a API /v1/account-details da Kiwify?",
    "Como verificar se uma entidade legal está ativa na Kiwify API?",
    "Onde encontrar a chave PIX de uma conta Kiwify pela API?",
    "A API da Kiwify retorna dados sensíveis como CPF?",
    "Como validar o formato dos dados fiscais retornados pela API Kiwify?",
    "O que significa o campo active nas entidades legais da Kiwify?",
    "Como usar o ID da entidade legal em outras chamadas da API Kiwify?",
    "Quais erros podem ocorrer ao consultar os detalhes de uma conta Kiwify?",
    "Como saber quando uma entidade legal foi atualizada pela última vez?"
  ],
  "reasoning_pathways": ["retrieval", "filtering", "verification", "integration", "compliance"],
  "typical_usage_frequency": "Média-Alta",
  "rate_limit_category": "Standard",
  "authentication_requirements": ["Bearer Token", "x-kiwify-account-id Header"],
  "typical_integration_points": ["Painéis Administrativos Customizados", "Sistemas ERP/CRM", "Ferramentas de Compliance", "Plataformas de BI", "Gateways de Pagamento"],
  "common_error_patterns": ["invalid_token (401)", "permission_denied (403)", "account_not_found (404)", "rate_limit_exceeded (429)"],
  "security_considerations": ["Dados PII", "LGPD", "Armazenamento Seguro", "Logs de Acesso"]
}
```




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 12. Checklist de Implementação (Opcional)




> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação da integração com o endpoint `/v1/account-details`.




- [ ] **Autenticação**
  - [ ] Implementar fluxo OAuth 2.0 para obter `Bearer Token`.
  - [ ] Armazenar o token de forma segura (não exposto em código-fonte, logs ou front-end).
  - [ ] Implementar renovação automática do token expirado.
  - [ ] Incluir corretamente os cabeçalhos `Authorization` e `x-kiwify-account-id` em cada requisição.


- [ ] **Tratamento de Erros**
  - [ ] Implementar lógica para tratar códigos de status `4xx` (especialmente 401, 403, 404, 429).
  - [ ] Implementar tratamento para erros `5xx` (500, 503).
  - [ ] Registrar erros detalhadamente para depuração, incluindo `request_id` das respostas de erro.
  - [ ] Criar mensagens de erro amigáveis para usuários finais quando aplicável.


- [ ] **Retries (429, 5xx)**
  - [ ] Implementar backoff exponencial começando com delay inicial de 1 segundo.
  - [ ] Adicionar jitter (variação aleatória) para evitar sincronização em retentativas.
  - [ ] Respeitar o cabeçalho `Retry-After` quando presente.
  - [ ] Definir número máximo de tentativas (ex: 5) para evitar loops infinitos.


- [ ] **Processamento da Resposta**
  - [ ] Mapear a estrutura JSON da resposta para classes/objetos da aplicação.
  - [ ] Lidar corretamente com campos que podem ser vazios (ex: `company_cnpj`).
  - [ ] Validar e processar datas no formato ISO 8601 (UTC).
  - [ ] Implementar filtragem das entidades legais ativas vs. inativas conforme necessário.


- [ ] **Segurança e Conformidade (LGPD)**
  - [ ] **CRÍTICO:** Implementar medidas para proteger os dados sensíveis (PII) retornados (CPF, CNPJ, PIX).
  - [ ] Criptografar dados em trânsito (HTTPS) e em repouso, se armazenados.
  - [ ] Implementar controle de acesso granular aos dados na aplicação.
  - [ ] Criar logs de auditoria para acessos aos dados sensíveis.
  - [ ] Definir política de retenção de dados (quanto tempo os dados serão armazenados).


- [ ] **Monitoramento e Logs**
  - [ ] Registrar o tempo de resposta das chamadas à API.
  - [ ] Monitorar a taxa de sucesso e erro das requisições.
  - [ ] Implementar alertas para erros frequentes ou taxas de erro elevadas.
  - [ ] Incluir IDs de correlação (trace IDs) para rastreamento de requisições.


- [ ] **Otimização**
  - [ ] Implementar cache local para os detalhes da conta quando apropriado.
  - [ ] Definir estratégia de invalidação de cache (TTL ou baseado em eventos).
  - [ ] Minimizar o número de requisições, agrupando operações quando possível.
  - [ ] Implementar timeout adequado para evitar requisições pendentes indefinidamente.


- [ ] **Testes**
  - [ ] Criar testes unitários para o código que processa respostas da API.
  - [ ] Implementar testes de integração com mocks ou sandbox.
  - [ ] Testar cenários de erro (401, 403, 404, 429, 500, etc.).
  - [ ] Verificar a manipulação correta de dados sensíveis.




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 13. Glossário de Termos Técnicos




> **Resumo:** Definições claras e concisas dos principais termos técnicos utilizados nesta documentação.




| Termo                     | Definição                                                    |
| :------------------------ | :----------------------------------------------------------- |
| `API (Application Programming Interface)` | Conjunto de regras e protocolos que permite que diferentes sistemas de software se comuniquem entre si. A API Kiwify permite que sistemas externos interajam com a plataforma programaticamente. |
| `Conta (Kiwify)`          | A entidade principal na plataforma Kiwify que representa um usuário ou organização, à qual entidades legais e outros recursos estão associados. Identificada por um ID único (ex: `XvS0qfkdzCZTg8z`). |
| `Entidade Legal`          | Representação de uma pessoa física (CPF) ou jurídica (CNPJ) dentro da plataforma Kiwify, usada para fins fiscais e de transação. Associada a uma Conta e pode ter status ativo ou inativo. |
| `Endpoint`                | Um URL específico onde uma API pode ser acessada para realizar uma operação. Neste caso, `/v1/account-details` é o endpoint para obter detalhes da conta. |
| `GET`                     | Método HTTP usado para solicitar dados de um recurso especificado. Não deve ter efeitos colaterais (não modifica dados). |
| `OAuth 2.0`               | Padrão de autorização aberto que permite que aplicações obtenham acesso limitado a contas de usuário em um serviço HTTP. A Kiwify utiliza OAuth 2.0 para autenticação da API. |
| `Bearer Token`            | Tipo de token de acesso OAuth 2.0. A aplicação que o possui ("bearer") pode usá-lo para acessar recursos protegidos. Enviado no cabeçalho `Authorization: Bearer {token}`. |
| `Header (HTTP)`           | Componente de uma requisição ou resposta HTTP que contém metadados sobre a comunicação. Cabeçalhos personalizados da Kiwify começam com `x-kiwify-`. |
| `Authorization`           | Cabeçalho HTTP padrão usado para enviar credenciais de autenticação (neste caso, o `Bearer Token`). |
| `x-kiwify-account-id`     | Cabeçalho HTTP customizado pela Kiwify para especificar o ID da conta alvo da operação. |
| `JSON (JavaScript Object Notation)` | Formato leve de intercâmbio de dados, amplamente utilizado em APIs web. Todas as respostas deste endpoint são em JSON. |
| `CPF`                     | Cadastro de Pessoas Físicas. Identificador fiscal único para pessoas físicas no Brasil. Retornado no campo `director_cpf`. |
| `CNPJ`                    | Cadastro Nacional da Pessoa Jurídica. Identificador fiscal único para empresas e outras organizações no Brasil. Retornado no campo `company_cnpj`. |
| `PIX`                     | Sistema brasileiro de pagamentos instantâneos implementado pelo Banco Central. Uma `Chave PIX` (email, telefone, CPF/CNPJ, chave aleatória) identifica uma conta para recebimento e é retornada no campo `pix_key`. |
| `UUID (Universally Unique Identifier)` | Identificador de 128 bits usado para garantir unicidade em sistemas distribuídos. Utilizado no campo `id` das entidades legais. |
| `ISO 8601`                | Padrão internacional para representação de datas e horas (ex: `2023-09-27T18:10:37.697Z`). O `Z` indica fuso horário UTC. Usado nos campos `created_at` e `updated_at`. |
| `PII (Personally Identifiable Information)` | Informações que podem ser usadas para identificar um indivíduo específico (ex: Nome, CPF). Requer tratamento especial de segurança e privacidade. |
| `LGPD (Lei Geral de Proteção de Dados)` | Legislação brasileira (Lei nº 13.709/2018) que regula o tratamento de dados pessoais. Aplicável aos dados retornados por este endpoint. |
| `Rate Limit`              | Restrição imposta por uma API sobre o número de requisições que um cliente pode fazer em um determinado período. Resulta em erros 429 quando excedido. |
| `Backoff Exponencial`     | Estratégia de retentativa onde o tempo de espera entre tentativas aumenta exponencialmente após cada falha (ex: 1s, 2s, 4s, 8s...), usada para lidar com erros `429` ou `5xx`. |
| `Jitter`                  | Pequena variação aleatória adicionada aos tempos de espera em estratégias de backoff para evitar que múltiplos clientes tentem reconectar simultaneamente. |
| `Retry-After`             | Cabeçalho HTTP que indica quanto tempo (em segundos) o cliente deve esperar antes de fazer uma nova requisição após receber um erro 429 ou 503. |
| `Status Active`           | Indicador booleano (`true`/`false`) que determina se uma entidade legal está ativa e pode ser usada para transações. |




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*
---




## 14. Observações Finais sobre Formatação




> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.




*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados e comparativos (parâmetros, códigos de status, glossário).
*   Use blocos de código (``` ```) com indicação de linguagem (`bash`, `json`, `javascript`) para exemplos de código e JSON.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa. Evite ambiguidades.
*   Formate nomes de parâmetros (`x-kiwify-account-id`), campos JSON (`company_name`), valores de exemplo (`true`, `Bearer {token}`) e métodos HTTP (`GET`) com backticks (` `).
*   **Crucial:** Inclua a referência `(Ref: [TITULO_CURTO], ID [ID_INTERNO])` no final de **CADA SEÇÃO PRINCIPAL (##)** para garantir a atribuição correta do contexto durante a recuperação em sistemas RAG. Adicione também a referências em subitens importantes (como cada Caso de Uso) para maior granularidade.
*   Mantenha os resumos de seção (`> **Resumo:** ...`) concisos (1-2 linhas) e informativos, capturando a essência da seção.
*   Use listas (bullets `*` ou `-`, ou numeradas `1.`) para informações sequenciais ou enumeradas (casos de uso, checklist).
*   Defina acrônimos e termos técnicos na primeira utilização ou no glossário (Seção 13).




*(Ref: Kiwify Account Details, ID kiwify_accountdetails_001)*