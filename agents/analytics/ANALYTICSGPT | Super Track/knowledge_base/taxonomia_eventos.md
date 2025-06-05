# Análise e Otimização do Documento "Taxonomia de Eventos & Parâmetros"

---
versão: 1.0  
última_atualização: 2025-04-15  
autor: AnalyticsGPT  
status: Ativo  
---

## 📋 Propósito Fundamental do Documento
Este documento serve como **fonte autoritativa e estruturada** para:
1. Padronizar a coleta de dados através de eventos
2. Garantir consistência entre plataformas de analytics
3. Fornecer ao agente conhecimento para validar, recomendar e criar implementações de rastreamento
4. Servir como referência técnica para governança de dados

## 🔍 Problemas Identificados no Documento Atual
1. **Formatação quebrada** nas tabelas (caracteres `|` aparecendo no texto)
2. **Falta estrutura alinhada** com o padrão de três seções definido
3. **Ausente conexão explícita** com o sistema de três camadas
4. **Instruções insuficientes** para o agente sobre como usar

## 🚀 Documento Otimizado e Reformatado

```markdown
# TAXONOMIA DE EVENTOS & PARÂMETROS

---
version: 6.0  
status: Ativo  
focus: Padrões e enriquecimento de eventos analíticos  
last_updated: 2024-01-15  
compatibility: ["GA4", "Meta Pixel", "GTM", "Adobe Analytics"]  
knowledge_layer: 2
criticality: HIGH
---

## VISÃO GERAL

### Propósito do Componente
Este documento define a **estrutura padronizada** para todos os eventos de analytics, estabelecendo:
- Nomenclatura consistente de eventos e parâmetros
- Parâmetros obrigatórios e opcionais por categoria
- Hierarquia de enriquecimento progressivo
- Compatibilidade cross-platform e best practices

### Principais Casos de Uso
1. **Implementação Técnica**: Guia a instrumentação de eventos em aplicações web/mobile
2. **Validação de Qualidade**: Checklist para verificar conformidade dos eventos
3. **Expansão Controlada**: Framework para adicionar novos eventos sem degradar a consistência
4. **Documentação de Sistema**: Referência para outros times interpretarem os dados

### Conexão com Outros Componentes
- **Dependência de**: `taxonomia_parametros.md` (definições detalhadas de parâmetros individuais)
- **Informa para**: `implementacao_eventos.md` (código de implementação prático)
- **Consultado por**: `validacao_qa.md` (testes de verificação)
- **Evolui através de**: `evolucao_dirigida/atualizacao_taxonomia.md` (processo de atualização)

### Instruções para o Agente
Quando consultado sobre eventos de analytics, o agente deve:
1. IDENTIFICAR a categoria do evento solicitado
2. VERIFICAR os parâmetros obrigatórios para aquela categoria
3. SUGERIR enriquecimentos apropriados baseados no contexto
4. VALIDAR se a implementação atende às regras de privacidade e limites técnicos

## CONTEÚDO DETALHADO

### 1. FUNDAMENTOS DE EVENTOS

#### 1.1 Convenções de Nomenclatura
- **Eventos**: formato `snake_case` com padrão `ação_objeto`
  - Exemplos: `page_view`, `form_submit`, `purchase`
- **Parâmetros**: formato `snake_case` com padrão `objeto_atributo`
  - Exemplos: `page_title`, `user_id_hashed`, `product_price`
- **Valores**: strings em minúsculas, sem espaços
  - Exemplos: `homepage`, `add_to_cart`, `email_signup`

#### 1.2 Estrutura Hierárquica
Eventos são organizados em camadas de complexidade incremental:

| Nível | Tipo | Exemplos | Enriquecimento |
|-------|------|----------|----------------|
| 1 | **Básicos** | `page_view`, `click` | Baixo |
| 2 | **Interação** | `file_download`, `video_play` | Médio |
| 3 | **Conversão** | `purchase`, `signup` | Alto |
| 4 | **Lifecycle** | `subscription_renew`, `churn` | Completo |

#### 1.3 Contexto Mínimo Obrigatório
Todo evento DEVE incluir:
```json
{
  "event": "nome_do_evento",
  "timestamp": "2024-01-15T12:34:56.789Z",
  "session_id": "sess_abc123",
  "event_id": "evt_xyz789",
  "page": {
    "location": "https://exemplo.com/pagina",
    "title": "Título da Página",
    "referrer": "https://google.com"
  }
}
```

### 2. CATEGORIAS DE EVENTOS E PARÂMETROS

#### 2.1 Eventos de Página

| Evento | Descrição | Parâmetros Obrigatórios | Parâmetros Recomendados |
|--------|-----------|-------------------------|-------------------------|
| `page_view` | Visualização de página | `page.location`, `page.title` | `page.type`, `page_referrer` |
| `scroll` | Rolagem de página | `scroll_depth_threshold`, `page.location` | `scroll_units`, `time_on_page` |
| `exit_intent` | Intenção de saída | `exit_type`, `page.location` | `time_on_page`, `scroll_depth` |

#### 2.2 Eventos de E-commerce

| Evento | Descrição | Parâmetros Obrigatórios | Exemplos de Valor |
|--------|-----------|-------------------------|-------------------|
| `view_item` | Visualização de produto | `item_id`, `item_name` | SKU-123, "Smartphone X" |
| `add_to_cart` | Adição ao carrinho | `items[]`, `currency`, `value` | [{item_id: "SKU-123"}], "BRL", 299.99 |
| `purchase` | Compra finalizada | `transaction_id`, `value`, `items[]` | "TXN-789", 299.99, [{item_id: "SKU-123"}] |

**Exemplo Completo de Evento de Compra:**
```json
{
  "event": "purchase",
  "ecommerce": {
    "transaction_id": "TXN-2024-789",
    "value": 299.97,
    "currency": "BRL",
    "items": [
      {
        "item_id": "SKU-123",
        "item_name": "Smartphone Premium",
        "price": 299.97,
        "quantity": 1,
        "category": "Eletrônicos/Celulares",
        "brand": "TechBrand",
        "variant": "128GB Azul",
        "margin_percent": 35.0,
        "inventory_age_days": 7
      }
    ],
    "checkout": {
      "steps": 4,
      "funnel_position": "completed",
      "payment_method": "credit_card",
      "shipping_tier": "express"
    }
  },
  "user": {
    "id_hashed": "sha256_abc123", 
    "segment": "high_value",
    "lifetime_value": 1250.00
  }
}
```

#### 2.3 Eventos de Engajamento

| Evento | Descrição | Parâmetros Obrigatórios | Parâmetros para Análise Avançada |
|--------|-----------|-------------------------|----------------------------------|
| `video_start` | Início de vídeo | `video.id`, `video.title` | `video.duration`, `video.player` |
| `video_progress` | Progresso do vídeo | `video.id`, `video.percent_watched` | `video.current_time`, `playback_rate` |
| `video_complete` | Conclusão do vídeo | `video.id`, `video.duration` | `video.engagement.attention_score` |

**Exemplo de Engajamento com Vídeo:**
```json
{
  "event": "video_progress",
  "video": {
    "id": "vid_12345",
    "title": "Tutorial Avançado",
    "duration": 325,
    "percent_watched": 75,
    "player": "vimeo",
    "engagement": {
      "attention_score": 0.82,
      "playback_events": ["play", "pause", "fullscreen"],
      "buffering_ratio": 0.05
    }
  }
}
```

#### 2.4 Eventos de Formulário

| Evento | Descrição | Parâmetros Obrigatórios | Insights Adicionais |
|--------|-----------|-------------------------|---------------------|
| `form_start` | Início de preenchimento | `form.id`, `form.name` | `form.fields_count`, `form.type` |
| `form_submit` | Envio do formulário | `form.id`, `form.success` | `form.completion_time`, `form.errors` |
| `form_abandonment` | Abandono de formulário | `form.id`, `form.last_field_touched` | `form.time_spent`, `form.completed_percent` |

### 3. CAMADAS DE ENRIQUECIMENTO

#### 3.1 Contexto de Usuário (Não-PII)
```json
{
  "user": {
    "id_hashed": "sha256_abc123", // SHA-256 com salt
    "anonymous_id": "anon_xyz789",
    "segment": "high_value",
    "tier": "premium",
    "lifetime_value": 1250.00,
    "days_since_first_visit": 127,
    "session_count": 8
  }
}
```

#### 3.2 Contexto de Dispositivo e Técnico
| Parâmetro | Tipo | Descrição | Coleta |
|-----------|------|-----------|--------|
| `device_type` | String | "desktop", "mobile", "tablet" | User-Agent |
| `device_fingerprint` | String | ID anônimo baseado em atributos | FingerprintJS |
| `viewport_size` | String | "1920x1080" | JS Properties |
| `connection_type` | String | "wifi", "4g", "3g" | Network Info API |
| `page_load_time` | Decimal | Tempo em segundos | Performance API |
| `memory_usage` | Integer | Uso de RAM em MB | Performance API |

#### 3.3 Atribuição de Marketing
```json
{
  "attribution": {
    "utm": {
      "source": "google",
      "medium": "cpc",
      "campaign": "black_friday"
    },
    "first_touch": {
      "source": "organic_search",
      "date": "2023-12-01"
    },
    "click_id": {
      "gclid": "CNy1kNGIq_cCFVAYHwod...",
      "fbclid": "AZ123456789"
    }
  }
}
```

### 4. COMPATIBILIDADE CROSS-PLATFORM

#### 4.1 Mapeamento de Parâmetros
| Nosso Parâmetro | GA4 | Meta Pixel | Adobe Analytics |
|-----------------|-----|------------|----------------|
| `user.id_hashed` | `user_id` | `external_id` | `visitorID` |
| `ecommerce.value` | `value` | `value` | `purchaseAmt` |
| `video.percent_watched` | `progress` | N/A | `mediaProgress` |

#### 4.2 Eventos Essenciais por Plataforma
| Plataforma | Eventos Críticos | Observações |
|------------|------------------|-------------|
| **GA4** | `page_view`, `purchase` | Requer implementação via Tag Manager |
| **Meta Pixel** | `PageView`, `Purchase` | Nomenclatura diferente (camelCase) |
| **Adobe** | `pageView`, `productPurchase` | Requer mapeamento adicional |

### 5. GOVERNANÇA E QUALIDADE

#### 5.1 Regras de Validação
```javascript
// Validação básica de evento
function validateEvent(event) {
  const required = ["event", "timestamp", "session_id"];
  const valid = required.every(field => event.hasOwnProperty(field));
  
  if (!valid) {
    console.error("Evento inválido - campos obrigatórios ausentes");
    recordValidationError(event);
  }
  
  return valid;
}
```

#### 5.2 Limites Técnicos e Performance
- **Máximo de Parâmetros**: 50 por evento
- **Tamanho Máximo**: 8KB por evento (limite GA4)
- **Frequência Máxima**: 20 eventos/segundo por usuário
- **Volume de Dados**: Considerar impacto em custos de processamento

#### 5.3 Considerações de Privacidade
- **Proibido**: Email, CPF, telefone em texto claro
- **Obrigatório**: Hash SHA-256 para identificadores pessoais
- **Minimização**: Coletar apenas dados necessários
- **Retenção**: Definir políticas de exclusão para dados sensíveis

## REFERÊNCIAS CRUZADAS

### Documentos Relacionados
- [Taxonomia de Parâmetros](taxonomia_parametros.md) - Definições detalhadas de cada parâmetro
- [Implementação de Eventos](implementacao_eventos.md) - Como implementar tecnicamente 
- [Validação e QA](validacao_qa.md) - Testes e validação de implementação
- [Segurança e Privacidade](seguranca_privacidade.md) - Requisitos de proteção de dados

### Recursos Externos
- [GA4 Event Reference](https://developers.google.com/analytics/devguides/collection/ga4/reference/events)
- [Meta Pixel Events](https://developers.facebook.com/docs/meta-pixel/reference)
- [JSON Schema Validator](https://www.jsonschemavalidator.net/) - Para validar estrutura de eventos

### Governança de Evolução
Para propor alterações nesta taxonomia, siga o processo em [Evolução de Taxonomia](evolucao_dirigida/atualizacao_taxonomia.md)

## EVOLUÇÃO DESTE DOCUMENTO

### Changelog
```markdown
### 2024-01-15 (v1.0)
- Primeira versão estável
```

### Alinhamento com Sistema de Três Camadas
Este documento é parte do **2️⃣ SISTEMA DE CONHECIMENTO EXPANSÍVEL**, servindo como:
- **Estrutura de Expansão Controlada**: Define regras para crescimento consistente
- **Fonte de Validação**: Permite ao agente verificar implementações contra padrões
- **Interface com Camada 1**: Implementa conceitos fundamentais da Camada 1
- **Base para Camada 3**: Fornece métricas de avaliação para evolução

<!-- METADADOS PARA O AGENTE -->  
<<ENTITY_TYPE>> = "event_taxonomy"  
<<KNOWLEDGE_LAYER>> = 2  
<<CRITICALITY>> = "high"  
<<FRAGILITY_ZONES>> = ["param_conflicts", "platform_mapping"]  
<<VALIDATION_SCRIPT>> = "/scripts/validate_events.py"
```

## ✅ Melhorias Aplicadas
1. **Estrutura Aprimorada**: Reformatada para seguir exatamente o padrão de três seções
2. **Tabelas Corrigidas**: Formatação markdown adequada
3. **Instruções para o Agente**: Adicionadas diretrizes claras de uso
4. **Conexão com as Três Camadas**: Explicitado posicionamento no sistema
5. **Exemplos Enriquecidos**: Mantidos mas reorganizados como exemplos práticos
6. **Governança**: Ampliada com regras de validação práticas
7. **Metadados para IA**: Adicionados no final para facilitar navegação do agente

## 🔄 Modificações Deliberadas
1. **Redução de Código JavaScript**: Mantido apenas o essencial para ilustrar conceitos
2. **Categorização mais Clara**: Eventos agrupados por domínio funcional
3. **Progressive Enhancement**: Estrutura de camadas de enriquecimento mais explícita
4. **Manutenção Futura**: Adicionado processo de governança de evolução

Este documento agora está perfeitamente adequado como parte do Sistema de Conhecimento Expansível, fornecendo ao agente todos os recursos necessários para implementar, validar e evoluir a taxonomia de eventos, sem "gordura" desnecessária.