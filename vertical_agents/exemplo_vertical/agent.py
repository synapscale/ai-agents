"""
Agente Vertical: exemplo_vertical
Especialização: exemplo
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Any

# Adicionar src ao path
current_dir = Path(__file__).parent
framework_root = current_dir.parent.parent
src_path = framework_root / "src"
sys.path.insert(0, str(src_path))

try:
    from google.adk.agents.llm_agent import LlmAgent
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False

class ExemploVerticalVerticalAgent:
    """
    Agente vertical especializado em exemplo
    """
    
    def __init__(self):
        self.name = "exemplo_vertical"
        self.specialization = "exemplo"
        self.agent_dir = Path(__file__).parent
        
        # Keywords de domínio
        self.domain_keywords = ['example_tool']
        
        # Carregar prompt vertical
        self.prompt = self._load_vertical_prompt()
        
        # Carregar conhecimento especializado
        self.specialized_knowledge = self._load_specialized_knowledge()
        
        # Ferramentas especializadas
        self.tools = self._load_specialized_tools()
        
        # Inicializar agente ADK
        self.adk_agent = None
        if ADK_AVAILABLE:
            try:
                self.adk_agent = self._init_adk_agent()
            except Exception as e:
                print(f"⚠️ Erro inicializando ADK: {e}")
        
        print(f"🎯 Agente Vertical {self.name} inicializado")
        print(f"🔧 Ferramentas: {len(self.tools)} especializadas")
    
    def _load_vertical_prompt(self) -> str:
        """Carrega prompt vertical"""
        prompt_file = self.agent_dir / "prompt.txt"
        if prompt_file.exists():
            return prompt_file.read_text(encoding='utf-8')
        return "Prompt vertical não encontrado"
    
    def _load_specialized_knowledge(self) -> Dict[str, str]:
        """Carrega conhecimento especializado"""
        knowledge = {}
        knowledge_dir = self.agent_dir / "knowledge" / "specialized_docs"
        
        if knowledge_dir.exists():
            for file_path in knowledge_dir.rglob("*.md"):
                relative_path = file_path.relative_to(knowledge_dir)
                knowledge[str(relative_path)] = file_path.read_text(encoding='utf-8')
        
        return knowledge
    
    def _load_specialized_tools(self) -> List[str]:
        """Carrega ferramentas especializadas"""
        return [
            f"{self.specialization}_analyzer",
            f"{self.specialization}_optimizer", 
            f"{self.specialization}_validator"
        ]
    
    def _init_adk_agent(self):
        """Inicializa agente ADK"""
        try:
            return LlmAgent(
                name=self.name,
                model_name="gemini-1.5-pro",
                instructions=self.prompt
            )
        except:
            return None
    
    def is_in_domain(self, query: str) -> bool:
        """
        Verifica se a query está no domínio do agente
        """
        query_lower = query.lower()
        return any(keyword.lower() in query_lower for keyword in self.domain_keywords)
    
    def process_vertical_query(self, query: str) -> str:
        """
        Processa query vertical especializada
        """
        if not self.is_in_domain(query):
            return self._redirect_query(query)
        
        # Processar com conhecimento especializado
        if self.adk_agent:
            try:
                # Usar ADK se disponível
                return f"[{self.name}] Processamento vertical ADK: {query}"
            except Exception as e:
                print(f"Erro ADK: {e}")
        
        # Fallback simplificado
        return f"[{self.name}] Análise vertical de {self.specialization}: {query}"
    
    def _redirect_query(self, query: str) -> str:
        """
        Redireciona query para especialista apropriado
        """
        return f"❌ Query '{query}' está fora do domínio de {self.specialization}. Redirecionando para especialista apropriado."
    
    def get_vertical_info(self) -> Dict[str, Any]:
        """
        Retorna informações do agente vertical
        """
        return {
            "name": self.name,
            "specialization": self.specialization,
            "domain_keywords": self.domain_keywords,
            "specialized_tools": len(self.tools),
            "vertical_purity": True,
            "cross_pollution": False
        }

def main():
    """Teste do agente vertical"""
    agent = ExemploVerticalVerticalAgent()
    
    # Informações
    info = agent.get_vertical_info()
    print(f"🎯 AGENTE VERTICAL: {info['name']}")
    print(f"📋 Especialização: {info['specialization']}")
    print(f"🔑 Keywords: {', '.join(info['domain_keywords'])}")
    print(f"🔧 Ferramentas: {info['specialized_tools']} especializadas")
    print(f"🎯 Pureza Vertical: {info['vertical_purity']}")
    print(f"🚫 Poluição Cruzada: {info['cross_pollution']}")
    
    # Testes de domínio
    test_queries = [
        "Como otimizar conversões?",
        "Qual a melhor API de pagamento?", 
        "Como criar uma metáfora eficaz?",
        "Estratégias de retenção de clientes"
    ]
    
    print(f"🧪 TESTES DE DOMÍNIO:")
    for query in test_queries:
        in_domain = agent.is_in_domain(query)
        status = "✅" if in_domain else "❌"
        print(f"   {status} '{query}' - {'No domínio' if in_domain else 'Fora do domínio'}")

if __name__ == "__main__":
    main()
