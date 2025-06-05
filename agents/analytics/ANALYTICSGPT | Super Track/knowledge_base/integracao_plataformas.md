# INTEGRAÇÃO ENTRE PLATAFORMAS

---
version: 1.0  
status: Ativo  
focus: Sincronização e consistência entre sistemas de analytics  
last_updated: 2025-04-15  
knowledge_layer: 2  
criticality: HIGH  
compatibility: ["GA4", "Meta Pixel", "GTM", "CAPI", "Server-Side Tagging"]  
---

## VISÃO GERAL

### Propósito do Componente
Este documento estabelece as **arquiteturas, padrões e métodos** para integrar diferentes plataformas de analytics, garantindo:
- Consistência de dados entre sistemas de rastreamento
- Mapeamento correto de parâmetros entre plataformas
- Implementação eficiente de rastreamento server-side
- Maximização de precisão em atribuição cross-platform
- Resiliência de dados em diferentes ambientes

### Principais Casos de Uso
1. **Sincronização de Eventos**: Garantir que dados sejam consistentes entre GA4, Meta Pixel e outros sistemas
2. **Server-Side Tracking**: Implementação de coleta server-side para superar bloqueadores e melhorar precisão
3. **Enriquecimento de Dados**: Complementar eventos client-side com dados disponíveis apenas no servidor
4. **Resiliência de Rastreamento**: Lidar com perda de conexão e falhas de serviço
5. **Conformidade com Privacidade**: Implementar tracking eficiente respeitando consentimento do usuário

### Conexão com Outros Componentes
- **Depende de**: `taxonomia_eventos.md` (definições padrão de eventos/parâmetros)
- **Suporta**: `validacao_qa.md` (métodos para validar integrações)
- **Complementa**: `seguranca_privacidade.md` (implementação segura respeitando normas)
- **Informa**: `implementacao_eventos.md` (métodos práticos de implementação)

## CONTEÚDO DETALHADO

### 1. MAPEAMENTO ENTRE PLATAFORMAS

#### 1.1 Matriz de Correlação de Parâmetros

| Parâmetro Universal | GA4 | Meta Pixel | Meta CAPI | GTM | CRM |
|---------------------|-----|------------|-----------|-----|-----|
| **ID do Evento** | `client_event_id` | `event_id` | `event_id` | `event.id` | `external_event_id` |
| **ID do Usuário** | `user_id` | - | `external_id` | `userId` | `id` |
| **ID do Cliente** | `client_id` | - | - | `clientId` | `analytics_id` |
| **ID da Transação** | `transaction_id` | - | `order_id` | `id` | `order_number` |
| **URL da Página** | `page_location` | `event_source_url` | `event_source_url` | `page.url` | `page_url` |
| **Email** | - | - | `em` (hashed) | - | `email` |
| **Telefone** | - | - | `ph` (hashed) | - | `phone` |
| **Valor** | `value` | `value` | `value` | - | `total` |
| **Produtos** | `items` | `content_ids`+`contents` | `contents` | `products` | `line_items` |
| **Moeda** | `currency` | `currency` | `currency` | - | `currency_code` |
| **Timestamp** | `timestamp` | - | `event_time` | `timestamp` | `created_at` |

#### 1.2 Mapeamento de Nomes de Eventos

| Evento Universal | GA4 | Meta Pixel | Meta CAPI |
|------------------|-----|------------|-----------|
| **Visualização de Página** | `page_view` | `PageView` | `PageView` |
| **Visualização de Item** | `view_item` | `ViewContent` | `ViewContent` |
| **Adicionar ao Carrinho** | `add_to_cart` | `AddToCart` | `AddToCart` |
| **Iniciar Checkout** | `begin_checkout` | `InitiateCheckout` | `InitiateCheckout` |
| **Adicionar Dados Pagamento** | `add_payment_info` | `AddPaymentInfo` | `AddPaymentInfo` |
| **Compra** | `purchase` | `Purchase` | `Purchase` |
| **Cadastro** | `sign_up` | `CompleteRegistration` | `CompleteRegistration` |
| **Lead** | `generate_lead` | `Lead` | `Lead` |
| **Pesquisa** | `search` | `Search` | `Search` |

### 2. ARQUITETURAS DE INTEGRAÇÃO

#### 2.1 Client-Side + Server-Side Híbrido

```
┌──────────────┐       ┌─────────────────┐       ┌──────────────┐
│  NAVEGADOR   │──────▶│  TAG MANAGER    │──────▶│ ANALYTICS    │
│  DO USUÁRIO  │       │  CLIENT-SIDE    │       │ CLIENT-SIDE  │
└──────┬───────┘       └─────────────────┘       └──────────────┘
       │                                                 
       │               ┌─────────────────┐       ┌──────────────┐
       └──────────────▶│  TAG MANAGER    │──────▶│ ANALYTICS    │
                       │  SERVER-SIDE    │       │ SERVER-SIDE  │
                       └─────────────────┘       └──────────────┘
```

**Principais características:**
- Coleta paralela client/server para máxima disponibilidade
- Deduplicação baseada em `event_id` nas plataformas de destino
- Enriquecimento server-side com dados não disponíveis no cliente
- Resiliência contra bloqueadores de rastreamento

#### 2.2 Servidor como Fonte Primária

```
┌──────────────┐       ┌─────────────────┐       ┌──────────────┐
│  NAVEGADOR   │──────▶│  ENDPOINT DA    │──────▶│ TAG MANAGER  │
│  DO USUÁRIO  │       │  APLICAÇÃO      │       │ SERVER-SIDE  │
└──────────────┘       └─────────────────┘       └──────┬───────┘
                                                        │
                       ┌─────────────────┐              │
                       │  ANALYTICS      │◀──────┬──────┘
                       │  DESTINATIONS   │       │ 
                       └─────────────────┘       │
                                                 │
                       ┌─────────────────┐       │
                       │  CRM / DATA     │◀──────┘
                       │  WAREHOUSE      │        
                       └─────────────────┘        
```

**Principais características:**
- Controle total sobre dados enviados (sem dependência do navegador)
- Enriquecimento nativo com dados do backend
- Alta precisão e disponibilidade
- Complexidade técnica maior na implementação
- Necessidade de proxy para preservar contexto do cliente

### 3. CLIENT-TO-SERVER (C2S) IMPLEMENTATION

#### 3.1 Implementação Client-Side para Meta CAPI

```javascript
/**
 * Configura o rastreamento Client-to-Server para Meta CAPI
 * Intercepta eventos do dataLayer para envio server-side
 */
function setupMetaServerTracking() {
  // Interceptar eventos do dataLayer
  window.dataLayer = window.dataLayer || [];
  const originalPush = window.dataLayer.push;
  
  window.dataLayer.push = function(event) {
    // Chamar implementação original
    originalPush.apply(this, arguments);
    
    // Processar somente eventos de conversão relevantes
    if (isConversionEvent(event)) {
      // Converter para formato CAPI
      const capiPayload = formatEventForCAPI(event);
      
      // Enviar para endpoint interno
      sendToServerEndpoint('/api/conversions/meta', capiPayload);
    }
  };
}

/**
 * Verifica se um evento deve ser enviado para CAPI
 * @param {Object} event - Evento do dataLayer
 * @returns {Boolean} 
 */
function isConversionEvent(event) {
  // Lista de eventos que devem ser enviados para CAPI
  const conversionEvents = [
    'purchase', 'add_to_cart', 'begin_checkout', 
    'view_item', 'generate_lead', 'sign_up'
  ];
  
  return event && 
         event.event && 
         conversionEvents.includes(event.event);
}

/**
 * Formata evento para o padrão Meta CAPI
 * @param {Object} event - Evento do dataLayer
 * @returns {Object} Payload formatado para CAPI
 */
function formatEventForCAPI(event) {
  // Mapeamento de nomes de eventos GA4 para Meta
  const eventNameMap = {
    'purchase': 'Purchase',
    'add_to_cart': 'AddToCart',
    'begin_checkout': 'InitiateCheckout',
    'view_item': 'ViewContent',
    'generate_lead': 'Lead',
    'sign_up': 'CompleteRegistration'
  };

  // Criar payload base
  const capiEvent = {
    event_name: eventNameMap[event.event] || event.event,
    event_time: Math.floor(Date.now() / 1000),
    event_id: event.event_id || generateUniqueId(),
    event_source_url: event.page_location || window.location.href,
    action_source: 'website',
    user_data: extractUserData(event),
    custom_data: extractCustomData(event)
  };

  return capiEvent;
}

/**
 * Extrai dados do usuário para CAPI com anonimização adequada
 * @param {Object} event - Evento original
 * @returns {Object} Dados do usuário formatados para CAPI
 */
function extractUserData(event) {
  const userData = {
    client_user_agent: navigator.userAgent,
    client_ip_address: null, // Será preenchido pelo servidor
    fbp: getCookie('_fbp'),
    fbc: getCookie('_fbc')
  };

  // Adicionar external_id se disponível
  if (event.user_id) {
    userData.external_id = [event.user_id];
  }

  // Adicionar identificadores com hash (se disponíveis)
  // Nota: hashing deve ser feito no servidor para maior segurança
  
  return userData;
}

/**
 * Extrai dados específicos do evento baseado em seu tipo
 * @param {Object} event - Evento original
 * @returns {Object} Dados customizados para CAPI
 */
function extractCustomData(event) {
  const customData = {};
  
  // Dados comuns para eventos de e-commerce
  if (event.currency) customData.currency = event.currency;
  if (event.value) customData.value = event.value;
  
  // Dados específicos baseados no tipo de evento
  switch (event.event) {
    case 'purchase':
      if (event.transaction_id) customData.order_id = event.transaction_id;
      if (event.items) {
        customData.contents = event.items.map(item => ({
          id: item.item_id,
          quantity: item.quantity,
          item_price: item.price
        }));
        customData.content_ids = event.items.map(item => item.item_id);
      }
      break;
      
    case 'add_to_cart':
    case 'view_item':
      if (event.items && event.items.length > 0) {
        customData.content_ids = event.items.map(item => item.item_id);
        customData.contents = event.items.map(item => ({
          id: item.item_id,
          quantity: item.quantity || 1,
          item_price: item.price
        }));
        customData.content_type = 'product';
      }
      break;
      
    case 'generate_lead':
      if (event.lead_id) customData.lead_id = event.lead_id;
      break;
  }
  
  return customData;
}

/**
 * Envia o evento para endpoint interno do servidor
 * @param {String} endpoint - Caminho do endpoint
 * @param {Object} payload - Dados a serem enviados
 */
function sendToServerEndpoint(endpoint, payload) {
  fetch(endpoint, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(payload),
    keepalive: true // Garante envio mesmo durante navegação
  })
  .catch(error => {
    console.error('Error sending to server:', error);
    storeEventForRetry(endpoint, payload);
  });
}

/**
 * Armazena evento para retry em caso de falha
 * @param {String} endpoint - Endpoint destino
 * @param {Object} payload - Dados do evento
 */
function storeEventForRetry(endpoint, payload) {
  try {
    // Obter fila existente
    const queueKey = 'analytics_retry_queue';
    let queue = JSON.parse(localStorage.getItem(queueKey) || '[]');
    
    // Adicionar evento à fila
    queue.push({
      endpoint,
      payload,
      timestamp: Date.now(),
      retryCount: 0
    });
    
    // Limitar tamanho da fila
    if (queue.length > 50) queue = queue.slice(-50);
    
    // Salvar fila atualizada
    localStorage.setItem(queueKey, JSON.stringify(queue));
  } catch (error) {
    console.error('Error storing event for retry:', error);
  }
}
```

#### 3.2 Implementação Server-Side (Node.js)

```javascript
const express = require('express');
const axios = require('axios');
const crypto = require('crypto');
const router = express.Router();

/**
 * Endpoint para receber eventos de conversão Meta
 */
router.post('/conversions/meta', async (req, res) => {
  try {
    const event = req.body;
    
    // Validação básica
    if (!event.event_name || !event.event_id) {
      return res.status(400).json({ 
        error: 'Missing required fields'
      });
    }
    
    // Verificar duplicação
    const isDuplicate = await checkDuplicateEvent(event.event_id);
    if (isDuplicate) {
      return res.status(200).json({ 
        status: 'skipped', 
        reason: 'duplicate'
      });
    }
    
    // Adicionar IP do cliente (para melhorar match rate)
    if (!event.user_data) event.user_data = {};
    event.user_data.client_ip_address = req.ip;
    
    // Enriquecer com dados do servidor
    await enrichEventWithServerData(event);
    
    // Aplicar hash em dados sensíveis
    hashUserData(event.user_data);
    
    // Enviar para Meta Conversions API
    const metaResponse = await sendToMetaConversionsAPI(event);
    
    // Registrar evento processado
    await logProcessedEvent(event, metaResponse);
    
    return res.status(200).json({ 
      status: 'success',
      meta_response: metaResponse.data 
    });
    
  } catch (error) {
    console.error('Server error processing conversion:', error);
    
    // Armazenar para retry posterior
    await queueEventForRetry(req.body);
    
    return res.status(500).json({ 
      status: 'queued_for_retry',
      error: error.message 
    });
  }
});

/**
 * Aplica hash SHA-256 em dados sensíveis do usuário
 * @param {Object} userData - Objeto user_data do evento
 */
function hashUserData(userData) {
  // Lista de campos que precisam de hash
  const fieldsToHash = ['em', 'ph', 'fn', 'ln', 'ct', 'st', 'zp', 'country'];
  
  for (const field of fieldsToHash) {
    if (userData[field] && Array.isArray(userData[field])) {
      userData[field] = userData[field].map(value => 
        isAlreadyHashed(value) ? value : sha256Hash(value)
      );
    }
  }
}

/**
 * Verifica se um valor já está em formato hash SHA-256
 * @param {String} value - Valor a verificar
 * @returns {Boolean}
 */
function isAlreadyHashed(value) {
  // Verificar se é string com 64 caracteres hex (SHA-256)
  return typeof value === 'string' && 
         value.length === 64 && 
         /^[a-f0-9]{64}$/i.test(value);
}

/**
 * Aplica hash SHA-256 em um valor
 * @param {String} value - Valor a ser hasheado
 * @returns {String} Hash SHA-256
 */
function sha256Hash(value) {
  if (!value) return null;
  
  // Normalizar: remover espaços extras e converter para minúsculas
  value = value.trim().toLowerCase();
  
  // Aplicar hash SHA-256
  return crypto.createHash('sha256').update(value).digest('hex');
}

/**
 * Enriquece evento com dados adicionais do servidor
 * @param {Object} event - Evento a ser enriquecido
 */
async function enrichEventWithServerData(event) {
  // Identificar usuário
  let userId = null;
  
  // Tentar obter ID do usuário de diferentes fontes
  if (event.user_data?.external_id?.length > 0) {
    userId = event.user_data.external_id[0];
  }
  
  if (!userId) return;
  
  try {
    // Buscar dados complementares no banco/CRM
    const userData = await getUserFromDatabase(userId);
    
    if (!userData) return;
    
    // Enriquecer com dados adicionais (não sobrescrever existentes)
    if (!event.user_data.em && userData.email) {
      event.user_data.em = [userData.email];
    }
    
    if (!event.user_data.ph && userData.phone) {
      event.user_data.ph = [userData.phone];
    }
    
    // Adicionar localização se disponível
    if (userData.city) event.user_data.ct = [userData.city];
    if (userData.state) event.user_data.st = [userData.state];
    if (userData.zip) event.user_data.zp = [userData.zip];
    if (userData.country) event.user_data.country = [userData.country];
    
    // Para compras, adicionar dados da transação
    if (event.event_name === 'Purchase' && event.custom_data?.order_id) {
      const transactionId = event.custom_data.order_id;
      const orderData = await getOrderFromDatabase(transactionId);
      
      if (orderData) {
        // Enriquecer com dados complementares da compra
        if (orderData.ltv) event.custom_data.customer_ltv = orderData.ltv;
        if (orderData.customer_type) event.custom_data.customer_type = orderData.customer_type;
        
        // Adicionar produtos completos se não enviados pelo cliente
        if (orderData.items && (!event.custom_data.contents || !event.custom_data.contents.length)) {
          event.custom_data.contents = orderData.items.map(item => ({
            id: item.id,
            quantity: item.quantity,
            item_price: item.price
          }));
          event.custom_data.content_ids = orderData.items.map(item => item.id);
        }
      }
    }
  } catch (error) {
    console.error('Error enriching event:', error);
    // Continuar mesmo sem enriquecimento
  }
}

/**
 * Envia evento para a Conversions API do Meta
 * @param {Object} event - Evento formatado
 * @returns {Promise<Object>} Resposta da API
 */
async function sendToMetaConversionsAPI(event) {
  const accessToken = process.env.META_API_ACCESS_TOKEN;
  const pixelId = process.env.META_PIXEL_ID;
  
  const endpoint = `https://graph.facebook.com/v17.0/${pixelId}/events`;
  
  const payload = {
    data: [event],
    access_token: accessToken,
    test_event_code: process.env.NODE_ENV === 'development' ? 
                     process.env.META_TEST_EVENT_CODE : undefined
  };
  
  return await axios.post(endpoint, payload);
}
```

### 4. UNIFIED TRACKING LAYER (MÚLTIPLAS PLATAFORMAS)

#### 4.1 Camada Unificada de Rastreamento

```javascript
/**
 * Rastreia eventos de forma unificada em múltiplas plataformas
 * @param {String} eventName - Nome do evento universal
 * @param {Object} eventParams - Parâmetros do evento
 * @returns {Object} Detalhes do rastreamento
 */
function trackEvent(eventName, eventParams = {}) {
  // 1. Gerar ID único para correlacionar entre plataformas
  const eventId = eventParams.event_id || generateUUID();
  
  // 2. Preparar parâmetros base
  const commonParams = {
    event_id: eventId,
    timestamp: new Date().toISOString(),
    page_location: window.location.href,
    page_referrer: document.referrer,
    ...eventParams
  };
  
  // 3. Rastrear no GA4 (via dataLayer)
  const ga4EventName = mapEventName(eventName, 'ga4');
  const ga4Params = mapParams(commonParams, 'ga4');
  
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: ga4EventName,
    ...ga4Params
  });
  
  // 4. Rastrear no Meta Pixel (se disponível)
  if (typeof fbq !== 'undefined') {
    const metaEventName = mapEventName(eventName, 'meta');
    const metaParams = mapParams(commonParams, 'meta');
    
    fbq('track', metaEventName, metaParams);
  }
  
  // 5. Preparar dados para Server-Side (Meta CAPI, etc)
  const serverEvent = {
    event: 'server_side_event',
    destination: ['meta_capi', 'ga4'],
    eventName: eventName,
    eventId: eventId,
    timestamp: commonParams.timestamp,
    params: commonParams
  };
  
  // Enviar para processamento server-side
  window.dataLayer.push(serverEvent);
  
  // 6. Log para debugging (em modo desenvolvimento)
  if (isDevelopment()) {
    console.groupCollapsed(`📊 Event: ${eventName} [${eventId}]`);
    console.log('Common:', commonParams);
    console.log('GA4:', { event: ga4EventName, ...ga4Params });
    console.log('Meta:', { event: mapEventName(eventName, 'meta'), ...mapParams(commonParams, 'meta') });
    console.log('Server:', serverEvent);
    console.groupEnd();
  }
  
  // 7. Retornar detalhes para possível uso
  return {
    event_id: eventId,
    platforms: {
      ga4: { name: ga4EventName, params: ga4Params },
      meta: { name: mapEventName(eventName, 'meta'), params: mapParams(commonParams, 'meta') },
      server: serverEvent
    }
  };
}

/**
 * Mapeia nomes de eventos entre plataformas
 * @param {String} eventName - Nome do evento universal
 * @param {String} platform - Plataforma destino ('ga4', 'meta')
 * @returns {String} Nome mapeado para a plataforma
 */
function mapEventName(eventName, platform) {
  // Mapas de conversão para cada plataforma
  const eventMaps = {
    ga4: {
      'page-view': 'page_view',
      'product-view': 'view_item',
      'add-to-cart': 'add_to_cart',
      'checkout': 'begin_checkout',
      'purchase': 'purchase',
      'signup': 'sign_up',
      'lead': 'generate_lead'
      // Adicionar mais mapeamentos conforme necessário
    },
    meta: {
      'page-view': 'PageView',
      'product-view': 'ViewContent',
      'add-to-cart': 'AddToCart',
      'checkout': 'InitiateCheckout',
      'purchase': 'Purchase',
      'signup': 'CompleteRegistration',
      'lead': 'Lead'
      // Adicionar mais mapeamentos conforme necessário
    }
  };
  
  // Obter mapa específico da plataforma
  const map = eventMaps[platform] || {};
  
  // Retornar nome mapeado ou o original se não houver mapeamento
  return map[eventName] || eventName;
}

/**
 * Mapeia parâmetros entre plataformas
 * @param {Object} params - Parâmetros universais
 * @param {String} platform - Plataforma destino ('ga4', 'meta')
 * @returns {Object} Parâmetros mapeados para a plataforma
 */
function mapParams(params, platform) {
  const result = { ...params };
  
  // Mapeamentos específicos por plataforma
  if (platform === 'ga4') {
    // GA4 usa snake_case
    if (params.items) result.items = params.items;
    if (params.transaction_id) result.transaction_id = params.transaction_id;
  } 
  else if (platform === 'meta') {
    // Meta Pixel usa camelCase e alguns campos específicos
    if (params.transaction_id) result.order_id = params.transaction_id;
    
    // Converter itens para formato Meta
    if (params.items) {
      result.content_type = 'product';
      result.content_ids = params.items.map(item => item.item_id);
      result.contents = params.items.map(item => ({
        id: item.item_id,
        quantity: item.quantity,
        item_price: item.price
      }));
      
      // Remover campo original
      delete result.items;
    }
  }
  
  return result;
}
```

### 5. SERVER-SIDE TAG MANAGER IMPLEMENTATION

#### 5.1 Configuração Server-Side GTM

```javascript
/**
 * Implementação server-side GTM usando Express (Node.js)
 */
const express = require('express');
const bodyParser = require('body-parser');
const { ServerContainer } = require('@google-cloud/serverless-gtm');
const app = express();

// Configuração de middleware
app.use(bodyParser.json());

// Inicializar container GTM server-side
const gtmServer = new ServerContainer({
  containerId: process.env.GTM_SERVER_CONTAINER_ID,
  containerVersion: process.env.GTM_CONTAINER_VERSION,
  apiKey: process.env.GOOGLE_API_KEY
});

/**
 * Endpoint principal para coleta de dados
 */
app.post('/collect', async (req, res) => {
  try {
    const payload = req.body;
    
    // Adicionar metadados do servidor
    payload.server_timestamp = new Date().toISOString();
    payload.client_ip = anonymizeIP(req.ip);
    payload.user_agent = req.headers['user-agent'] || '';
    
    // Processar pelo GTM Server
    const result = await gtmServer.process(payload);
    
    // Responder rapidamente ao cliente
    res.status(200).json({ 
      status: 'success',
      event_id: payload.event_id || 'unknown'
    });
    
    // Log dos resultados (após responder ao cliente)
    console.log('GTM Processing Result:', JSON.stringify({
      event_id: payload.event_id,
      event: payload.event,
      tags_executed: result.tagsExecuted,
      status: result.status
    }));
    
  } catch (error) {
    console.error('Error processing server event:', error);
    
    // Ainda responder com sucesso para não bloquear o cliente
    res.status(202).json({ 
      status: 'accepted',
      message: 'Event queued for processing'
    });
    
    // Adicionar à fila de retry em segundo plano
    queueForRetry(req.body);
  }
});

/**
 * Anonimiza endereço IP para conformidade com privacidade
 * @param {String} ip - Endereço IP
 * @returns {String} IP anonimizado
 */
function anonymizeIP(ip) {
  if (!ip) return null;
  
  // IPv4: Manter apenas os 3 primeiros octetos
  if (ip.includes('.')) {
    const parts = ip.split('.');
    if (parts.length === 4) {
      return `${parts[0]}.${parts[1]}.${parts[2]}.0`;
    }
  }
  
  // IPv6: Manter apenas os 4 primeiros grupos
  if (ip.includes(':')) {
    const parts = ip.split(':');
    if (parts.length >= 4) {
      return `${parts[0]}:${parts[1]}:${parts[2]}:${parts[3]}::`;
    }
  }
  
  return ip;
}
```

#### 5.2 Cliente para Server-Side GTM

```javascript
/**
 * Cliente JavaScript para envio de eventos ao Server-Side GTM
 */
class ServerSideClient {
  /**
   * Inicializa o cliente
   * @param {Object} config - Configurações
   */
  constructor(config = {}) {
    this.endpoint = config.endpoint || '/collect';
    this.debug = config.debug || false;
    this.retryQueue = [];
    this.offlineSupport = config.offlineSupport !== false;
    this.maxRetries = config.maxRetries || 3;
    
    // Inicializar suporte offline
    if (this.offlineSupport) {
      this.initOfflineSupport();
    }
  }
  
  /**
   * Envia evento para servidor
   * @param {String} eventName - Nome do evento
   * @param {Object} params - Parâmetros do evento
   * @returns {Promise} Resultado do envio
   */
  async track(eventName, params = {}) {
    // Criar payload completo
    const payload = {
      event: eventName,
      event_id: params.event_id || this.generateEventId(),
      timestamp: new Date().toISOString(),
      ...params
    };
    
    // Logging se debug habilitado
    if (this.debug) {
      console.log(`📤 Sending to server: ${eventName}`, payload);
    }
    
    try {
      // Enviar para o servidor
      const response = await fetch(this.endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        keepalive: true // Importante para eventos na saída da página
      });
      
      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }
      
      const result = await response.json();
      
      if (this.debug) {
        console.log(`✅ Server response:`, result);
      }
      
      return result;
      
    } catch (error) {
      if (this.debug) {
        console.error(`❌ Error sending event:`, error);
      }
      
      // Adicionar à fila de retry se suporte offline ativado
      if (this.offlineSupport) {
        this.addToRetryQueue(eventName, params);
      }
      
      return { 
        status: 'error',
        message: error.message,
        queued: this.offlineSupport
      };
    }
  }
  
  /**
   * Adiciona evento à fila de retry
   * @param {String} eventName - Nome do evento
   * @param {Object} params - Parâmetros do evento
   */
  addToRetryQueue(eventName, params) {
    this.retryQueue.push({
      event: eventName,
      params: params,
      timestamp: Date.now(),
      retryCount: 0
    });
    
    // Salvar fila no localStorage
    this.saveQueueToStorage();
    
    // Agendar retry se online
    if (navigator.onLine) {
      setTimeout(() => this.processRetryQueue(), 2000);
    }
  }
  
  /**
   * Processa a fila de retry
   */
  async processRetryQueue() {
    if (this.retryQueue.length === 0 || !navigator.onLine) return;
    
    // Processar cada evento na fila
    const eventQueue = [...this.retryQueue];
    this.retryQueue = [];
    
    for (const item of eventQueue) {
      try {
        // Incrementar contador de tentativas
        item.retryCount++;
        
        // Tentar enviar novamente
        if (item.retryCount <= this.maxRetries) {
          await this.track(item.event, item.params);
        } else if (this.debug) {
          console.warn(`⚠️ Max retries exceeded for event:`, item);
        }
      } catch (error) {
        // Se falhar novamente, retornar à fila
        if (item.retryCount < this.maxRetries) {
          this.retryQueue.push(item);
        }
      }
    }
    
    // Atualizar storage
    this.saveQueueToStorage();
  }
  
  /**
   * Inicializa suporte para modo offline
   */
  initOfflineSupport() {
    // Carregar fila existente
    this.loadQueueFromStorage();
    
    // Adicionar listeners para mudanças de conectividade
    window.addEventListener('online', () => {
      if (this.debug) {
        console.log('🌐 Device online, processing queued events');
      }
      this.processRetryQueue();
    });
    
    // Salvar fila ao fechar a página
    window.addEventListener('beforeunload', () => {
      this.saveQueueToStorage();
    });
    
    // Tentar processar imediatamente se estiver online
    if (navigator.onLine) {
      setTimeout(() => this.processRetryQueue(), 1000);
    }
  }
  
  /**
   * Salva fila de retry no localStorage
   */
  saveQueueToStorage() {
    if (!window.localStorage) return;
    
    try {
      localStorage.setItem('ssgtm_queue', JSON.stringify(this.retryQueue));
    } catch (error) {
      if (this.debug) {
        console.error('Error saving queue to localStorage:', error);
      }
    }
  }
  
  /**
   * Carrega fila de retry do localStorage
   */
  loadQueueFromStorage() {
    if (!window.localStorage) return;
    
    try {
      const queue = localStorage.getItem('ssgtm_queue');
      if (queue) {
        this.retryQueue = JSON.parse(queue) || [];
        
        if (this.debug && this.retryQueue.length > 0) {
          console.log(`📋 Loaded ${this.retryQueue.length} queued events`);
        }
      }
    } catch (error) {
      if (this.debug) {
        console.error('Error loading queue from localStorage:', error);
      }
      this.retryQueue = [];
    }
  }
  
  /**
   * Gera ID único para eventos
   * @returns {String} UUID único
   */
  generateEventId() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      const r = Math.random() * 16 | 0;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }
}
```

## REFERÊNCIAS CRUZADAS

### Documentos Relacionados
- [Taxonomia de Eventos](taxonomia_eventos.md) - Definições dos eventos e parâmetros a serem sincronizados
- [Validação e QA](validacao_qa.md) - Métodos para validar integrações entre plataformas
- [Segurança e Privacidade](seguranca_privacidade.md) - Requisitos de conformidade para transferência de dados
- [Implementação de Eventos](implementacao_eventos.md) - Métodos práticos de implementação

### Recursos Externos
- [Meta Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/) - Documentação oficial
- [GA4 Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4) - Documentação oficial
- [GTM Server-Side](https://developers.google.com/tag-platform/tag-manager/server-side) - Guia de implementação

## INSTRUÇÕES PARA O AGENTE

### Quando Consultar Este Documento
- Ao implementar integrações entre múltiplas plataformas de analytics
- Ao configurar rastreamento server-side para Meta CAPI ou GA4
- Ao mapear parâmetros e eventos entre sistemas diferentes
- Ao diagnosticar problemas de consistência de dados entre plataformas
- Ao desenvolver uma camada unificada de tracking para múltiplos destinos

### Como Utilizar Este Conhecimento
1. IDENTIFIQUE a configuração de plataformas do usuário (GA4+Meta, etc.)
2. SELECIONE a arquitetura apropriada (Client-Side, Server-Side ou Híbrida)
3. UTILIZE a Matriz de Correlação para mapear parâmetros consistentemente
4. IMPLEMENTE utilizando os exemplos de código como referência
5. VALIDE integrações seguindo os protocolos em [validacao_qa.md](validacao_qa.md)

## POSICIONAMENTO NO SISTEMA DE TRÊS CAMADAS

### Conexão com 1️⃣ NÚCLEO FUNDAMENTAL
- **Entrada**: Recebe princípios de consistência de dados e precisão de rastreamento
- **Saída**: Aplica esses princípios em implementações técnicas específicas

### Conexão com 3️⃣ MECANISMOS DE EVOLUÇÃO DIRIGIDA
- **Entrada**: Recebe feedback sobre novas plataformas e métodos de integração
- **Saída**: Fornece métricas de confiabilidade de dados entre sistemas

<!-- METADADOS PARA O AGENTE -->
<<ENTITY_TYPE>> = "integration_architecture"
<<KNOWLEDGE_LAYER>> = 2
<<CRITICALITY>> = "high"
<<FRAGILITY_ZONES>> = ["server_side_tagging", "cross_platform_sync", "privacy_compliance"]
<<RELATED_CONCEPTS>> = ["data_consistency", "server_side_tracking", "offline_tracking", "event_deduplication"]