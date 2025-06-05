"""
Agente paradigm_architect - Integração com ADK (Versão Corrigida)

Agente migrado do multi-agent-ai-system para unified-sales-framework
com integração completa ao Agent Development Kit (ADK).
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any, List, Optional

# Adicionar ADK ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../src'))

try:
    from google.adk.agents.llm_agent import LlmAgent
    from google.adk.agents.loop_agent import LoopAgent
    from unified_sales_framework.knowledge import UnifiedKnowledgeToolset
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    print("⚠️ ADK não disponível, usando implementação simplificada")


class ParadigmArchitectAgent:
    """
    paradigm_architect - Agente especializado migrado do multi-agent-ai-system.
    
    Categoria: agents_copywriters
    Especialização: paradigm_transformation
    """
    
    def __init__(
        self,
        model_name: str = "gemini-1.5-pro",
        knowledge_base_path: str = "/home/ubuntu/multi-agent-ai-system-git",
        **kwargs
    ):
        # Inicializar atributos básicos
        self.model_name = model_name
        self.knowledge_base_path = knowledge_base_path
        
        # Carregar prompt original
        self.prompt_file = Path(__file__).parent / "prompt.txt"
        self.instruction = self._load_prompt()
        
        # Configurar especialização
        self.specialization = "paradigm_transformation"
        self.category = "agents_copywriters"
        self.agent_name = "paradigm_architect"
        
        # Inicializar agente ADK se disponível
        if ADK_AVAILABLE:
            try:
                # Criar instância do LlmAgent
                self.llm_agent = LlmAgent(
                    model_name=model_name,
                    instructions=self.instruction,
                    **kwargs
                )
                
                # Integrar sistema de conhecimento
                self.knowledge_toolset = UnifiedKnowledgeToolset(knowledge_base_path)
                self.adk_integrated = True
            except Exception as e:
                print(f"⚠️ Erro inicializando ADK: {e}")
                self.adk_integrated = False
        else:
            # Implementação simplificada
            self.instructions = self.instruction
            self.adk_integrated = False
        
        # Carregar subagentes se existirem
        self.sub_agents = self._load_sub_agents()
        
        # Carregar configurações
        self.config = self._load_config()
        
        print(f"🤖 {self.agent_name} inicializado com especialização: {self.specialization}")
        print(f"🔧 Integração ADK: {self.adk_integrated}")
        print(f"👥 Subagentes carregados: {len(self.sub_agents)}")
    
    def _load_prompt(self) -> str:
        """Carrega o prompt original do agente."""
        try:
            if self.prompt_file.exists():
                with open(self.prompt_file, 'r', encoding='utf-8') as f:
                    return f.read()
            return f"Você é {self.agent_name}, um agente especializado em {self.specialization}."
        except Exception as e:
            print(f"⚠️ Erro carregando prompt: {e}")
            return f"Você é {self.agent_name}, um agente especializado."
    
    def _load_sub_agents(self) -> List[Dict[str, Any]]:
        """Carrega subagentes se existirem."""
        sub_agents = []
        sub_agents_dir = Path(__file__).parent / "sub_agents"
        
        if sub_agents_dir.exists():
            for sub_dir in sub_agents_dir.iterdir():
                if sub_dir.is_dir():
                    prompt_file = sub_dir / "prompt.txt"
                    if prompt_file.exists():
                        try:
                            with open(prompt_file, 'r', encoding='utf-8') as f:
                                prompt = f.read()
                            
                            sub_agents.append({
                                "name": sub_dir.name,
                                "prompt": prompt,
                                "specialization": self._determine_sub_specialization(sub_dir.name)
                            })
                        except Exception as e:
                            print(f"⚠️ Erro carregando subagente {sub_dir.name}: {e}")
        
        return sub_agents
    
    def _load_config(self) -> Dict[str, Any]:
        """Carrega configurações do agente."""
        config = {}
        
        # Tentar carregar tools.yaml
        tools_file = Path(__file__).parent / "tools.yaml"
        if tools_file.exists():
            try:
                import yaml
                with open(tools_file, 'r', encoding='utf-8') as f:
                    config['tools'] = yaml.safe_load(f)
            except Exception as e:
                print(f"⚠️ Erro carregando tools.yaml: {e}")
        
        # Tentar carregar outros configs
        for config_file in Path(__file__).parent.glob("*.yaml"):
            if config_file.name != "tools.yaml":
                try:
                    import yaml
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config[config_file.stem] = yaml.safe_load(f)
                except Exception as e:
                    print(f"⚠️ Erro carregando {config_file.name}: {e}")
        
        return config
    
    def _determine_sub_specialization(self, sub_name: str) -> str:
        """Determina especialização de um subagente."""
        # Mapeamento específico para paradigm_architect
        specialization_map = {
            "AXIOM-ARCHAEOLOGIST": "axiom_discovery",
            "CONCEPT-ARCHITECT": "concept_creation", 
            "PARADIGMATIC-LINGUIST": "linguistic_persuasion",
            "LEGITIMACY-ENGINEER": "credibility_building",
            "TRANSDISCIPLINARY-SYNTHESIZER": "transdisciplinary_synthesis"
        }
        
        return specialization_map.get(sub_name, "general")
    
    def run(self, query: str) -> str:
        """Executa query no agente."""
        if self.adk_integrated and hasattr(self, 'llm_agent'):
            return self.llm_agent.run(query)
        else:
            # Simulação básica
            return f"[{self.agent_name}] Processando: {query[:100]}..."
    
    def process_with_knowledge(self, query: str, context: Dict[str, Any] = None) -> str:
        """Processa query usando conhecimento especializado."""
        
        if not self.adk_integrated:
            return f"{self.agent_name} processando: {query}"
        
        # Buscar conhecimento relevante
        if hasattr(self, 'knowledge_toolset'):
            try:
                knowledge_tool = self.knowledge_toolset.get_tool_by_name("knowledge_retrieval")
                if knowledge_tool:
                    relevant_knowledge = knowledge_tool.retrieve(
                        query=query,
                        agent_id=self.agent_name,
                        limit=3
                    )
                    
                    # Processar com conhecimento
                    enhanced_query = f"""
{self.instruction}

CONHECIMENTO RELEVANTE:
{relevant_knowledge}

QUERY: {query}
CONTEXTO: {context or 'Nenhum contexto adicional'}

Processe esta query usando seu conhecimento especializado e o conhecimento relevante fornecido.
"""
                    
                    return self.run(enhanced_query)
            except Exception as e:
                print(f"⚠️ Erro acessando conhecimento: {e}")
        
        # Fallback para processamento básico
        return self.run(f"{query}\n\nContexto: {context or 'Nenhum'}")
    
    def delegate_to_subagent(self, query: str, sub_agent_name: str) -> str:
        """Delega tarefa para um subagente específico."""
        
        # Encontrar subagente
        sub_agent = None
        for sa in self.sub_agents:
            if sa['name'] == sub_agent_name:
                sub_agent = sa
                break
        
        if not sub_agent:
            return f"Subagente {sub_agent_name} não encontrado"
        
        # Processar com prompt do subagente
        sub_prompt = f"""
{sub_agent['prompt']}

TAREFA DELEGADA: {query}

Processe esta tarefa usando sua especialização em {sub_agent['specialization']}.
"""
        
        return self.run(sub_prompt)
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Retorna capacidades do agente."""
        return {
            "name": self.agent_name,
            "category": self.category,
            "specialization": self.specialization,
            "sub_agents": [sa['name'] for sa in self.sub_agents],
            "has_knowledge_base": (Path(__file__).parent / "knowledge_base").exists(),
            "config_files": [f.name for f in Path(__file__).parent.glob("*.yaml")],
            "adk_integrated": self.adk_integrated,
            "model_name": self.model_name
        }


def create_agent(**kwargs) -> ParadigmArchitectAgent:
    """Factory function para criar instância do agente."""
    return ParadigmArchitectAgent(**kwargs)


# Exemplo de uso
if __name__ == "__main__":
    # Criar agente
    agent = create_agent()
    
    # Mostrar capacidades
    capabilities = agent.get_capabilities()
    print(f"\n🤖 AGENTE: {capabilities['name']}")
    print(f"📂 Categoria: {capabilities['category']}")
    print(f"🎯 Especialização: {capabilities['specialization']}")
    print(f"👥 Subagentes: {len(capabilities['sub_agents'])}")
    for sub_name in capabilities['sub_agents']:
        print(f"   - {sub_name}")
    print(f"📚 Base de conhecimento: {capabilities['has_knowledge_base']}")
    print(f"⚙️ Arquivos de config: {len(capabilities['config_files'])}")
    print(f"🔧 Integração ADK: {capabilities['adk_integrated']}")
    print(f"🤖 Modelo: {capabilities['model_name']}")
    
    # Teste básico
    print(f"\n📋 Teste básico:")
    result = agent.run("Teste de funcionamento do agente paradigm_architect")
    print(result)
    
    # Teste com subagente se disponível
    if capabilities['sub_agents']:
        print(f"\n👥 Teste de delegação para subagente:")
        sub_result = agent.delegate_to_subagent(
            "Identifique bloqueios mentais em vendas",
            capabilities['sub_agents'][0]
        )
        print(sub_result[:200] + "..." if len(sub_result) > 200 else sub_result)

