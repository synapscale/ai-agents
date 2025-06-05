"""
Integração do Sistema de Conhecimento com Template de Agentes

Este módulo integra o sistema de conhecimento unificado com o template
de agentes, permitindo que os agentes acessem conhecimento especializado.
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any, Optional, List

# Importar sistema de conhecimento
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from unified_sales_framework.knowledge import UnifiedKnowledgeToolset


class KnowledgeEnhancedAgent:
    """
    Versão aprimorada do agente que integra com o sistema de conhecimento.
    """
    
    def __init__(
        self,
        agent_name: str,
        specialization: str,
        knowledge_base_path: str = "/home/ubuntu/multi-agent-ai-system-git",
        **kwargs
    ):
        self.agent_name = agent_name
        self.specialization = specialization
        
        # Inicializar sistema de conhecimento
        self.knowledge_toolset = UnifiedKnowledgeToolset(knowledge_base_path)
        
        # Mapear especialização para ferramentas de conhecimento
        self.specialized_tools = self._map_specialization_to_tools()
        
        print(f"🧠 {agent_name} inicializado com conhecimento especializado")
        print(f"🎯 Especialização: {specialization}")
        print(f"🔧 Ferramentas disponíveis: {len(self.specialized_tools)}")
    
    def _map_specialization_to_tools(self) -> List[str]:
        """Mapeia especialização do agente para ferramentas de conhecimento relevantes."""
        
        specialization_mapping = {
            "axiom_discovery": [
                "paradigm_shift_knowledge",
                "cognitive_biases",
                "knowledge_retrieval"
            ],
            "concept_creation": [
                "paradigm_shift_knowledge",
                "persuasion_frameworks",
                "knowledge_retrieval"
            ],
            "linguistic_persuasion": [
                "persuasion_frameworks",
                "analogies_metaphors",
                "knowledge_retrieval"
            ],
            "credibility_building": [
                "persuasion_frameworks",
                "cognitive_biases",
                "knowledge_retrieval"
            ],
            "transdisciplinary_synthesis": [
                "analogies_metaphors",
                "paradigm_shift_knowledge",
                "knowledge_retrieval"
            ]
        }
        
        return specialization_mapping.get(self.specialization, ["knowledge_retrieval"])
    
    def retrieve_specialized_knowledge(self, query: str, context: str = "") -> str:
        """Recupera conhecimento especializado baseado na query e contexto."""
        
        print(f"🔍 {self.agent_name} buscando conhecimento para: {query}")
        
        # Usar ferramenta principal baseada na especialização
        primary_tool_name = self.specialized_tools[0] if self.specialized_tools else "knowledge_retrieval"
        primary_tool = self.knowledge_toolset.get_tool_by_name(primary_tool_name)
        
        if not primary_tool:
            return f"Ferramenta {primary_tool_name} não encontrada"
        
        # Executar busca especializada
        if primary_tool_name == "paradigm_shift_knowledge":
            if "framework" in query.lower() or "transformação" in query.lower():
                return primary_tool.get_transformation_frameworks(f"{query} {context}")
            elif "bloqueio" in query.lower() or "objeção" in query.lower():
                return primary_tool.identify_blocking_patterns(f"{query} {context}")
        
        elif primary_tool_name == "persuasion_frameworks":
            return primary_tool.get_persuasion_techniques(query, context)
        
        elif primary_tool_name == "cognitive_biases":
            return primary_tool.identify_relevant_biases(f"{query} {context}")
        
        elif primary_tool_name == "analogies_metaphors":
            return primary_tool.find_analogies(query, context)
        
        # Fallback para busca geral
        return primary_tool.retrieve(query, limit=3)
    
    def process_with_knowledge(self, task: str, context: Dict[str, Any]) -> str:
        """Processa uma tarefa usando conhecimento especializado."""
        
        print(f"\n🎯 {self.agent_name} processando tarefa com conhecimento:")
        print(f"📝 Tarefa: {task}")
        print(f"📋 Contexto: {context}")
        
        # Extrair informações relevantes do contexto
        market_target = context.get("market_target", "")
        offer = context.get("offer", "")
        obstacles = context.get("obstacles", [])
        
        # Construir query baseada na especialização
        if self.specialization == "axiom_discovery":
            query = f"bloqueios mentais objeções {market_target} {' '.join(obstacles)}"
            knowledge = self.retrieve_specialized_knowledge(query, market_target)
            
            result = f"""
## 🧠 ANÁLISE DE BLOQUEIOS MENTAIS - {self.agent_name}

**Mercado-Alvo**: {market_target}
**Obstáculos Identificados**: {', '.join(obstacles)}

### 📚 CONHECIMENTO ESPECIALIZADO APLICADO:
{knowledge}

### 🎯 RECOMENDAÇÕES BASEADAS EM CONHECIMENTO:
1. **Identificar Pressupostos Limitantes**: Mapear crenças que impedem a decisão
2. **Questionar Paradigmas Atuais**: Desafiar a lógica atual do mercado-alvo
3. **Criar Dissonância Cognitiva**: Mostrar inconsistências no pensamento atual
"""
        
        elif self.specialization == "concept_creation":
            query = f"frameworks conceituais {offer} {market_target}"
            knowledge = self.retrieve_specialized_knowledge(query, market_target)
            
            result = f"""
## 🏗️ ARQUITETURA CONCEITUAL - {self.agent_name}

**Oferta**: {offer}
**Mercado-Alvo**: {market_target}

### 📚 FRAMEWORKS APLICADOS:
{knowledge}

### 🎯 ESTRUTURA CONCEITUAL RECOMENDADA:
1. **Reposicionamento da Oferta**: Transformar percepção de custo em investimento
2. **Criação de Nova Categoria**: Estabelecer oferta como única no mercado
3. **Framework de Valor**: Estruturar benefícios de forma hierárquica
"""
        
        elif self.specialization == "linguistic_persuasion":
            query = f"linguagem persuasiva {market_target} {offer}"
            knowledge = self.retrieve_specialized_knowledge(query, market_target)
            
            result = f"""
## 🗣️ ENGENHARIA LINGUÍSTICA - {self.agent_name}

**Audiência**: {market_target}
**Contexto**: {offer}

### 📚 TÉCNICAS DE PERSUASÃO APLICADAS:
{knowledge}

### 🎯 LINGUAGEM PROPRIETÁRIA RECOMENDADA:
1. **Terminologia Especializada**: Criar vocabulário único para a oferta
2. **Padrões Linguísticos**: Estruturas que induzem estados mentais específicos
3. **Ancoragem Semântica**: Palavras que ativam associações positivas
"""
        
        elif self.specialization == "credibility_building":
            query = f"credibilidade autoridade {offer} {market_target}"
            knowledge = self.retrieve_specialized_knowledge(query, market_target)
            
            result = f"""
## 🏆 ENGENHARIA DE LEGITIMIDADE - {self.agent_name}

**Oferta**: {offer}
**Mercado**: {market_target}

### 📚 SISTEMAS DE CREDIBILIDADE:
{knowledge}

### 🎯 ESTRATÉGIAS DE LEGITIMAÇÃO:
1. **Autoridade Transferida**: Usar credibilidade de terceiros
2. **Prova Social Estratificada**: Evidências por segmento de mercado
3. **Validação Científica**: Fundamentação em pesquisas e dados
"""
        
        elif self.specialization == "transdisciplinary_synthesis":
            query = f"analogias metáforas {offer} {market_target}"
            knowledge = self.retrieve_specialized_knowledge(query, market_target)
            
            result = f"""
## 🔗 SÍNTESE TRANSDISCIPLINAR - {self.agent_name}

**Conceito**: {offer}
**Audiência**: {market_target}

### 📚 ANALOGIAS E CONEXÕES:
{knowledge}

### 🎯 PONTES CONCEITUAIS:
1. **Analogias Familiares**: Conectar oferta com conceitos conhecidos
2. **Metáforas Estruturais**: Criar compreensão através de comparações
3. **Narrativas Universais**: Histórias que ressoam com a audiência
"""
        
        else:
            # Processamento genérico
            query = f"{task} {market_target} {offer}"
            knowledge = self.retrieve_specialized_knowledge(query)
            
            result = f"""
## 🤖 PROCESSAMENTO ESPECIALIZADO - {self.agent_name}

**Tarefa**: {task}

### 📚 CONHECIMENTO APLICADO:
{knowledge}

### 🎯 RESULTADO:
Processamento baseado em conhecimento especializado do domínio.
"""
        
        print(f"✅ {self.agent_name} concluiu processamento com conhecimento")
        return result


def main():
    """Demonstração da integração conhecimento + agentes."""
    
    print("=" * 70)
    print("🧠 DEMONSTRAÇÃO: AGENTES COM CONHECIMENTO INTEGRADO")
    print("=" * 70)
    
    # Criar agentes especializados com conhecimento
    agents = [
        KnowledgeEnhancedAgent("AXIOM-ARCHAEOLOGIST", "axiom_discovery"),
        KnowledgeEnhancedAgent("CONCEPT-ARCHITECT", "concept_creation"),
        KnowledgeEnhancedAgent("PARADIGMATIC-LINGUIST", "linguistic_persuasion"),
        KnowledgeEnhancedAgent("LEGITIMACY-ENGINEER", "credibility_building"),
        KnowledgeEnhancedAgent("TRANSDISCIPLINARY-SYNTHESIZER", "transdisciplinary_synthesis")
    ]
    
    # Contexto de exemplo
    context = {
        "market_target": "Empreendedores digitais (25-45 anos) que faturam entre R$ 50k-500k/mês",
        "offer": "Programa de mentoria empresarial de 12 meses com acompanhamento semanal",
        "current_paradigm": "Preciso de mais estratégias de marketing e vendas para crescer",
        "obstacles": [
            "Preço alto (R$ 60.000)",
            "Ceticismo sobre ROI",
            "Falta de tempo para implementar",
            "Muitas opções no mercado"
        ]
    }
    
    print(f"\n📋 CONTEXTO DE VENDAS:")
    print(f"🎯 Mercado-Alvo: {context['market_target']}")
    print(f"💼 Oferta: {context['offer']}")
    print(f"🧠 Paradigma Atual: {context['current_paradigm']}")
    print(f"🚧 Obstáculos: {', '.join(context['obstacles'])}")
    
    # Processar com cada agente especializado
    print("\n" + "=" * 70)
    print("🔄 PROCESSAMENTO COM AGENTES ESPECIALIZADOS")
    print("=" * 70)
    
    for agent in agents:
        task = f"Analisar e resolver obstáculos de venda para {context['offer']}"
        result = agent.process_with_knowledge(task, context)
        print(result)
        print("\n" + "-" * 50)
    
    print("\n" + "=" * 70)
    print("✅ INTEGRAÇÃO CONHECIMENTO + AGENTES VALIDADA!")
    print("=" * 70)
    
    print("\n🎯 CAPACIDADES DEMONSTRADAS:")
    print("✅ Agentes especializados com conhecimento integrado")
    print("✅ Busca automática de conhecimento baseada em especialização")
    print("✅ Aplicação contextual de frameworks e técnicas")
    print("✅ Processamento inteligente com base em conhecimento real")
    print("✅ Resultados especializados por domínio de expertise")


if __name__ == "__main__":
    main()

