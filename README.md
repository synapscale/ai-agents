# 🚀 Unified Sales Framework

## 📋 O Que É Este Projeto?

O **Unified Sales Framework** é uma plataforma que unifica dois sistemas poderosos:
1. **Multi-Agent-AI-System** - Especializado em agentes de vendas e copywriting
2. **Google ADK (Agent Development Kit)** - Framework robusto para desenvolvimento de agentes de IA

Este repositório contém **22 agentes de IA especializados** prontos para uso em vendas, copywriting, análise e integração de APIs.

## 🔧 Instalação Rápida (2 minutos)

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/unified-sales-framework.git
cd unified-sales-framework

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Teste a instalação
python scripts/unified_cli.py list-agents
```

## 🤖 Agentes Disponíveis

### Agentes Tradicionais (14)
- **Analytics**: ANALYTICSGPT, Super Track
- **APIs**: APIUnifyMaster, APIsImputOutputMapper, HotmartAPIMaster, KiwifyAPIMaster, PaytAPIMaster, PerfectpayAPIMaster
- **Copywriting**: conversion_catalyst, metaphor_architect, neurohook_ultra, pain_detector, paradigm_architect, retention_architect
- **Knowledge**: DocRAGOptimizer

### Agentes Verticais (8)
- analytics_specialist
- api_integration_specialist
- persuasion_copywriter
- neurohook_specialist
- metaphor_architect
- retention_optimizer
- knowledge_curator
- exemplo_vertical

## 📘 Guia de Uso Passo a Passo

### 1️⃣ Listar Todos os Agentes Disponíveis
```bash
python scripts/unified_cli.py list-agents
```

### 2️⃣ Criar um Novo Agente a Partir de Template
```bash
# Criar agente vertical
python scripts/unified_cli.py from-template templates/yaml_examples/vertical_agent.yaml

# Criar agente tradicional
python scripts/unified_cli.py from-template templates/yaml_examples/traditional_agent.yaml
```

### 3️⃣ Usar um Agente em Seu Código Python
```python
# Exemplo de uso do Paradigm Architect
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente
agent = create_unified_agent('paradigm_architect', 'Especialista em transformação paradigmática')

# Usar o agente
result = agent.process("Crie um framework persuasivo para venda de software B2B")
print(result)
```

### 4️⃣ Validar o Sistema
```bash
# Executar validação completa
python scripts/real_validation.py

# Testar agentes específicos
python scripts/agent_specific_tests.py
```

## 📁 Estrutura do Projeto (O Que Está Onde)

```
unified-sales-framework/
├── agents/                     # Agentes tradicionais (14)
│   ├── analytics/              # Agentes de análise
│   ├── apis/                   # Agentes de integração de APIs
│   ├── copywriting/            # Agentes de copywriting
│   └── knowledge_masters/      # Agentes de conhecimento
│
├── vertical_agents/            # Agentes verticais especializados (8)
│   ├── analytics_specialist/   # Especialista em análise
│   ├── persuasion_copywriter/  # Copywriter de persuasão
│   └── ...                     # Outros agentes verticais
│
├── scripts/                    # Scripts de automação
│   ├── unified_cli.py          # CLI principal
│   ├── real_validation.py      # Validação do sistema
│   └── ...                     # Outros scripts úteis
│
├── templates/                  # Templates para criação de agentes
│   └── yaml_examples/          # Exemplos de YAML para criar agentes
│
├── src/                        # Código fonte principal
│   └── unified_sales_framework/# Pacote principal
│       ├── core/               # Componentes core
│       ├── knowledge/          # Sistema de conhecimento
│       └── ...                 # Outros módulos
│
├── docs/                       # Documentação completa
│   ├── guides/                 # Guias de uso
│   └── tutorials/              # Tutoriais passo a passo
│
└── examples/                   # Exemplos práticos de uso
```

## 🔍 Exemplos Práticos

### Exemplo 1: Gerar Copy Persuasivo
```python
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente de copywriting
agent = create_unified_agent('persuasion_copywriter', 'Especialista em persuasão')

# Gerar copy persuasivo
briefing = """
Produto: Software de automação de marketing
Público: Pequenas empresas
Problema principal: Falta de tempo para gerenciar campanhas
Benefício principal: Aumento de 30% em conversões
"""

result = agent.process(f"Crie um email persuasivo com base neste briefing: {briefing}")
print(result)
```

### Exemplo 2: Integrar com APIs de Pagamento
```python
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente de integração de APIs
agent = create_unified_agent('api_integration_specialist', 'Especialista em APIs')

# Gerar código de integração
api_request = """
Preciso integrar a API do Hotmart para:
1. Verificar status de compra
2. Gerar link de pagamento
3. Configurar webhook de compra aprovada
"""

result = agent.process(api_request)
print(result)
```

### Exemplo 3: Analisar Dados de Vendas
```python
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente de análise
agent = create_unified_agent('analytics_specialist', 'Especialista em análise')

# Analisar dados de vendas
data_analysis_request = """
Tenho os seguintes dados de vendas:
- 100 visitas por dia
- 5% taxa de conversão
- R$ 297 ticket médio
- 30% taxa de abandono

Como posso melhorar meus resultados?
"""

result = agent.process(data_analysis_request)
print(result)
```

## 🛠️ Comandos Úteis (Makefile)

```bash
# Instalar dependências
make install

# Instalar dependências de desenvolvimento
make install-dev

# Executar testes
make test

# Validar sistema
make test-validation

# Listar agentes
make list-agents

# Formatar código
make format

# Limpar arquivos temporários
make clean
```

## 📚 Documentação Detalhada

Para documentação mais detalhada, consulte:

1. **Guia de Instalação**: [docs/guides/installation.md](docs/guides/installation.md)
2. **Tutorial Inicial**: [docs/tutorials/getting-started.md](docs/tutorials/getting-started.md)
3. **Referência da API**: [docs/api/reference.md](docs/api/reference.md)
4. **Arquitetura do Sistema**: [docs/architecture/overview.md](docs/architecture/overview.md)

## ❓ Perguntas Frequentes

### Como criar meu próprio agente?
Crie um arquivo YAML baseado nos exemplos em `templates/yaml_examples/` e use o comando:
```bash
python scripts/unified_cli.py from-template seu_template.yaml
```

### Como funciona a integração com o Google ADK?
O sistema usa uma versão adaptada do Google ADK com fallback automático. Veja detalhes em `src/unified_sales_framework/core/fixed_adk.py`.

### Posso usar os agentes em produção?
Sim! O sistema foi validado e está pronto para uso em produção.

### Como contribuir para o projeto?
Veja o guia de contribuição em [CONTRIBUTING.md](CONTRIBUTING.md).

## 🤝 Suporte e Ajuda

Se precisar de ajuda:

1. Consulte a [documentação](docs/)
2. Verifique os [exemplos](examples/)
3. Execute `python scripts/unified_cli.py --help`

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

**Pronto para começar?** Execute `python scripts/unified_cli.py list-agents` para ver todos os agentes disponíveis!

