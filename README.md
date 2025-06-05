# Unified Sales Framework

**Combinando a especialização vertical do Multi-Agent-AI-System com a infraestrutura robusta do ADK-Python**

## Visão Geral

O Unified Sales Framework é uma plataforma revolucionária que unifica:

1. **Agentes de Vendas Especializados** - 67 agentes verticais profundamente especializados em copywriting, APIs, analytics e knowledge management
2. **Infraestrutura Robusta** - Baseada no Agent Development Kit (ADK) do Google para deploy empresarial e escalabilidade
3. **Geração Automática** - Sistema de geração de agentes a partir de templates YAML
4. **Conhecimento Especializado** - 42 bases de conhecimento vetoriais para diferentes domínios de vendas
5. **Monitoramento Avançado** - Métricas específicas de vendas e conversão

## Arquitetura

```
unified-sales-framework/
├── src/                      # Código fonte principal
│   ├── agents/               # Agentes especializados
│   │   ├── copywriting/      # Agentes de copywriting (PARADIGM-ARCHITECT, etc.)
│   │   ├── apis/             # Agentes de integração de APIs (APIUnifyMaster, etc.)
│   │   ├── analytics/        # Agentes de análise (ANALYTICSGPT, etc.)
│   │   └── knowledge/        # Agentes de gestão de conhecimento (DocRAGOptimizer, etc.)
│   ├── core/                 # Componentes core do framework
│   ├── tools/                # Ferramentas especializadas
│   ├── knowledge/            # Sistema de conhecimento unificado
│   └── generation/           # Sistema de geração automática
├── templates/                # Templates para geração de agentes
│   └── unified_sales_agent_template/  # Template definitivo unificado
├── examples/                 # Exemplos práticos
├── deployment/               # Configurações de deployment
├── cli/                      # Interface de linha de comando
├── tests/                    # Testes automatizados
└── docs/                     # Documentação
```

## Recursos Principais

### 1. Template Definitivo Unificado

O coração do framework é o **Template Definitivo Unificado** que combina:

- **Estrutura Hierárquica** - Agente principal + 5 subagentes especializados
- **Sistema de Conhecimento Multi-Domínio** - Com VectorMemoryService
- **Ferramentas Especializadas** - Para cada função de vendas
- **Modelos Múltiplos** - Com fallback automático
- **Deploy Empresarial** - Com scaling e monitoramento

### 2. CLI Unificado

```bash
# Criar agente de vendas especializado
uaf create sales-agent --type=paradigm-architect --market=b2b_saas

# Migrar agente existente
uaf migrate agent --source=paradigm_architect --target=unified_sales

# Gerar campanha completa
uaf generate campaign --agent=paradigm_architect --briefing=./client_briefings/tech_startup.yaml

# Deploy para produção
uaf deploy agent --name=PARADIGM-ARCHITECT --platform=vertex_ai
```

### 3. Sistema de Conhecimento Unificado

- **42 Bases de Conhecimento** - Organizadas por domínio
- **Embeddings Otimizados** - Para recuperação precisa
- **RAG Avançado** - Com feedback loop para melhoria contínua
- **Ferramentas de Recuperação** - Integradas aos agentes

### 4. Monitoramento Especializado

- **Métricas de Conversão** - Por agente e campanha
- **Efetividade de Paradigma** - Medição de mudança conceitual
- **Tempo de Ciclo de Venda** - Otimização de funil
- **Satisfação do Cliente** - Via feedback automatizado

## Começando

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/unified-sales-framework/unified-sales-framework.git
cd unified-sales-framework

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# Instalar dependências
make install-dev
```

### Configuração

1. Copie `.env.example` para `.env.local` e configure suas credenciais:
   ```bash
   cp .env.example .env.local
   ```

2. Edite `.env.local` com suas chaves de API e configurações

### Uso Básico

```python
from unified_sales_framework.agents import ParadigmArchitectAgent
from unified_sales_framework.core import UnifiedKnowledgeSystem

# Inicializar sistema de conhecimento
knowledge = UnifiedKnowledgeSystem()
knowledge.load_domain("paradigm_shift")

# Criar agente
agent = ParadigmArchitectAgent(
    memory_service=knowledge.get_memory_service("paradigm_shift"),
    tools=[knowledge.get_retrieval_tool("paradigm_shift")]
)

# Executar agente
result = agent.run("Crie um framework persuasivo para venda de software B2B")
print(result)
```

## Documentação

Para documentação completa, visite [docs.unified-sales-framework.com](https://docs.unified-sales-framework.com)

## Contribuindo

Contribuições são bem-vindas! Por favor, leia [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre nosso código de conduta e processo de submissão de pull requests.

## Licença

Este projeto é licenciado sob a Licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- Google ADK Team - Pela infraestrutura robusta
- Multi-Agent-AI-System Team - Pelos agentes especializados

