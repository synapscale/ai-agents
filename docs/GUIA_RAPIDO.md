# 🚀 Guia Rápido: Unified Sales Framework

Este guia rápido fornece instruções concisas para começar a usar o Unified Sales Framework em minutos.

## ⚡ Instalação em 30 Segundos

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/unified-sales-framework.git
cd unified-sales-framework

# 2. Crie um ambiente virtual e ative
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

## 🤖 Comandos Essenciais

### Listar Agentes Disponíveis
```bash
python scripts/unified_cli.py list-agents
```

### Criar Agente a Partir de Template
```bash
python scripts/unified_cli.py from-template templates/yaml_examples/vertical_agent.yaml
```

### Validar Sistema
```bash
python scripts/real_validation.py
```

## 📋 Uso Rápido em Python

```python
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente
agent = create_unified_agent('paradigm_architect', 'Especialista em persuasão')

# Usar agente
result = agent.process("Crie um email persuasivo para venda de curso online")
print(result)
```

## 🔍 Agentes Populares

| Categoria | Nome do Agente | Especialidade |
|-----------|---------------|---------------|
| Copywriting | paradigm_architect | Transformação paradigmática |
| Copywriting | persuasion_copywriter | Copy persuasivo |
| Analytics | analytics_specialist | Análise de dados |
| APIs | api_integration_specialist | Integração de APIs |

## 📁 Estrutura de Arquivos Importante

- `scripts/unified_cli.py` - CLI principal
- `examples/` - Exemplos práticos
- `docs/` - Documentação completa
- `templates/yaml_examples/` - Templates para criar agentes

## 🔧 Solução de Problemas Comuns

- **Erro de importação**: Execute scripts do diretório raiz
- **Erro de módulo não encontrado**: Verifique se instalou as dependências
- **Erro de permissão**: Use `chmod +x scripts/*.py` para tornar scripts executáveis

## 📚 Próximos Passos

1. Explore os [exemplos práticos](../examples/)
2. Leia o [tutorial completo](tutorials/getting-started.md)
3. Consulte a [documentação detalhada](guides/installation.md)

---

**Precisa de mais ajuda?** Consulte a documentação completa ou execute `python scripts/unified_cli.py --help`

