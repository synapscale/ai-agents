"""
Agente neurohook_ultra - Integração com ADK

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


class NeurohookUltraAgent(LlmAgent if ADK_AVAILABLE else object):
    """
    neurohook_ultra - Agente especializado migrado do multi-agent-ai-system.
    
    Categoria: agents_copywriters
    Especialização: neurological_hooks
    """
    
    def __init__(
        self,
        model_name: str = "gemini-1.5-pro",
        knowledge_base_path: str = "/home/ubuntu/multi-agent-ai-system-git",
        **kwargs
    ):
        # Carregar prompt original
        self.get_attr("prompt_file") = Path(__file__).parent / "prompt.txt"
        self.get_attr("instruction") = self._load_prompt()
        
        # Configurar especialização
        self.get_attr("specialization") = "neurological_hooks"
        self.get_attr("category") = "agents_copywriters"
        self.get_attr("agent_name") = "neurohook_ultra"
        
        # Inicializar agente ADK se disponível
        if ADK_AVAILABLE:
            super().__init__(
                model_name=model_name,
                instructions=self.get_attr("instruction"),
                **kwargs
            )
            
            # Integrar sistema de conhecimento
            self.get_attr("knowledge_toolset") = UnifiedKnowledgeToolset(knowledge_base_path)
        else:
            # Implementação simplificada
            self.get_attr("model_name") = model_name
            self.get_attr("instructions") = self.get_attr("instruction")
        
        # Carregar subagentes se existirem
        self.get_attr("sub_agents") = self._load_sub_agents()
        
        # Carregar configurações
        self.get_attr("config") = self._load_config()
        
        print(f"🤖 {self.get_attr(\'agent_name\', \'Unknown\')} inicializado com especialização: {self.get_attr(\'specialization\', \'general\')}")
    
    def _load_prompt(self) -> str:
        """Carrega o prompt original do agente."""
        try:
            if self.get_attr("prompt_file").exists():
                with open(self.get_attr("prompt_file"), 'r', encoding='utf-8') as f:
                    return f.read()
            return f"Você é {self.get_attr("agent_name", "Unknown")}, um agente especializado em {self.get_attr("specialization", "general")}."
        except Exception as e:
            print(f"⚠️ Erro carregando prompt: {e}")
            return f"Você é {self.get_attr("agent_name", "Unknown")}, um agente especializado."
    
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
        # Mapeamento básico baseado no nome
        specialization_map = {
            "1": "analysis",
            "1 copy": "synthesis", 
            "1 copy 2": "validation",
            "1 copy 3": "optimization",
            "1 copy 4": "implementation"
        }
        
        return specialization_map.get(sub_name, "general")
    
    def process_with_knowledge(self, query: str, context: Dict[str, Any] = None) -> str:
        """Processa query usando conhecimento especializado."""
        
        if not ADK_AVAILABLE:
            return f"{self.get_attr("agent_name", "Unknown")} processando: {query}"
        
        # Buscar conhecimento relevante
        if hasattr(self, "knowledge_toolset"):
            knowledge_tool = self.knowledge_toolset.get_tool_by_name("knowledge_retrieval")
            if knowledge_tool:
                relevant_knowledge = knowledge_tool.retrieve(
                    query=query,
                    agent_id=self.get_attr("agent_name"),
                    limit=3
                )
                
                # Processar com conhecimento
                enhanced_query = f"""
{self.get_attr("instruction", "")}

CONHECIMENTO RELEVANTE:
{relevant_knowledge}

QUERY: {query}
CONTEXTO: {context or 'Nenhum contexto adicional'}

Processe esta query usando seu conhecimento especializado e o conhecimento relevante fornecido.
"""
                
                return self.run(enhanced_query)
        
        # Fallback para processamento básico
        return self.run(f"{query}\n\nContexto: {context or 'Nenhum'}")
    
    def delegate_to_subagent(self, query: str, sub_agent_name: str) -> str:
        """Delega tarefa para um subagente específico."""
        
        # Encontrar subagente
        sub_agent = None
        for sa in self.get_attr("sub_agents"):
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
        
        if ADK_AVAILABLE and hasattr(self, "run"):
            return self.run(sub_prompt)
        else:
            return f"{sub_agent_name} processando: {query}"
    

    def get_attr(self, name: str, default=None):
        """Acessa atributo de forma segura."""
        return self.__dict__.get(name, default)
    def get_capabilities(self) -> Dict[str, Any]:
        """Retorna capacidades do agente."""
        return {
            "name": self.get_attr("agent_name"),
            "category": self.get_attr("category"),
            "specialization": self.get_attr("specialization"),
            "sub_agents": [sa['name'] for sa in self.get_attr("sub_agents")],
            "has_knowledge_base": (Path(__file__).parent / "knowledge_base").exists(),
            "config_files": list(Path(__file__).parent.glob("*.yaml")),
            "adk_integrated": ADK_AVAILABLE
        }


def create_agent(**kwargs) -> NeurohookUltraAgent:
    """Factory function para criar instância do agente."""
    return NeurohookUltraAgent(**kwargs)


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
    print(f"📚 Base de conhecimento: {capabilities['has_knowledge_base']}")
    print(f"🔧 Integração ADK: {capabilities['adk_integrated']}")
    
    # Teste básico
    if capabilities['adk_integrated']:
        result = agent.process_with_knowledge(
            "Teste de funcionamento do agente",
            {"context": "teste_migracao"}
        )
        print(f"\n📋 Resultado do teste:")
        print(result[:200] + "..." if len(result) > 200 else result)
