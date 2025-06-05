# Taxonomia Fundamental de Parâmetros

---
version: 1.0  
last_updated: 2025-04-15  
changelog:  
  - 2025-04-15: Versão inicial (v1.0.0)  
 
---


## VISÃO GERAL

*   **Propósito:** Este documento serve como o dicionário centralizado e a fonte de verdade para todos os parâmetros utilizados no sistema de rastreamento hiper-enriquecido do AnalyticsGPT. Ele define a nomenclatura, significado, formato, prioridade e considerações de privacidade para garantir a consistência, completude e qualidade dos dados coletados.
*   **Principais Casos de Uso:**
    *   Referência para desenvolvedores ao construir objetos `dataLayer`.
    *   Guia para configurar Variáveis e Tags no Google Tag Manager (Client-Side e Server-Side).
    *   Base para debug e validação de implementações de rastreamento.
    *   Dicionário de dados para analistas interpretarem os datasets coletados.
    *   Definição do esquema de dados para integração com Data Warehouses ou CRMs.
*   **Como se Conecta:**
    *   É a base para a `taxonomia_eventos.md` (quais parâmetros pertencem a quais eventos).
    *   Informa as estratégias em `coleta_persistencia.md` (como e onde armazenar esses parâmetros).
    *   Define os identificadores usados em `redundancia_fallbacks.md`.
    *   Guia as verificações em `validacao_qa.md`.
    *   Destaca considerações abordadas em `seguranca_privacidade.md`.

## FLUXO DE UTILIZAÇÃO PELO AGENTE  

Este documento é consultado pelo AnalyticsGPT nas seguintes situações:  

1. **Geração de Código:** Quando precisa criar snippets para GTM/dataLayer  
2. **Validação de Implementação:** Para checar se eventos existentes estão completos  
3. **Resolução de Dúvidas:** Quando questionado sobre nomes/formato de parâmetros  
4. **Diagnóstico de Problemas:** Para identificar parâmetros faltantes em relatórios  

Padrão de priorização:  
- Parâmetros marcados como "Mandatório" devem SEMPRE estar presentes  
- Parâmetros "Alta/Média" priorizados conforme contexto da pergunta  
- Parâmetros "Baixa" só incluídos quando explicitamente solicitados  

## RESTRIÇÕES DE USO  

Parâmetros que NUNCA devem ser combinados:  
- `user_id` + `email_hash` em eventos enviados para o Meta Pixel  
- `ip_address` + `user_agent` em logs não anonimizados  

Contextos proibidos:  
- Parâmetros PII nunca devem ser armazenados no client-side sem hash  
- `click_text` não deve ser usado em eventos enviados para redes de ads  

## CONTEÚDO DETALHADO

### Introdução e Convenções

Esta seção cataloga os parâmetros recomendados, agrupados por sua função principal. As colunas das tabelas a seguir têm os seguintes significados:

*   **Parâmetro:** O nome técnico do parâmetro, seguindo a convenção `snake_case`. Este é o nome a ser usado no `dataLayer` e nas configurações.
*   **Descrição:** Explicação clara do que o parâmetro representa.
*   **Tipo de Dado:** O formato esperado do valor (e.g., String, Integer, Float, Boolean, Timestamp (ms), Array[Object], UUID).
*   **Aplicação/Contexto:** Onde ou quando este parâmetro é tipicamente usado (e.g., Todos os eventos, Eventos de e-commerce, Primeiro evento da sessão).
*   **Prioridade:** A importância relativa do parâmetro (Mandatório, Alta, Média, Baixa).
*   **Privacidade:** Classificação quanto à sensibilidade dos dados (Não PII, Sensível, PII). Requer atenção especial para conformidade.
*   **Notas/Considerações:** Detalhes adicionais, exemplos, origem (Client/Server), requisitos de formato específicos, ou links relevantes.

**IMPORTANTE:** As plataformas de analytics (Google, Meta, etc.) evoluem constantemente. Embora este documento vise a precisão, **sempre verifique a documentação oficial mais recente** das respectivas plataformas antes de finalizar implementações críticas.

### 1. Parâmetros Globais Essenciais

Parâmetros fundamentais que devem, idealmente, acompanhar *todos* os eventos enviados.

| Parâmetro         | Descrição                                      | Tipo de Dado    | Aplicação/Contexto | Prioridade | Privacidade | Notas/Considerações                                                                                                |
| :---------------- | :--------------------------------------------- | :-------------- | :----------------- | :--------- | :---------- | :----------------------------------------------------------------------------------------------------------------- |
| `event_id`        | Identificador único universal para este evento | UUID / String   | Todos os eventos   | Mandatório | Não PII     | Essencial para deduplicação (especialmente CAPI/Server-Side). Gerar no cliente. Formato: UUID v4 ou `timestamp_ms_random`. |
| `event_name`      | Nome padronizado do evento                     | String          | Todos os eventos   | Mandatório | Não PII     | Usar `snake_case`. Deve corresponder à `taxonomia_eventos.md`. Ex: `add_to_cart`.                                  |
| `event_timestamp` | Momento exato em que o evento ocorreu          | Timestamp (ms)  | Todos os eventos   | Mandatório | Não PII     | Unix timestamp em milissegundos (UTC). `Date.now()`. Crucial para ordenação e análise temporal.                     |
| `event_source`    | Origem da coleta do evento                     | String          | Todos os eventos   | Alta       | Não PII     | Valores: `web`, `app`, `server`, `offline`, `crm`. Ajuda a segmentar e depurar fontes de dados.                  |
| `user_id`         | ID único do usuário autenticado                | String          | Eventos pós-login  | Alta       | PII         | ID interno do sistema (CRM, DB). **Hashear (SHA-256)** antes de enviar a plataformas de terceiros se necessário.      |
| `session_id`      | ID único da sessão de navegação atual          | String          | Todos os eventos   | Alta       | Não PII     | Gerado no início da sessão. Pode ser `timestamp_inicio_ms_random`. Persiste via `sessionStorage` ou cookie.       |
| `ga_session_id`   | ID da sessão específico do GA4                 | String          | Todos os eventos   | Média      | Não PII     | Extraído do cookie `_ga` ou parâmetro `_ga_...`. Útil para join com dados do GA4.                                |
| `ga_session_number`| Número da sessão do usuário no GA4            | Integer         | Todos os eventos   | Média      | Não PII     | Extraído do cookie `_ga` ou parâmetro `_ga_...`. Indica se é a 1ª, 2ª, etc., sessão.                             |
| `page_location`   | URL completa da página onde o evento ocorreu   | String (URL)    | Eventos Web        | Mandatório | Sensível    | `window.location.href`. Incluir protocolo, domínio, path e query strings. Pode conter PII em parâmetros.         |
| `page_title`      | Título da página (`<title>`)                   | String          | Eventos Web        | Alta       | Não PII     | `document.title`. Útil para análise de conteúdo.                                                                 |
| `page_referrer`   | URL da página anterior que levou à atual       | String (URL)    | Eventos Web        | Alta       | Sensível    | `document.referrer`. Pode ser vazio ou "direct". Importante para análise de fluxo.                               |
| `language`        | Idioma preferencial do navegador/usuário       | String          | Todos os eventos   | Média      | Não PII     | Formato `IETF BCP 47` (e.g., `pt-BR`, `en-US`). `navigator.language`.                                             |
| `consent_state`   | Estado atual do consentimento do usuário       | String          | Todos os eventos   | Alta       | Não PII     | Valores: `granted_full`, `granted_partial`, `denied`, `pending`. Gerenciado pelo `Consent Manager`.                |

### 2. Parâmetros de Identidade (ID Resolution)

Identificadores usados para unificar a jornada do usuário entre sessões, dispositivos e plataformas.

| Parâmetro         | Descrição                                      | Tipo de Dado    | Persistência        | Prioridade | Privacidade | Notas/Considerações                                                                                                                               |
| :---------------- | :--------------------------------------------- | :-------------- | :------------------ | :--------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `user_id`         | ID primário do usuário (ver Globais)           | String          | Permanente (Servidor) | Alta       | PII         | **Hashear (SHA-256)** para plataformas externas. A fonte mais confiável.                                                                         |
| `client_id`       | ID do dispositivo/navegador (GA4)              | String          | ~2 anos (Cookie)    | Alta       | Não PII     | Principal fallback para `user_id`. Extraído do cookie `_ga`. Ex: `GA1.1.123456789.1678886400`.                                                     |
| `anonymous_id`    | ID temporário gerado se nenhum outro existe    | String          | Sessão (Storage)    | Média      | Não PII     | Fallback final. Pode ser igual ao `session_id` ou um UUID gerado na sessão. Útil para conectar eventos anônimos dentro de uma sessão.             |
| `email_hash`      | Hash SHA-256 do email do usuário               | String (SHA-256)| Vinculado à conta   | Média      | PII (Hashed)| **Não enviar email bruto**. Usar SHA-256 normalizado (lowercase, trim). Crucial para CAPI (parâmetro `em`).                                      |
| `phone_hash`      | Hash SHA-256 do telefone do usuário            | String (SHA-256)| Vinculado à conta   | Média      | PII (Hashed)| **Não enviar telefone bruto**. Normalizar (só dígitos) e usar SHA-256. Crucial para CAPI (parâmetro `ph`).                                   |
| `fbp`             | Facebook Browser ID (gerado pelo Pixel)        | String          | ~90 dias (Cookie)   | Média      | Não PII     | Gerado e gerenciado pelo script do Meta Pixel. Capturar do cookie `_fbp`. Usado para atribuição e CAPI.                                          |
| `fbc`             | Facebook Click ID (adicionado à URL)           | String          | ~28 dias (Cookie)   | Média      | Não PII     | Presente na URL após clique em anúncio do Facebook (`fbclid=...`). Capturar e persistir em cookie. Usado para atribuição e CAPI.                  |
| `device_id`       | ID único do dispositivo para Apps Móveis       | String          | Permanente (App)    | Alta (Apps)| Não PII     | IDFA (iOS, requer consentimento ATT), Advertising ID (Android).                                                                                   |
| `crm_id`          | ID do usuário no sistema de CRM                | String          | Permanente (Servidor) | Média      | PII         | Se diferente do `user_id` principal. Útil para integrações diretas com CRM. **Hashear** se necessário.                                            |

### 3. Parâmetros de Origem e Atribuição

Parâmetros que descrevem como o usuário chegou ao site/app. Essenciais para análise de canais e campanhas.

| Parâmetro            | Descrição                                       | Tipo de Dado | Armazenamento           | Prioridade | Privacidade | Notas/Considerações                                                                                                                            |
| :------------------- | :---------------------------------------------- | :----------- | :---------------------- | :--------- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `utm_source`         | Fonte de tráfego (e.g., google, facebook)       | String       | Sessão & First-touch    | Alta       | Não PII     | Capturado da URL (`?utm_source=...`). Persistir first-touch em `localStorage`.                                                               |
| `utm_medium`         | Meio de marketing (e.g., cpc, email, organic)   | String       | Sessão & First-touch    | Alta       | Não PII     | Capturado da URL (`?utm_medium=...`). Persistir first-touch.                                                                                |
| `utm_campaign`       | Nome da campanha específica                     | String       | Sessão & First-touch    | Alta       | Não PII     | Capturado da URL (`?utm_campaign=...`). Persistir first-touch.                                                                              |
| `utm_content`        | Identifica o criativo/link específico           | String       | Sessão & First-touch    | Média      | Não PII     | Capturado da URL (`?utm_content=...`). Útil para A/B testing de anúncios/links. Persistir first-touch.                                        |
| `utm_term`           | Palavra-chave de busca paga                     | String       | Sessão & First-touch    | Média      | Sensível    | Capturado da URL (`?utm_term=...`). Pode conter termos de busca. Persistir first-touch.                                                       |
| `utm_source_first`   | Primeira `utm_source` registrada para o usuário | String       | Permanente (Storage)    | Alta       | Não PII     | Armazenado em `localStorage` na primeira visita com UTMs. Essencial para atribuição first-touch.                                             |
| `utm_medium_first`   | Primeiro `utm_medium` registrado                | String       | Permanente (Storage)    | Alta       | Não PII     | Armazenado em `localStorage`.                                                                                                                |
| `utm_campaign_first` | Primeiro `utm_campaign` registrado              | String       | Permanente (Storage)    | Alta       | Não PII     | Armazenado em `localStorage`.                                                                                                                |
| `utm_content_first`  | Primeiro `utm_content` registrado               | String       | Permanente (Storage)    | Média      | Não PII     | Armazenado em `localStorage`.                                                                                                                |
| `utm_term_first`     | Primeiro `utm_term` registrado                  | String       | Permanente (Storage)    | Média      | Sensível    | Armazenado em `localStorage`.                                                                                                                |
| `gclid`              | Google Click ID                                 | String       | ~90 dias (Cookie/URL)   | Alta       | Não PII     | Adicionado por Google Ads. Capturar da URL e persistir. Crucial para atribuição Google Ads e conversões offline.                               |
| `fbclid`             | Facebook Click ID (ver Identidade)              | String       | ~28 dias (Cookie/URL)   | Alta       | Não PII     | Adicionado por Facebook Ads. Capturar da URL e persistir.                                                                                    |
| `msclkid`            | Microsoft Click ID                              | String       | ~90 dias (Cookie/URL)   | Média      | Não PII     | Adicionado por Microsoft Advertising. Capturar da URL e persistir.                                                                           |
| `dclid`              | Display Click ID (Google Marketing Platform)    | String       | ~90 dias (Cookie/URL)   | Média      | Não PII     | Usado para atribuição de campanhas de Display. Capturar da URL e persistir.                                                                    |
| `ttclid`             | TikTok Click ID                                 | String       | ~28 dias (Cookie/URL)   | Média      | Não PII     | Adicionado por TikTok Ads. Capturar da URL e persistir.                                                                                      |
| `sclid`              | Snapchat Click ID                               | String       | ~28 dias (Cookie/URL)   | Média      | Não PII     | Adicionado por Snapchat Ads. Capturar da URL e persistir.                                                                                    |
| `campaign_id`        | ID interno da campanha (se houver)              | String       | Permanente (Mapeamento) | Média      | Não PII     | Mapeado a partir de `utm_campaign` ou outras fontes. Útil para joins internos.                                                               |
| `referrer_domain`    | Domínio da URL de referência                    | String       | Sessão                  | Média      | Não PII     | Extraído do `page_referrer`. Ex: `google.com`, `facebook.com`.                                                                             |
| `traffic_source_type`| Categoria da fonte (calculado)                | String       | Sessão                  | Alta       | Não PII     | Classificação baseada em `utm_source`, `utm_medium`, `referrer_domain`. Ex: `paid_search`, `organic_social`, `direct`, `referral`, `email`. |
| `landing_page`       | Primeira URL da sessão atual                    | String (URL) | Sessão                  | Alta       | Sensível    | URL da primeira página visitada na sessão. Importante para análise de entrada.                                                              |
| `utm_full_string`    | String completa de parâmetros UTM da sessão     | String       | Sessão                  | Média      | Sensível    | Concatenação de todos os `utm_*` presentes na URL. Útil para depuração e preservação em redirects.                                            |

### 4. Parâmetros de Contexto Técnico

Informações sobre o ambiente técnico do usuário (dispositivo, navegador, etc.).

| Parâmetro           | Descrição                                    | Tipo de Dado | Prioridade | Privacidade | Notas/Considerações                                                                                                 |
| :------------------ | :------------------------------------------- | :----------- | :--------- | :---------- | :------------------------------------------------------------------------------------------------------------------ |
| `device_category`   | Categoria do dispositivo                     | String       | Alta       | Não PII     | Valores: `desktop`, `mobile`, `tablet`. Essencial para análise de usabilidade e performance.                       |
| `operating_system`  | Sistema Operacional                          | String       | Média      | Não PII     | Ex: `Windows`, `macOS`, `iOS`, `Android`, `Linux`. Parseado do User Agent.                                          |
| `os_version`        | Versão do Sistema Operacional                | String       | Baixa      | Não PII     | Ex: `10`, `11.4`, `15.1`. Parseado do User Agent.                                                                   |
| `browser`           | Navegador                                    | String       | Média      | Não PII     | Ex: `Chrome`, `Safari`, `Firefox`, `Edge`. Parseado do User Agent.                                                  |
| `browser_version`   | Versão do Navegador                          | String       | Baixa      | Não PII     | Ex: `98.0.4758.102`. Parseado do User Agent.                                                                        |
| `user_agent`        | String completa do User Agent do navegador   | String       | Baixa      | Não PII     | `navigator.userAgent`. Grande e complexa. Usar bibliotecas para parsear ou confiar nos parâmetros derivados acima. |
| `screen_resolution` | Resolução da tela do dispositivo             | String       | Média      | Não PII     | Formato `LarguraxAltura` (e.g., `1920x1080`). `window.screen.width` x `window.screen.height`.                      |
| `viewport_size`     | Tamanho da área visível do navegador (viewport)| String       | Média      | Não PII     | Formato `LarguraxAltura` (e.g., `1280x720`). `window.innerWidth` x `window.innerHeight`.                          |
| `screen_orientation`| Orientação da tela                           | String       | Média      | Não PII     | Valores: `landscape`, `portrait`. Relevante para mobile.                                                            |
| `connection_type`   | Tipo de conexão de rede estimada             | String       | Média      | Não PII     | Ex: `wifi`, `cellular`, `ethernet`. Pode vir de `navigator.connection.effectiveType` (e.g., `4g`, `3g`).          |
| `network_type`      | Tipo de rede detalhado (se disponível)       | String       | Baixa      | Não PII     | Ex: `wifi`, `4g`, `3g`, `2g`, `bluetooth`, `ethernet`. `navigator.connection.type`.                               |
| `page_load_time`    | Tempo de carregamento da página (cliente)    | Integer (ms) | Média      | Não PII     | Calculado via `PerformanceNavigationTiming API`. Diferença entre `loadEventEnd` e `startTime`.                      |
| `ip_address`        | Endereço IP do usuário                       | String       | Média      | PII         | **Coletar apenas no Server-Side**. **Anonimizar** (remover último octeto) antes de armazenar ou enviar a terceiros. |

### 5. Parâmetros de Interação e Comportamento

Descrevem ações específicas realizadas pelo usuário na interface.

| Parâmetro         | Descrição                                      | Tipo de Dado | Eventos Aplicáveis         | Prioridade | Privacidade | Notas/Considerações                                                                                              |
| :---------------- | :--------------------------------------------- | :----------- | :------------------------- | :--------- | :---------- | :--------------------------------------------------------------------------------------------------------------- |
| `click_id`        | ID único do clique específico                  | String       | `click`                    | Média      | Não PII     | Gerado no momento do clique. Útil para rastrear cliques individuais.                                             |
| `click_text`      | Texto visível do elemento clicado              | String       | `click`, `outbound_click`  | Alta       | Sensível    | Conteúdo de texto do `<a>`, `<button>`, etc. Pode conter PII se for input do usuário.                           |
| `click_url`       | URL de destino do link clicado (`href`)        | String (URL) | `click`                    | Alta       | Sensível    | Atributo `href` de tags `<a>`.                                                                                   |
| `click_element`   | Tipo de elemento HTML clicado                  | String       | `click`                    | Média      | Não PII     | Tag name em lowercase (e.g., `button`, `a`, `div`, `span`).                                                      |
| `click_classes`   | Classes CSS do elemento clicado                | String       | `click`                    | Baixa      | Não PII     | Lista de classes separadas por espaço.                                                                         |
| `click_region`    | Região da página onde ocorreu o clique         | String       | `click`, `outbound_click`  | Média      | Não PII     | Identificador da seção (e.g., `header`, `footer`, `product_card`, `sidebar`). Definido via atributos `data-*`. |
| `element_id`      | ID HTML do elemento interagido                 | String       | `click`, `form_submit`, etc. | Média      | Não PII     | Atributo `id` do elemento.                                                                                       |
| `element_path`    | Seletor CSS ou XPath do elemento interagido    | String       | `click`, `form_submit`, etc. | Baixa      | Não PII     | Útil para identificar elementos sem ID ou classes únicas. Pode ser longo.                                        |
| `scroll_depth`    | Profundidade máxima de rolagem na página       | Integer (%)  | `scroll`                   | Média      | Não PII     | Percentual da página rolada (e.g., 25, 50, 75, 90).                                                              |
| `time_on_page`    | Tempo gasto na página antes de sair/evento     | Integer (ms) | `page_exit`, `user_engagement`| Média      | Não PII     | Calculado entre `page_view` e o próximo evento/saída.                                                            |
| `engagement_time_msec`| Tempo de engajamento ativo (GA4)           | Integer (ms) | `user_engagement`          | Alta       | Não PII     | Tempo em que a página esteve em primeiro plano e ativa. Parâmetro padrão GA4.                                  |
| `video_title`     | Título do vídeo                                | String       | Eventos de vídeo           | Média      | Não PII     |                                                                                                                  |
| `video_provider`  | Plataforma do vídeo (e.g., YouTube, Vimeo)   | String       | Eventos de vídeo           | Média      | Não PII     |                                                                                                                  |
| `video_percent`   | Percentual do vídeo assistido                  | Integer (%)  | `video_progress`           | Média      | Não PII     | Pontos comuns: 10, 25, 50, 75, 90.                                                                               |
| `video_current_time`| Tempo atual de reprodução do vídeo           | Integer (s)  | Eventos de vídeo           | Média      | Não PII     | Tempo em segundos.                                                                                               |
| `video_duration`  | Duração total do vídeo                         | Integer (s)  | Eventos de vídeo           | Média      | Não PII     |                                                                                                                  |
| `form_id`         | ID HTML do formulário                          | String       | Eventos de formulário      | Alta       | Não PII     | Atributo `id` da tag `<form>`.                                                                                   |
| `form_name`       | Nome do formulário                             | String       | Eventos de formulário      | Média      | Não PII     | Atributo `name` da tag `<form>` ou `data-form-name`.                                                             |
| `form_step`       | Etapa atual em um formulário multi-etapas      | String/Int   | Eventos de formulário      | Média      | Não PII     | Útil para funis de formulário.                                                                                   |
| `form_field_name` | Nome do campo que causou erro/interação        | String       | `form_error`               | Média      | Sensível    | Pode identificar campos PII.                                                                                     |
| `outbound_link`   | URL do link externo clicado                    | String (URL) | `outbound_click`           | Alta       | Sensível    | Link que leva para fora do domínio atual.                                                                        |
| `file_name`       | Nome do arquivo baixado                        | String       | `file_download`            | Alta       | Sensível    | Nome do arquivo (e.g., `relatorio_vendas.pdf`). Pode conter PII.                                                 |
| `file_extension`  | Extensão do arquivo baixado                    | String       | `file_download`            | Alta       | Não PII     | Ex: `pdf`, `xlsx`, `docx`, `zip`.                                                                                |
| `search_term`     | Termo pesquisado na busca interna do site      | String       | `search`                   | Alta       | Sensível    | O que o usuário digitou na barra de busca. Pode conter PII.                                                      |
| `search_results_count`| Número de resultados retornados pela busca | Integer      | `search`                   | Média      | Não PII     |                                                                                                                  |
| `error_message`   | Mensagem de erro exibida ao usuário            | String       | `error`                    | Média      | Sensível    | Texto da mensagem de erro. Pode expor informações.                                                               |
| `error_type`      | Categoria do erro                              | String       | `error`                    | Média      | Não PII     | Ex: `validation`, `server`, `404`, `javascript`.                                                                 |
| `error_code`      | Código específico do erro (se houver)          | String/Int   | `error`                    | Baixa      | Não PII     |                                                                                                                  |

### 6. Parâmetros de E-commerce

Parâmetros específicos para rastreamento de interações em lojas virtuais, seguindo padrões como o Enhanced Ecommerce do GA4.

| Parâmetro           | Descrição                                      | Tipo de Dado    | Eventos Aplicáveis                 | Prioridade | Privacidade | Notas/Considerações                                                                                                                                   |
| :------------------ | :--------------------------------------------- | :-------------- | :--------------------------------- | :--------- | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `items`             | Array de produtos envolvidos no evento         | Array[Object]   | `view_item_list`, `view_item`, etc. | Mandatório | Sensível    | Contém objetos, cada um representando um item com seus próprios parâmetros (ver abaixo). Pode conter nomes/categorias sensíveis.                        |
| `item_id`           | ID/SKU único do produto (dentro de `items`)    | String          | Itens dentro do array `items`      | Mandatório | Não PII     | Identificador principal do produto.                                                                                                                   |
| `item_name`         | Nome do produto (dentro de `items`)            | String          | Itens dentro do array `items`      | Mandatório | Sensível    | Nome completo do produto.                                                                                                                             |
| `item_brand`        | Marca do produto (dentro de `items`)           | String          | Itens dentro do array `items`      | Média      | Não PII     |                                                                                                                                                       |
| `item_category`     | Categoria principal (dentro de `items`)        | String          | Itens dentro do array `items`      | Alta       | Sensível    | Ex: "Calçados". Usar hierarquia (`item_category`, `item_category2`, ... `item_category5`).                                                            |
| `item_variant`      | Variante do produto (e.g., Cor/Tamanho)        | String          | Itens dentro do array `items`      | Média      | Não PII     | Ex: "Preto/42".                                                                                                                                       |
| `price`             | Preço unitário do produto (dentro de `items`)  | Float           | Itens dentro do array `items`      | Mandatório | Não PII     | Usar ponto como separador decimal (e.g., `199.90`). Não incluir símbolo de moeda.                                                                     |
| `quantity`          | Quantidade do item (dentro de `items`)         | Integer         | Itens dentro do array `items`      | Mandatório | Não PII     | Quantidade adicionada, removida ou comprada.                                                                                                          |
| `currency`          | Código da moeda da transação                   | String          | Eventos com valor monetário        | Mandatório | Não PII     | Código ISO 4217 (e.g., `BRL`, `USD`, `EUR`).                                                                                                          |
| `value`             | Valor monetário total do evento                | Float           | `purchase`, `add_to_cart`, etc.    | Mandatório | Não PII     | Valor total (itens * quantidade). Para `purchase`, é o valor total da transação (subtotal + frete + imposto - desconto). Usar ponto decimal.        |
| `coupon`            | Código do cupom aplicado                       | String          | `begin_checkout`, `purchase`       | Média      | Não PII     |                                                                                                                                                       |
| `discount`          | Valor total do desconto aplicado               | Float           | `purchase`                         | Média      | Não PII     | Valor absoluto do desconto. Usar ponto decimal.                                                                                                       |
| `shipping`          | Custo do frete                                 | Float           | `add_shipping_info`, `purchase`    | Alta       | Não PII     | Usar ponto decimal.                                                                                                                                   |
| `tax`               | Valor total dos impostos                       | Float           | `purchase`                         | Alta       | Não PII     | Usar ponto decimal.                                                                                                                                   |
| `transaction_id`    | ID único da transação/pedido                   | String          | `purchase`                         | Mandatório | Não PII     | ID do pedido no sistema da loja. Essencial para join com dados de backend.                                                                            |
| `affiliation`       | Loja ou filial onde a compra ocorreu           | String          | `purchase`                         | Baixa      | Não PII     | Útil para marketplaces ou redes de lojas. Ex: "Loja Online", "App iOS", "Loja Física SP".                                                              |
| `payment_type`      | Método de pagamento usado                      | String          | `add_payment_info`, `purchase`     | Média      | Não PII     | Ex: `credit_card`, `boleto`, `pix`, `paypal`.                                                                                                         |
| `shipping_tier`     | Modalidade de envio escolhida                  | String          | `add_shipping_info`, `purchase`    | Média      | Não PII     | Ex: `standard`, `express`, `next_day`.                                                                                                                |
| `item_list_name`    | Nome da lista onde o item foi visto/clicado    | String          | `view_item_list`, `select_item`    | Alta       | Não PII     | Ex: "Resultados da Busca", "Produtos Relacionados", "Categoria X".                                                                                    |
| `item_list_id`      | ID da lista onde o item foi visto/clicado      | String          | `view_item_list`, `select_item`    | Média      | Não PII     | ID interno da lista, se houver.                                                                                                                       |
| `index`             | Posição do item na lista (dentro de `items`)   | Integer         | Itens em `view_item_list`, `select_item` | Alta   | Não PII     | Posição baseada em 1 (primeiro item é 1).                                                                                                             |
| `creative_name`     | Nome do criativo interno (banner, etc.)        | String          | `view_promotion`, `select_promotion` | Média  | Não PII     | Nome do banner ou promoção visualizada.                                                                                                               |
| `creative_slot`     | Posição/Slot do criativo                       | String          | `view_promotion`, `select_promotion` | Média  | Não PII     | Identificador da posição onde o criativo apareceu (e.g., `home_banner_1`, `sidebar_promo`).                                                           |
| `promotion_id`      | ID da promoção interna                         | String          | `view_promotion`, `select_promotion` | Média  | Não PII     | ID da promoção ou cupom visualizado/selecionado.                                                                                                      |
| `promotion_name`    | Nome da promoção interna                       | String          | `view_promotion`, `select_promotion` | Média  | Não PII     | Nome da promoção visualizada/selecionada.                                                                                                             |

### 7. Parâmetros para Verticais Específicas

#### 7.1 B2B/SaaS
Parâmetros específicos para negócios B2B, SaaS e ambientes corporativos.

| Parâmetro           | Descrição                                      | Tipo de Dado    | Eventos Aplicáveis                 | Prioridade | Privacidade | Notas/Considerações                                                                                                                                   |
| :------------------ | :--------------------------------------------- | :-------------- | :--------------------------------- | :--------- | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `account_id`        | ID da conta corporativa                        | String          | Todos os eventos B2B/SaaS          | Alta       | PII         | Identificador da empresa/organização. **Hashear** se enviado para plataformas externas.                                                               |
| `account_name`      | Nome da empresa/organização                    | String          | Eventos relevantes em B2B          | Média      | PII         | Nome da empresa cliente. **Evitar** enviar para plataformas externas sem hash.                                                                        |
| `account_type`      | Tipo/categoria da conta                        | String          | Eventos relevantes em B2B          | Média      | Não PII     | Ex: `enterprise`, `smb`, `startup`, `agency`.                                                                                                         |
| `mrr_value`         | Valor de receita recorrente mensal             | Float           | `subscription_started`, `purchase` | Alta       | Não PII     | Valor da assinatura mensal. Crucial para análise de revenue em SaaS.                                                                                  |
| `subscription_plan` | Plano de assinatura                            | String          | `subscription_started`             | Alta       | Não PII     | Ex: `basic`, `pro`, `enterprise`.                                                                                                                     |
| `subscription_term` | Duração do contrato de assinatura              | String/Integer  | `subscription_started`             | Média      | Não PII     | Ex: `monthly`, `annual`, `biennial` ou duração em meses.                                                                                              |
| `lead_score`        | Pontuação do lead no sistema                   | Integer         | Eventos de lead nurturing          | Média      | Não PII     | Score numérico. Útil para análise de qualidade de leads.                                                                                              |
| `qualified_state`   | Estado de qualificação do lead                 | String          | Eventos de lead nurturing          | Alta       | Não PII     | Ex: `MQL`, `SQL`, `SAL`. Estados do funil de vendas.                                                                                                  |
| `industry`          | Indústria/setor da empresa-cliente             | String          | Eventos relevantes em B2B          | Média      | Não PII     | Categorização do setor. Ex: `technology`, `healthcare`, `financial_services`.                                                                         |
| `company_size`      | Tamanho da empresa por funcionários            | String          | Eventos relevantes em B2B          | Média      | Não PII     | Categorias como `1-10`, `11-50`, `51-200`, `201-500`, `500+`.                                                                                         |
| `feature_used`      | Recurso/funcionalidade utilizada               | String          | Eventos de uso de produto          | Alta       | Não PII     | Nome do recurso específico usado. Crucial para análise de engajamento em SaaS.                                                                        |
| `user_role`         | Função/cargo do usuário                        | String          | Eventos em plataformas B2B         | Média      | Sensível    | Ex: `admin`, `manager`, `viewer`. Evitar cargos específicos que possam identificar.                                                                   |

#### 7.2 Conteúdo e Mídia
Parâmetros para sites de notícias, blogs, streaming de conteúdo e mídia.

| Parâmetro           | Descrição                                      | Tipo de Dado    | Eventos Aplicáveis                 | Prioridade | Privacidade | Notas/Considerações                                                                                                                                   |
| :------------------ | :--------------------------------------------- | :-------------- | :--------------------------------- | :--------- | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content_type`      | Tipo de conteúdo consumido                     | String          | `view_item`, `content_view`        | Alta       | Não PII     | Ex: `article`, `video`, `podcast`, `gallery`, `infographic`.                                                                                          |
| `content_id`        | ID único do conteúdo                           | String          | `view_item`, `content_view`        | Alta       | Não PII     | Identificador do conteúdo no sistema de CMS.                                                                                                          |
| `content_title`     | Título do conteúdo                             | String          | `view_item`, `content_view`        | Alta       | Sensível    | Título do artigo, vídeo, etc.                                                                                                                         |
| `content_category`  | Categoria principal do conteúdo                | String          | `view_item`, `content_view`        | Alta       | Não PII     | Ex: `politics`, `technology`, `entertainment`, `sports`.                                                                                              |
| `content_tags`      | Tags/tópicos do conteúdo                       | Array[String]   | `view_item`, `content_view`        | Média      | Não PII     | Array de tags relacionadas ao conteúdo.                                                                                                               |
| `author_id`         | ID do autor do conteúdo                        | String          | `view_item`, `content_view`        | Média      | Não PII     | Identificador do autor no sistema.                                                                                                                    |
| `author_name`       | Nome do autor/criador                          | String          | `view_item`, `content_view`        | Média      | Não PII     | Nome do autor/jornalista/criador do conteúdo.                                                                                                         |
| `publish_date`      | Data de publicação                             | Timestamp/String| `view_item`, `content_view`        | Média      | Não PII     | Data em que o conteúdo foi publicado. Formato ISO 8601.                                                                                               |
| `content_length`    | Duração ou tamanho do conteúdo                 | Integer         | `view_item`, `content_view`        | Média      | Não PII     | Em segundos para vídeo/áudio, número de palavras para texto, ou número de imagens para galerias.                                                       |
| `subscription_type` | Tipo de assinatura do usuário                  | String          | Eventos em sites de conteúdo       | Alta       | Não PII     | Ex: `free`, `premium`, `metered`.                                                                                                                     |
| `content_group`     | Agrupamento editorial do conteúdo              | String          | `view_item`, `content_view`        | Média      | Não PII     | Ex: `editorial`, `sponsored`, `user_generated`.                                                                                                       |
| `word_count`        | Quantidade de palavras no artigo               | Integer         | `view_item`, `content_view`        | Baixa      | Não PII     | Útil para análise de engajamento vs. tamanho do conteúdo.                                                                                            |
| `page_number`       | Número da página em conteúdo paginado          | Integer         | `page_view` em conteúdo paginado   | Média      | Não PII     | Em sites de conteúdo com paginação de artigos.                                                                                                        |

### 8. Parâmetros de Experimentação e Personalização

Parâmetros relacionados a testes A/B, personalização e segmentação de usuários.

| Parâmetro           | Descrição                                      | Tipo de Dado    | Eventos Aplicáveis                 | Prioridade | Privacidade | Notas/Considerações                                                                                                                                   |
| :------------------ | :--------------------------------------------- | :-------------- | :--------------------------------- | :--------- | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `experiment_id`     | ID do experimento A/B                          | String          | Eventos com exposição a experimentos| Alta       | Não PII     | Identificador único do teste/experimento.                                                                                                              |
| `experiment_name`   | Nome descritivo do experimento                 | String          | Eventos com exposição a experimentos| Média      | Não PII     | Nome descritivo do experimento. Ex: "Homepage Hero Banner Test".                                                                                       |
| `experiment_variant`| Variante/grupo de teste                        | String          | Eventos com exposição a experimentos| Alta       | Não PII     | Ex: `control`, `variant_a`, `variant_b`. Também pode ser: `0`/`1`, `A`/`B`.                                                                            |
| `personalization_id`| ID da regra de personalização aplicada         | String          | Eventos com conteúdo personalizado | Média      | Não PII     | Identificador da regra que levou à experiência personalizada.                                                                                          |
| `user_segment`      | Segmento do usuário para personalização        | String          | Todos os eventos                   | Média      | Sensível    | Ex: `new_visitor`, `returning_customer`, `high_value`. Pode conter informações de segmentação demográfica.                                             |
| `optimizely_experiment_id` | ID do experimento no Optimizely         | String          | Eventos com exposição a experimentos| Baixa      | Não PII     | Para integrações com a plataforma Optimizely.                                                                                                          |
| `abtest_group`      | Grupo de experimento (valor legado)            | String          | Eventos com exposição a experimentos| Baixa      | Não PII     | Nome simplificado para ferramentas que não suportam a estrutura experiment_id/variant.                                                                 |

### 9. Parâmetros de Consentimento e Privacidade

Parâmetros relacionados à gestão do consentimento do usuário, cruciais para conformidade.

| Parâmetro           | Descrição                                      | Tipo de Dado    | Aplicação/Contexto | Prioridade | Privacidade | Notas/Considerações                                                                                                                               |
| :------------------ | :--------------------------------------------- | :-------------- | :----------------- | :--------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `consent_state`     | Estado geral do consentimento (ver Globais)    | String          | Todos os eventos   | Alta       | Não PII     | `granted_full`, `granted_partial`, `denied`, `pending`.                                                                                           |
| `consent_analytics` | Consentimento específico para analytics        | Boolean         | Todos os eventos   | Alta       | Não PII     | `true` se o usuário consentiu com cookies/rastreamento de analytics.                                                                              |
| `consent_marketing` | Consentimento específico para marketing/ads    | Boolean         | Todos os eventos   | Alta       | Não PII     | `true` se o usuário consentiu com cookies/rastreamento para fins publicitários.                                                                   |
| `ad_user_data`      | Consentimento para uso de dados do usuário p/ Ads | String        | Todos os eventos   | Alta       | Não PII     | Parâmetro do Google Consent Mode v2. Valores: `granted`, `denied`.                                                                                |
| `ad_personalization`| Consentimento para personalização de Ads       | String          | Todos os eventos   | Alta       | Não PII     | Parâmetro do Google Consent Mode v2. Valores: `granted`, `denied`.                                                                                |
| `consent_update_source`| Origem da atualização do consentimento      | String          | Evento `consent_update` | Média    | Não PII     | Ex: `cookie_banner`, `privacy_center`, `default`.                                                                                                 |
| `data_processing_region` | Região de processamento de dados          | String          | Todos os eventos   | Média      | Não PII     | Relevante para GDPR/regionalização. Ex: `eu`, `us`, `global`.                                                                                     |
| `gdpr_applies`      | Indica se GDPR é aplicável ao usuário          | Boolean         | Todos os eventos   | Alta       | Não PII     | Baseado na localização do usuário. Importante para fluxos de consentimento.                                                                       |
| `ccpa_applies`      | Indica se CCPA é aplicável ao usuário          | Boolean         | Todos os eventos   | Alta       | Não PII     | Baseado na localização (Califórnia). Importante para conformidade.                                                                                |
| `consent_method`    | Como o consentimento foi obtido                | String          | Evento `consent_update` | Média    | Não PII     | Ex: `explicit`, `implied`, `inherited`. Útil para auditoria.                                                                                     |
| `consent_timestamp` | Momento em que o consentimento foi dado        | Timestamp (ms)  | Evento `consent_update` | Média    | Não PII     | Importante para registro de audit trail do consentimento.                                                                                         |

### 10. Parâmetros Específicos de Server-Side

Parâmetros relevantes principalmente no contexto de GTM Server-Side ou envio direto para APIs.

| Parâmetro           | Descrição                                      | Tipo de Dado    | Aplicação/Contexto | Prioridade | Privacidade | Notas/Considerações                                                                                                                               |
| :------------------ | :--------------------------------------------- | :-------------- | :----------------- | :--------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ip_override`       | Endereço IP do cliente original                | String          | Server-Side        | Alta       | PII         | Necessário para geolocalização correta no servidor. **Anonimizar** antes de usar/enviar a terceiros. Capturado dos headers HTTP (`X-Forwarded-For`). |
| `user_agent_override`| User Agent string do cliente original          | String          | Server-Side        | Alta       | Não PII     | Necessário para detecção correta de dispositivo/browser no servidor. Capturado do header `User-Agent`.                                              |
| `server_timestamp_offset`| Diferença de tempo entre cliente e servidor| Integer (ms)  | Server-Side        | Baixa      | Não PII     | Pode ser usado para ajustar timestamps se houver grande latência ou dessincronização.                                                              |
| `http_request_method`| Método HTTP da requisição original           | String          | Server-Side        | Baixa      | Não PII     | Ex: `POST`, `GET`. Útil para depuração de endpoints.                                                                                              |
| `http_request_url`  | URL completa da requisição ao servidor         | String (URL)    | Server-Side        | Baixa      | Sensível    | URL do endpoint que recebeu o evento.                                                                                                             |
| `x_forwarded_for`   | Header original de IP encaminhado              | String          | Server-Side        | Média      | PII         | Header HTTP completo. **Não armazenar** sem anonimização.                                                                                          |
| `data_source`       | Origem dos dados no Server-Side                | String          | Server-Side        | Média      | Não PII     | Ex: `web`, `app`, `crm_import`, `webhook`. Identifica a fonte de dados no servidor.                                                               |
| `server_processing_latency`| Tempo de processamento no servidor      | Integer (ms)    | Server-Side        | Baixa      | Não PII     | Métrica de performance do servidor.                                                                                                               |
| `client_server_timestamp_delta`| Diferença entre timestamp cliente e servidor | Integer (ms) | Server-Side | Baixa | Não PII    | Útil para identificar problemas de sincronização de relógio.                                                                                     |

### Melhores Práticas de Implementação

1. **Consistência de Valores:**
   - Use os mesmos formatos e convenções em todas as plataformas
   - Padronize casing (minúsculas para parâmetros, valores consistentes)
   - Normalize valores como emails (lowercase) antes de hashear

2. **Tratamento de Valores Nulos:**
   - Evite enviar parâmetros com valores vazios, nulos ou undefined
   - Para arrays vazios, é preferível omitir o parâmetro que enviar `[]`
   - Use valores padrão sensatos quando apropriado (ex: `0` para contadores)

3. **Validação e QA:**
   - Verifique cada implementação com GTM Preview para garantir:
     - Formato correto dos parâmetros
     - Presença de todos os parâmetros obrigatórios
     - Valores dentro dos limites esperados (tamanhos, formatos)
   - Configure alertas para eventos sem parâmetros obrigatórios

4. **Evolução do Esquema:**
   - Documente todas as alterações neste esquema de parâmetros
   - Mantenha um controle de versões com datas de alteração
   - Atualize as implementações quando este esquema for atualizado
   - Defina um processo claro para adicionar novos parâmetros

5. **Considerações de Privacidade:**
   - Aplique hashing (SHA-256) para dados PII antes de enviar para plataformas externas
   - Aplique pseudonimização para endereços IP (removendo último octeto)
   - Respeite as preferências de consentimento ao enviar dados

### Limitações e Considerações Técnicas

- **Tamanho Máximo:** GA4 limita eventos a 25 parâmetros personalizados, Meta tem limites similares
- **Comprimento de Strings:** Mantenha parâmetros abaixo de 100 caracteres quando possível
- **Arrays:** GA4 suporta até 200 itens no array `items` (produtos)
- **Performance:** Grandes objetos dataLayer (>50KB) podem impactar tempo de carregamento
- **Timing:** Alguns parâmetros (como `time_on_page`) só podem ser calculados em determinados momentos
- **Sanitização:** Strings longas podem ser truncadas por plataformas; certifique-se de que informações críticas estejam no início
- **Compatibilidade:** Nem todas as plataformas suportam todos os tipos de dados; por exemplo, alguns sistemas não processam arrays aninhados corretamente
- **Rate Limiting:** APIs de servidor podem ter limites de requisições; implemente estratégias de retry e batch quando necessário
- **Ordem de Eventos:** Alguns parâmetros dependem do sequenciamento correto de eventos (ex: `page_view` antes de `user_engagement`)

### Exemplo de Implementação

O exemplo abaixo mostra um objeto dataLayer hiper-enriquecido para um evento de compra:

```javascript
// EXEMPLO DE OBJETO DATALAYER HIPER-ENRIQUECIDO - PURCHASE
window.dataLayer.push({
  event: "purchase",
  event_id: "evt_1674829465_8f72be3a",
  event_timestamp: 1674829465000,
  event_source: "web",
  user_id: "sha256_hash_do_id_123456",
  client_id: "GA1.1.1234567890.1234567890",
  session_id: "1674829160_5fc3b7",
  page_location: "https://loja.exemplo.com.br/checkout/confirmation",
  page_title: "Confirmação de Pedido - #12345 | Loja Exemplo",
  page_referrer: "https://loja.exemplo.com.br/checkout/payment",
  consent_state: "granted_full",
  
  // Parâmetros de identidade adicionais
  email_hash: "598a02d9a4...", // SHA-256 do email
  fbp: "fb.1.1674729160077.1234567890",
  fbc: "fb.1.1674729160077.AbCdEfGhIjKlMnOp",
  
  // Parâmetros de atribuição
  utm_source: "google",
  utm_medium: "cpc",
  utm_campaign: "black_friday_2023",
  utm_content: "banner_01",
  utm_term: "tênis running",
  utm_source_first: "instagram",
  utm_medium_first: "social",
  utm_campaign_first: "lancamento_colecao_verao",
  gclid: "EAIaIQobChMI123456789",
  
  // Parâmetros técnicos
  device_category: "mobile",
  browser: "Chrome",
  operating_system: "Android",
  screen_resolution: "1080x1920",
  viewport_size: "412x892",
  
  // Parâmetros de e-commerce
  ecommerce: {
    transaction_id: "ORD-12345",
    value: 389.80,
    tax: 35.80,
    shipping: 15.00,
    currency: "BRL",
    coupon: "BLACKFRIDAY20",
    discount: 77.96,
    shipping_tier: "express",
    payment_type: "credit_card",
    affiliation: "Loja Online",
    
    items: [
      {
        item_id: "SKU123456",
        item_name: "Tênis Running Performance Max",
        item_brand: "RunTech",
        item_category: "Calçados",
        item_category2: "Esportivos",
        item_category3: "Running",
        item_variant: "Preto/42",
        price: 229.90,
        quantity: 1,
        discount: 45.98,
        coupon: "BLACKFRIDAY20",
        index: 1,
        item_list_name: "Resultados de busca",
        item_list_id: "search_results"
      },
      {
        item_id: "SKU789012",
        item_name: "Meia Esportiva Cushion Pro",
        item_brand: "RunTech",
        item_category: "Acessórios",
        item_category2: "Meias",
        item_variant: "Branco/G",
        price: 29.90,
        quantity: 2,
        discount: 11.96,
        coupon: "BLACKFRIDAY20",
        index: 2,
        item_list_name: "Resultados de busca",
        item_list_id: "search_results"
      }
    ]
  },
  
  // Experimentação e personalização
  experiment_id: "exp_homepage_hero_20231101",
  experiment_variant: "variant_a",
  user_segment: "returning_customer"
});
```
## MATRIZ DE COMPATIBILIDADE  

| Parâmetro          | GA4  | Meta Pixel | CAPI | Adobe Analytics | Mixpanel |  
|--------------------|------|------------|------|-----------------|----------|  
| `user_id`          | ✅   | ❌         | ✅*  | ✅              | ✅       |  
| `email_hash`       | ❌   | ❌         | ✅   | ❌              | ✅       |  
| `items[]`          | ✅   | ✅         | ✅   | ✅              | ✅       |  
| ...                | ...  | ...        | ...  | ...             | ...      |  

> *Requer configuração especial no Meta Events Manager*

## DIAGNÓSTICO DE PROBLEMAS COMUNS  

**Sintoma: Parâmetro não aparece nos relatórios**  
- [ ] Verificar se o nome está exatamente como na taxonomia  
- [ ] Checar se o parâmetro não está em sub-objetos (e.g., `ecommerce.items`)  
- [ ] Validar limites de caracteres/tamanho da plataforma  

**Sintoma: Valores truncados ou inconsistentes**  
- [ ] Verificar formato (string vs number)  
- [ ] Checar caracteres especiais não permitidos  
- [ ] Validar encoding (UTF-8 obrigatório)  


## REFERÊNCIAS CRUZADAS

*   **Internas:**
    *   `taxonomia_eventos.md`: Define quais parâmetros são esperados para cada `event_name`.
    *   `coleta_persistencia.md`: Detalha como e onde estes parâmetros devem ser armazenados (cookies, localStorage, etc.).
    *   `redundancia_fallbacks.md`: Explica como usar os parâmetros de identidade em cascata.
    *   `seguranca_privacidade.md`: Aborda o tratamento de parâmetros PII e sensíveis, e a gestão de consentimento.
    *   `validacao_qa.md`: Metodologias para validar a implementação correta destes parâmetros.
    *   `integracao_plataformas.md`: Como mapear estes parâmetros para diferentes plataformas (GA4, Meta, etc.).

*   **Externas:**
    *   [Documentação de Parâmetros de Eventos Recomendados GA4](https://support.google.com/analytics/answer/9267735)
    *   [Documentação de Parâmetros Padrão do Meta Pixel](https://developers.facebook.com/docs/meta-pixel/reference#standard-events)
    *   [Documentação de Parâmetros da API de Conversões do Meta (User Data & Custom Data)](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters)
    *   [Especificação do dataLayer do Google Tag Manager](https://developers.google.com/tag-manager/devguide)
    *   [Guia de Implementação de Enhanced E-commerce](https://developers.google.com/analytics/devguides/collection/ua/gtm/enhanced-ecommerce)
    *   [Guia de Limitações Técnicas do GA4](https://support.google.com/analytics/answer/9267744)
    *   [Melhores Práticas para Naming Conventions do Mixpanel](https://help.mixpanel.com/hc/en-us/articles/115004708186-Naming-Conventions)