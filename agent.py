# /workspaces/ai-agents/agent.py
"""
Ponto de entrada principal para ADK Web Interface
Integra com os agentes existentes do projeto ai-agents
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any, Optional
import json

# Adicionar paths necessários
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

try:
    # Importar agentes existentes
    from agents.apis.APIUnifyMaster.agent import ApiunifymasterAgent
    from src.google.adk.agents.llm_agent import LlmAgent
    ADK_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Importação ADK falhou: {e}")
    ADK_AVAILABLE = False

class MainAgent:
    """Agente principal para interface web do ADK"""
    
    def __init__(self):
        self.name = "AI-Agents System"
        self.description = "Sistema multi-agente para APIs e analytics"
        
        # Inicializar agentes disponíveis
        self.agents = {}
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Inicializa os agentes disponíveis"""
        try:
            # APIUnifyMaster
            self.agents['api_unify'] = ApiunifymasterAgent()
            print("✅ APIUnifyMaster carregado")
        except Exception as e:
            print(f"⚠️ Erro carregando APIUnifyMaster: {e}")
        
        # Adicionar outros agentes conforme necessário
        # self.agents['hotmart'] = HotmartAgent()
        # self.agents['kiwify'] = KiwifyAgent()
    
    def process(self, query: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Processa uma query usando os agentes disponíveis"""
        
        if not query:
            return self.get_status()
        
        # Determinar qual agente usar baseado na query
        if 'api' in query.lower() or 'integr' in query.lower():
            if 'api_unify' in self.agents:
                try:
                    return self.agents['api_unify'].process_with_knowledge(query, context)
                except Exception as e:
                    return f"Erro processando com APIUnifyMaster: {e}"
        
        # Resposta padrão
        return f"""
Sistema AI-Agents processando: {query}

Agentes disponíveis:
{', '.join(self.agents.keys())}

Para usar um agente específico, inclua palavras-chave relacionadas na sua query.
        """
    
    def get_status(self) -> str:
        """Retorna status do sistema"""
        status = {
            "system": "AI-Agents Multi-Agent System",
            "status": "operational",
            "agents_loaded": list(self.agents.keys()),
            "adk_integration": ADK_AVAILABLE,
            "capabilities": [
                "API Integration (APIUnifyMaster)",
                "Knowledge Processing",
                "Multi-Agent Coordination"
            ]
        }
        
        return json.dumps(status, indent=2)

# Instância global
main_agent = MainAgent()

# Funções de interface para ADK
def agent_main(input_data: str = "") -> str:
    """Interface principal para ADK"""
    try:
        return main_agent.process(input_data)
    except Exception as e:
        return f"Erro no agente principal: {e}"

async def main(request: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Interface async para ADK"""
    try:
        if request:
            query = request.get('query', '')
            context = request.get('context', {})
            result = main_agent.process(query, context)
        else:
            result = main_agent.get_status()
        
        return {"result": result, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "error"}

if __name__ == "__main__":
    print("🚀 AI-Agents System - ADK Interface")
    print("=" * 50)
    print(main_agent.get_status())
    print("\n💡 Para usar: adk web .")
    print("🌐 Interface: http://localhost:8000")