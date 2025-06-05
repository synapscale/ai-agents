# Convenções e Padrões - Unified Sales Framework

## Convenções de Nomenclatura

### Agentes

#### Classes de Agentes
- **Formato**: `{Nome}Agent` (PascalCase)
- **Exemplos**: 
  - `ParadigmArchitectAgent`
  - `PainDetectorAgent`
  - `ApiUnifyMasterAgent`

#### Arquivos de Agentes
- **Formato**: `{nome_snake_case}/agent.py`
- **Exemplos**:
  - `src/agents/copywriting/paradigm_architect/agent.py`
  - `src/agents/apis/api_unify_master/agent.py`

#### Subagentes
- **Formato**: `{Nome}SubAgent` (PascalCase)
- **Exemplos**:
  - `AxiomArchaeologistSubAgent`
  - `ConceptArchitectSubAgent`

### Ferramentas

#### Classes de Ferramentas
- **Formato**: `{Nome}Tool` (PascalCase)
- **Exemplos**:
  - `ParadigmAnalysisTool`
  - `ConversionOptimizationTool`
  - `HubSpotIntegrationTool`

#### Arquivos de Ferramentas
- **Formato**: `{categoria}/{nome_snake_case}_tool.py`
- **Exemplos**:
  - `src/tools/sales_tools/paradigm_analysis_tool.py`
  - `src/tools/api_tools/hubspot_integration_tool.py`

### Configurações

#### Arquivos YAML
- **Formato**: `{tipo}_config.yaml`
- **Exemplos**:
  - `agent_config.yaml`
  - `tools_config.yaml`
  - `memory_config.yaml`

### Conhecimento

#### Domínios de Conhecimento
- **Formato**: `{dominio_snake_case}`
- **Exemplos**:
  - `paradigm_shift`
  - `pain_detection`
  - `conversion_optimization`

## Padrões de Código

### Estrutura de Classes de Agentes ADK

```python
from google.adk import Agent, LlmAgent, LoopAgent
from google.adk.tools import RetrievalTool
from google.adk.memory import VectorMemoryService
from typing import List, Optional

class ParadigmArchitectAgent(Agent):
    """
    Agente especializado em transformação de paradigmas de venda.
    
    Combina:
    - Estrutura hierárquica do template original
    - Poderes avançados do ADK
    - Especialização em vendas
    """
    
    def __init__(
        self,
        model: str = "claude-3-sonnet",
        memory_service: Optional[VectorMemoryService] = None,
        tools: Optional[List] = None,
        **kwargs
    ):
        # Prompt original preservado
        instruction = """
        # PARADIGM-ARCHITECT: Transformador de Paradigmas de Venda
        ## MISSÃO PRINCIPAL
        TRANSFORME completamente como prospectos enxergam problemas e soluções...
        """
        
        # Configuração de subagentes
        sub_agents = [
            AxiomArchaeologistSubAgent(),
            ConceptArchitectSubAgent(),
            LegitimacyEngineerSubAgent(),
            ParadigmaticLinguistSubAgent(),
            TransdisciplinarySynthesizerSubAgent()
        ]
        
        # Ferramentas especializadas
        if tools is None:
            tools = [
                ParadigmAnalysisTool(),
                ConceptMappingTool(),
                PersuasionFrameworkTool()
            ]
        
        super().__init__(
            instruction=instruction,
            model=model,
            sub_agents=sub_agents,
            tools=tools,
            memory_service=memory_service,
            **kwargs
        )
```

### Estrutura de Ferramentas Customizadas

```python
from google.adk.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Any, Dict

class ParadigmAnalysisInput(BaseModel):
    """Input para análise de paradigma."""
    current_paradigm: str = Field(description="Paradigma atual do prospecto")
    target_market: str = Field(description="Mercado alvo")
    pain_points: List[str] = Field(description="Pontos de dor identificados")

class ParadigmAnalysisTool(BaseTool):
    """Ferramenta para análise e transformação de paradigmas."""
    
    name: str = "paradigm_analysis"
    description: str = "Analisa paradigmas atuais e cria estratégias de transformação"
    input_schema: type[BaseModel] = ParadigmAnalysisInput
    
    def run(self, input_data: ParadigmAnalysisInput) -> Dict[str, Any]:
        """Executa análise de paradigma."""
        # Lógica de análise
        return {
            "paradigm_shift_strategy": "...",
            "key_leverage_points": [...],
            "transformation_framework": "..."
        }
```

### Estrutura de Configuração YAML

```yaml
# agent_config.yaml
agent:
  name: "PARADIGM-ARCHITECT"
  type: "Agent"  # Agent, LlmAgent, LoopAgent
  model: "claude-3-sonnet"
  fallback_model: "gpt-4-turbo"
  max_tokens: 4000
  temperature: 0.7
  
delegation:
  threshold: 0.75
  max_iterations: 5
  
subagents:
  - name: "AXIOM-ARCHAEOLOGIST"
    type: "LlmAgent"
    model: "claude-3-haiku"
    specialization: "axiom_discovery"
  
  - name: "CONCEPT-ARCHITECT"
    type: "LoopAgent"
    model: "gpt-4-turbo"
    specialization: "concept_creation"
    max_iterations: 3

knowledge:
  domains:
    - "paradigm_shift"
    - "persuasion_frameworks"
    - "sales_psychology"
  
  retrieval:
    top_k: 5
    similarity_threshold: 0.8

tools:
  - name: "paradigm_analysis"
    type: "custom"
    class: "ParadigmAnalysisTool"
  
  - name: "hubspot_integration"
    type: "openapi"
    spec_url: "https://api.hubapi.com/api-catalog-public/v1/apis"
```

## Padrões de Testes

### Testes Unitários

```python
import pytest
from unified_sales_framework.agents import ParadigmArchitectAgent
from unified_sales_framework.tools import ParadigmAnalysisTool

class TestParadigmArchitectAgent:
    """Testes para ParadigmArchitectAgent."""
    
    def test_agent_initialization(self):
        """Testa inicialização do agente."""
        agent = ParadigmArchitectAgent()
        assert agent.name == "PARADIGM-ARCHITECT"
        assert len(agent.sub_agents) == 5
    
    def test_paradigm_analysis(self):
        """Testa análise de paradigma."""
        agent = ParadigmArchitectAgent()
        result = agent.run("Analise paradigma de vendas B2B")
        assert "paradigm_shift_strategy" in result
```

### Testes de Integração

```python
import pytest
from unified_sales_framework.core import UnifiedKnowledgeSystem
from unified_sales_framework.agents import ParadigmArchitectAgent

class TestAgentKnowledgeIntegration:
    """Testes de integração agente-conhecimento."""
    
    def test_knowledge_retrieval(self):
        """Testa recuperação de conhecimento."""
        knowledge = UnifiedKnowledgeSystem()
        knowledge.load_domain("paradigm_shift")
        
        agent = ParadigmArchitectAgent(
            memory_service=knowledge.get_memory_service("paradigm_shift")
        )
        
        result = agent.run("Como transformar paradigma de vendas?")
        assert result is not None
```

## Padrões de Deploy

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY templates/ ./templates/

EXPOSE 8000

CMD ["uvicorn", "unified_sales_framework.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: paradigm-architect-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: paradigm-architect-agent
  template:
    metadata:
      labels:
        app: paradigm-architect-agent
    spec:
      containers:
      - name: agent
        image: gcr.io/project/paradigm-architect-agent:latest
        ports:
        - containerPort: 8000
        env:
        - name: GOOGLE_CLOUD_PROJECT
          value: "your-project"
        - name: VERTEX_AI_LOCATION
          value: "us-central1"
```

## Padrões de Documentação

### Docstrings

```python
def create_paradigm_shift_strategy(
    current_paradigm: str,
    target_paradigm: str,
    market_context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Cria estratégia de mudança de paradigma.
    
    Args:
        current_paradigm: Paradigma atual do prospecto
        target_paradigm: Paradigma desejado
        market_context: Contexto do mercado
    
    Returns:
        Estratégia de transformação com:
        - leverage_points: Pontos de alavancagem
        - transformation_steps: Passos de transformação
        - success_metrics: Métricas de sucesso
    
    Raises:
        ValueError: Se paradigmas são incompatíveis
    
    Example:
        >>> strategy = create_paradigm_shift_strategy(
        ...     current_paradigm="feature_focused",
        ...     target_paradigm="outcome_focused",
        ...     market_context={"industry": "saas", "size": "enterprise"}
        ... )
        >>> print(strategy["leverage_points"])
        ["roi_demonstration", "case_studies", "peer_validation"]
    """
```

## Estrutura de Arquivos

### Agente Completo

```
src/agents/copywriting/paradigm_architect/
├── agent.py                 # Classe principal do agente
├── config/
│   ├── agent_config.yaml   # Configuração do agente
│   ├── tools_config.yaml   # Configuração de ferramentas
│   └── memory_config.yaml  # Configuração de memória
├── subagents/
│   ├── axiom_archaeologist/
│   │   ├── agent.py
│   │   └── config.yaml
│   └── concept_architect/
│       ├── agent.py
│       └── config.yaml
├── tools/
│   ├── paradigm_analysis_tool.py
│   └── concept_mapping_tool.py
├── knowledge/
│   ├── paradigm_shift_knowledge.md
│   └── persuasion_frameworks.md
└── tests/
    ├── test_agent.py
    ├── test_tools.py
    └── test_integration.py
```

## Convenções de Commit

### Formato de Commit

```
<tipo>(<escopo>): <descrição>

<corpo opcional>

<rodapé opcional>
```

### Tipos de Commit

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas de manutenção

### Exemplos

```
feat(agents): adiciona ParadigmArchitectAgent com 5 subagentes

- Implementa estrutura hierárquica completa
- Integra sistema de conhecimento especializado
- Adiciona ferramentas de análise de paradigma

Closes #123
```

```
fix(tools): corrige bug na ParadigmAnalysisTool

O threshold de similaridade estava muito alto, causando
poucos resultados na recuperação de conhecimento.

Fixes #456
```

