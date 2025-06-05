# API Perfect Pay - Webhooks




# TEMPLATE PADRÃO PARA DOCUMENTAÇÃO DE APIS


# 1. Cabeçalho e Identificação
| Campo                     | Valor                                                           |
| :------------------------ | :-------------------------------------------------------------- |
| **Título do Documento**   | API Perfect Pay - Webhooks |
| **Identificador Interno** | perfectpay_ntf_001                                     |
| **Título Curto (Ref.)**   | PerfectPay Webhooks                                   |
| **Versão do Documento**   | 1.0.1                                                         |
| **Data de Criação**       | 2025-04-27                                                   |
| **Última Atualização**    | 2025-04-27                                                    |
| **Autor/Responsável**     | Equipe de Documentação                                        |
| **Fonte Original**        | Perfect Pay Documentation                                     |
| **URL de Referência**     | https://support.perfectpay.com.br/doc/perfect-pay/postback/integracao-via-webhook-com-a-perfect-pay |
| **Status do Documento**   | Em Uso                                                        |
| **Ambiente de Referência**| Produção                                                      |
| **Idioma Original**       | Português (BR)                                                |
| **Formato de Datas (API)**| YYYY-MM-DD HH:MM:SS (datetime), YYYY-MM-DD (date)             |


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 2. Contexto


> **Resumo:** Esta seção descreve o propósito e o contexto da funcionalidade de webhooks da Perfect Pay para notificação de eventos.


Este documento descreve como a plataforma Perfect Pay utiliza webhooks para notificar sistemas externos sobre eventos específicos (ex: vendas, alterações de status de pagamento). A integração via webhook permite a automação de processos e a sincronização de dados em tempo real entre a Perfect Pay e outros sistemas (CRM, ERP, plataformas de automação). O ID Interno desta documentação é `perfectpay_ntf_001`.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 3. Visão Geral da API/Endpoint(s)


> **Resumo:** Visão de alto nível sobre o mecanismo de webhook da Perfect Pay e seus casos de uso principais.


A Perfect Pay oferece um mecanismo de notificação via webhook onde, após a ocorrência de eventos selecionados (como uma venda aprovada, um boleto gerado, etc.), a plataforma envia uma requisição HTTP POST para uma URL configurada pelo cliente. Esta requisição contém um payload JSON com detalhes do evento ocorrido.


Principais funcionalidades habilitadas:
*   Sincronização de status de vendas e pagamentos.
*   Automação de entrega de produtos digitais.
*   Atualização de sistemas de CRM e ERP.
*   Cálculo de comissões e relatórios financeiros.


**Nota:** A implementação de um endpoint para receber e processar estes webhooks requer conhecimento técnico em desenvolvimento de software.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 4. Detalhes Técnicos


> **Resumo:** Especificações técnicas sobre como a Perfect Pay envia os webhooks e como o endpoint receptor deve ser configurado.


### Webhook Event Notification (Enviado pela Perfect Pay)
*   **Endpoint URL (Destino):** URL definida pelo cliente no painel da Perfect Pay para receber as notificações.
*   **Método HTTP:** `POST` (Inferido, pois é o padrão para envio de webhooks com payload JSON. A documentação original não especifica explicitamente).
*   **Autenticação:** A validação da origem da requisição pode ser feita verificando o campo `token` presente no payload JSON enviado.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 5. Parâmetros de Entrada


> **Resumo:** Detalhamento dos parâmetros necessários para configurar o webhook na plataforma Perfect Pay (não disponíveis na documentação fornecida).


### Configuração do Webhook (No Painel Perfect Pay)
A documentação original não detalha os parâmetros ou o processo de configuração do webhook na interface da Perfect Pay. Tipicamente, isso envolve:
1.  Fornecer a URL do seu endpoint que receberá as notificações.
2.  Selecionar os tipos de eventos que devem disparar o webhook (ex: Venda Aprovada, Boleto Gerado, Assinatura Cancelada).


Consulte a interface administrativa da Perfect Pay ou o suporte para detalhes sobre a configuração.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 6. Parâmetros de Saída (Estrutura da Resposta JSON)


> **Resumo:** Documentação completa da estrutura de dados JSON enviada pela Perfect Pay no corpo (payload) da requisição webhook.


### Payload do Webhook (Enviado pela Perfect Pay)


#### 6.1 Estrutura Raiz
| Campo                | Descrição | Tipo   | Notas |
| :------------------- | :-------- | :----- | :---- |
| `token`              | Token para identificar o postback recebido pela PerfectPay. Usado para validação. | string | |
| `code`               | Código identificador único da venda na Perfect Pay. | string | |
| `sale_amount`        | Valor total da venda (plano + frete). | decimal | |
| `currency_enum`      | Código da moeda (1 => BRL). | small integer | Consulte documentação para outros possíveis valores. |
| `coupon_code`        | Código do cupom de desconto utilizado, se houver. | string | `null` se não aplicado. |
| `installments`       | Número de parcelas da compra. | integer | |
| `installment_amount` | Valor de cada parcela. | decimal | `null` se não aplicável. |
| `shipping_type_enum` | Tipo de frete (1 => grátis, 2 => fixo). | small integer | |
| `shipping_amount`    | Valor do frete cobrado. | decimal | `null` se não aplicável. |
| `payment_method_enum`| Código do método de pagamento. | integer | Ver tabela de códigos abaixo. |
| `payment_type_enum`  | Código do tipo de pagamento. | small integer | Ver tabela de códigos abaixo. |
| `billet_url`         | URL para visualização/impressão do boleto. | string | Vazio se não for boleto. |
| `billet_number`      | Linha digitável do boleto. | string | `null` se não for boleto. |
| `billet_expiration`  | Data de vencimento do boleto. | datetime | Formato `YYYY-MM-DD HH:MM:SS`. `null` se não for boleto. |
| `quantity`           | Quantidade total de itens/produtos na venda. | integer | |
| `sale_status_enum`   | Código do status atual da venda. | small integer | Ver tabela de códigos abaixo. |
| `sale_status_detail` | Descrição textual detalhada do status da venda. | string | Ex: `checkout_saved`, `approved`. |
| `date_created`       | Data e hora da criação do pedido/checkout. | datetime | Formato `YYYY-MM-DD HH:MM:SS`. |
| `date_approved`      | Data e hora da aprovação do pagamento. | datetime | Formato `YYYY-MM-DD HH:MM:SS`. `null` se ainda não aprovado. |
| `product`            | Objeto contendo informações do produto principal. | object | Ver detalhes abaixo. |
| `plan`               | Objeto contendo informações do plano adquirido. | object | Ver detalhes abaixo. |
| `plan_itens`         | Array de itens adicionais entregues com o produto/plano. | array | Estrutura interna não detalhada na documentação. |
| `customer`           | Objeto contendo informações do comprador. | object | Ver detalhes abaixo. |
| `metadata`           | Objeto contendo metadados customizados (ex: UTMs). | object | Ver detalhes abaixo. |
| `webhook_owner`      | Código identificador do usuário Perfect Pay que configurou o webhook. | string | |
| `commission`         | Array de objetos, cada um representando uma comissão associada à venda. | array | Ver detalhes abaixo. |
| `marketplaces`       | Objeto contendo informações sobre marketplaces relacionados. | object | Ver detalhes abaixo. |


#### 6.2 Detalhes do Objeto `product`
| Campo Aninhado           | Descrição | Tipo |
| :----------------------- | :-------- | :--- |
| `code`                   | Código identificador do produto na Perfect Pay. | string |
| `name`                   | Nome do produto adquirido. | string |
| `external_reference`     | Código de referência externo do produto (para integração). | string |
| `guarantee`              | Período de garantia do produto em dias. | integer |


#### 6.3 Detalhes do Objeto `plan`
| Campo Aninhado        | Descrição | Tipo |
| :-------------------- | :-------- | :--- |
| `code`                | Código identificador do plano na Perfect Pay. | string |
| `name`                | Nome do plano adquirido. | string |
| `quantity`            | Quantidade de itens/acessos incluídos no plano. | integer |


#### 6.4 Detalhes do Objeto `customer`
| Campo Aninhado                | Descrição | Tipo | Notas |
| :---------------------------- | :-------- | :--- | :---- |
| `customer_type_enum`          | Tipo de cliente (1 => Pessoa Física, 2 => Pessoa Jurídica). | integer | `1` = 'physics', `2` = 'juridical'. |
| `full_name`                   | Nome completo do comprador. | string | |
| `email`                       | E-mail do comprador. | string | |
| `identification_type`         | Tipo do documento de identificação (ex: CPF, CNPJ). | string | |
| `identification_number`       | Número do documento de identificação. | string | |
| `birthday`                    | Data de nascimento do comprador. | date | Formato `YYYY-MM-DD`. |
| `phone_area_code`             | DDD do telefone do comprador. | string | |
| `phone_number`                | Número do telefone do comprador. | string | |
| `country`                     | Código do país do comprador (ex: BR). | string | |
| `state`                       | Sigla do estado do comprador (ex: RJ). | string | |
| `city`                        | Nome da cidade do comprador. | string | |
| `zip_code`                    | CEP do comprador. | string | |
| `street_name`                 | Nome da rua do endereço do comprador. | string | |
| `street_number`               | Número do endereço do comprador. | string | |
| `complement`                  | Complemento do endereço do comprador. | string | |
| `district`                    | Bairro do comprador. | string | |


#### 6.5 Detalhes do Objeto `metadata`
| Campo Aninhado           | Descrição | Tipo |
| :----------------------- | :-------- | :--- |
| `src`                    | Parâmetro `src` da URL de origem. | string |
| `utm_source`             | Parâmetro `utm_source` da URL de origem. | string |
| `utm_medium`             | Parâmetro `utm_medium` da URL de origem. | string |
| `utm_campaign`           | Parâmetro `utm_campaign` da URL de origem. | string |
| `utm_term`               | Parâmetro `utm_term` da URL de origem. | string |
| `utm_content`            | Parâmetro `utm_content` da URL de origem. | string |
| `utm_perfect`            | Parâmetro `utm_perfect` (específico da Perfect Pay). | string |


#### 6.6 Detalhes do Array `commission` (Cada objeto no array)
| Campo Aninhado                | Descrição | Tipo | Notas |
| :---------------------------- | :-------- | :--- | :---- |
| `affiliation_code`            | Código identificador do afiliado/parceiro. | string | |
| `affiliation_type_enum`       | Código do tipo de comissionado. | small integer | Ver tabela de códigos abaixo. |
| `name`                        | Nome do afiliado/parceiro. | string | |
| `email`                       | E-mail do afiliado/parceiro. | string | |
| `identification_number`       | CPF/CNPJ do afiliado/parceiro. | string | |
| `commission_amount`           | Valor da comissão para este afiliado/parceiro nesta venda. | decimal | |


#### 6.7 Detalhes do Objeto `marketplaces`
| Campo Aninhado                     | Descrição | Tipo | Notas |
| :--------------------------------- | :-------- | :--- | :---- |
| `marketplaces.{code}.name`         | Nome do marketplace. | string | `{code}` é o código identificador do marketplace. |
| `marketplaces.{code}.itens`        | Valor total cobrado referente aos itens vendidos neste marketplace. | double | |
| `marketplaces.{code}.sale`         | Valor total cobrado referente ao pedido neste marketplace. | double | |


#### 6.8 Tabelas de Códigos Enum
**`payment_method_enum` (Método de Pagamento):**
| Código | Descrição |
| :----- | :---------- |
| 0 | none |
| 1 | visa |
| 2 | bolbradesco |
| 3 | amex |
| 4 | elo |
| 5 | hipercard |
| 6 | master |
| 7 | melicard |
| 8 | free_price |


**`payment_type_enum` (Tipo de Pagamento):**
| Código | Descrição |
| :----- | :---------- |
| 0 | none |
| 1 | credit_card |
| 2 | ticket (Boleto) |
| 3 | paypal |
| 4 | credit_card_recurrent |
| 5 | free_price |
| 6 | credit_card_upsell |


**`sale_status_enum` (Status da Venda):**
| Código | Descrição |
| :----- | :---------- |
| 0 | none |
| 1 | pending |
| 2 | approved |
| 3 | in_process |
| 4 | in_mediation |
| 5 | rejected |
| 6 | cancelled |
| 7 | refunded |
| 8 | authorized |
| 9 | charged_back |
| 10 | completed |
| 11 | checkout_error |
| 12 | precheckout |
| 13 | expired |
| 16 | in_review |


**`affiliation_type_enum` (Tipo de Comissão):**
| Código | Descrição |
| :----- | :---------- |
| 0 | platform |
| 1 | producer |
| 2 | co_producer |
| 3 | affiliate_management |
| 4 | partner |
| 5 | affiliate |
| 6 | premium |
| 7 | provider |


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 7. Exemplos de Requisição e Resposta


> **Resumo:** Exemplo prático do payload JSON enviado pela Perfect Pay e a resposta esperada do endpoint receptor.


### Exemplo de Requisição Webhook (Payload Recebido pelo Seu Endpoint)
```json
{
  "token": "7378fa24f96b38a3b1805d7a6887bc82",
  "code": "PPCPMTB58MNF4E",
  "sale_amount": 385.00,
  "currency_enum": 1,
  "coupon_code": null,
  "installments": 12,
  "installment_amount": null,
  "shipping_type_enum": 1,
  "shipping_amount": null,
  "payment_method_enum": 4,
  "payment_type_enum": 1,
  "billet_url": "",
  "billet_number": null,
  "billet_expiration": null,
  "quantity": 5,
  "sale_status_enum": 2,
  "sale_status_detail": "approved",
  "date_created": "2019-03-09 08:24:02",
  "date_approved": "2019-03-09 08:25:15",
  "product": {
    "code": "PPPB3A07",
    "name": "Herus Caps",
    "external_reference": "42433",
    "guarantee": 30
  },
  "plan": {
    "code": "PPLQQ9Q9R",
    "name": "Herus Caps | 3 potes + 2 potes gratis",
    "quantity": 5
  },
  "plan_itens": [],
  "customer": {
    "customer_type_enum": 1,
    "full_name": "USER EXAMPLE",
    "email": "user_example2019@hotmail89254",
    "identification_type": "CPF",
    "identification_number": "57856874587",
    "birthday": "2020-08-28",
    "phone_area_code": "47",
    "phone_number": "9965568558",
    "street_name": "Rua Example Street",
    "street_number": "54",
    "district": "Example",
    "complement": "",
    "zip_code": "65875-564",
    "city": "Example City",
    "state": "RJ",
    "country": "BR"
  },
  "metadata": {
    "src": null,
    "utm_source": "google",
    "utm_medium": "cpc",
    "utm_campaign": "promo_natal",
    "utm_term": "suplemento",
    "utm_content": "ad_variation_1",
    "utm_perfect": null
  },
  "webhook_owner": "PPAKIOL",
  "commission": [
    {
      "affiliation_code": "PPAJFTR",
      "affiliation_type_enum": 5,
      "name": "USER EXAMPLE NAME",
      "email": "user_example@gmail.com",
      "identification_number": "07958658745",
      "commission_amount": 38.50
    },
    {
      "affiliation_code": "PPAGSDE",
      "affiliation_type_enum": 1,
      "name": "User Affiliation Example",
      "email": "affiliation_example@gmail.com",
      "identification_number": "08745785448",
      "commission_amount": 200.00
    },
    {
      "name": "PerfectPay",
      "commission_amount": 19.25,
      "affiliation_type_enum": 0
    }
  ],
  "marketplaces": {
    "PPMPCJI1G1": {
      "name": "HubSmart",
      "itens": -9.5,
      "sale": -26
    }
  }
}
```


### Exemplo de Resposta do Seu Endpoint (Enviada para a Perfect Pay)
Seu endpoint deve responder rapidamente à Perfect Pay para confirmar o recebimento. Uma resposta `200 OK` com um corpo JSON simples é recomendada. O processamento real dos dados pode ser feito de forma assíncrona.


```json
{
  "status": "received",
  "message": "Webhook received successfully and queued for processing."
}
```


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 8. Códigos de Status e Tratamento de Erros


> **Resumo:** Códigos de status HTTP que seu endpoint receptor deve usar e como lidar com erros comuns.


Seu endpoint receptor de webhooks deve retornar os seguintes códigos HTTP para a Perfect Pay:


| Status Code            | Descrição (Resposta do Seu Endpoint)                       | Ação Esperada da Perfect Pay |
| :--------------------- | :--------------------------------------------------------- | :------------------------- |
| `200 OK`               | Webhook recebido e aceito para processamento (síncrono ou assíncrono). | Considera a entrega bem-sucedida. |
| `202 Accepted`         | Webhook recebido e enfileirado para processamento assíncrono. | Considera a entrega bem-sucedida. |
| `400 Bad Request`      | Payload inválido ou malformado (erro do lado da Perfect Pay ou da integração). | Pode tentar reenviar ou marcar como falha. Verificar logs. |
| `401 Unauthorized`     | Falha na validação do token (se implementado).             | Pode tentar reenviar ou marcar como falha. Verificar configuração do token. |
| `429 Too Many Requests`| Seu endpoint está sobrecarregado.                           | Provavelmente tentará reenviar com backoff. |
| `500 Internal Server Error` | Erro inesperado no processamento do seu lado.             | Provavelmente tentará reenviar. |
| `503 Service Unavailable` | Seu endpoint está temporariamente indisponível.             | Provavelmente tentará reenviar. |


**Importante:** Responda rapidamente com um código `2xx` para evitar retentativas desnecessárias da Perfect Pay. Qualquer erro no processamento interno deve ser tratado de forma assíncrona e logado.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 9. Casos de Uso Comuns (20 Exemplos Específicos)


> **Resumo:** Lista abrangente de 20 aplicações práticas do webhook da Perfect Pay para automação e integração.


1.  **Atualizar Status de Venda no CRM:** 
    *   Objetivo: Manter registros de clientes e vendas sincronizados automaticamente
    *   Como Fazer: Usar `code` e `sale_status_enum` para sincronizar o status do pedido no seu CRM
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


2.  **Entregar Produto Digital:** 
    *   Objetivo: Liberação automática de acesso a produtos digitais após pagamento confirmado
    *   Como Fazer: Ao receber `sale_status_enum` = 2 (approved), enviar acesso ao curso/software para `customer.email`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


3.  **Monitorar Pagamentos por Boleto:** 
    *   Objetivo: Acompanhar ciclo de vida de boletos emitidos para prever fluxo de caixa
    *   Como Fazer: Filtrar por `payment_type_enum` = 2 e acompanhar `sale_status_enum` para status (pending, approved, expired)
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


4.  **Calcular Comissões de Afiliados:** 
    *   Objetivo: Automatizar o cálculo e registro de comissões para relatórios financeiros
    *   Como Fazer: Iterar sobre o array `commission` e registrar `commission_amount` por `affiliation_code` quando a venda for aprovada
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


5.  **Gerar Relatório de Vendas por Produto:** 
    *   Objetivo: Manter dashboard de desempenho de produtos atualizado em tempo real
    *   Como Fazer: Agrupar vendas aprovadas por `product.code` e somar `sale_amount`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


6.  **Recuperação de Carrinho:** 
    *   Objetivo: Aumentar taxa de conversão com estratégias de recuperação de carrinho abandonado
    *   Como Fazer: Identificar eventos com `sale_status_detail` = "checkout_saved" e iniciar fluxo de recuperação se não houver aprovação posterior
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


7.  **Segmentar Clientes por Valor:** 
    *   Objetivo: Criar estratégias de marketing diferenciadas baseadas em valor de cliente
    *   Como Fazer: Usar `sale_amount` de vendas aprovadas para classificar clientes (ex: High Value, Medium Value)
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


8.  **Rastrear Eficácia de Campanhas:** 
    *   Objetivo: Avaliar ROI de campanhas de marketing com dados precisos de conversão
    *   Como Fazer: Analisar `metadata` (utm_source, utm_campaign) de vendas aprovadas para atribuir conversões
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


9.  **Enviar Lembretes de Vencimento de Boleto:** 
    *   Objetivo: Reduzir taxa de abandono de boletos e aumentar conversão
    *   Como Fazer: Ao receber boleto gerado (`payment_type_enum` = 2, `sale_status_enum` = 1), agendar lembrete antes de `billet_expiration`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


10. **Gerenciar Estoque:** 
    *   Objetivo: Manter níveis de estoque atualizados automaticamente após vendas
    *   Como Fazer: Decrementar estoque usando `product.external_reference` quando `sale_status_enum` = 2
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


11. **Emitir Nota Fiscal:** 
    *   Objetivo: Automatizar processos fiscais e contábeis após vendas confirmadas
    *   Como Fazer: Coletar dados de `customer` e `product` para emissão automática quando `sale_status_enum` = 2
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


12. **Monitorar Chargebacks:** 
    *   Objetivo: Detectar e responder rapidamente a disputas de pagamento
    *   Como Fazer: Criar alerta ou processo interno quando `sale_status_enum` = 9 (charged_back)
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


13. **Análise de Fraude:** 
    *   Objetivo: Identificar padrões de transações suspeitas para prevenção de fraudes
    *   Como Fazer: Logar e analisar padrões em `customer` e `payment_method_enum` para vendas com status suspeitos ou rejeitados (`sale_status_enum` = 5)
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


14. **Enviar Pesquisa de Satisfação:** 
    *   Objetivo: Coletar feedback de clientes para melhorar produtos e serviços
    *   Como Fazer: Agendar envio de pesquisa para `customer.email` X dias após `date_approved`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


15. **Análise de Preferência de Pagamento:** 
    *   Objetivo: Otimizar opções de pagamento oferecidas com base em dados reais
    *   Como Fazer: Contabilizar vendas aprovadas por `payment_method_enum` e `payment_type_enum`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


16. **Iniciar Processo de Logística:** 
    *   Objetivo: Acelerar processo de separação e envio para maior satisfação do cliente
    *   Como Fazer: Enviar dados de `customer` e `product` para o sistema de WMS/fulfillment quando `sale_status_enum` = 2
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


17. **Dashboard Financeiro:** 
    *   Objetivo: Manter métricas financeiras atualizadas em tempo real
    *   Como Fazer: Atualizar métricas de receita (MRR, Vendas Diárias) usando `sale_amount` e `date_approved`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


18. **Análise Geográfica de Vendas:** 
    *   Objetivo: Identificar regiões com maior conversão para estratégias geotargeting
    *   Como Fazer: Mapear vendas aprovadas usando `customer.state` e `customer.city`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


19. **Taxa de Conversão por Plano:** 
    *   Objetivo: Otimizar configurações de planos baseado em dados de conversão
    *   Como Fazer: Calcular conversão comparando checkouts iniciados vs. aprovados por `plan.code`
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


20. **Programa de Fidelidade:** 
    *   Objetivo: Recompensar clientes recorrentes automaticamente com pontos ou benefícios
    *   Como Fazer: Atribuir pontos baseados em `sale_amount` para `customer.email` em vendas aprovadas
    *(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 10. Notas Adicionais


> **Resumo:** Informações complementares importantes sobre segurança, idempotência, performance e tratamento de eventos.


*   **Segurança:** Valide sempre o `token` recebido no payload para garantir que a requisição é originada pela Perfect Pay. Considere também validar o IP de origem, se a Perfect Pay fornecer uma lista de IPs fixos.
*   **Idempotência:** Seu sistema deve ser capaz de processar o mesmo evento (mesmo `code` e `sale_status_enum`, por exemplo) múltiplas vezes sem causar efeitos colaterais indesejados. Webhooks podem ser reenviados em caso de falha na entrega. Use o `code` da venda e o status/timestamp como chave de idempotência.
*   **Performance:** Responda à requisição webhook o mais rápido possível (idealmente < 2 segundos) com um status `2xx`. Realize processamentos demorados de forma assíncrona (usando filas de mensagens, por exemplo).
*   **Ordem dos Eventos:** Não há garantia de que os webhooks chegarão na ordem exata em que os eventos ocorreram. Use timestamps (`date_created`, `date_approved`) para lidar com a ordem correta, se necessário.
*   **Monitoramento e Logs:** Implemente logging detalhado para cada webhook recebido e processado. Monitore a taxa de erros e o tempo de resposta do seu endpoint.
*   **Falhas e Retentativas:** Esteja ciente de que a Perfect Pay pode tentar reenviar webhooks que falharam na entrega (não receberam resposta `2xx`). Verifique a política de retentativas da Perfect Pay.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 11. Metadados Internos (Para Indexação e RAG)


> **Resumo:** Metadados estruturados em formato JSON para facilitar a indexação e recuperação por sistemas RAG.


```json
{
  "doc_id": "perfectpay_ntf_001",
  "api_provider": "Perfect Pay",
  "api_product_area": "Notificações",
  "endpoint_focus": ["Receber Webhooks de Eventos", "Processar Notificações de Pagamento", "Sincronizar Status de Venda"],
  "version_api_endpoint": "N/A (Webhook Push)",
  "data_sensitivity": "Financial, PII",
  "integration_priority": "High",
  "business_impact": "Alto",
  "implementation_complexity": "Média",
  "key_entities_handled": ["Venda", "Pagamento", "Cliente", "Produto", "Plano", "Comissão", "Webhook"],
  "context_level": ["intermediate", "advanced"],
  "topic_cluster": ["pagamentos", "notificações", "webhooks", "e-commerce", "integração"],
  "db_relations": {
    "tables": ["sales", "customers", "products", "plans", "commissions", "webhook_logs"],
    "schemas": ["payments", "crm"]
  },
  "related_concepts": ["Integração de sistemas", "Processamento de pagamentos", "Notificações em tempo real", "Automação de marketing", "Sincronização de dados", "Idempotência"],
  "question_embeddings": [
    "Como integrar meu sistema com a Perfect Pay usando webhooks?",
    "Quais dados são enviados no webhook da Perfect Pay?",
    "Como processar notificações de pagamento da Perfect Pay?",
    "Como sei se um pagamento foi aprovado via webhook da Perfect Pay?",
    "Qual a estrutura do JSON do webhook da Perfect Pay?",
    "Como validar um webhook da Perfect Pay?",
    "O que significa o status de venda 'approved' (código 2) na Perfect Pay?",
    "Como obter informações do cliente a partir do webhook da Perfect Pay?",
    "Como calcular comissões usando o webhook da Perfect Pay?"
  ],
  "reasoning_pathways": ["event-driven", "process", "conditional", "data-mapping"],
  "typical_usage_frequency": "Alta (por evento)",
  "rate_limit_category": "N/A (Push)",
  "authentication_requirements": ["Token Validation (in payload)"],
  "typical_integration_points": ["CRM", "ERP", "Plataforma de Automação", "Sistema de Fulfillment", "Sistema Financeiro"],
  "common_error_patterns": ["Falha na validação do token", "Erro de processamento assíncrono", "Falha de idempotência", "Timeout na resposta"]
}
```


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 12. Checklist de Implementação (Opcional)


> **Resumo:** Lista verificável dos aspectos técnicos a serem considerados na implementação do receptor de webhooks.


- [ ] **Endpoint Receptor:**
  - [ ] Criar endpoint HTTP(S) público para receber requisições POST
  - [ ] Configurar certificado SSL válido (HTTPS)
  - [ ] Garantir alta disponibilidade do endpoint


- [ ] **Validação de Segurança:**
  - [ ] Implementar validação do `token` recebido no payload
  - [ ] (Opcional) Implementar validação de IP de origem, se aplicável
  - [ ] Proteger contra possíveis ataques (injeção, DoS)


- [ ] **Resposta Rápida:**
  - [ ] Garantir que o endpoint responda com `2xx` em menos de 2 segundos
  - [ ] Otimizar código para validação básica sem processamento pesado


- [ ] **Processamento Assíncrono:**
  - [ ] Implementar fila de mensagens (RabbitMQ, SQS, etc.)
  - [ ] Configurar workers para processamento posterior
  - [ ] Estabelecer mecanismo de retry interno


- [ ] **Tratamento de Erros:**
  - [ ] Capturar e logar exceções durante o processamento
  - [ ] Implementar política de retentativas internas para falhas transitórias
  - [ ] Alertar sobre erros críticos ou problemas persistentes


- [ ] **Idempotência:**
  - [ ] Implementar tabela/registro de eventos processados
  - [ ] Verificar duplicidade antes de executar ações com efeitos colaterais
  - [ ] Usar combinação de `code` + `sale_status_enum` + `date_approved` como chave


- [ ] **Mapeamento de Dados:**
  - [ ] Converter a estrutura do payload JSON para os modelos de dados internos
  - [ ] Lidar corretamente com campos opcionais/nulos
  - [ ] Validar formatos de dados (datas, números, enums)


- [ ] **Lógica de Negócios:**
  - [ ] Implementar regras específicas baseadas em `sale_status_enum`
  - [ ] Estabelecer fluxos para diferentes tipos de pagamento
  - [ ] Integrar com sistemas internos (CRM, ERP, etc.)


- [ ] **Logging:**
  - [ ] Registrar payload completo de cada webhook recebido
  - [ ] Logar timestamp, status de processamento e resultados
  - [ ] Implementar rastreabilidade (trace ID) entre sistemas


- [ ] **Monitoramento:**
  - [ ] Configurar alertas para falhas de processamento
  - [ ] Monitorar latência de resposta e processamento
  - [ ] Criar dashboard para volume de webhooks e taxas de sucesso/falha


- [ ] **Testes:**
  - [ ] Criar testes unitários para validação e processamento
  - [ ] Implementar testes de integração com payloads de exemplo
  - [ ] Simular cenários de falha e recuperação


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 13. Glossário de Termos Técnicos


> **Resumo:** Definições claras dos principais termos técnicos utilizados nesta documentação.


| Termo                     | Definição                                                                                                |
| :------------------------ | :------------------------------------------------------------------------------------------------------- |
| `Webhook`                 | Mecanismo de notificação onde um sistema (Perfect Pay) envia automaticamente dados para outro sistema (seu endpoint) via HTTP POST quando um evento específico ocorre. |
| `Endpoint Receptor`       | A URL no seu sistema configurada para receber as notificações (requisições HTTP POST) do webhook.        |
| `Payload`                 | O corpo (body) da requisição HTTP POST enviada pelo webhook, geralmente em formato JSON, contendo os dados do evento. |
| `Token de Validação`      | Uma string secreta (`token` no payload) usada para verificar se a requisição webhook é autêntica e vem da Perfect Pay. |
| `Idempotência`            | Propriedade que garante que processar o mesmo webhook múltiplas vezes terá o mesmo efeito que processá-lo uma única vez. Essencial para lidar com retentativas. |
| `Processamento Assíncrono`| Técnica onde a resposta rápida (`2xx`) é enviada imediatamente ao receber o webhook, e o processamento real dos dados é feito posteriormente (ex: em uma fila). |
| `Enum (Enumeração)`       | Campo que utiliza códigos numéricos (`small integer`, `integer`) para representar um conjunto finito de valores possíveis (ex: `sale_status_enum`). |
| `CRM`                     | Customer Relationship Management - Sistema de Gerenciamento de Relacionamento com o Cliente.             |
| `ERP`                     | Enterprise Resource Planning - Sistema Integrado de Gestão Empresarial.                                  |
| `PII`                     | Personally Identifiable Information - Informações Pessoalmente Identificáveis (ex: nome, email, CPF).    |
| `Boleto`                  | Método de pagamento brasileiro onde um documento bancário com código de barras é gerado para pagamento posterior. |
| `Chargeback`              | Processo onde o cliente contesta uma cobrança diretamente com o emissor do cartão, resultando em potencial estorno do valor. |
| `UTM Parameters`          | Parâmetros de URL (utm_source, utm_medium, etc.) usados para rastrear a origem do tráfego e eficácia de campanhas de marketing. |
| `Webhook Owner`           | O usuário da Perfect Pay que configurou o webhook e receberá as notificações em seu endpoint. |
| `Fila de Mensagens`       | Sistema intermediário (como RabbitMQ, Amazon SQS) usado para armazenar eventos do webhook para processamento posterior, garantindo que nenhum evento seja perdido. |


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---


## 14. Observações Finais sobre Formatação


> **Resumo:** Diretrizes de formatação para garantir a consistência e adequação do documento para sistemas RAG.


*   Use headings (`#`, `##`, `###`) para estruturar hierarquicamente o documento.
*   Use tabelas Markdown para apresentar dados estruturados (parâmetros, códigos enum).
*   Use blocos de código (```json ... ```) com indicação de linguagem para exemplos de payload JSON.
*   Mantenha linguagem clara, objetiva e tecnicamente precisa.
*   Formate nomes de campos (`token`, `sale_amount`) e valores de exemplo com backticks (`exemplo`).
*   **Crucial:** Inclua `(Ref: PerfectPay Webhooks, ID perfectpay_ntf_001)` no final de **CADA SEÇÃO PRINCIPAL (##)** e opcionalmente em subitens/chunks importantes (como cada Caso de Uso).
*   Mantenha os resumos de seção (`> **Resumo:** ...`) concisos (1-2 linhas) e informativos.
*   Use listas e bullets para informações sequenciais ou enumeradas (como no Checklist).
*   Evite abreviações não explicadas ou jargão não definido no Glossário.


*(Ref: PerfectPay Webhooks, ID perfectpay_webhook_001)*
---