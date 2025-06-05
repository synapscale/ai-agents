# 🚀 Tutorial: Primeiros Passos

Este tutorial guiará você pelos primeiros passos com o Unified Sales Framework, mostrando como usar os agentes de IA para tarefas práticas de vendas e marketing.

## 📋 Pré-requisitos

- Unified Sales Framework instalado (veja [Guia de Instalação](../guides/installation.md))
- Ambiente virtual ativado
- Conhecimento básico de Python

## 🎯 O Que Você Aprenderá

1. Como listar e explorar os agentes disponíveis
2. Como usar um agente de copywriting para criar conteúdo persuasivo
3. Como usar um agente de integração de APIs
4. Como criar seu próprio agente personalizado
5. Como combinar múltiplos agentes para um fluxo de trabalho completo

## 🔍 Passo 1: Explorar os Agentes Disponíveis

Vamos começar explorando quais agentes estão disponíveis no framework:

```bash
# Listar todos os agentes
python scripts/unified_cli.py list-agents
```

Você verá uma lista de agentes organizados por categoria. Vamos examinar um agente específico:

```python
# Arquivo: explore_agent.py
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente
agent = create_unified_agent('paradigm_architect', 'Especialista em transformação paradigmática')

# Verificar capacidades
capabilities = agent.get_capabilities()
print(f"Capacidades do agente: {capabilities}")

# Verificar ferramentas disponíveis
tools = agent.get_available_tools()
print(f"Ferramentas disponíveis: {tools}")
```

Execute este script para ver as capacidades e ferramentas do agente:

```bash
python explore_agent.py
```

## 🖋️ Passo 2: Criar Conteúdo Persuasivo

Vamos usar o agente `paradigm_architect` para criar um texto persuasivo:

```python
# Arquivo: create_copy.py
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente de copywriting
agent = create_unified_agent('paradigm_architect', 'Especialista em transformação paradigmática')

# Definir briefing
briefing = """
Produto: Curso de Marketing Digital
Público: Empreendedores iniciantes
Problema principal: Dificuldade em atrair clientes online
Benefício principal: Aumento de 300% em leads qualificados em 60 dias
Preço: R$ 997,00
"""

# Gerar copy persuasivo
prompt = f"""
Com base neste briefing, crie uma página de vendas persuasiva:
{briefing}

Inclua:
1. Headline principal
2. 3 subtítulos
3. 5 benefícios principais
4. 3 objeções respondidas
5. Call to action final
"""

result = agent.process(prompt)

# Salvar resultado
with open("copy_resultado.md", "w", encoding="utf-8") as f:
    f.write(result)

print("Copy persuasivo gerado e salvo em 'copy_resultado.md'")
```

Execute este script para gerar o conteúdo:

```bash
python create_copy.py
```

## 🔌 Passo 3: Integrar com APIs

Agora, vamos usar um agente especializado em APIs para gerar código de integração:

```python
# Arquivo: api_integration.py
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente de integração de APIs
agent = create_unified_agent('api_integration_specialist', 'Especialista em APIs')

# Definir requisito de integração
api_request = """
Preciso integrar a API do Hotmart para:
1. Verificar status de compra
2. Gerar link de pagamento
3. Configurar webhook de compra aprovada

Por favor, forneça o código Python completo com exemplos.
"""

# Gerar código de integração
result = agent.process(api_request)

# Salvar resultado
with open("hotmart_integration.py", "w", encoding="utf-8") as f:
    f.write(result)

print("Código de integração gerado e salvo em 'hotmart_integration.py'")
```

Execute este script para gerar o código de integração:

```bash
python api_integration.py
```

## 🛠️ Passo 4: Criar Seu Próprio Agente

Vamos criar um agente personalizado usando um template YAML:

1. Primeiro, crie um arquivo YAML com a configuração do seu agente:

```yaml
# Arquivo: meu_agente.yaml
name: meu_agente_vendas
type: vertical
display_name: "Especialista em Vendas B2B"
description: "Agente especializado em estratégias de vendas para mercado B2B"
domain: "b2b_sales"
capabilities:
  - sales_strategy
  - lead_qualification
  - objection_handling
knowledge_domains:
  - b2b_sales
  - enterprise_negotiation
prompt_template: |
  Você é um especialista em vendas B2B com foco em:
  
  1. Qualificação avançada de leads
  2. Estratégias de negociação empresarial
  3. Manejo de objeções complexas
  4. Ciclos de venda longos
  
  Use seu conhecimento para ajudar em estratégias de vendas B2B.
```

2. Agora, use o CLI para criar o agente:

```bash
python scripts/unified_cli.py from-template meu_agente.yaml
```

3. Teste seu novo agente:

```python
# Arquivo: test_custom_agent.py
from unified_sales_framework.core.fixed_adk import create_unified_agent

# Criar agente personalizado
agent = create_unified_agent('meu_agente_vendas', 'Especialista em Vendas B2B')

# Testar agente
query = """
Estou tentando vender um software de automação de marketing (R$ 2.500/mês) 
para uma empresa de médio porte. Já fiz 2 reuniões com o diretor de marketing,
mas ele está hesitante devido ao preço. Como devo proceder?
"""

result = agent.process(query)
print(result)
```

Execute este script para testar seu agente personalizado:

```bash
python test_custom_agent.py
```

## 🔄 Passo 5: Fluxo de Trabalho Completo

Agora, vamos combinar múltiplos agentes para criar um fluxo de trabalho completo de vendas:

```python
# Arquivo: sales_workflow.py
from unified_sales_framework.core.fixed_adk import create_unified_agent

# 1. Análise de mercado com agente de analytics
analytics_agent = create_unified_agent('analytics_specialist', 'Especialista em análise')
market_analysis = analytics_agent.process("""
Analise o mercado de software de automação de marketing para pequenas empresas:
1. Tamanho do mercado
2. Principais concorrentes
3. Tendências atuais
4. Oportunidades de diferenciação
""")

print("=== ANÁLISE DE MERCADO CONCLUÍDA ===")

# 2. Criação de copy persuasivo
copy_agent = create_unified_agent('persuasion_copywriter', 'Especialista em persuasão')
persuasive_copy = copy_agent.process(f"""
Com base nesta análise de mercado, crie um email persuasivo para prospecção:

{market_analysis}

O email deve:
1. Chamar atenção no assunto
2. Identificar a dor do cliente
3. Apresentar solução única
4. Incluir call-to-action para agendar demonstração
""")

print("=== COPY PERSUASIVO CRIADO ===")

# 3. Integração com CRM
api_agent = create_unified_agent('api_integration_specialist', 'Especialista em APIs')
crm_integration = api_agent.process("""
Crie um script Python para integrar este fluxo de prospecção com o RD Station CRM:
1. Registrar lead quando abrir o email
2. Atualizar status quando clicar no link
3. Notificar vendedor quando solicitar demonstração
""")

print("=== INTEGRAÇÃO COM CRM CONFIGURADA ===")

# 4. Preparação para objeções
objection_agent = create_unified_agent('paradigm_architect', 'Especialista em objeções')
objection_handling = objection_agent.process("""
Prepare respostas para as 5 objeções mais comuns em vendas de software de automação de marketing:
1. "É muito caro"
2. "Já usamos outra ferramenta"
3. "Não temos equipe para operar"
4. "Podemos implementar isso internamente"
5. "Precisamos consultar mais pessoas"
""")

print("=== MANEJO DE OBJEÇÕES PREPARADO ===")

# Salvar resultados completos
with open("fluxo_vendas_completo.md", "w", encoding="utf-8") as f:
    f.write("# Fluxo de Vendas Completo\n\n")
    f.write("## 1. Análise de Mercado\n\n")
    f.write(market_analysis)
    f.write("\n\n## 2. Copy Persuasivo\n\n")
    f.write(persuasive_copy)
    f.write("\n\n## 3. Integração com CRM\n\n```python\n")
    f.write(crm_integration)
    f.write("\n```\n\n## 4. Manejo de Objeções\n\n")
    f.write(objection_handling)

print("\n✅ Fluxo de trabalho completo gerado e salvo em 'fluxo_vendas_completo.md'")
```

Execute este script para ver o fluxo de trabalho completo:

```bash
python sales_workflow.py
```

## 📊 Visualizando Resultados

Para visualizar os resultados gerados:

```bash
# No Linux/macOS
cat fluxo_vendas_completo.md

# No Windows
type fluxo_vendas_completo.md
```

Ou abra os arquivos em seu editor de texto preferido.

## 🧪 Validação do Sistema

Para garantir que tudo está funcionando corretamente:

```bash
# Executar validação completa
python scripts/real_validation.py

# Testar agentes específicos
python scripts/agent_specific_tests.py
```

## 📚 Próximos Passos

Agora que você domina os conceitos básicos, recomendamos:

1. Explorar a [Referência da API](../api/reference.md) para entender todas as opções disponíveis
2. Verificar a [Arquitetura do Sistema](../architecture/overview.md) para entender como tudo funciona
3. Experimentar os [Exemplos Avançados](../../examples/advanced/) para casos de uso mais complexos

## ❓ Perguntas Frequentes

### Como posso personalizar o comportamento de um agente?

Você pode personalizar o comportamento passando parâmetros adicionais:

```python
agent = create_unified_agent(
    'paradigm_architect',
    'Especialista em transformação paradigmática',
    model="gpt-4",
    temperature=0.7,
    max_tokens=2000
)
```

### Como posso usar minha própria base de conhecimento?

Você pode criar uma pasta com documentos de conhecimento e carregá-la:

```python
from unified_sales_framework.knowledge.unified_knowledge_service import UnifiedKnowledgeService

# Inicializar serviço de conhecimento
knowledge_service = UnifiedKnowledgeService()

# Carregar conhecimento personalizado
knowledge_service.load_custom_knowledge("./meu_conhecimento")

# Usar em agente
agent = create_unified_agent(
    'paradigm_architect',
    'Especialista em transformação paradigmática',
    knowledge_service=knowledge_service
)
```

---

**Parabéns!** Você agora sabe como usar o Unified Sales Framework para tarefas práticas de vendas e marketing. Continue explorando os recursos avançados e personalizando os agentes para suas necessidades específicas.

