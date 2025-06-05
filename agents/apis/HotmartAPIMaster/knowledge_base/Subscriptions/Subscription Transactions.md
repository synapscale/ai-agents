# API Hotmart - Assinaturas - Obter Transações de Assinatura (Subscription Transactions)


| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Hotmart - Assinaturas - Obter Transações de Assinatura (Subscription Transactions) |
| **Identificador Interno** | hotmart_sub_001                                                 |
| **Título Curto (Ref.)**   | Hotmart Subscription Transactions                               |
| **Versão do Documento**   | 1.0.1                                                           |
| **Data de Criação**       | 2025-04-22                                                      |
| **Última Atualização**    | 2025-04-22                                                      |
| **Autor/Responsável**     | Equipe de Documentação                                          |
| **Fonte Original**        | Documentação oficial da API Hotmart                             |
| **URL de Referência**     | https://developers.hotmart.com/docs/pt-BR/v1/subscription/get-subscription-transactions/ |
| **Status do Documento**   | Em Uso                                                          |
| **Ambiente de Referência**| Produção                                                        |
| **Idioma Original**       | Português (BR)                                                  |
| **Formato de Datas (API)**| Timestamp Unix em milissegundos (UTC)                           |
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 2. Contexto
Este endpoint fornece um detalhamento completo de transações associadas a diferentes tipos de cobranças recorrentes na plataforma Hotmart, incluindo assinaturas regulares, Smart Installments (parcelamentos inteligentes) e Smart Recovery (recuperação de transações). O endpoint permite monitorar e analisar o histórico de pagamentos, recorrências e previsões de liberação. Os dados fornecidos apresentam defasagem de até 24 horas, sendo recomendado o uso do endpoint de Obter Assinaturas para informações em tempo real sobre o status atual das assinaturas. A funcionalidade é essencial para análises financeiras, reconciliação contábil, monitoramento de churn e acompanhamento detalhado do ciclo de vida de assinaturas. ID Interno: hotmart_sub_001.
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 3. Visão Geral da API/Endpoint(s)
O endpoint de Transações de Assinaturas permite consultar e rastrear todas as transações financeiras relacionadas a assinaturas, incluindo detalhes sobre pagamentos, status de recorrência, histórico e informações detalhadas sobre o assinante e produtor. Por padrão, retorna dados dos últimos 30 dias, mas pode ser configurado para intervalos personalizados através dos parâmetros de data. Suporta filtragem por diferentes critérios como nome do assinante, tipo de cobrança, status da assinatura, método de pagamento e códigos específicos. A resposta inclui informações abrangentes sobre cada transação, incluindo valor, comissões, datas relevantes, informações de trial, detalhes do plano e dados do assinante. O endpoint implementa paginação para lidar com grandes volumes de dados.
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 4. Detalhes Técnicos
### Endpoint de Transações de Assinatura
*   **Endpoint URL:** `https://developers.hotmart.com/payments/api/v1/subscriptions/transactions`
*   **Método HTTP:** `GET`
*   **Autenticação:** Bearer Token no cabeçalho `Authorization`. Ex: `Authorization: Bearer :access_token`
*   **Limitação de Taxa:** Sujeito às políticas de rate limit da Hotmart (consulte a documentação oficial para limites específicos por ambiente)
*   **Formato da Resposta:** JSON
*   **Codificação:** UTF-8
*   **Paginação:** Baseada em token (`page_token`, `next_page_token`, `prev_page_token`)
*   **Timeout Recomendado:** 30 segundos
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 5. Parâmetros de Entrada (Query Parameters)


| Parâmetro             | Descrição Detalhada                                                                                                                                                           | Tipo    | Notas / Exemplo                                                                                                                                                           |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `max_results`         | Define o número máximo de itens (transações) a serem retornados em uma única página de resultados. Útil para controlar o volume de dados por requisição e gerenciar a performance da API. Se não for especificado, um valor padrão definido pelo sistema será usado. | integer | Ex: `50`. Os valores típicos variam entre 10 e 100, dependendo da política da API. Valores menores resultam em respostas mais rápidas, enquanto valores maiores podem ser mais eficientes para processamento em lote. |
| `page_token`          | Token alfanumérico obtido no campo `page_info.next_page_token` ou `page_info.prev_page_token` da resposta anterior. Usado para navegar para a próxima ou página anterior de resultados, respectivamente. Funciona como um ponteiro para a posição na lista completa de resultados. | string  | Ex: `05b60506b6d4f87a9c7a5f908b23c8a1`. Se omitido, retorna a primeira página. Possui comprimento fixo de 32 caracteres alfanuméricos. Não é possível manipular ou construir este token manualmente. |
| `product_id`          | Filtra transações associadas a um produto específico usando seu Identificador Único (ID) na Hotmart. Útil para análises de desempenho de produto específico ou para extração de dados relativos apenas a um produto. | integer | Ex: `1234567`. Formato: Número inteiro positivo de até 10 dígitos. Deve corresponder a um ID de produto válido ao qual o usuário autenticado tenha acesso. |
| `transaction`         | Filtra por um código de transação específico (único). Retorna apenas os detalhes da transação correspondente a este código. Útil para consultar detalhes completos de uma transação específica quando se conhece seu identificador único. | string  | Ex: `HP1771601234`. Formato: String alfanumérica com prefixo específico (geralmente "HP" para Hotmart Payment) seguido de números. Comprimento típico entre 10-15 caracteres. |
| `subscriber_name`     | Filtra transações pelo nome do comprador (assinante). A busca é parcial e case-insensitive, retornando resultados onde o nome do assinante contenha o texto informado. Útil para suporte ao cliente quando se conhece apenas parte do nome. | string  | Ex: `"João Silva"`. Aceita caracteres especiais, acentos e espaços. Recomenda-se usar pelo menos 3 caracteres para evitar resultados muito amplos. |
| `subscriber_email`    | Filtra transações pelo e-mail exato do comprador (assinante). A busca é case-insensitive, mas deve corresponder ao e-mail completo. Método mais preciso para identificar um assinante específico. | string  | Ex: `"joao.silva@email.com"`. Deve ser um endereço de e-mail válido em formato padrão. |
| `billing_type`        | Filtra transações com base no tipo de cobrança. Permite distinguir entre diferentes modelos de pagamento implementados pela Hotmart. Valores possíveis: `SUBSCRIPTION` (Cobrança recorrente padrão), `SMART_INSTALLMENT` (Parcelamento inteligente, onde cada parcela é uma nova transação), `SMART_RECOVERY` (Recuperação automatizada de transação previamente negada). | string  | Ex: `SMART_INSTALLMENT`. Sensível a maiúsculas e minúsculas, deve usar exatamente o formato especificado. |
| `subscription_status` | Filtra transações com base na situação atual da assinatura associada. Valores possíveis: `STARTED` (Iniciada, aguardando primeiro pagamento), `INACTIVE` (Inativa, nunca ativada), `ACTIVE` (Ativa e em dia), `DELAYED` (Ativa mas com pagamento atrasado), `CANCELLED_BY_ADMIN` (Cancelada por administrador da plataforma), `CANCELLED_BY_CUSTOMER` (Cancelada pelo cliente), `CANCELLED_BY_SELLER` (Cancelada pelo vendedor/produtor), `OVERDUE` (Vencida, não renovada após término). | string  | Ex: `ACTIVE`. Sensível a maiúsculas e minúsculas, deve usar exatamente o formato especificado. |
| `recurrency_status`   | Filtra transações com base no status de pagamento da recorrência específica. Valores possíveis: `PAID` (Paga com sucesso), `NOT_PAID` (Não paga, pendente ou recusada), `CLAIMED` (Em disputa), `REFUNDED` (Reembolsada), `CHARGEBACK` (Estorno via operadora do cartão). | string  | Ex: `PAID`. Sensível a maiúsculas e minúsculas, deve usar exatamente o formato especificado. |
| `purchase_status`     | Filtra transações com base na situação geral da compra associada à recorrência. Este campo oferece status mais granulares sobre o processamento da transação financeira específica. | string  | Ex: `APPROVED`, `PENDING`, `REFUSED`. Outros valores incluem: `BILLET_PRINTED` (Boleto gerado), `WAITING_PAYMENT` (Aguardando pagamento), `COMPLETE` (Processada completamente), `CANCELED` (Cancelada). Sensível a maiúsculas e minúsculas. |
| `transaction_date`    | Data inicial (inclusive) do período para o filtro de transações, baseada na data da transação. Define o limite inferior do intervalo de datas para a consulta. | long    | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1609459200000` (01/01/2021 00:00:00 UTC). Deve ser menor ou igual a `end_transaction_date` se ambos forem especificados. |
| `end_transaction_date`| Data final (inclusive) do período para o filtro de transações, baseada na data da transação. Define o limite superior do intervalo de datas para a consulta. | long    | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1640995199000` (31/12/2021 23:59:59 UTC). Deve ser maior ou igual a `transaction_date` se ambos forem especificados. |
| `offer_code`          | Filtra transações associadas a uma oferta específica, usando a chave da oferta como identificador da assinatura original. Útil para análises de desempenho por oferta ou campanha específica. | string  | Ex: `DEFAULT_OFFER`. Outras ofertas comuns podem ter códigos como `SPECIAL_LAUNCH`, `BLACK_FRIDAY`, `SUMMER_SALE`. Sensível a maiúsculas e minúsculas. |
| `purchase_payment_type` | Filtra transações pelo método de pagamento utilizado na compra. Permite analisar padrões de pagamento ou resolver problemas específicos de determinados métodos. | string  | Valores disponíveis: `CREDIT_CARD` (Cartão de crédito), `BILLET` (Boleto bancário), `PIX` (Pagamento instantâneo brasileiro), `PAYPAL` (PayPal), `GOOGLE_PAY` (Google Pay), `APPLE_PAY` (Apple Pay), `CASH_PAYMENT` (Pagamento em dinheiro), `WALLET` (Carteira digital), `BANK_TRANSFER` (Transferência bancária). Sensível a maiúsculas e minúsculas. |
| `subscriber_code`     | Filtra transações associadas a uma instância específica de assinatura de um comprador, usando seu código alfanumérico único. Útil quando um mesmo comprador tem múltiplas assinaturas do mesmo produto. É o identificador mais preciso para uma assinatura específica. | string  | Ex: `SUB1A2B3C`. Formato: String alfanumérica geralmente começando com "SUB" seguida de caracteres alfanuméricos. Comprimento típico entre 8-12 caracteres. Sensível a maiúsculas e minúsculas. |
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 6. Parâmetros de Saída (Estrutura da Resposta JSON)
### Endpoint de Transações de Assinatura
#### 6.1.1 Estrutura Geral
| Campo         | Descrição Detalhada                                                                                                  | Tipo   |
| :------------ | :------------------------------------------------------------------------------------------------------------------- | :----- |
| `items`       | Array (lista) contendo os objetos de transação de assinatura que correspondem aos critérios de filtro da requisição. Cada objeto representa uma transação única com todos seus detalhes relacionados. O array estará vazio se nenhum resultado for encontrado para os filtros aplicados. | array  |
| `page_info`   | Objeto contendo informações sobre a paginação dos resultados, incluindo tokens para navegação entre páginas e estatísticas sobre a quantidade de resultados. Este objeto estará sempre presente, mesmo quando não há resultados ou quando todos os resultados cabem em uma única página. | object |


#### 6.1.2 Detalhes do Objeto `items` (Cada item no array `items`)
| Campo Aninhado             | Descrição Detalhada                                                                                                                                | Tipo      | Notas / Exemplo                                                                                             |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------- |
| `subscription_id`          | Identificador numérico único da assinatura na plataforma Hotmart. Este ID é consistente para todas as transações relacionadas à mesma assinatura, permitindo rastrear todo o histórico de uma assinatura específica. | integer   | Ex: `12345`. Número inteiro positivo que pode conter de 1 a 10 dígitos. Permanece constante para a mesma assinatura, mesmo após renovações, atualizações ou mudanças de status. |
| `last_update`              | Data e hora da última atualização registrada para esta transação específica. Reflete o momento mais recente em que qualquer informação desta transação foi modificada. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1577890800000` (01/01/2020 00:00:00 UTC). |
| `subscriber_code`          | Código alfanumérico único que identifica a instância específica da assinatura para um assinante. Um mesmo comprador pode ter vários `subscriber_code`s diferentes para diferentes produtos ou mesmo para múltiplas assinaturas do mesmo produto. Este código permanece o mesmo durante toda a vida da assinatura. | string    | Ex: `SUB000001`. Formato: Geralmente começa com "SUB" seguido de caracteres alfanuméricos. Comprimento típico entre 8-12 caracteres. |
| `status`                   | Situação atual da assinatura no momento da consulta. Indica o estado operacional da assinatura como um todo, não apenas da transação específica. | string    | Valores possíveis: `STARTED`, `INACTIVE`, `ACTIVE`, `DELAYED`, `CANCELLED_BY_ADMIN`, `CANCELLED_BY_CUSTOMER`, `CANCELLED_BY_SELLER`, `OVERDUE`. Veja detalhes completos na descrição do parâmetro de entrada `subscription_status`. |
| `billing_type`             | Indica o tipo de cobrança desta transação. Define o modelo de negócio aplicado a esta recorrência específica. | string    | Valores: `SUBSCRIPTION` (Assinatura regular), `SMART_INSTALLMENT` (Parcelamento inteligente), `SMART_RECOVERY` (Recuperação automática). |
| `adoption_date`            | Data e hora em que o cliente originalmente aderiu (comprou) a assinatura. Representa o início do relacionamento comercial para esta assinatura. Esta data permanece a mesma para todas as transações relacionadas à mesma assinatura. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Permanece constante para todas as transações da mesma assinatura. |
| `date_next_charge`         | Data e hora agendada para a próxima tentativa de cobrança da recorrência. Importante para prever fluxo de caixa futuro e para comunicações proativas com clientes. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Pode ser `null` se a assinatura estiver cancelada, finalizada ou se for a última recorrência de um plano com número fixo de ciclos. |
| `last_recurrency_start_date` | Data e hora em que a última (ou atual) recorrência desta assinatura foi iniciada. Representa o início do ciclo de cobrança atual. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Utilizada para cálculos de período ativo e para determinar quando será a próxima cobrança. |
| `cancellation_date`        | Data e hora em que a assinatura foi cancelada. Importante para análises de churn e para determinar períodos de acesso residual após cancelamento. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Será `null` se a assinatura não estiver cancelada. Quando presente, indica que não haverá mais cobranças futuras. |
| `max_cycles`               | Número máximo de ciclos (recorrências) definidos para este plano de assinatura pelo produtor. Define a duração máxima prevista para a assinatura. | integer   | Ex: `12` (para um plano anual com pagamentos mensais). Pode ser `null` ou `0` para assinaturas vitalícias/sem limite de ciclos. É comum em cursos ou produtos com acesso vitalício após determinado número de pagamentos. |
| `last_recurrency_number`   | Número sequencial da última (ou atual) recorrência processada para esta assinatura. Indica em qual ciclo de cobrança a assinatura se encontra. | integer   | Ex: `1` (primeira recorrência), `12` (décima segunda). Começa em 1 para a primeira cobrança e incrementa a cada novo ciclo. Útil para comparar com `max_cycles` e determinar quando uma assinatura está prestes a completar todos os ciclos. |
| `has_unpaid_recurrency`    | Indica (true/false) se existem recorrências anteriores desta assinatura que não foram pagas. Útil para identificar assinantes com histórico de inadimplência. | boolean   | `true` (existem recorrências não pagas anteriores) ou `false` (todas as recorrências anteriores foram pagas ou não houve recorrências anteriores). |
| `has_credit_card_change`   | Indica (true/false) se a cobrança foi suspensa devido a problemas ou restrições com o cartão de crédito registrado. Sinaliza necessidade de atualização dos dados de pagamento. | boolean   | `true` (há problema com o cartão, exigindo atualização) ou `false` (não há problemas conhecidos com o método de pagamento). |
| `is_paid_anticipation`     | Indica (true/false) se esta transação específica corresponde a uma antecipação de recorrências paga. Identifica pagamentos antecipados que cobrem múltiplos ciclos futuros. | boolean   | `true` (esta transação representa um pagamento antecipado de ciclos futuros) ou `false` (transação normal de um único ciclo). Quando `true`, geralmente o campo `recurrency.number_list` conterá os números dos ciclos cobertos por esta antecipação. |
| `is_paid_negotiation`      | Indica (true/false) se esta transação específica corresponde a uma negociação de dívida paga. Identifica acordos especiais para regularização de pagamentos atrasados. | boolean   | `true` (esta transação representa um acordo de negociação de dívida) ou `false` (transação normal). |
| `product`                  | Objeto contendo detalhes do produto associado a esta assinatura. Fornece contexto sobre qual produto ou serviço está sendo assinado. | object    | Ver detalhes abaixo (6.1.3). Este objeto estará sempre presente em cada item do array `items`. |
| `trial_info`               | Objeto contendo informações sobre o período de trial (teste gratuito), se aplicável. Relevante para análises de conversão de trial para assinatura paga. | object    | Ver detalhes abaixo (6.1.4). Este objeto estará sempre presente, mesmo que a assinatura não tenha período trial (nesse caso, `trial` será `false`). |
| `plan`                     | Objeto contendo detalhes do plano de assinatura específico. Inclui informações sobre a periodicidade, nome comercial e oferta associada. | object    | Ver detalhes abaixo (6.1.5). Este objeto estará sempre presente em cada item do array `items`. |
| `recurrency`               | Objeto contendo detalhes sobre a recorrência específica desta transação. Fornece informações detalhadas sobre o ciclo de cobrança atual. | object    | Ver detalhes abaixo (6.1.6). Este objeto estará sempre presente em cada item do array `items`. |
| `purchase`                 | Objeto contendo detalhes sobre a transação de compra específica associada a esta recorrência. Inclui informações financeiras e de processamento do pagamento. | object    | Ver detalhes abaixo (6.1.7). Este objeto estará sempre presente em cada item do array `items`. |
| `subscriber`               | Objeto contendo detalhes sobre o comprador (assinante). Fornece informações de contato e identificação do cliente. | object    | Ver detalhes abaixo (6.1.8). Este objeto estará sempre presente em cada item do array `items`. |
| `producer`                 | Objeto contendo detalhes sobre o vendedor (produtor) do produto. Identifica o responsável pelo produto ou serviço. | object    | Contém o campo `name` (string) com o nome do produtor/vendedor conforme registrado na plataforma Hotmart. |


#### 6.1.3 Detalhes do Objeto `items.product`
| Campo Aninhado | Descrição Detalhada         | Tipo    | Notas / Exemplo |
| :------------- | :-------------------------- | :------ | :-------------- |
| `id`           | ID numérico único do produto na plataforma Hotmart. Este identificador permanece consistente em todas as transações relacionadas ao mesmo produto, independente do assinante ou do plano. | integer | Ex: `1001`. Número inteiro positivo que pode conter de 1 a 10 dígitos. É o mesmo ID usado em outros endpoints da API Hotmart relacionados a produtos. |
| `name`         | Nome comercial do produto conforme cadastrado pelo produtor na plataforma Hotmart. Este é o nome visível para os clientes durante o processo de compra e nos recibos. | string  | Ex: `"Curso Avançado de Marketing Digital"`. Pode conter qualquer caractere, incluindo espaços, números e caracteres especiais. Comprimento típico entre 5-100 caracteres. |


#### 6.1.4 Detalhes do Objeto `items.trial_info`
| Campo Aninhado   | Descrição Detalhada                                            | Tipo      | Notas / Exemplo                                                       |
| :--------------- | :------------------------------------------------------------- | :-------- | :-------------------------------------------------------------------- |
| `trial`          | Indica (true/false) se a assinatura incluiu um período trial (teste gratuito ou com valor reduzido). Fundamental para análises de conversão e efetividade de períodos de teste. | boolean   | `true` (assinatura iniciou com período trial) ou `false` (sem período trial). |
| `trial_period`   | Duração do período trial em dias. Define quanto tempo o cliente teve acesso ao produto antes do início das cobranças regulares. | integer   | Ex: `7` (uma semana), `30` (um mês). Será `0` ou `null` se `trial` for `false`. Números inteiros positivos, tipicamente entre 1-90 dias. |
| `trial_end`      | Data e hora em que o período trial terminou ou terminará. Marca o momento em que a primeira cobrança regular deveria ocorrer após o período de teste. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1580482800000` (31/01/2020 00:00:00 UTC). Relevante apenas se `trial` é `true`. Será `null` ou igual a `adoption_date` se não houver trial. |


#### 6.1.5 Detalhes do Objeto `items.plan`
| Campo Aninhado      | Descrição Detalhada                                                       | Tipo    | Notas / Exemplo                                          |
| :------------------ | :------------------------------------------------------------------------ | :------ | :------------------------------------------------------- |
| `name`              | Nome do plano de assinatura específico conforme definido pelo produtor. Identifica a variante ou nível do produto que o cliente assinou. | string  | Ex: `"Plano Mensal Premium"`. Pode conter qualquer caractere, incluindo espaços e caracteres especiais. Comprimento típico entre 3-50 caracteres. |
| `recurrency_period` | Frequência de cobrança em dias (intervalo entre recorrências). Define o ciclo de faturamento da assinatura. | integer | Ex: `30` (mensal), `365` (anual), `7` (semanal), `15` (quinzenal), `90` (trimestral), `180` (semestral). Número inteiro positivo representando a quantidade de dias entre cobranças. |
| `recurrency_type`   | Descrição textual da frequência de cobrança. Versão legível para humanos do `recurrency_period`. | string  | Valores comuns: `"MONTHLY"` (30 dias), `"YEARLY"` (365 dias), `"WEEKLY"` (7 dias), `"BIWEEKLY"` (15 dias), `"QUARTERLY"` (90 dias), `"SEMIANNUAL"` (180 dias). |
| `coupon_code`       | Código do cupom de desconto aplicado na adesão, se houver. Identifica promoções específicas utilizadas pelo cliente. | string  | Ex: `"PROMO10"`, `"BLACK50"`, `"LAUNCH25"`. Pode ser `null` se nenhum cupom foi aplicado. Formato: String alfanumérica, geralmente entre 3-20 caracteres. |
| `offer`             | Objeto contendo informações sobre a oferta específica usada na assinatura. Identifica a campanha de marketing ou variante de oferta aplicada. | object  | Contém três campos principais: `code` (string, código interno da oferta), `description` (string, descrição legível da oferta), `key` (string, identificador único da oferta). |


#### 6.1.6 Detalhes do Objeto `items.recurrency`
| Campo Aninhado             | Descrição Detalhada                                                                                                                             | Tipo      | Notas / Exemplo                                                                                              |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :----------------------------------------------------------------------------------------------------------- |
| `status`                   | Situação do pagamento desta recorrência específica. Indica se a cobrança atual foi paga, está pendente, foi reembolsada, etc. | string    | Valores possíveis: `PAID` (Paga com sucesso), `NOT_PAID` (Não paga, inclui pendentes e recusadas), `CLAIMED` (Em disputa aberta pelo cliente), `REFUNDED` (Reembolsada, valor devolvido ao cliente), `CHARGEBACK` (Estorno via operadora do cartão, geralmente contestação formal). |
| `number`                   | Número sequencial desta recorrência dentro da assinatura. Identifica qual ciclo de cobrança esta transação representa. | integer   | Ex: `1` (primeira cobrança), `2` (segunda cobrança), `12` (décima segunda cobrança). Começa em 1 e incrementa por 1 a cada ciclo de cobrança. Importante para rastrear a progressão da assinatura. |
| `start_datetime`           | Data e hora em que esta recorrência específica foi iniciada (ou deveria ter iniciado). Marca o início do ciclo de cobrança atual. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1577890800000` (01/01/2020 00:00:00 UTC). Esta data, combinada com `recurrency_period`, determina quando a próxima cobrança ocorrerá. |
| `payment_delay_days`       | Número de dias de atraso no pagamento desta recorrência, calculado a partir da data de vencimento até a data atual (se `status` for `NOT_PAID`). Útil para categorizações de inadimplência. | integer   | Ex: `5` (cinco dias de atraso). Será `0` se a recorrência foi paga em dia, ainda não venceu, ou possui status diferente de `NOT_PAID`. Número inteiro não-negativo. |
| `transaction_type`         | Tipo específico desta transação de recorrência. Indica se é uma cobrança regular, uma retentativa ou uma intervenção manual. | string    | Valores possíveis: `"RECURRING"` (cobrança automática normal do ciclo), `"MANUAL"` (cobrança gerada manualmente, geralmente pelo suporte), `"RETRY"` (retentativa automática após falha anterior). Outros valores podem incluir `"RECOVERY"` (recuperação especial) ou `"RESCHEDULED"` (reagendada). |
| `number_list`              | Lista de números de recorrência (separados por vírgula) incluídos em caso de antecipação ou negociação. Identifica quais ciclos futuros ou atrasados estão sendo cobertos por esta transação única. | string    | Ex: `"3, 4, 5"` (esta transação cobre as recorrências 3, 4 e 5). Será `null` para transações normais que cobrem apenas um ciclo. Relevante quando `is_paid_anticipation` ou `is_paid_negotiation` é `true`. |
| `transaction_sequence`     | Enumera as tentativas de transação dentro da *mesma* recorrência. Identifica se esta é a primeira tentativa de cobrança ou uma retentativa subsequente para o mesmo ciclo. | integer   | Ex: `1` (primeira tentativa), `2` (primeira retentativa), `3` (segunda retentativa). Começa em 1 para a primeira tentativa e incrementa a cada nova tentativa para a mesma recorrência. Diferente de `number`, que identifica o ciclo. |
| `is_current_purchase`      | Indica (true/false) se esta é a transação mais recente (atual) para esta recorrência específica. Útil quando há múltiplas tentativas de transação para o mesmo ciclo de recorrência. | boolean   | `true` (esta é a transação mais recente/atual para este ciclo) ou `false` (existe uma transação mais recente para este mesmo ciclo). Importante para identificar o status atual quando há múltiplas tentativas/entradas para a mesma recorrência. |
| `has_retry`                | Indica (true/false) se já foram realizadas retentativas automáticas de cobrança para esta recorrência. Sinaliza se o sistema já tentou processar novamente uma cobrança que falhou inicialmente. | boolean   | `true` (pelo menos uma retentativa já foi realizada) ou `false` (ainda não houve retentativas ou não foram necessárias). Ajuda a entender o histórico de processamento da recorrência. |
| `scheduled_retry`          | Data e hora da próxima retentativa automática de cobrança agendada para esta recorrência. Informa quando o sistema tentará novamente processar uma cobrança que falhou anteriormente. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1578063600000` (03/01/2020 00:00:00 UTC). Será `null` se não houver retentativa agendada (porque a recorrência já foi paga ou porque o sistema não fará mais tentativas). |


#### 6.1.7 Detalhes do Objeto `items.purchase`
| Campo Aninhado             | Descrição Detalhada                                                                                                                    | Tipo      | Notas / Exemplo                                                                                                                                 |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `transaction`              | Identificador alfanumérico único desta transação de compra específica. Código de referência único para cada operação financeira individual na plataforma Hotmart. | string    | Ex: `"HP17716123456789"`. Formato: Geralmente começa com "HP" (Hotmart Payment) seguido de números. Comprimento típico entre 10-15 caracteres. Este código é utilizado em comprovantes e para consultas específicas. |
| `order_date`               | Data e hora em que a ordem de transação foi criada. Representa o momento em que a solicitação de cobrança foi inicialmente registrada no sistema. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1577890800000` (01/01/2020 00:00:00 UTC). Esta data pode ser anterior à `approved_date` no caso de pagamentos não instantâneos como boletos. |
| `approved_date`            | Data e hora em que o pagamento desta transação foi confirmado/aprovado. Marca o momento em que o valor foi efetivamente recebido ou a transação foi autorizada pelo meio de pagamento. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1577890800000` (01/01/2020 00:00:00 UTC). Será `null` se o pagamento não foi aprovado (pendente, recusado, etc.). Importante para reconhecimento de receita. |
| `status`                   | Descreve a situação atual desta transação de compra específica. Status detalhado do processamento financeiro, mais granular que o `recurrency.status`. | string    | Valores comuns: `APPROVED` (Aprovada), `PENDING` (Pendente), `REFUSED` (Recusada), `REFUNDED` (Reembolsada), `CHARGEBACK` (Estorno via operadora), `BILLET_PRINTED` (Boleto gerado), `WAITING_PAYMENT` (Aguardando pagamento), `COMPLETE` (Completada), `CANCELED` (Cancelada). |
| `price`                    | Objeto contendo detalhes sobre o preço cobrado nesta transação. Inclui informações sobre moeda, valor da recorrência e valor total com taxas, se aplicável. | object    | Contém três campos principais: `currency` (string, código da moeda em formato ISO, ex: "BRL", "USD"), `value` (float, valor base da recorrência), `total_value` (float, valor total incluindo taxas adicionais, se houver). |
| `installment`              | Objeto detalhando o parcelamento, se aplicável a esta transação. Mais comum em Smart Installments, mas pode aparecer em transações regulares quando o cliente optou por parcelar no cartão de crédito. | object    | Contém dois campos principais: `installment_type` (string, ex: "MONTHLY" para parcelas mensais) e `installment_number` (integer, número de parcelas, ex: 3 para pagamento em 3 vezes). Pode ter valores padrão mesmo quando não há parcelamento efetivo. |
| `payment`                  | Objeto com detalhes específicos do método de pagamento usado nesta transação. Inclui informações como tipo de pagamento, bandeira do cartão, datas de expiração, etc. | object    | Ver detalhes abaixo (6.1.7.1). Este objeto estará sempre presente em cada transação no array `items`. |
| `commission`               | Objeto detalhando a comissão associada a esta transação. Contém valores brutos, líquidos e informações sobre taxas de conversão para produtor e afiliados. | object    | Contém vários campos monetários como `currency` (string, moeda), `original_value` (float, valor bruto), `producer_value` (float, valor líquido para o produtor), `conversion_rate` (float, taxa de conversão aplicada), `producer_paid_value` (float, valor efetivamente pago ao produtor), entre outros. |


##### 6.1.7.1 Detalhes do Objeto `items.purchase.payment`
| Campo Aninhado             | Descrição Detalhada                                                                                              | Tipo      | Notas / Exemplo                                                                                                                               |
| :------------------------- | :--------------------------------------------------------------------------------------------------------------- | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_type`             | Forma de pagamento utilizada nesta transação específica. Identifica o método pelo qual o cliente realizou o pagamento. | string    | Valores possíveis: `CREDIT_CARD` (Cartão de crédito), `BILLET` (Boleto bancário), `PIX` (Pagamento instantâneo brasileiro), `PAYPAL` (PayPal), `GOOGLE_PAY` (Google Pay), `APPLE_PAY` (Apple Pay), `CASH_PAYMENT` (Pagamento em dinheiro), `WALLET` (Carteira digital), `BANK_TRANSFER` (Transferência bancária). |
| `credit_card_flag`         | Bandeira do cartão de crédito informada no checkout (se `payment_type` for `CREDIT_CARD`). Identifica a instituição financeira emissora do cartão. | string    | Ex: `"VISA"`, `"MASTERCARD"`, `"AMEX"`, `"DINERS"`, `"ELO"`, `"HIPERCARD"`. Será `null` se o método de pagamento não for cartão de crédito. |
| `refusal_message`          | Mensagem descrevendo o motivo da recusa do pagamento, se `status` for `REFUSED`. Fornece detalhes sobre por que uma transação não foi aprovada. | string    | Ex: `"INSUFFICIENT FUNDS"`, `"CARD EXPIRED"`, `"SUSPECTED FRAUD"`, `"INVALID SECURITY CODE"`. Será `null` se o pagamento foi aprovado ou está pendente. Mensagens podem variar conforme a operadora e o gateway de pagamento. |
| `refund_chargeback_date`   | Data e hora em que ocorreu o reembolso ou chargeback desta transação. Marca o momento em que o valor foi devolvido ao cliente ou estornado. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1580482800000` (31/01/2020 00:00:00 UTC). Será `null` se não houve reembolso/chargeback. Relevante quando `status` é `REFUNDED` ou `CHARGEBACK`. |
| `pix_expiration_date`      | Data e hora de expiração do código PIX gerado (se `payment_type` for `PIX`). Define até quando o código PIX gerado pode ser utilizado pelo cliente para pagamento. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1577934000000` (01/01/2020 12:00:00 UTC). Será `null` se não for PIX ou se já foi pago/expirado. Tipicamente definido para algumas horas ou dias após a geração. |
| `billet_expiration_date`   | Data e hora de vencimento do boleto (se `payment_type` for `BILLET`). Define até quando o boleto bancário pode ser pago pelo cliente sem acréscimos. | timestamp | Formato: Timestamp Unix em milissegundos (UTC). Ex: `1578614400000` (10/01/2020 00:00:00 UTC). Será `null` se não for Boleto ou se já foi pago/expirado. Geralmente definido para alguns dias após a geração. |
| `billet_reprint_code`      | URL ou código para reimpressão/consulta do boleto (se `payment_type` for `BILLET`). Permite acessar o boleto para pagamento ou verificação. | string    | Ex: `"https://payment.hotmart.com/boleto/12345678"` ou código alfanumérico que pode ser usado para recuperar o boleto. Pode ser `null` se o boleto não estiver mais disponível ou se o método de pagamento não for boleto. |
| `billet_recovery_type`     | Indica se a emissão do boleto foi automática (pelo sistema) ou manual (pelo usuário/suporte). Relevante para boletos de segunda via ou recuperação. | string    | Valores possíveis: `"MANUAL"` (gerado por intervenção humana), `"AUTOMATIC"` (gerado automaticamente pelo sistema). Pode ser `null` se não for boleto ou se for a primeira emissão regular. |


#### 6.1.8 Detalhes do Objeto `items.subscriber`
| Campo Aninhado | Descrição Detalhada                                                  | Tipo    | Notas / Exemplo                   |
| :------------- | :------------------------------------------------------------------- | :------ | :-------------------------------- |
| `id`           | ID numérico único do usuário comprador na plataforma Hotmart. Identificador permanente que não muda entre diferentes compras ou assinaturas do mesmo cliente. | integer | Ex: `10001`. Número inteiro positivo que pode conter de 1 a 10 dígitos. É o mesmo ID usado em outros endpoints da API Hotmart relacionados a clientes. |
| `name`         | Nome do comprador conforme registrado na Hotmart. Nome completo fornecido pelo cliente durante o processo de compra ou criação de conta. | string  | Ex: `"João da Silva"`. Pode conter qualquer caractere, incluindo espaços e caracteres especiais. Comprimento típico entre 3-100 caracteres. |
| `email`        | E-mail do comprador informado no momento da compra. Principal canal de contato com o cliente e identificador único para comunicações. | string  | Ex: `"joao.silva@exemplo.com"`. Formato padrão de endereço de email. Este é o email onde o cliente recebe comprovantes, acesso e comunicações sobre a assinatura. |
| `phone_ddd`    | Código DDD do telefone do comprador informado no momento da compra. Utilizado principalmente para o mercado brasileiro. | string  | Ex: `"11"` (São Paulo), `"21"` (Rio de Janeiro). Formato: String com 2 dígitos numéricos. Pode ser `null` se não foi informado ou não é aplicável ao país. |
| `phone`        | Número do telefone do comprador informado no momento da compra. Canal secundário de contato com o cliente. | string  | Ex: `"987654321"`. Formato: String contendo apenas dígitos numéricos, sem formatação. Comprimento típico entre 8-9 dígitos (no Brasil). Pode ser `null` se não foi informado pelo cliente. |


#### 6.1.9 Detalhes do Objeto `page_info`
| Campo Aninhado       | Descrição Detalhada                                                                                              | Tipo    | Notas / Exemplo                                                                   |
| :------------------- | :--------------------------------------------------------------------------------------------------------------- | :------ | :-------------------------------------------------------------------------------- |
| `next_page_token`    | Token alfanumérico para requisitar a próxima página de resultados. Use este valor no parâmetro `page_token` da próxima requisição para avançar na lista de resultados. | string  | Ex: `"05b60506b6d4f87a9c7a5f908b23c8a1"`. Será `null` se esta for a última página (não há mais resultados). Possui comprimento fixo de 32 caracteres alfanuméricos. |
| `prev_page_token`    | Token alfanumérico para requisitar a página anterior de resultados. Use este valor no parâmetro `page_token` da próxima requisição para voltar à página anterior da lista. | string  | Ex: `"cf1fg8a9d2e7b14c8f6a3d9e8b7c4a5f"`. Será `null` se esta for a primeira página (não há página anterior). Possui comprimento fixo de 32 caracteres alfanuméricos. |
| `results_per_page`   | Número real de itens retornados nesta página específica. Pode ser menor que o `max_results` solicitado, especialmente na última página quando não há itens suficientes para completar o tamanho solicitado. | integer | Ex: `50`. Número inteiro positivo representando a quantidade de itens no array `items` da resposta atual. Será `0` se nenhum resultado for encontrado para os filtros aplicados. |
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 7. Exemplos de Requisição e Resposta
### Endpoint de Transações de Assinatura
#### 7.1.1 Exemplo de Requisição (cURL)
```bash
curl --location --request GET 'https://developers.hotmart.com/payments/api/v1/subscriptions/transactions?transaction_date=1262354400000&end_transaction_date=1735830000000&max_results=10&subscriber_email=subscriberA@example.com' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer :access_token'
```


#### 7.1.2 Exemplo de Resposta (JSON - Sucesso 2xx)
```json
{
  "items": [
    {
      "last_recurrency_start_date": 1694113403000,
      "has_unpaid_recurrency": false,
      "product": {
        "name": "Product A",
        "id": 1001
      },
      "subscriber": {
        "phone": "1234567890",
        "name": "Subscriber A",
        "id": 10001,
        "phone_ddd": "12",
        "email": "subscriberA@example.com"
      },
      "recurrency": {
        "number": 1,
        "scheduled_retry": null, 
        "number_list": null,
        "transaction_sequence": 1,
        "start_datetime": 1694113403000,
        "payment_delays_days": 0,
        "transaction_type": "RECURRING",
        "is_current_purchase": true,
        "has_retry": false,
        "status": "PAID"
      },
      "last_recurrency_number": 1,
      "trial_info": {
        "trial_end": 1696705403000,
        "trial_period": 30,
        "trial": true
      },
      "purchase": {
        "order_date": 1577890800000,
        "price": {
          "total_value": 29.99,
          "currency": "USD",
          "value": 29.99
        },
        "installment": {
          "installment_number": 1,
          "installment_type": "MONTHLY"
        },
        "payment": {
          "refusal_message": null,
          "refund_chargeback_date": null,
          "payment_type": "CREDIT_CARD",
          "billet_expiration_date": null,
          "billet_recovery_type": null,
          "pix_expiration_date": null,
          "billet_reprint_code": null,
          "credit_card_flag": "VISA"
        },
        "commission": {
          "original_value": 29.99,
          "producer_paid_value": 20.0,
          "currency": "USD",
          "original_paid_value": 29.99,
          "conversion_rate": 1.0,
          "producer_value": 20.0
        },
        "approved_date": 1577890800000,
        "transaction": "TXN000001",
        "status": "APPROVED"
      },
      "cancellation_date": null,
      "is_paid_anticipation": false,
      "max_cycles": 12,
      "adoption_date": 1694113403000,
      "subscriber_code": "SUB000001",
      "date_next_charge": 1696705403000,
      "is_paid_negotiation": false,
      "last_update": 1577890800000,
      "billing_type": "SUBSCRIPTION",
      "producer": {
        "name": "Producer A"
      },
      "subscription_id": 1,
      "has_credit_card_change": false,
      "plan": {
        "offer": {
          "code": "OFFER_CODE_A",
          "description": "Offer A",
          "key": "OFFER_KEY_A"
        },
        "recurrency_period": 30,
        "coupon_code": "COUPON001",
        "recurrency_type": "MONTHLY",
        "name": "Plan A"
      },
      "status": "ACTIVE"
    }
  ],
  "page_info": {
    "results_per_page": 1,
    "next_page_token": null,
    "prev_page_token": null
  }
}
```


#### 7.1.3 Exemplo de Resposta (JSON - Erro 400 Bad Request)
```json
{
  "error": "INVALID_PARAMETER",
  "error_description": "Invalid value for parameter 'transaction_date'. Expected format: long (milliseconds)."
}
```
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 8. Códigos de Status e Tratamento de Erros
| Status Code            | Descrição Geral                                                                                                |
| :--------------------- | :------------------------------------------------------------------------------------------------------------- |
| `200 OK`               | Sucesso. A requisição foi bem-sucedida e os dados das transações foram retornados no corpo da resposta. Este status é retornado mesmo quando nenhum resultado é encontrado para os filtros aplicados (neste caso, o array `items` estará vazio). |
| `400 Bad Request`      | Erro na requisição. Verifique se os parâmetros fornecidos são válidos, se os formatos estão corretos (especialmente datas em formato timestamp) e se os valores estão dentro dos limites permitidos. Comum quando há erros de formatação nos parâmetros de consulta. |
| `401 Unauthorized`     | Falha na autenticação. O token de acesso (`Bearer Token`) está ausente, inválido ou expirado. É necessário obter um novo token de acesso válido antes de realizar novas requisições. |
| `403 Forbidden`        | Acesso negado. O token de acesso é válido, mas não possui permissão para acessar este recurso específico. Verifique se o usuário autenticado tem as permissões necessárias para consultar transações de assinatura. |
| `404 Not Found`        | Recurso não encontrado. Pode indicar que a URL está incorreta ou que os filtros aplicados são muito restritivos e não retornaram dados. Também pode significar que o endpoint foi movido ou descontinuado. |
| `429 Too Many Requests`| Limite de requisições excedido (Rate Limit). Aguarde antes de fazer novas chamadas. A API Hotmart implementa limites de taxa para proteger a infraestrutura. Implemente lógica de retry com backoff exponencial para lidar com este cenário. |
| `500 Internal Server Error` | Erro inesperado no servidor da API Hotmart. Tente novamente mais tarde ou contate o suporte. Este erro não está relacionado com sua requisição, mas com problemas internos da plataforma Hotmart. |
| `502 Bad Gateway`      | Problema de comunicação entre servidores da Hotmart. Indica um problema temporário na infraestrutura da API. Recomenda-se implementar retentativas após um breve intervalo. |
| `503 Service Unavailable` | Serviço temporariamente indisponível devido a sobrecarga ou manutenção. O serviço deve voltar ao normal automaticamente após um período. Implemente uma estratégia de retry com intervalos progressivos. |
| `504 Gateway Timeout`  | Timeout na comunicação interna dos servidores Hotmart. Similar ao 502, indica um problema temporário onde um servidor interno não respondeu a tempo. Recomenda-se implementar retentativas após um breve intervalo. |
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 9. Casos de Uso Comuns (20 Exemplos Específicos)
1. **Listar todas as transações de assinatura do último mês**
   * Objetivo: Obter histórico recente de todas as transações para análise financeira mensal
   * Como Fazer: Enviar requisição sem filtros específicos (usa filtro padrão de 30 dias) e implementar paginação para obter todos os resultados
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


2. **Consultar transações de um produto específico**
   * Objetivo: Analisar transações associadas apenas a um produto para relatórios de desempenho por produto
   * Como Fazer: Utilizar parâmetro `product_id=1234567` (ID do produto) e combinar com filtros de data para análise de período específico
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


3. **Verificar transações de assinatura ativas**
   * Objetivo: Identificar apenas assinaturas ativas para cálculo de MRR (Monthly Recurring Revenue) atual
   * Como Fazer: Usar parâmetro `subscription_status=ACTIVE` e implementar paginação para obter a lista completa
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


4. **Obter histórico de uma assinatura específica por código**
   * Objetivo: Analisar todas as transações de uma instância de assinatura específica para suporte ao cliente ou análise de caso
   * Como Fazer: Usar parâmetro `subscriber_code=SUB123456` para obter o histórico completo de uma assinatura individual
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


5. **Monitorar recuperações inteligentes (Smart Recovery)**
   * Objetivo: Verificar eficácia e volume do Smart Recovery para otimizar estratégias de retenção de clientes
   * Como Fazer: Filtrar por `billing_type=SMART_RECOVERY` e analisar a taxa de sucesso comparando os status das transações resultantes
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


6. **Analisar parcelamentos inteligentes (Smart Installment)**
   * Objetivo: Acompanhar transações de parcelamentos em andamento para previsão de fluxo de caixa futuro
   * Como Fazer: Filtrar por `billing_type=SMART_INSTALLMENT` e verificar datas de próximos pagamentos nas transações resultantes
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


7. **Acompanhar transações de um período específico (ex: último trimestre)**
   * Objetivo: Analisar desempenho financeiro entre datas específicas para relatório trimestral de receita
   * Como Fazer: Usar `transaction_date=1625097600000` (01/07/2021) e `end_transaction_date=1632960000000` (30/09/2021) para o terceiro trimestre de 2021
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


8. **Identificar transações por cartão de crédito VISA**
   * Objetivo: Analisar pagamentos feitos via cartão VISA para negociação de taxas com operadoras
   * Como Fazer: Filtrar por `purchase_payment_type=CREDIT_CARD` e após receber os resultados, filtrar programaticamente aqueles onde `items.purchase.payment.credit_card_flag == "VISA"`
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


9. **Verificar transações via PIX**
   * Objetivo: Analisar adoção e volume de pagamentos PIX para otimização de métodos de pagamento oferecidos
   * Como Fazer: Filtrar por `purchase_payment_type=PIX` e analisar a taxa de conversão e tempo médio de pagamento
   *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


10. **Monitorar assinaturas canceladas pelo cliente**
    * Objetivo: Analisar padrões e volume de cancelamento pelo cliente (churn) para identificar causas e implementar estratégias de retenção
    * Como Fazer: Filtrar por `subscription_status=CANCELLED_BY_CUSTOMER` e analisar dados como duração da assinatura e ciclo em que ocorreu o cancelamento
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


11. **Identificar assinaturas com recorrências não pagas**
    * Objetivo: Gerenciar inadimplência e iniciar processos de cobrança ou recuperação
    * Como Fazer: Filtrar por `recurrency_status=NOT_PAID` e ordenar por `payment_delay_days` para priorizar os casos mais críticos
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


12. **Analisar transações reembolsadas em um período**
    * Objetivo: Monitorar volume de reembolsos e seu impacto financeiro para ajustar projeções de receita
    * Como Fazer: Filtrar por `recurrency_status=REFUNDED` e definir intervalo com `transaction_date` e `end_transaction_date` para análise de período específico
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


13. **Monitorar chargebacks recebidos**
    * Objetivo: Acompanhar estornos e disputas para análise de risco e implementação de medidas preventivas
    * Como Fazer: Filtrar por `recurrency_status=CHARGEBACK` e analisar padrões nas transações estornadas (valor, produto, região, método de pagamento)
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


14. **Buscar transações por email do cliente**
    * Objetivo: Encontrar rapidamente o histórico de assinaturas de um cliente específico para suporte ou resolução de problemas
    * Como Fazer: Usar parâmetro `subscriber_email=cliente@exemplo.com` para obter todas as transações associadas a esse endereço de email
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


15. **Analisar assinaturas que usaram período de trial**
    * Objetivo: Monitorar taxa de conversão de clientes após período de teste para otimização de estratégias de marketing
    * Como Fazer: Listar transações e após receber os resultados, filtrar programaticamente aquelas onde `items.trial_info.trial == true` para análise de conversão
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


16. **Identificar assinaturas que completaram o último ciclo**
    * Objetivo: Prever churn natural de assinaturas com ciclos definidos para preparar campanhas de renovação ou upsell
    * Como Fazer: Filtrar por `subscription_status=ACTIVE` e após receber os resultados, identificar aquelas onde `items.last_recurrency_number` está próximo ou igual a `items.max_cycles`
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


17. **Verificar pagamentos via boleto pendentes de compensação**
    * Objetivo: Estimar receita futura de boletos emitidos mas ainda não pagos
    * Como Fazer: Filtrar por `purchase_payment_type=BILLET` e `purchase_status=BILLET_PRINTED` ou `purchase_status=WAITING_PAYMENT` para identificar boletos emitidos pendentes
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


18. **Monitorar transações com status de pagamento atrasado**
    * Objetivo: Identificar clientes com pagamentos atrasados para ações proativas de recuperação
    * Como Fazer: Filtrar por `subscription_status=DELAYED` e ordenar por data para priorizar os casos mais antigos
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


19. **Analisar transações por valor específico ou faixa de valor**
    * Objetivo: Segmentar clientes ou analisar desempenho de planos por preço para estratégias de precificação
    * Como Fazer: Listar transações (possivelmente filtradas por produto ou plano) e após receber os resultados, filtrar programaticamente por `items.purchase.price.value` para identificar faixas de preço específicas
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*


20. **Listar todas as assinaturas vencidas (OVERDUE)**
    * Objetivo: Identificar assinaturas que não foram renovadas após o término do período pago para campanhas de reativação
    * Como Fazer: Filtrar por `subscription_status=OVERDUE` e analisar tempo desde o vencimento para estratégias personalizadas de recuperação
    *(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 10. Notas Adicionais
*   **Defasagem de Dados:** Os dados retornados por este endpoint podem ter **até 24 horas de atraso** em relação ao estado atual das assinaturas e transações. Para informações em tempo real sobre o status atual da assinatura (sem o histórico detalhado de transações), utilize o endpoint `Obter Assinaturas`. Esta defasagem deve ser considerada especialmente em integrações que exigem dados atualizados para tomada de decisão.


*   **Período Padrão:** Se os parâmetros `transaction_date` e `end_transaction_date` não forem fornecidos, a API retorna dados dos **últimos 30 dias** a partir da data atual, exceto se o filtro `transaction` for usado para buscar uma transação específica. Para análises históricas completas, sempre especifique explicitamente o intervalo de datas desejado.


*   **Rate Limits:** A API Hotmart implementa limites de requisições por minuto e por hora que variam conforme o tipo de conta e ambiente. Exceder esses limites resultará em respostas com status code `429 Too Many Requests`. Recomenda-se implementar lógica de retry com backoff exponencial e distribuir requisições de grande volume ao longo do tempo. Consulte a documentação oficial da Hotmart para os limites específicos aplicáveis à sua conta.


*   **Paginação:** Para conjuntos de dados extensos, é essencial implementar corretamente a lógica de paginação usando `page_token` e `max_results`. O processo consiste em: 1) fazer a primeira requisição com `max_results` definido, 2) armazenar os resultados, 3) verificar se `page_info.next_page_token` não é nulo, 4) se houver mais páginas, fazer nova requisição incluindo `page_token=valor_do_next_page_token`, 5) repetir até que `next_page_token` seja nulo. Isso garante a recuperação completa do conjunto de dados.


*   **Formatos de Data:** Todas as datas na API são representadas como **Timestamp Unix em milissegundos (UTC)** no formato `long`. Ao converter esses valores para apresentação ao usuário, considere o fuso horário local do usuário. Para converter de uma data legível para timestamp, use funções como `new Date('2021-01-01').getTime()` em JavaScript ou equivalentes em outras linguagens. Para converter de timestamp para data legível, use `new Date(1609459200000).toLocaleString()`.


*   **Status de Assinatura vs. Status de Recorrência vs. Status de Compra:** É importante entender a distinção entre estes três status que aparecem na resposta:
    * `status` (na raiz do item) - Refere-se ao estado geral da assinatura (ACTIVE, CANCELLED, etc.)
    * `recurrency.status` - Refere-se ao estado do pagamento deste ciclo específico (PAID, NOT_PAID, etc.)
    * `purchase.status` - Refere-se ao estado detalhado da transação financeira específica (APPROVED, PENDING, etc.)
    
    Uma assinatura pode estar ACTIVE (status) com uma recorrência atual NOT_PAID (recurrency.status) e uma transação PENDING (purchase.status).


*   **Criptografia e Segurança:** Como este endpoint pode retornar informações financeiras e dados pessoais dos clientes, todas as comunicações devem usar HTTPS e os dados armazenados devem seguir as práticas recomendadas de segurança e conformidade com regulamentos como LGPD (Brasil) ou GDPR (Europa).


*   **Diferenças entre Ambientes:** Podem existir pequenas variações de comportamento entre os ambientes de sandbox e produção. Recomenda-se testar integrações completamente no ambiente de sandbox antes de implementar em produção, e estar preparado para lidar com possíveis discrepâncias.


*   **Otimização de Consultas:** Para melhor performance, especialmente ao lidar com grandes volumes de dados, recomenda-se usar filtros tão específicos quanto possível para reduzir o tamanho dos resultados. Por exemplo, em vez de buscar todas as transações e filtrar programaticamente, use os parâmetros de filtro disponíveis na API sempre que possível.
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
---
## 11. Metadados Internos (Para Indexação e RAG)
```json
{
  "doc_id": "hotmart_sub_001",
  "api_provider": "Hotmart",
  "api_product_area": "Assinaturas",
  "endpoint_focus": ["Obter Transações de Assinatura", "Consultar Histórico de Pagamentos Recorrentes", "Analisar Detalhes de Recorrências"],
  "version_api_endpoint": "v1",
  "data_sensitivity": "Confidential",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Assinatura", "Transação", "Recorrência", "Pagamento", "Assinante", "Produto", "Plano", "Oferta", "Comissão"],
  "context_level": ["intermediate", "advanced"],
  "topic_cluster": ["assinaturas", "cobrança recorrente", "pagamentos", "histórico financeiro", "hotmart api"],
  "db_relations": {
    "tables": ["subscribers", "subscriptions", "subscription_plans", "products", "transactions", "recurrences", "payments", "commissions"],
    "schemas": ["hotmart_payments", "hotmart_subscriptions", "hotmart_sales"]
  },
  "related_concepts": [
    "Smart Installment",
    "Smart Recovery",
    "Subscription Lifecycle",
    "Recurring Billing",
    "Payment Processing",
    "Churn Analysis",
    "MRR (Monthly Recurring Revenue)",
    "Data Lag",
    "API Pagination"
  ],
  "question_embeddings": [
    "Como obter o histórico detalhado de todas as transações de uma assinatura específica na Hotmart?",
    "Quais são os status possíveis para uma recorrência de assinatura na API da Hotmart?",
    "Como filtrar transações de assinatura por tipo de pagamento (PIX, Boleto, Cartão) na Hotmart?",
    "Como verificar a data da próxima cobrança de uma assinatura pela API?",
    "É possível consultar detalhes de comissão por transação de assinatura via API Hotmart?",
    "Como listar todas as transações de Smart Installment de um produto?",
    "Qual endpoint usar para ver o histórico de pagamentos de assinaturas Hotmart com até 24h de atraso?",
    "Como funciona a paginação na API de transações de assinatura da Hotmart?"
  ],
  "reasoning_pathways": [
    "subscription_payment_history_retrieval",
    "financial_data_filtering",
    "recurring_billing_analysis",
    "api_pagination_logic"
  ],
  "typical_usage_frequency": "Alta",
  "rate_limit_category": "Standard"
}
```
*(Ref: Hotmart Subscription Transactions, ID hotmart_subscriptiontransactions_001)*
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