# PROTOCOLOS DE VALIDAÇÃO E QA

---
version: 1.0  
status: Ativo  
focus: Garantia de qualidade ponta-a-ponta em implementações de analytics  
last_updated: 2025-04-15  
knowledge_layer: 2  
criticality: HIGH  
author: Analytics Engineering Team
---

## VISÃO GERAL

### Propósito do Componente
Este documento estabelece os processos sistemáticos, ferramentas e critérios para validar implementações de analytics, garantindo:
- **Integridade Absoluta**: Dados completos, precisos e válidos em todo o ciclo
- **Conformidade Rigorosa**: Aderência total aos padrões da Taxonomia de Eventos
- **Detecção Proativa**: Identificação precoce de falhas e riscos de privacidade
- **Confiabilidade Comprovada**: Base sólida para tomada de decisão e operação do agente

### Principais Casos de Uso
1. Validação de novas implementações de tracking
2. Diagnóstico de problemas em dados analíticos
3. Auditoria periódica de qualidade dos dados
4. Verificação de conformidade com LGPD/GDPR
5. Gate de qualidade entre ambientes (DEV > QA > PROD)

### Conexão com Outros Componentes
- **Depende de**: `taxonomia_eventos.md` (padrões a validar)
- **Informa**: `implementacao_eventos.md` (correções necessárias)
- **Suporta**: `integracao_plataformas.md` (validação específica)
- **Alimenta**: `evolucao_dirigida/feedback_qualidade.md` (métricas para evolução)
- **Verifica**: `seguranca_privacidade.md` (regras de privacidade)

## CONTEÚDO DETALHADO

### 1. METODOLOGIA DE VALIDAÇÃO

#### 1.1 Abordagem em 5 Camadas
| Camada | Escopo | Foco | Ferramentas |
|--------|--------|------|-------------|
| **Unitária** | Parâmetro | Formato e valor | JSON Schema |
| **Funcional** | Evento | Contexto e regras | Debug Consoles |
| **Integração** | Fluxo | Sequência e IDs | Session Recorders |
| **Sistema** | Plataforma | Integridade | Analytics Audits |
| **Privacidade** | Todos | Consentimento e PII | CMP Validators |

#### 1.2 Framework de Qualidade
1. **Completude**: Parâmetros obrigatórios presentes
2. **Precisão**: Valores refletem a realidade
3. **Consistência**: Estrutura uniforme
4. **Validade**: Formatos corretos
5. **Unicidade**: Sem duplicação
6. **Temporalidade**: Timestamp adequado

### 2. CHECKLISTS DE VALIDAÇÃO

#### 2.1 Essencial (Todos Eventos)
- [ ] `event_id`: UUID único presente
- [ ] `event_name`: snake_case e na Taxonomia
- [ ] `user_id`: Hash SHA-256 (se logado)
- [ ] `timestamp`: ISO 8601 (UTC)
- [ ] `page_location`: URL sem PII
- [ ] `page_referrer`: Capturado corretamente

#### 2.2 Atribuição e Marketing
- [ ] UTMs capturados da URL
- [ ] First-touch armazenado ≥90 dias
- [ ] Click IDs (`gclid`, `fbclid`) presentes
- [ ] Modelo de atribuição documentado

#### 2.3 E-commerce (Exemplo Purchase)
```json
{
  "event": "purchase",
  "validation": {
    "required_params": ["transaction_id", "value", "items"],
    "business_rules": [
      "value > 0",
      "value = sum(items) + tax + shipping",
      "transaction_id único em 90 dias"
    ]
  }
}
```

#### 2.4 Consentimento (CMP)
- [ ] Tags só disparam após consentimento
- [ ] Nenhum dado coletado se rejeitado
- [ ] Estado persistido entre sessões
- [ ] Nenhum PII em campos livres

#### 2.5 Server-Side Tagging
- [ ] Deduplicação funcionando
- [ ] Latência <500ms
- [ ] IDs consistentes client/server
- [ ] Fallback para falhas

### 3. FERRAMENTAS DE DIAGNÓSTICO

#### 3.1 Ferramentas Chave
| Categoria | Exemplos | Uso |
|-----------|----------|-----|
| **Extensões** | Tag Assistant, Pixel Helper | Validação rápida |
| **Proxies** | Charles, Fiddler | Inspeção de payload |
| **Plataforma** | GA4 DebugView | Visualização em tempo real |
| **CMP** | Ferramentas do fornecedor | Verificação consentimento |

#### 3.2 Debug Mode (Exemplo)
```javascript
function enableDebug(options = {}) {
  const config = {
    console: true,
    validate: true,
    ...options
  };
  
  const originalPush = window.dataLayer.push;
  window.dataLayer.push = function(event) {
    if (config.console) {
      console.group(`Event: ${event.event}`);
      console.log('Payload:', event);
      if (config.validate) validateEvent(event);
      console.groupEnd();
    }
    return originalPush.apply(this, arguments);
  };
}
```

### 4. PROCEDIMENTOS DE QA

#### 4.1 Processo por Fase
| Fase | Escopo | Responsável |
|------|--------|-------------|
| Desenvolvimento | Evento único | Dev |
| Integração | Fluxo completo | QA |
| Pré-Prod | Plataformas | Analytics Eng |
| Produção | Monitoramento | Data Ops |

#### 4.2 Testes Automatizados
```javascript
// Exemplo Cypress
it('valida evento purchase', () => {
  cy.completePurchase();
  cy.wait('@ga4Event').then(({request}) => {
    expect(request.body).to.include('event=purchase');
    expect(request.body).to.include('transaction_id=');
  });
});
```

#### 4.3 Matriz Cross-Platform
| Evento | GA4 | Meta | CAPI | Validação |
|--------|-----|------|------|-----------|
| purchase | ✓ | ✓ | ✓ | transaction_id único |
| lead | ✓ | ✓ | ✓ | Dados sincronizados com CRM |

### 5. MONITORAMENTO

#### 5.1 Indicadores (DQI)
| Métrica | Threshold | Alerta |
|---------|-----------|--------|
| Completude | >99% | <98% |
| Taxa Erro | <1% | >2% |
| Reconciliação | >99% | <97% |
| Latência | <150ms | >400ms |

#### 5.2 Alertas Críticos
- Queda >30% em purchase/lead
- PII detectada
- Falha CMP
- Discrepância >5% com backend

## REFERÊNCIAS CRUZADAS
- [Taxonomia de Eventos](taxonomia_eventos.md)
- [Implementação](implementacao_eventos.md)
- [Integração](integracao_plataformas.md)
- [Segurança](seguranca_privacidade.md)

## POSICIONAMENTO
- **Núcleo Fundamental**: Implementa princípios de qualidade
- **Evolução Dirigida**: Fornece métricas para melhoria

<!-- METADADOS -->
<<ENTITY_TYPE>> = "validation_protocols"
<<KNOWLEDGE_LAYER>> = 2
<<CRITICALITY>> = "critical"
<<FRAGILITY_ZONES>> = ["SST_validation", "CMP_compliance"]