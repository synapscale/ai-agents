# 💡 Exemplos Práticos do Unified Sales Framework

Este diretório contém exemplos práticos que demonstram como usar o Unified Sales Framework em cenários reais. Os exemplos estão organizados por nível de complexidade.

## 🚀 Como Executar os Exemplos

Todos os exemplos podem ser executados diretamente do terminal. Certifique-se de que você:

1. Instalou todas as dependências (`pip install -r requirements.txt`)
2. Está no diretório raiz do projeto (`cd unified-sales-framework`)
3. Tem seu ambiente virtual ativado (se estiver usando um)

## 📁 Estrutura de Exemplos

### 📂 Exemplos Básicos (`basic/`)

Exemplos simples que demonstram funcionalidades individuais:

#### 🖋️ Geração de Copy Persuasivo

```bash
# Executar com configurações padrão
python examples/basic/copywriting_example.py

# Personalizar parâmetros
python examples/basic/copywriting_example.py --product "Curso de Python Avançado" --audience "Desenvolvedores intermediários" --price "R$ 1.997,00"
```

Este exemplo usa o agente `paradigm_architect` para gerar copy persuasivo para uma página de vendas.

#### 🔌 Integração de API

```bash
# Executar com configurações padrão (Hotmart)
python examples/basic/api_integration_example.py

# Usar outra plataforma
python examples/basic/api_integration_example.py --platform "Stripe" --output "stripe_integration.py"
```

Este exemplo usa o agente `api_integration_specialist` para gerar código de integração com APIs de pagamento.

### 📂 Exemplos Avançados (`advanced/`)

Exemplos mais complexos que combinam múltiplos agentes e funcionalidades:

#### 🔄 Fluxo de Trabalho Completo de Vendas

```bash
# Executar com configurações padrão
python examples/advanced/complete_sales_workflow.py

# Personalizar parâmetros
python examples/advanced/complete_sales_workflow.py --product "Software de CRM" --audience "Empresas de médio porte" --industry "Tecnologia" --price "R$ 997/mês"
```

Este exemplo demonstra um fluxo de trabalho completo de vendas, incluindo:
1. Análise de mercado
2. Criação de copy persuasivo
3. Geração de sequência de emails
4. Script de manejo de objeções
5. Especificação de dashboard de vendas

Os resultados são salvos em arquivos separados no diretório `sales_workflow_output/`.

## 🛠️ Criando Seus Próprios Exemplos

Você pode usar estes exemplos como base para criar seus próprios scripts personalizados. Aqui está um modelo básico:

```python
#!/usr/bin/env python3
"""
Exemplo Personalizado: [Descrição]
"""

import os
import sys
from pathlib import Path

# Adicionar diretório raiz ao path para importações
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente
agent = create_unified_agent('nome_do_agente', 'Descrição do agente')

# Definir prompt
prompt = """
Seu prompt aqui...
"""

# Processar com o agente
result = agent.process(prompt)

# Fazer algo com o resultado
print(result)
```

## 📚 Recursos Adicionais

- [Guia de Instalação](../docs/guides/installation.md)
- [Tutorial de Primeiros Passos](../docs/tutorials/getting-started.md)
- [Referência da API](../docs/api/reference.md)
- [Arquitetura do Sistema](../docs/architecture/overview.md)

## ❓ Solução de Problemas

### Erro: "No module named 'unified_sales_framework'"

**Solução**: Certifique-se de que está executando os exemplos do diretório raiz do projeto:

```bash
cd unified-sales-framework
python examples/basic/copywriting_example.py
```

### Erro: "ImportError: Cannot import name 'create_unified_agent'"

**Solução**: Verifique se todas as dependências foram instaladas corretamente:

```bash
pip install -r requirements.txt
```

### Erro: "ModuleNotFoundError: No module named 'google.adk'"

**Solução**: O sistema usa uma versão adaptada do Google ADK com fallback automático. Não é necessário instalar o ADK separadamente.

---

**Dica**: Experimente modificar os exemplos para atender às suas necessidades específicas. Os agentes são flexíveis e podem ser adaptados para diversos casos de uso!

