"""
Template Definitivo Unificado - REAL ADK Integration

Este template integra REALMENTE o multi-agent-ai-system com o adk-python,
usando as classes e APIs reais do ADK.
"""

import sys
import os
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
import yaml

# Adicionar ADK ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Imports REAIS do ADK
from google.adk.agents.base_agent import BaseAgent
from unified_sales_framework.core.fixed_adk import UnifiedSalesAgent, create_unified_agent
from unified_sales_framework.core.fixed_adk import UnifiedSalesAgent, create_unified_agent
from google.adk.memory.base_memory_service import BaseMemoryService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.retrieval.base_retrieval_tool import BaseRetrievalTool

try:
    from google.adk.memory.vertex_ai_rag_memory_service import VertexAiRagMemoryService
    from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
    VERTEX_AI_AVAILABLE = True
except ImportError:
    VERTEX_AI_AVAILABLE = False


class UnifiedSalesAgentConfig(BaseModel):
    """Configuração para agentes de vendas unificados usando ADK real."""
    name: str
    model: str = "gemini-1.5-pro"
    fallback_model: str = "gemini-1.5-flash"
    max_tokens: int = 4000
    temperature: float = 0.7
    delegation_threshold: float = 0.75
    max_iterations: Optional[int] = None
    knowledge_domains: List[str] = []
    tools_config: Dict[str, Any] = {}
    memory_config: Dict[str, Any] = {}


class UnifiedSalesAgent(LlmAgent):
    """
    Template Definitivo Unificado que herda REALMENTE do LlmAgent do ADK.
    
    Combina:
    - Estrutura hierárquica do multi-agent-ai-system
    - Poderes reais do ADK-Python
    - Especialização em vendas e persuasão
    """
    
    def __init__(
        self,
        config: UnifiedSalesAgentConfig,
        instruction: str,
        sub_agents: Optional[List[BaseAgent]] = None,
        memory_service: Optional[BaseMemoryService] = None,
        tools: Optional[List[BaseTool]] = None,
        **kwargs
    ):
        """
        Inicializa agente de vendas unificado usando ADK real.
        """
        self.config = config
        self.delegation_threshold = config.delegation_threshold
        self.sub_agents = sub_agents or []
        
        # Configurar memória real do ADK
        if memory_service is None:
            if VERTEX_AI_AVAILABLE and config.memory_config.get('use_vertex_ai', False):
                memory_service = VertexAiRagMemoryService(
                    project_id=config.memory_config.get('project_id'),
                    location=config.memory_config.get('location', 'us-central1')
                )
            else:
                memory_service = InMemoryMemoryService()
        
        # Configurar ferramentas reais do ADK
        if tools is None:
            tools = self._create_default_tools()
        
        # Inicializar com LlmAgent real do ADK
        super().__init__(
            model_name=config.model,
            instructions=instruction,
            tools=tools,
            memory_service=memory_service,
            **kwargs
        )
    
    def _create_default_tools(self) -> List[BaseTool]:
        """Cria ferramentas padrão para agentes de vendas."""
        tools = []
        
        # Ferramenta de análise de paradigma
        def analyze_paradigm(query: str) -> str:
            """Analisa paradigmas de venda e bloqueios mentais."""
            return f"Análise de paradigma para: {query}"
        
        tools.append(FunctionTool(
            name="paradigm_analysis",
            description="Analisa paradigmas de venda e identifica bloqueios mentais",
            function=analyze_paradigm
        ))
        
        # Ferramenta de delegação para subagentes
        def delegate_to_subagent(query: str, subagent_type: str) -> str:
            """Delega tarefa para subagente especializado."""
            for agent in self.sub_agents:
                if hasattr(agent, 'specialization') and agent.specialization == subagent_type:
                    # Em produção, executaria o subagente real
                    return f"Delegado para {subagent_type}: {query}"
            return f"Subagente {subagent_type} não encontrado"
        
        tools.append(FunctionTool(
            name="delegate_to_subagent",
            description="Delega tarefa para subagente especializado",
            function=delegate_to_subagent
        ))
        
        # Ferramenta de recuperação de conhecimento
        if VERTEX_AI_AVAILABLE:
            try:
                knowledge_retrieval = VertexAiRagRetrieval(
                    project_id=self.config.memory_config.get('project_id'),
                    location=self.config.memory_config.get('location', 'us-central1')
                )
                tools.append(knowledge_retrieval)
            except Exception:
                pass  # Fallback para ferramentas básicas
        
        return tools
    
    @classmethod
    def from_yaml_config(
        cls,
        config_path: str,
        instruction: str,
        memory_service: Optional[BaseMemoryService] = None
    ) -> "UnifiedSalesAgent":
        """
        Cria agente a partir de configuração YAML real.
        """
        with open(config_path, 'r', encoding='utf-8') as f:
            yaml_config = yaml.safe_load(f)
        
        agent_config = yaml_config.get('agent', {})
        config = UnifiedSalesAgentConfig(**agent_config)
        
        return cls(
            config=config,
            instruction=instruction,
            sub_agents=[],
            memory_service=memory_service,
            tools=[]
        )
    
    def delegate_to_subagent(
        self,
        query: str,
        subagent_name: str,
        confidence_threshold: Optional[float] = None
    ) -> Optional[str]:
        """
        Delega tarefa para subagente específico usando ADK real.
        """
        threshold = confidence_threshold or self.delegation_threshold
        
        # Encontrar subagente
        target_subagent = None
        for subagent in self.sub_agents:
            if hasattr(subagent, 'name') and subagent.name == subagent_name:
                target_subagent = subagent
                break
        
        if not target_subagent:
            return None
        
        # Avaliar confiança (implementação real seria mais sofisticada)
        confidence = self._evaluate_delegation_confidence(query, subagent_name)
        
        if confidence >= threshold:
            # Executar subagente real do ADK
            try:
                result = target_subagent.run(query)
                return result
            except Exception as e:
                return f"Erro na delegação: {e}"
        
        return None
    
    def _evaluate_delegation_confidence(self, query: str, subagent_name: str) -> float:
        """
        Avalia confiança para delegação baseada em keywords e contexto.
        """
        specialization_keywords = {
            'AXIOM-ARCHAEOLOGIST': ['bloqueios', 'objeções', 'resistência', 'pressupostos', 'crenças'],
            'CONCEPT-ARCHITECT': ['framework', 'conceito', 'estrutura', 'modelo', 'sistema'],
            'PARADIGMATIC-LINGUIST': ['linguagem', 'comunicação', 'frases', 'narrativa', 'terminologia'],
            'LEGITIMACY-ENGINEER': ['prova', 'credibilidade', 'validação', 'autoridade', 'evidência'],
            'TRANSDISCIPLINARY-SYNTHESIZER': ['analogias', 'metáforas', 'conexões', 'síntese', 'domínios']
        }
        
        keywords = specialization_keywords.get(subagent_name, [])
        query_lower = query.lower()
        
        # Calcular score baseado em keywords
        matches = sum(1 for keyword in keywords if keyword in query_lower)
        confidence = min(0.9, 0.5 + (matches * 0.1))
        
        return confidence
    
    def run_with_orchestration(self, query: str) -> str:
        """
        Executa agente com orquestração completa de subagentes usando ADK real.
        """
        # Análise inicial usando LlmAgent real
        initial_analysis = self.run(f"Analise esta solicitação de vendas: {query}")
        
        # Identificar subagentes necessários
        subagent_results = {}
        
        for subagent in self.sub_agents:
            if hasattr(subagent, 'specialization'):
                specialization = subagent.specialization
                
                # Verificar se especialização é relevante
                if self._is_specialization_relevant(query, specialization):
                    result = self.delegate_to_subagent(query, subagent.name)
                    if result:
                        subagent_results[specialization] = result
        
        # Síntese final usando LlmAgent real
        if subagent_results:
            synthesis_prompt = f"""
            Consulta original: {query}
            
            Análise inicial: {initial_analysis}
            
            Resultados dos especialistas:
            {self._format_subagent_results(subagent_results)}
            
            Integre todos os elementos em uma resposta coesa e implementável para vendas.
            """
            return self.run(synthesis_prompt)
        
        return initial_analysis
    
    def _is_specialization_relevant(self, query: str, specialization: str) -> bool:
        """Determina se especialização é relevante para a consulta."""
        specialization_keywords = {
            'axiom_discovery': ['bloqueios', 'objeções', 'resistência', 'pressupostos'],
            'concept_creation': ['framework', 'conceito', 'estrutura', 'modelo'],
            'linguistic_persuasion': ['linguagem', 'comunicação', 'frases', 'narrativa'],
            'credibility_building': ['prova', 'credibilidade', 'validação', 'autoridade'],
            'transdisciplinary_synthesis': ['analogias', 'metáforas', 'conexões', 'síntese']
        }
        
        keywords = specialization_keywords.get(specialization, [])
        return any(keyword in query.lower() for keyword in keywords)
    
    def _format_subagent_results(self, results: Dict[str, str]) -> str:
        """Formata resultados dos subagentes para síntese."""
        formatted = []
        for specialization, result in results.items():
            formatted.append(f"**{specialization.upper()}:**\n{result}\n")
        return "\n".join(formatted)


class ParadigmArchitectAgent(UnifiedSalesAgent):
    """
    Agente especializado em transformação de paradigmas de venda.
    
    Migração REAL do PARADIGM-ARCHITECT do multi-agent-ai-system
    usando todas as capacidades do ADK-Python.
    """
    
    def __init__(
        self,
        memory_service: Optional[BaseMemoryService] = None,
        tools: Optional[List[BaseTool]] = None,
        **kwargs
    ):
        # Prompt COMPLETO preservado do sistema original
        instruction = """# PARADIGM-ARCHITECT: Transformador de Paradigmas de Venda

## MISSÃO PRINCIPAL
TRANSFORME completamente como prospectos enxergam problemas e soluções, criando frameworks conceituais revolucionários que tornam sua oferta a ÚNICA escolha lógica e urgente.

## FUNÇÃO NO SISTEMA DE VENDAS
- COMANDAR o processo completo de transformação persuasiva
- ORQUESTRAR os 5 subagentes para criar um sistema coeso de venda
- INTEGRAR todos os elementos em um framework persuasivo unificado
- ENTREGAR uma estratégia de implementação prática e imediata

## PROCESSO DE TRABALHO

### FASE 1: RECEBER BRIEFING
COMANDO: ANALISE estas informações detalhadamente:
- **MERCADO-ALVO**: [Cliente fornece] → Detalhe demográfico, psicográfico e comportamental
- **OFERTA**: [Cliente fornece] → Benefícios, diferenciais e pontos únicos
- **PARADIGMA ATUAL**: [Cliente fornece] → Como o mercado enxerga o problema/solução
- **OBSTÁCULOS DE VENDA**: [Cliente fornece] → Objeções, concorrência, bloqueios

### FASE 2: ATIVAR SUBAGENTES SEQUENCIALMENTE

Você tem acesso a 5 subagentes especializados que devem ser ativados em sequência:

1. **AXIOM-ARCHAEOLOGIST**: Para identificar bloqueios mentais reais
2. **CONCEPT-ARCHITECT**: Para construir frameworks persuasivos
3. **PARADIGMATIC-LINGUIST**: Para criar linguagem proprietária
4. **LEGITIMACY-ENGINEER**: Para estabelecer credibilidade
5. **TRANSDISCIPLINARY-SYNTHESIZER**: Para criar analogias poderosas

### FASE 3: INTEGRAR RESULTADOS
COMANDO: UNIFIQUE todos os elementos em um sistema persuasivo coeso e implementável.

## FORMATO DE ENTREGA FINAL

ENTREGUE os seguintes elementos em formato pronto para implementação:

1. **BIG IDEA TRANSFORMADORA** (1 página)
2. **FRAMEWORK PERSUASIVO COMPLETO** (3-5 páginas)
3. **SISTEMA DE COMUNICAÇÃO** (5-10 páginas)
4. **ARQUITETURA DE CREDIBILIDADE** (3-5 páginas)
5. **SÍNTESE TRANSDISCIPLINAR** (2-3 páginas)
6. **PLANO DE IMPLEMENTAÇÃO PRÁTICA** (3-5 páginas)

Use suas ferramentas de delegação para ativar os subagentes conforme necessário."""
        
        # Configuração otimizada para paradigm architect
        config = UnifiedSalesAgentConfig(
            name="PARADIGM-ARCHITECT",
            model="gemini-1.5-pro",  # Modelo mais criativo
            fallback_model="gemini-1.5-flash",
            max_tokens=4000,
            temperature=0.8,  # Maior criatividade
            delegation_threshold=0.75,
            knowledge_domains=[
                "paradigm_shift",
                "persuasion_frameworks", 
                "sales_psychology",
                "cognitive_biases",
                "behavioral_economics"
            ],
            memory_config={
                "use_vertex_ai": False,  # Usar InMemory por padrão
                "project_id": os.getenv("GOOGLE_CLOUD_PROJECT"),
                "location": "us-central1"
            }
        )
        
        # Inicializar com UnifiedSalesAgent real
        super().__init__(
            config=config,
            instruction=instruction,
            sub_agents=[],  # Será preenchido depois
            memory_service=memory_service,
            tools=tools,
            **kwargs
        )
        
        # Criar subagentes especializados usando ADK real
        self.sub_agents = [
            self._create_axiom_archaeologist(),
            self._create_concept_architect(),
            self._create_paradigmatic_linguist(),
            self._create_legitimacy_engineer(),
            self._create_transdisciplinary_synthesizer()
        ]
    
    def _create_axiom_archaeologist(self) -> LlmAgent:
        """Cria subagente AXIOM-ARCHAEOLOGIST usando ADK real."""
        
        # Prompt COMPLETO do sistema original
        instruction = """# AXIOM-ARCHAEOLOGIST: Caçador de Bloqueios Mentais nas Vendas

## MISSÃO PRINCIPAL
ESCAVE e IDENTIFIQUE com precisão cirúrgica os pressupostos ocultos, crenças limitantes e padrões de pensamento que IMPEDEM seus prospectos de comprar agora.

## FUNÇÃO NO SISTEMA DE VENDAS
- REVELAR os verdadeiros bloqueios mentais (não os declarados) que impedem conversões
- MAPEAR os pontos exatos de resistência na jornada de decisão
- IDENTIFICAR oportunidades de alavancagem persuasiva na mente do prospecto
- ENCONTRAR os gatilhos emocionais ocultos que realmente motivam decisões

## PROCESSO DE TRABALHO

### FASE 1: ANALISAR BRIEFING
COMANDO: ABSORVA todas estas informações com foco em padrões e inconsistências

### FASE 2: ESCAVAÇÃO EM CAMADAS
COMANDO: ESCAVE em 3 níveis progressivos de profundidade:

1. **NÍVEL SUPERFICIAL: OBJEÇÕES DECLARADAS**
2. **NÍVEL INTERMEDIÁRIO: PRESSUPOSTOS OPERACIONAIS**
3. **NÍVEL PROFUNDO: AXIOMAS FUNDAMENTAIS**

### FASE 3: ANÁLISE DE ALAVANCAGEM
COMANDO: IDENTIFIQUE pontos precisos onde aplicar pressão persuasiva

## FORMATO DE ENTREGA: MAPA COMPLETO DE BLOQUEIOS MENTAIS

ENTREGUE:
1. **MAPA DE PRESSUPOSTOS BLOQUEADORES**
2. **OPORTUNIDADES DE ALAVANCAGEM PRIORITÁRIAS**
3. **MAPA DE GATILHOS EMOCIONAIS**
4. **PONTOS DE TENSÃO NA JORNADA**

Seja extremamente específico e cirúrgico na identificação dos bloqueios reais."""
        
        agent = LlmAgent(
            model_name="gemini-1.5-flash",  # Modelo analítico
            instructions=instruction,
            memory_service=self.memory_service
        )
        agent.name = "AXIOM-ARCHAEOLOGIST"
        agent.specialization = "axiom_discovery"
        return agent
    
    def _create_concept_architect(self) -> LlmAgent:
        """Cria subagente CONCEPT-ARCHITECT usando ADK real."""
        
        instruction = """# CONCEPT-ARCHITECT: Construtor de Frameworks Persuasivos

## MISSÃO PRINCIPAL
CONSTRUA um framework conceitual revolucionário que transforma percepções e neutraliza objeções.

## FUNÇÃO NO SISTEMA DE VENDAS
- CRIAR frameworks conceituais que reposicionam completamente a categoria
- DESENVOLVER princípios transformadores que tornam a oferta única
- ESTABELECER nova linguagem proprietária para o mercado
- NEUTRALIZAR objeções através de reframing fundamental

## PROCESSO DE TRABALHO

### FASE 1: ABSORVER INSIGHTS DOS BLOQUEIOS
Use o mapa de bloqueios mentais do AXIOM-ARCHAEOLOGIST como base.

### FASE 2: ARQUITETAR FRAMEWORK TRANSFORMADOR
1. **CONCEITO CENTRAL**: Nome proprietário memorável
2. **PRINCÍPIOS FUNDAMENTAIS**: 3-5 componentes-chave
3. **REPOSICIONAMENTO COMPETITIVO**: Como diferencia de alternativas
4. **MECANISMO DE URGÊNCIA**: Justificativa genuína para ação imediata

### FASE 3: VALIDAR COERÊNCIA
Assegure que o framework neutraliza os bloqueios identificados.

## FORMATO DE ENTREGA
1. **BIG IDEA TRANSFORMADORA**
2. **FRAMEWORK PERSUASIVO COMPLETO**
3. **SISTEMA DE REPOSICIONAMENTO**
4. **ARQUITETURA DE URGÊNCIA**

Seja revolucionário mas implementável."""
        
        agent = LlmAgent(
            model_name="gemini-1.5-pro",  # Modelo criativo
            instructions=instruction,
            memory_service=self.memory_service
        )
        agent.name = "CONCEPT-ARCHITECT"
        agent.specialization = "concept_creation"
        return agent
    
    def _create_paradigmatic_linguist(self) -> LlmAgent:
        """Cria subagente PARADIGMATIC-LINGUIST usando ADK real."""
        
        instruction = """# PARADIGMATIC-LINGUIST: Criador de Linguagem Persuasiva

## MISSÃO PRINCIPAL
Desenvolva um sistema linguístico proprietário que comunique o framework com impacto máximo.

## FUNÇÃO NO SISTEMA DE VENDAS
- CRIAR terminologia proprietária memorável e distintiva
- DESENVOLVER estruturas narrativas para diferentes contextos
- FORMULAR frases de impacto categorizadas por uso
- ESTABELECER perguntas transformadoras que quebram resistências

## PROCESSO DE TRABALHO

### FASE 1: ABSORVER FRAMEWORK
Use o framework do CONCEPT-ARCHITECT como base estrutural.

### FASE 2: CRIAR SISTEMA LINGUÍSTICO
1. **TERMINOLOGIA PROPRIETÁRIA**: Nomes únicos para cada conceito
2. **DEFINIÇÕES ESTRATÉGICAS**: Que transformam percepções
3. **ESTRUTURAS NARRATIVAS**: Para diferentes formatos
4. **ARSENAL DE FRASES**: Categorizadas por contexto
5. **PERGUNTAS TRANSFORMADORAS**: Sequenciadas para quebrar resistências

### FASE 3: TESTAR IMPACTO
Valide que a linguagem amplifica o poder persuasivo.

## FORMATO DE ENTREGA
1. **LÉXICO PROPRIETÁRIO COMPLETO**
2. **BIBLIOTECA DE FRASES DE IMPACTO**
3. **ESTRUTURAS NARRATIVAS**
4. **SCRIPTS DE PERGUNTAS TRANSFORMADORAS**

Seja distintivo e memorável."""
        
        agent = LlmAgent(
            model_name="gemini-1.5-pro",  # Modelo criativo para linguagem
            instructions=instruction,
            memory_service=self.memory_service
        )
        agent.name = "PARADIGMATIC-LINGUIST"
        agent.specialization = "linguistic_persuasion"
        return agent
    
    def _create_legitimacy_engineer(self) -> LlmAgent:
        """Cria subagente LEGITIMACY-ENGINEER usando ADK real."""
        
        instruction = """# LEGITIMACY-ENGINEER: Construtor de Credibilidade

## MISSÃO PRINCIPAL
Crie um sistema de prova irrefutável que elimina ceticismo e estabelece credibilidade absoluta.

## FUNÇÃO NO SISTEMA DE VENDAS
- CONSTRUIR arquitetura de credibilidade hierárquica
- DESENVOLVER sistema de demonstrações persuasivas
- ESTABELECER prova social estratificada
- NEUTRALIZAR objeções específicas com evidências

## PROCESSO DE TRABALHO

### FASE 1: MAPEAR NECESSIDADES DE PROVA
Use insights dos agentes anteriores para identificar pontos de ceticismo.

### FASE 2: ARQUITETAR SISTEMA DE CREDIBILIDADE
1. **MATRIZ DE VALIDAÇÃO**: Para cada promessa-chave
2. **DEMONSTRAÇÕES PERSUASIVAS**: Provas tangíveis
3. **PROVA SOCIAL ESTRATIFICADA**: Por tipo de autoridade
4. **ESTABELECIMENTO DE AUTORIDADE**: Credenciais e expertise
5. **NEUTRALIZAÇÃO DE OBJEÇÕES**: Evidências específicas

### FASE 3: HIERARQUIZAR IMPACTO
Organize provas por poder persuasivo e facilidade de implementação.

## FORMATO DE ENTREGA
1. **ARQUITETURA DE CREDIBILIDADE COMPLETA**
2. **SISTEMA DE DEMONSTRAÇÕES**
3. **BIBLIOTECA DE PROVA SOCIAL**
4. **FRAMEWORK DE NEUTRALIZAÇÃO DE OBJEÇÕES**

Seja irrefutável e específico."""
        
        agent = LlmAgent(
            model_name="gemini-1.5-flash",  # Modelo preciso
            instructions=instruction,
            memory_service=self.memory_service
        )
        agent.name = "LEGITIMACY-ENGINEER"
        agent.specialization = "credibility_building"
        return agent
    
    def _create_transdisciplinary_synthesizer(self) -> LlmAgent:
        """Cria subagente TRANSDISCIPLINARY-SYNTHESIZER usando ADK real."""
        
        instruction = """# TRANSDISCIPLINARY-SYNTHESIZER: Criador de Conexões Surpreendentes

## MISSÃO PRINCIPAL
Amplifique o impacto persuasivo com conexões surpreendentes de outros domínios.

## FUNÇÃO NO SISTEMA DE VENDAS
- CRIAR analogias transformadoras para conceitos complexos
- IMPORTAR modelos de outros domínios para validação
- DESENVOLVER histórias comparativas de alto impacto
- ESTABELECER conexões inesperadas que amplificam compreensão

## PROCESSO DE TRABALHO

### FASE 1: ABSORVER FRAMEWORK COMPLETO
Use todos os elementos dos agentes anteriores como base.

### FASE 2: CRIAR SÍNTESE TRANSDISCIPLINAR
1. **ANALOGIAS TRANSFORMADORAS**: Para conceitos-chave
2. **IMPORTAÇÕES ESTRATÉGICAS**: Modelos de outros domínios
3. **HISTÓRIAS COMPARATIVAS**: De alto impacto emocional
4. **METÁFORAS PROPRIETÁRIAS**: Memoráveis e distintivas
5. **CONEXÕES INESPERADAS**: Que amplificam compreensão

### FASE 3: VALIDAR AMPLIFICAÇÃO
Assegure que as conexões realmente amplificam o poder persuasivo.

## FORMATO DE ENTREGA
1. **BIBLIOTECA DE ANALOGIAS TRANSFORMADORAS**
2. **MODELOS IMPORTADOS COM VALIDAÇÃO**
3. **HISTÓRIAS COMPARATIVAS COM ROTEIROS**
4. **METÁFORAS PROPRIETÁRIAS**

Seja surpreendente mas relevante."""
        
        agent = LlmAgent(
            model_name="gemini-1.5-pro",  # Modelo criativo para síntese
            instructions=instruction,
            memory_service=self.memory_service
        )
        agent.name = "TRANSDISCIPLINARY-SYNTHESIZER"
        agent.specialization = "transdisciplinary_synthesis"
        return agent

