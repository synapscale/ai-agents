# API Hotmart - Vendas - Obter Participantes de Vendas (Sales Users)


## 1. Cabeçalho e Identificação
| Campo                     | Valor                                                      |
| :------------------------ | :--------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Vendas - Obter Participantes de Vendas (Sales Users) |
| **Identificador Interno** | `hotmart_sales_001`                                        |
| **Título Curto (Ref.)**   | `Hotmart Sales Users`                                      |
| **Versão do Documento**   | `1.0.0`                                                    |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação RAG                                 |
| **Fonte Original**        | Documentação oficial Hotmart Developers                    |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/v1/sales/sales-users/  |
| **Status do Documento**   | Em Uso                                                     |
| **Ambiente de Referência**| Produção                                                   |
| **Idioma Original**       | Português (BR)                                             |
| **Formato de Datas (API)**| Timestamp Unix em Milissegundos                            |
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 2. Contexto
Este endpoint (`/sales/users`) da API Hotmart V1 foi projetado para fornecer informações detalhadas sobre todos os participantes envolvidos em transações de vendas na plataforma. Os participantes podem incluir Compradores (`BUYER`), Produtores (`PRODUCER`), Co-produtores (`COPRODUCER`) e Afiliados (`AFFILIATE`). O principal objetivo é permitir a consulta e análise de dados relacionados aos usuários de vendas, facilitando tarefas como reconciliação financeira, análise de desempenho de afiliados, segmentação de clientes e auditoria de transações. O identificador único deste documento é `hotmart_sales_001`.
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 3. Visão Geral da API/Endpoint(s)
Este documento detalha o endpoint `GET /payments/api/v1/sales/users`. Ele permite recuperar uma lista paginada de transações, incluindo detalhes sobre os produtos vendidos e os usuários participantes (compradores, produtores, etc.). A API oferece diversos parâmetros de consulta para filtrar os resultados por transação específica, status da transação, produto, período de datas, e-mail do comprador, nome do afiliado, entre outros. Por padrão, se nenhum filtro de status for aplicado, apenas vendas com status `APPROVED` e `COMPLETE` são retornadas.
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 4. Detalhes Técnicos
### Endpoint de Participantes de Vendas
*   **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/sales/users`
*   **Método HTTP:** `GET`
*   **Autenticação:** Requer um token de acesso do tipo Bearer no cabeçalho HTTP `Authorization`. Formato: `Authorization: Bearer :access_token`.
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 5. Parâmetros de Entrada
### Endpoint de Participantes de Vendas (Query Parameters)


| Parâmetro          | Descrição Detalhada | Tipo | Notas / Exemplo |
| :----------------- | :------------------ | :--- | :-------------- |
| `transaction`      | Código único que identifica uma transação específica na Hotmart. Use este parâmetro para buscar os detalhes de uma única venda. | string | **Opcional.** Ex: `HP17715690036014` |
| `transaction_status` | Filtra as transações pelo seu estado atual. Se omitido, a API retorna **apenas** transações com status `APPROVED` e `COMPLETE`. | string | **Opcional.** Valores possíveis: `APPROVED`, `BLOCKED`, `CANCELLED`, `CHARGEBACK`, `COMPLETE`, `EXPIRED`, `NO_FUNDS`, `OVERDUE`, `PARTIALLY_REFUNDED`, `PRE_ORDER`, `PRINTED_BILLET`, `PROCESSING_TRANSACTION`, `PROTESTED`, `REFUNDED`, `STARTED`, `UNDER_ANALISYS`, `WAITING_PAYMENT`. Ex: `APPROVED` |
| `max_results`      | Define o número máximo de itens (transações) que devem ser retornados em uma única página de resultados. Útil para controlar o volume de dados por requisição. | integer | **Opcional.** O valor padrão pode variar; consulte a documentação oficial para limites. Ex: `50` |
| `page_token`       | Token opaco fornecido na resposta anterior (`page_info.next_page_token`) para solicitar a próxima página de resultados. Essencial para navegar por listas que excedem `max_results`. | string | **Opcional.** Ex: `eyJwYWdlIjoyLCJyb3dzIjozfQ==` |
| `product_id`       | Identificador numérico único (ID) de um produto na Hotmart. Use para filtrar e retornar apenas as vendas relacionadas a este produto específico. | integer | **Opcional.** Ex: `178598` |
| `start_date`       | Filtra transações ocorridas a partir desta data e hora. O valor deve ser um timestamp Unix em **milissegundos**. | long | **Opcional.** Ex: `1678886400000` (Representa 2023-03-15 12:00:00 GMT) |
| `end_date`         | Filtra transações ocorridas até esta data e hora (inclusive). O valor deve ser um timestamp Unix em **milissegundos**. | long | **Opcional.** Ex: `1678972800000` (Representa 2023-03-16 12:00:00 GMT) |
| `buyer_email`      | Filtra transações buscando pelo endereço de e-mail exato do comprador. Útil para localizar todas as compras de um cliente específico. | string | **Opcional.** Ex: `comprador@email.com` |
| `sales_source`     | Filtra vendas com base no código de rastreamento (parâmetro `src`) utilizado no link de checkout. Permite identificar vendas originadas de campanhas ou fontes específicas. | string | **Opcional.** Ex: `facebook_ads_campanha_xyz` |
| `buyer_name`       | Filtra transações pelo nome do comprador. A correspondência pode ser exata ou parcial (consulte a documentação oficial para o comportamento exato). | string | **Opcional.** Ex: `João da Silva` |
| `affiliate_name`   | Filtra transações pelo nome do afiliado que foi creditado pela venda. | string | **Opcional.** Ex: `Afiliado Exemplo` |
| `commission_as`    | Filtra as vendas onde o usuário autenticado (dono do token da API) foi comissionado com um papel específico na transação. | string | **Opcional.** Valores possíveis: `PRODUCER` (Produtor), `COPRODUCER` (Co-produtor), `AFFILIATE` (Afiliado). Ex: `AFFILIATE` |
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Endpoint de Participantes de Vendas
#### 6.1.1 Estrutura Geral
| Campo         | Descrição | Tipo   |
| :------------ | :-------- | :----- |
| `items`       | Lista contendo os detalhes das transações encontradas, de acordo com os filtros aplicados. Cada elemento da lista representa uma transação. | array |
| `page_info`   | Objeto contendo informações sobre a paginação dos resultados, permitindo navegar por múltiplas páginas de dados. | object |


#### 6.1.2 Detalhes do Objeto `items` (Cada item representa uma transação)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `transaction`       | Código único de referência da transação (alfanumérico). | string | Ex: `HP17715690036014` |
| `product`           | Objeto contendo informações básicas do produto vendido nesta transação. | object | Ver detalhes abaixo (Seção 6.1.3). |
| `users`             | Lista de objetos, cada um representando um participante da venda (Comprador, Produtor, Afiliado, Co-produtor). Uma transação pode ter múltiplos participantes. | array | Ver detalhes abaixo (Seção 6.1.4). |


#### 6.1.3 Detalhes do Objeto `items.product`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `name`              | Nome comercial do produto vendido. | string | Ex: `Curso Online de Marketing Digital Avançado` |
| `id`                | Identificador numérico único do produto na plataforma Hotmart. | integer | Ex: `178598` |


#### 6.1.4 Detalhes do Objeto `items.users` (Cada item representa um participante)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `role`              | Papel desempenhado por este usuário específico nesta transação. | string | Valores possíveis: `PRODUCER`, `BUYER`, `COPRODUCER`, `AFFILIATE`. |
| `user`              | Objeto contendo os dados cadastrais e de contato detalhados do participante. | object | Ver detalhes abaixo (Seção 6.1.5). |


#### 6.1.5 Detalhes do Objeto `items.users.user`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `ucode`             | Identificador único universal do usuário dentro da plataforma Hotmart. | string | Ex: `c9e5e3f4-097e-11e4-be45-22000b409f8a` |
| `locale`            | Combinação do código do país e idioma do participante, geralmente inferido a partir do endereço IP ou configurações do navegador no momento da interação. | string | Formato `language_COUNTRY`. Ex: `pt_BR` (Português Brasil), `en_US` (Inglês EUA), `es_ES` (Espanhol Espanha). |
| `name`              | Nome completo registrado do participante. | string | Ex: `Maria Joaquina Oliveira` |
| `trade_name`        | Nome fantasia ou nome comercial, se aplicável (geralmente para contas de Pessoa Jurídica). | string | Pode ser nulo ou vazio. Ex: `Consultoria Digital XYZ Ltda.` |
| `cellphone`         | Número do telefone celular do participante. | string | **Nota:** Para participantes `BUYER` de vendas internacionais (comprador fora do Brasil), o DDI (código de discagem internacional do país) pode ser incluído no início do número. Ex: `+15551234567` (EUA), `5511999999999` (Brasil). |
| `phone`             | Número do telefone fixo do participante. | string | **Nota:** Para participantes `BUYER` de vendas internacionais, o DDI pode ser incluído. Ex: `+442071234567` (Reino Unido), `551133334444` (Brasil). |
| `email`             | Endereço de e-mail principal do participante. | string | Ex: `maria.joaquina.oliveira@email.com` |
| `documents`         | Lista contendo os documentos de identificação registrados para o participante. Pode estar vazia. | array | Ver detalhes abaixo (Seção 6.1.6). |
| `address`           | Objeto contendo os detalhes do endereço registrado do participante. Pode conter campos nulos se o endereço não estiver completo. | object | Ver detalhes abaixo (Seção 6.1.7). |


#### 6.1.6 Detalhes do Array `items.users.user.documents` (Cada item é um documento)
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `value`             | O número ou código de identificação do documento. | string | Ex: `12345678900` (para CPF), `12345678000199` (para CNPJ). |
| `type`              | Tipo do documento de identificação. | string | Valores comuns incluem: `CPF` (Cadastro de Pessoa Física - Brasil), `CNPJ` (Cadastro Nacional da Pessoa Jurídica - Brasil), `RG` (Registro Geral - Brasil), `DNI` (Documento Nacional de Identidad - Países Hispanófonos), `CIF` (Código de Identificación Fiscal - Espanha), `DOCUMENT` (Tipo genérico para outros documentos). |


#### 6.1.7 Detalhes do Objeto `items.users.user.address`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `city`              | Nome da cidade do endereço. | string | Ex: `Belo Horizonte` |
| `state`             | Nome do estado, província ou região do endereço. | string | Ex: `Minas Gerais` ou `MG` |
| `country`           | Nome do país do endereço. | string | Ex: `Brasil` |
| `zip_code`          | Código postal (CEP no Brasil) do endereço. | string | Ex: `30140-000` |
| `address`           | Nome da rua, avenida, praça, etc. (logradouro). | string | Ex: `Rua dos Aimorés` |
| `complement`        | Informações adicionais do endereço, como apartamento, bloco, sala, etc. | string | Pode ser nulo ou vazio. Ex: `Sala 302` |
| `neighborhood`      | Nome do bairro. | string | Ex: `Funcionários` |
| `number`            | Número do imóvel no logradouro. | string | Ex: `486` |


#### 6.1.8 Detalhes do Objeto `page_info`
| Campo Aninhado      | Descrição | Tipo | Notas |
| :------------------ | :-------- | :--- | :---- |
| `total_results`     | Estimativa da quantidade total de itens (transações) que correspondem aos filtros aplicados, independentemente da paginação. | integer | **Nota:** Este campo pode não ser retornado em todas as consultas ou pode ser uma estimativa. |
| `next_page_token`   | Token opaco que deve ser enviado no parâmetro `page_token` da próxima requisição para obter a página seguinte de resultados. Presente apenas se houver mais páginas disponíveis. | string | Ex: `eyJwYWdlIjoyLCJyb3dzIjo1MH0=` |
| `prev_page_token`   | Token opaco que deve ser enviado no parâmetro `page_token` da próxima requisição para obter a página anterior de resultados. Presente apenas se a página atual não for a primeira. | string | Ex: `eyJwYWdlIjowLCJyb3dzIjo1MH0=` |
| `results_per_page`  | Número de itens (transações) efetivamente retornados na página atual. Geralmente corresponde ao valor de `max_results` solicitado, exceto na última página, que pode ter menos itens. | integer | Ex: `50` |
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 7. Exemplos de Requisição e Resposta
### Endpoint de Participantes de Vendas
#### 7.1.1 Exemplo de Requisição (cURL) - Buscando vendas aprovadas de um produto específico
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/sales/users?product_id=178598&transaction_status=APPROVED&max_results=1' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer [seu_token_de_acesso]'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
{
  "items": [
    {
      "transaction": "HP10014546320130",
      "product": {
        "name": "Product 1",
        "id": 178598
      },
      "users": [
        {
          "role": "PRODUCER",
          "user": {
            "ucode": "c9e5e3f4-097e-11e4-be45-22000b409f8a",
            "locale": "FR",
            "name": "Producer Name",
            "trade_name": "Producer Trade Name",
            "cellphone": "1199999999",
            "phone": "6825565681",
            "email": "producerEmail@email.com",
            "documents": [
              {
                "value": "564654",
                "type": "DOCUMENT"
              },
              {
                "value": "68658197646",
                "type": "CPF"
              }
            ],
            "address": {
              "city": "Campo Grande",
              "state": "Campo Grande",
              "country": "Brasil",
              "zip_code": "1213454",
              "address": "Rua Carlos Fortunato Paiva",
              "complement": "",
              "neighborhood": "",
              "number": "123"
            }
          }
        },
        {
          "role": "BUYER",
          "user": {
            "ucode": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
            "locale": "pt_BR",
            "name": "Comprador Exemplo Silva",
            "trade_name": null,
            "cellphone": "5531988887777",
            "phone": "553134567890",
            "email": "comprador.exemplo@email.com",
            "documents": [
              {
                "value": "98765432100",
                "type": "CPF"
              }
            ],
            "address": {
              "city": "Belo Horizonte",
              "state": "MG",
              "country": "Brasil",
              "zip_code": "30110-000",
              "address": "Avenida do Contorno",
              "complement": "Apto 500",
              "neighborhood": "Centro",
              "number": "1000"
            }
          }
        }
      ]
    }
  ],
  "page_info": {
    "total_results": 55,
    "next_page_token": "eyJwYWdlIjoyLCJyb3dzIjozfQ==",
    "results_per_page": 1
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro 400 Bad Request - Parâmetro Inválido)
```json
{
  "error": "invalid_parameter",
  "error_description": "Invalid value for parameter 'start_date'. Expected format: milliseconds timestamp."
}
```
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                              | Possível Ação / Causa Comum |
| :--------------------- | :----------------------------------------------------------- | :-------------------------- |
| `200 OK`               | Requisição bem-sucedida. A resposta contém os dados solicitados. | N/A - Sucesso.              |
| `400 Bad Request`      | A requisição está malformada ou contém parâmetros inválidos. | Verificar formato dos parâmetros (datas, IDs), valores inválidos para enums (`transaction_status`). |
| `401 Unauthorized`     | Falha na autenticação. O token de acesso está ausente, inválido ou expirado. | Verificar se o cabeçalho `Authorization: Bearer :access_token` está correto e se o token é válido. |
| `403 Forbidden`        | O token de acesso é válido, mas não tem permissão para acessar este recurso específico ou realizar a ação solicitada. | Verificar as permissões associadas ao token/aplicação na plataforma Hotmart. |
| `404 Not Found`        | O endpoint solicitado (`/sales/users`) não foi encontrado (raro se a URL base estiver correta). | Verificar a URL do endpoint. |
| `429 Too Many Requests`| O limite de requisições (Rate Limit) para a API foi excedido. | Implementar backoff exponencial e reduzir a frequência das chamadas. Verificar os limites na documentação oficial. |
| `500 Internal Server Error` | Ocorreu um erro inesperado no servidor da Hotmart ao processar a requisição. | Tentar novamente mais tarde. Se persistir, contatar o suporte da Hotmart. |
| `503 Service Unavailable` | O serviço está temporariamente indisponível, possivelmente devido a manutenção ou sobrecarga. | Tentar novamente mais tarde. |


*Nota: A documentação original não detalhava códigos de erro específicos além dos padrões HTTP. A resposta de erro geralmente inclui um objeto JSON com campos `error` e `error_description` para mais detalhes.*
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1.  **Listar todos os compradores de um produto específico:**
    *   Objetivo: Obter uma lista de todos os compradores de um produto.
    *   Como Fazer: Enviar requisição GET com `product_id={id_do_produto}`. Na resposta, iterar sobre `items` e, dentro de cada `users`, filtrar aqueles com `role="BUYER"`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
2.  **Verificar dados de um comprador específico por email:**
    *   Objetivo: Localizar informações de um comprador pelo email.
    *   Como Fazer: Enviar GET com `buyer_email={email_do_comprador}`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
3.  **Encontrar todas as vendas com status APPROVED em um período:**
    *   Objetivo: Listar vendas aprovadas em intervalo de datas específico.
    *   Como Fazer: Enviar GET com `transaction_status=APPROVED`, `start_date={timestamp_inicio_ms}` e `end_date={timestamp_fim_ms}`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
4.  **Identificar afiliados que realizaram vendas de um produto:**
    *   Objetivo: Listar afiliados ativos em vendas de produto específico.
    *   Como Fazer: Enviar GET com `product_id={id_do_produto}`. Na resposta, iterar sobre `items` e, dentro de cada `users`, coletar informações daqueles com `role="AFFILIATE"`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
5.  **Verificar dados completos de uma transação específica:**
    *   Objetivo: Obter todos os participantes e detalhes de uma transação.
    *   Como Fazer: Enviar GET com `transaction={codigo_da_transacao}`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
6.  **Identificar co-produtores de um produto específico:**
    *   Objetivo: Listar todos os co-produtores envolvidos nas vendas de um produto.
    *   Como Fazer: Enviar GET com `product_id={id_do_produto}`. Na resposta, iterar e coletar usuários com `role="COPRODUCER"`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
7.  **Localizar vendas realizadas por um afiliado específico (pelo nome):**
    *   Objetivo: Encontrar todas as vendas de um determinado afiliado.
    *   Como Fazer: Enviar GET com `affiliate_name={nome_do_afiliado}`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
8.  **Analisar vendas com status REFUNDED:**
    *   Objetivo: Identificar todas as vendas que foram reembolsadas.
    *   Como Fazer: Enviar GET com `transaction_status=REFUNDED`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
9.  **Obter dados de compradores para contato pós-venda (últimos 7 dias):**
    *   Objetivo: Coletar informações de contato de compradores recentes.
    *   Como Fazer: Calcular `start_date` (timestamp de 7 dias atrás) e `end_date` (timestamp atual). Enviar GET com essas datas e `transaction_status=APPROVED` (ou `COMPLETE`). Extrair `user.email`, `user.name`, `user.cellphone` dos participantes com `role="BUYER"`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
10. **Identificar vendas originadas de uma campanha específica (SRC):**
    *   Objetivo: Rastrear vendas provenientes de um código de fonte específico.
    *   Como Fazer: Enviar GET com `sales_source={codigo_src_da_campanha}`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
11. **Analisar vendas realizadas para compradores internacionais (fora do Brasil):**
    *   Objetivo: Identificar compradores de outros países.
    *   Como Fazer: Enviar GET (sem filtro de país). Na resposta, iterar sobre `items`, encontrar o `BUYER` e verificar se `user.address.country` é diferente de "Brasil" ou se `user.locale` não começa com "pt_".
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
12. **Verificar transações com status UNDER_ANALISYS:**
    *   Objetivo: Monitorar vendas que estão em análise manual ou antifraude.
    *   Como Fazer: Enviar GET com `transaction_status=UNDER_ANALISYS`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
13. **Obter detalhes do produtor em uma transação específica:**
    *   Objetivo: Identificar informações do produtor principal em uma venda.
    *   Como Fazer: Enviar GET com `transaction={codigo_da_transacao}`. Na resposta, encontrar o participante com `role="PRODUCER"`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
14. **Monitorar vendas expiradas de um produto:**
    *   Objetivo: Identificar transações (ex: boletos não pagos) que expiraram.
    *   Como Fazer: Enviar GET com `product_id={id_do_produto}` e `transaction_status=EXPIRED`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
15. **Listar vendas aguardando pagamento (ex: boleto gerado):**
    *   Objetivo: Identificar vendas pendentes de confirmação de pagamento.
    *   Como Fazer: Enviar GET com `transaction_status=WAITING_PAYMENT` ou `PRINTED_BILLET`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
16. **Verificar vendas com estorno (chargeback):**
    *   Objetivo: Identificar transações que sofreram chargeback pelo comprador.
    *   Como Fazer: Enviar GET com `transaction_status=CHARGEBACK`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
17. **Obter dados fiscais (CPF/CNPJ) de compradores para emissão de NFe:**
    *   Objetivo: Coletar informações de documentos fiscais para relatórios ou emissão fiscal.
    *   Como Fazer: Enviar GET (filtrando por período/status desejado). Na resposta, para cada `BUYER`, acessar `user.documents` e extrair o valor onde `type="CPF"` ou `type="CNPJ"`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
18. **Listar vendas completas navegando por páginas:**
    *   Objetivo: Processar um grande volume de vendas com status COMPLETE.
    *   Como Fazer: Enviar GET inicial com `transaction_status=COMPLETE` e `max_results={valor_desejado}`. Processar a primeira página. Se `page_info.next_page_token` existir, enviar nova requisição GET com `page_token={valor_do_token}` e os mesmos filtros. Repetir até `next_page_token` não ser retornado.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
19. **Verificar vendas com reembolso parcial:**
    *   Objetivo: Identificar transações onde apenas parte do valor foi reembolsado.
    *   Como Fazer: Enviar GET com `transaction_status=PARTIALLY_REFUNDED`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
20. **Filtrar compradores por nome específico:**
    *   Objetivo: Localizar transações de compradores com um nome específico para verificação.
    *   Como Fazer: Enviar GET com `buyer_name={nome_do_comprador}`.
    *(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 10. Notas Adicionais
*   **Filtros Padrão:** Lembre-se que se os filtros `transaction` ou `transaction_status` não forem especificados na requisição, a API retornará **apenas** as transações com status `APPROVED` e `COMPLETE`. Para obter todos os status, você precisaria fazer múltiplas chamadas ou verificar se há uma opção não documentada para "todos os status".
*   **Internacionalização (DDI):** Para vendas onde o comprador (`BUYER`) é de fora do Brasil, os campos `cellphone` e `phone` podem incluir o DDI (código de discagem internacional) do país correspondente.
*   **Paginação:** A API utiliza um sistema de paginação baseado em token (`page_token`). É fundamental implementar a lógica de paginação corretamente para garantir que todos os resultados sejam processados ao lidar com grandes volumes de dados. O campo `total_results` pode não ser exato ou sempre presente.
*   **Rate Limits:** A documentação original não especifica os limites exatos de requisições por minuto/hora. É importante monitorar respostas `429 Too Many Requests` e implementar uma estratégia de retentativa com backoff exponencial.
*   **Consistência de Dados:** Dados como nome, endereço e documentos dependem do preenchimento pelo usuário no momento da compra ou cadastro, podendo haver variações ou dados incompletos.
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sales_001",
  "api_provider": "Hotmart",
  "api_product_area": "Vendas",
  "endpoint_focus": ["Consultar Participantes Venda", "Listar Transações Venda", "Filtrar Vendas"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Comprador", "Produtor", "Afiliado", "Co-produtor", "Transação", "Produto", "Pagamento", "Status Transação", "Endereço", "Documento Fiscal"],
  "context_level": ["intermediate"],
  "topic_cluster": ["vendas", "transações", "participantes", "pagamentos", "afiliados", "hotmart_api"],
  "db_relations": {
    "tables": ["sales_transactions", "users", "products", "addresses", "user_documents", "affiliate_commissions"],
    "schemas": ["payments_api_schema", "users_schema"]
  },
  "related_concepts": ["status de pagamento", "comissionamento", "afiliação", "checkout", "webhook de vendas", "relatório de vendas", "dados do cliente"],
  "question_embeddings": [
    "Como obter a lista de compradores de um produto na Hotmart via API?",
    "Qual endpoint da API Hotmart retorna informações de afiliados em uma venda?",
    "Como filtrar vendas por status 'APPROVED' ou 'REFUNDED' na API da Hotmart?",
    "É possível buscar uma transação específica pelo seu código na API Hotmart?",
    "Como obter o CPF ou CNPJ de um comprador pela API de vendas da Hotmart?",
    "Quais são os possíveis status de transação retornados pela API /sales/users?",
    "Como funciona a paginação na API de participantes de vendas da Hotmart?",
    "Quais dados de endereço do comprador a API Hotmart fornece?",
    "Como listar todas as vendas de um afiliado específico usando a API?"
  ],
  "reasoning_pathways": ["query-filter", "pagination", "data-extraction", "entity-relationship-mapping", "status-based-filtering"],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*
---


## 12. Checklist de Implementação (Opcional)
- [ ] Autenticação (Bearer Token)
- [ ] Tratamento de Erros (4xx, 5xx)
- [ ] Retries (429, 5xx)
- [ ] Paginação (Implementar controle via tokens)
- [ ] Validação de Entrada (Parâmetros válidos)
- [ ] Mapeamento de Resposta (Modelo para object items)
- [ ] Logs & Monitoramento (Registro de transações importantes)
- [ ] Cache (Para chamadas frequentes com os mesmos parâmetros)
- [ ] Testes (Casos normais, Edge-cases)
- [ ] Rate Limits (Monitoramento e backoff exponencial)
- [ ] Tratamento de Datas (Conversão de timestamps)
- [ ] Tratamento de Dados Ausentes (Comprador sem informações completas)
- [ ] Internacionalização (Múltiplas moedas)
- [ ] Segurança (Armazenamento seguro de dados sensíveis)
- [ ] Tratamento de Valores Financeiros (Uso de precisão decimal adequada)
*(Ref: Hotmart Sales Users, ID hotmart_salesusers_001)*