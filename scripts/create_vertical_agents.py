#!/usr/bin/env python3
"""
Sistema de Criação de Agentes Verticais Especializados

Cria agentes com conhecimento exclusivo e focado de suas áreas específicas,
sem poluição de conhecimento de outras especialidades.
"""

import os
import sys
import shutil
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
import re
from collections import defaultdict


class VerticalAgentCreator:
    """Sistema para criar agentes verticais especializados."""
    
    def __init__(
        self,
        source_path: str = "/home/ubuntu/multi-agent-ai-system-git",
        target_path: str = "/home/ubuntu/unified-sales-framework"
    ):
        self.source_path = Path(source_path)
        self.target_path = Path(target_path)
        self.vertical_agents_dir = self.target_path / "vertical_agents"
        
        # Estatísticas
        self.stats = {
            "vertical_agents_created": 0,
            "knowledge_domains_isolated": 0,
            "specialized_tools_created": 0,
            "pure_prompts_generated": 0,
            "errors": []
        }
        
        # Definição de domínios verticais
        self.vertical_domains = {
            "analytics_specialist": {
                "description": "Especialista em analytics, tracking e métricas de performance",
                "keywords": ["analytics", "tracking", "metrics", "performance", "conversion", "roi", "kpi"],
                "agents": ["ANALYTICSGPT | Super Track"],
                "knowledge_focus": ["analytics", "tracking", "metrics", "performance_analysis"]
            },
            "api_integration_specialist": {
                "description": "Especialista em integrações de APIs e sistemas",
                "keywords": ["api", "integration", "webhook", "endpoint", "rest", "json", "http"],
                "agents": ["APIUnifyMaster", "APIsImputOutputMapper", "HotmartAPIMaster", "KiwifyAPIMaster", "PaytAPIMaster", "PerfectpayAPIMaster"],
                "knowledge_focus": ["api_integration", "webhooks", "payment_systems", "platform_apis"]
            },
            "persuasion_copywriter": {
                "description": "Especialista em copywriting persuasivo e transformação de paradigmas",
                "keywords": ["persuasion", "copywriting", "paradigm", "transformation", "conversion", "psychology"],
                "agents": ["paradigm_architect", "conversion_catalyst"],
                "knowledge_focus": ["persuasion_psychology", "paradigm_transformation", "conversion_optimization"]
            },
            "neurohook_specialist": {
                "description": "Especialista em hooks neurológicos e gatilhos mentais",
                "keywords": ["neurohook", "trigger", "psychology", "mental", "cognitive", "bias"],
                "agents": ["neurohook_ultra", "pain_detector"],
                "knowledge_focus": ["neurological_triggers", "cognitive_biases", "pain_points"]
            },
            "metaphor_architect": {
                "description": "Especialista em criação de metáforas e analogias",
                "keywords": ["metaphor", "analogy", "storytelling", "narrative", "comparison"],
                "agents": ["metaphor_architect"],
                "knowledge_focus": ["metaphor_creation", "analogies", "storytelling_techniques"]
            },
            "retention_optimizer": {
                "description": "Especialista em otimização de retenção e engajamento",
                "keywords": ["retention", "engagement", "loyalty", "churn", "lifetime_value"],
                "agents": ["retention_architect"],
                "knowledge_focus": ["retention_strategies", "engagement_optimization", "customer_lifecycle"]
            },
            "knowledge_curator": {
                "description": "Especialista em curadoria e gestão de conhecimento",
                "keywords": ["knowledge", "curation", "rag", "documentation", "information"],
                "agents": ["DocRAGOptimizer"],
                "knowledge_focus": ["knowledge_management", "rag_optimization", "documentation_systems"]
            }
        }
        
        print("🎯 Sistema de Agentes Verticais Especializados inicializado")
        print(f"📂 Origem: {self.source_path}")
        print(f"🎯 Destino: {self.vertical_agents_dir}")
    
    def create_all_vertical_agents(self) -> bool:
        """Cria todos os agentes verticais especializados."""
        
        print("\n🚀 CRIANDO AGENTES VERTICAIS ESPECIALIZADOS...")
        
        # Criar estrutura de destino
        self._create_vertical_structure()
        
        # Criar cada agente vertical
        for domain_id, domain_config in self.vertical_domains.items():
            print(f"\n📦 Criando agente vertical: {domain_id}")
            
            try:
                success = self._create_vertical_agent(domain_id, domain_config)
                if success:
                    self.stats["vertical_agents_created"] += 1
                    print(f"   ✅ Agente vertical {domain_id} criado com sucesso")
                else:
                    print(f"   ❌ Falha na criação do agente {domain_id}")
                    
            except Exception as e:
                error_msg = f"Erro criando agente vertical {domain_id}: {e}"
                self.stats["errors"].append(error_msg)
                print(f"   ❌ {error_msg}")
        
        # Relatório final
        self._print_vertical_report()
        
        return self.stats["vertical_agents_created"] == len(self.vertical_domains)
    
    def _create_vertical_structure(self):
        """Cria estrutura para agentes verticais."""
        
        print("🏗️ Criando estrutura para agentes verticais...")
        
        # Criar diretório principal
        self.vertical_agents_dir.mkdir(parents=True, exist_ok=True)
        
        # Criar subdiretórios por domínio
        for domain_id in self.vertical_domains.keys():
            domain_dir = self.vertical_agents_dir / domain_id
            domain_dir.mkdir(exist_ok=True)
            print(f"   📁 Criado: {domain_dir}")
    
    def _create_vertical_agent(self, domain_id: str, domain_config: Dict[str, Any]) -> bool:
        """Cria um agente vertical especializado."""
        
        try:
            agent_dir = self.vertical_agents_dir / domain_id
            
            # 1. Criar conhecimento vertical puro
            vertical_knowledge = self._extract_vertical_knowledge(domain_config)
            self._create_vertical_knowledge_base(agent_dir, vertical_knowledge)
            
            # 2. Criar prompt vertical puro
            vertical_prompt = self._create_vertical_prompt(domain_config, vertical_knowledge)
            self._save_vertical_prompt(agent_dir, vertical_prompt)
            
            # 3. Criar ferramentas especializadas
            specialized_tools = self._create_specialized_tools(domain_config)
            self._save_specialized_tools(agent_dir, specialized_tools)
            
            # 4. Criar agente vertical integrado com ADK
            self._create_vertical_agent_class(agent_dir, domain_id, domain_config)
            
            # 5. Criar configuração vertical
            self._create_vertical_config(agent_dir, domain_config)
            
            return True
            
        except Exception as e:
            self.stats["errors"].append(f"Erro criando agente vertical {domain_id}: {e}")
            return False
    
    def _extract_vertical_knowledge(self, domain_config: Dict[str, Any]) -> Dict[str, Any]:
        """Extrai conhecimento vertical puro para o domínio."""
        
        vertical_knowledge = {
            "domain": domain_config["description"],
            "keywords": domain_config["keywords"],
            "focus_areas": domain_config["knowledge_focus"],
            "documents": [],
            "specialized_content": []
        }
        
        # Buscar conhecimento específico dos agentes do domínio
        for agent_name in domain_config["agents"]:
            agent_knowledge = self._extract_agent_specific_knowledge(agent_name, domain_config["keywords"])
            if agent_knowledge:
                vertical_knowledge["documents"].extend(agent_knowledge)
        
        # Filtrar conhecimento geral por keywords
        general_knowledge = self._filter_general_knowledge_by_keywords(domain_config["keywords"])
        vertical_knowledge["specialized_content"].extend(general_knowledge)
        
        self.stats["knowledge_domains_isolated"] += 1
        return vertical_knowledge
    
    def _extract_agent_specific_knowledge(self, agent_name: str, keywords: List[str]) -> List[Dict[str, Any]]:
        """Extrai conhecimento específico de um agente."""
        
        knowledge_docs = []
        
        # Buscar base de conhecimento do agente
        for category in ["agents_analytics", "agents_apis", "agents_copywriters", "agents_knowledgebases_masters"]:
            agent_path = self.source_path / "agents" / category / agent_name / "knowledge_base"
            
            if agent_path.exists():
                # Processar todos os documentos da base de conhecimento
                for doc_file in agent_path.rglob("*.md"):
                    try:
                        with open(doc_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Verificar se o conteúdo é relevante para o domínio
                        if self._is_content_relevant(content, keywords):
                            knowledge_docs.append({
                                "file": str(doc_file.relative_to(self.source_path)),
                                "title": doc_file.stem,
                                "content": content,
                                "relevance_score": self._calculate_relevance_score(content, keywords),
                                "agent_source": agent_name
                            })
                    except Exception as e:
                        print(f"   ⚠️ Erro lendo {doc_file}: {e}")
        
        # Ordenar por relevância
        knowledge_docs.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        return knowledge_docs
    
    def _filter_general_knowledge_by_keywords(self, keywords: List[str]) -> List[Dict[str, Any]]:
        """Filtra conhecimento geral por keywords específicas."""
        
        filtered_knowledge = []
        
        # Buscar em toda a documentação geral
        for doc_file in self.source_path.rglob("*.md"):
            # Pular arquivos já processados nas bases de conhecimento específicas
            if "knowledge_base" in str(doc_file):
                continue
                
            try:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Verificar relevância
                if self._is_content_relevant(content, keywords):
                    relevance_score = self._calculate_relevance_score(content, keywords)
                    
                    # Apenas incluir se a relevância for alta
                    if relevance_score > 0.3:
                        filtered_knowledge.append({
                            "file": str(doc_file.relative_to(self.source_path)),
                            "title": doc_file.stem,
                            "content": content,
                            "relevance_score": relevance_score,
                            "source_type": "general_documentation"
                        })
            except Exception as e:
                continue
        
        # Ordenar por relevância e pegar apenas os mais relevantes
        filtered_knowledge.sort(key=lambda x: x["relevance_score"], reverse=True)
        return filtered_knowledge[:10]  # Máximo 10 documentos gerais
    
    def _is_content_relevant(self, content: str, keywords: List[str]) -> bool:
        """Verifica se o conteúdo é relevante para as keywords."""
        
        content_lower = content.lower()
        
        # Contar quantas keywords aparecem
        keyword_matches = sum(1 for keyword in keywords if keyword.lower() in content_lower)
        
        # Considerar relevante se pelo menos 2 keywords aparecem ou 1 keyword aparece múltiplas vezes
        if keyword_matches >= 2:
            return True
        
        if keyword_matches >= 1:
            # Verificar se a keyword aparece múltiplas vezes
            for keyword in keywords:
                if content_lower.count(keyword.lower()) >= 3:
                    return True
        
        return False
    
    def _calculate_relevance_score(self, content: str, keywords: List[str]) -> float:
        """Calcula score de relevância do conteúdo."""
        
        content_lower = content.lower()
        total_words = len(content.split())
        
        if total_words == 0:
            return 0.0
        
        # Contar ocorrências de keywords
        keyword_count = 0
        for keyword in keywords:
            keyword_count += content_lower.count(keyword.lower())
        
        # Calcular densidade de keywords
        keyword_density = keyword_count / total_words
        
        # Bonus por diversidade de keywords
        unique_keywords_found = sum(1 for keyword in keywords if keyword.lower() in content_lower)
        diversity_bonus = unique_keywords_found / len(keywords)
        
        # Score final
        relevance_score = (keyword_density * 10) + (diversity_bonus * 0.5)
        
        return min(relevance_score, 1.0)  # Máximo 1.0
    
    def _create_vertical_knowledge_base(self, agent_dir: Path, vertical_knowledge: Dict[str, Any]):
        """Cria base de conhecimento vertical pura."""
        
        knowledge_dir = agent_dir / "vertical_knowledge"
        knowledge_dir.mkdir(exist_ok=True)
        
        # Salvar documentos específicos
        docs_dir = knowledge_dir / "specialized_docs"
        docs_dir.mkdir(exist_ok=True)
        
        for i, doc in enumerate(vertical_knowledge["documents"]):
            doc_file = docs_dir / f"{i:03d}_{doc['title']}.md"
            with open(doc_file, 'w', encoding='utf-8') as f:
                f.write(f"# {doc['title']}\n\n")
                f.write(f"**Fonte:** {doc['agent_source']}\n")
                f.write(f"**Relevância:** {doc['relevance_score']:.3f}\n\n")
                f.write(doc['content'])
        
        # Salvar conteúdo geral filtrado
        general_dir = knowledge_dir / "filtered_general"
        general_dir.mkdir(exist_ok=True)
        
        for i, doc in enumerate(vertical_knowledge["specialized_content"]):
            doc_file = general_dir / f"{i:03d}_{doc['title']}.md"
            with open(doc_file, 'w', encoding='utf-8') as f:
                f.write(f"# {doc['title']}\n\n")
                f.write(f"**Fonte:** {doc['source_type']}\n")
                f.write(f"**Relevância:** {doc['relevance_score']:.3f}\n\n")
                f.write(doc['content'])
        
        # Criar índice de conhecimento
        index_file = knowledge_dir / "knowledge_index.yaml"
        with open(index_file, 'w', encoding='utf-8') as f:
            yaml.dump({
                "domain": vertical_knowledge["domain"],
                "keywords": vertical_knowledge["keywords"],
                "focus_areas": vertical_knowledge["focus_areas"],
                "specialized_docs_count": len(vertical_knowledge["documents"]),
                "general_docs_count": len(vertical_knowledge["specialized_content"]),
                "total_relevance_score": sum(doc["relevance_score"] for doc in vertical_knowledge["documents"])
            }, f, default_flow_style=False)
    
    def _create_vertical_prompt(self, domain_config: Dict[str, Any], vertical_knowledge: Dict[str, Any]) -> str:
        """Cria prompt vertical puro sem poluição."""
        
        # Extrair exemplos específicos do conhecimento
        examples = self._extract_domain_examples(vertical_knowledge)
        
        prompt = f"""# {domain_config['description'].upper()}

Você é um especialista EXCLUSIVO em {domain_config['description'].lower()}.

## 🎯 SUA ESPECIALIZAÇÃO VERTICAL

Você possui conhecimento PURO e FOCADO apenas em:
{chr(10).join(f"- {focus}" for focus in domain_config['knowledge_focus'])}

## 🚫 LIMITAÇÕES IMPORTANTES

- Você NÃO possui conhecimento sobre outras áreas
- Você NÃO deve tentar responder sobre tópicos fora da sua especialização
- Se perguntado sobre algo fora do seu domínio, redirecione para um especialista apropriado

## 🔑 PALAVRAS-CHAVE DO SEU DOMÍNIO

{', '.join(domain_config['keywords'])}

## 📚 BASE DE CONHECIMENTO ESPECIALIZADA

Você tem acesso a conhecimento curado e filtrado especificamente para sua área:
- {len(vertical_knowledge['documents'])} documentos especializados
- {len(vertical_knowledge['specialized_content'])} recursos gerais filtrados
- Conhecimento extraído de: {', '.join(domain_config['agents'])}

## 🎯 EXEMPLOS DE APLICAÇÃO

{examples}

## 📋 INSTRUÇÕES DE OPERAÇÃO

1. **Mantenha-se no seu domínio**: Responda apenas sobre sua especialização
2. **Use conhecimento vertical**: Aplique apenas conhecimento relevante da sua área
3. **Seja preciso e focado**: Forneça respostas específicas e especializadas
4. **Redirecione quando necessário**: Se a pergunta estiver fora do seu domínio, sugira o especialista apropriado
5. **Aplique conhecimento curado**: Use apenas o conhecimento filtrado da sua base especializada

## 🔄 PROCESSO DE RESPOSTA

1. Analise se a pergunta está dentro do seu domínio vertical
2. Se SIM: Use seu conhecimento especializado para responder
3. Se NÃO: Redirecione para o especialista apropriado
4. Sempre mantenha foco na sua especialização

Você está pronto para atuar como especialista vertical em {domain_config['description'].lower()}.
"""
        
        self.stats["pure_prompts_generated"] += 1
        return prompt
    
    def _extract_domain_examples(self, vertical_knowledge: Dict[str, Any]) -> str:
        """Extrai exemplos específicos do domínio."""
        
        examples = []
        
        # Buscar exemplos nos documentos especializados
        for doc in vertical_knowledge["documents"][:3]:  # Pegar apenas os 3 mais relevantes
            content_lines = doc["content"].split('\n')
            
            # Buscar linhas que parecem exemplos
            for line in content_lines:
                if any(indicator in line.lower() for indicator in ["exemplo:", "example:", "por exemplo", "como:"]):
                    if len(line.strip()) > 20 and len(line.strip()) < 200:
                        examples.append(f"- {line.strip()}")
                        if len(examples) >= 5:
                            break
            
            if len(examples) >= 5:
                break
        
        if not examples:
            examples = [f"- Aplicação especializada em {focus}" for focus in vertical_knowledge["focus_areas"][:3]]
        
        return '\n'.join(examples[:5])
    
    def _create_specialized_tools(self, domain_config: Dict[str, Any]) -> Dict[str, Any]:
        """Cria ferramentas especializadas para o domínio."""
        
        tools = {
            "vertical_knowledge_retrieval": {
                "name": f"{domain_config['description'].lower().replace(' ', '_')}_knowledge",
                "description": f"Recupera conhecimento especializado em {domain_config['description'].lower()}",
                "keywords": domain_config["keywords"],
                "focus_areas": domain_config["knowledge_focus"]
            },
            "domain_validation": {
                "name": f"{domain_config['description'].lower().replace(' ', '_')}_validator",
                "description": f"Valida se uma query está dentro do domínio de {domain_config['description'].lower()}",
                "keywords": domain_config["keywords"]
            },
            "specialist_redirect": {
                "name": "specialist_redirect",
                "description": "Redireciona para especialista apropriado quando query está fora do domínio",
                "available_specialists": list(self.vertical_domains.keys())
            }
        }
        
        self.stats["specialized_tools_created"] += len(tools)
        return tools
    
    def _save_specialized_tools(self, agent_dir: Path, tools: Dict[str, Any]):
        """Salva ferramentas especializadas."""
        
        tools_file = agent_dir / "vertical_tools.yaml"
        with open(tools_file, 'w', encoding='utf-8') as f:
            yaml.dump(tools, f, default_flow_style=False)
    
    def _save_vertical_prompt(self, agent_dir: Path, prompt: str):
        """Salva prompt vertical."""
        
        prompt_file = agent_dir / "vertical_prompt.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
    
    def _create_vertical_agent_class(self, agent_dir: Path, domain_id: str, domain_config: Dict[str, Any]):
        """Cria classe do agente vertical integrada com ADK."""
        
        class_name = self._to_class_name(domain_id)
        
        agent_code = f'''"""
Agente Vertical Especializado: {domain_id}

{domain_config['description']}
Conhecimento PURO e FOCADO sem poluição de outras áreas.
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import yaml

# Adicionar ADK ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

try:
    from google.adk.agents.llm_agent import LlmAgent
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    print("⚠️ ADK não disponível, usando implementação simplificada")


class {class_name}:
    """
    Agente Vertical Especializado em {domain_config['description']}
    
    Características:
    - Conhecimento PURO e FOCADO
    - SEM poluição de outras áreas
    - Especialização vertical exclusiva
    """
    
    def __init__(
        self,
        model_name: str = "gemini-1.5-pro",
        **kwargs
    ):
        self.domain_id = "{domain_id}"
        self.specialization = "{domain_config['description']}"
        self.keywords = {domain_config['keywords']}
        self.focus_areas = {domain_config['knowledge_focus']}
        
        # Carregar prompt vertical puro
        self.vertical_prompt = self._load_vertical_prompt()
        
        # Carregar ferramentas especializadas
        self.specialized_tools = self._load_specialized_tools()
        
        # Carregar conhecimento vertical
        self.vertical_knowledge = self._load_vertical_knowledge()
        
        # Inicializar agente ADK se disponível
        if ADK_AVAILABLE:
            try:
                self.llm_agent = LlmAgent(
                    model_name=model_name,
                    instructions=self.vertical_prompt,
                    **kwargs
                )
                self.adk_integrated = True
            except Exception as e:
                print(f"⚠️ Erro inicializando ADK: {{e}}")
                self.adk_integrated = False
        else:
            self.adk_integrated = False
        
        print(f"🎯 Agente Vertical {{self.domain_id}} inicializado")
        print(f"📚 Conhecimento: {{len(self.vertical_knowledge)}} documentos especializados")
        print(f"🔧 Ferramentas: {{len(self.specialized_tools)}} especializadas")
    
    def _load_vertical_prompt(self) -> str:
        """Carrega prompt vertical puro."""
        prompt_file = Path(__file__).parent / "vertical_prompt.txt"
        
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"⚠️ Erro carregando prompt vertical: {{e}}")
            return f"Você é um especialista vertical em {{self.specialization}}."
    
    def _load_specialized_tools(self) -> Dict[str, Any]:
        """Carrega ferramentas especializadas."""
        tools_file = Path(__file__).parent / "vertical_tools.yaml"
        
        try:
            with open(tools_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️ Erro carregando ferramentas: {{e}}")
            return {{}}
    
    def _load_vertical_knowledge(self) -> List[Dict[str, Any]]:
        """Carrega conhecimento vertical curado."""
        knowledge_dir = Path(__file__).parent / "vertical_knowledge"
        knowledge = []
        
        if knowledge_dir.exists():
            # Carregar documentos especializados
            specialized_dir = knowledge_dir / "specialized_docs"
            if specialized_dir.exists():
                for doc_file in specialized_dir.glob("*.md"):
                    try:
                        with open(doc_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        knowledge.append({{
                            "title": doc_file.stem,
                            "content": content,
                            "type": "specialized"
                        }})
                    except Exception as e:
                        continue
            
            # Carregar conteúdo geral filtrado
            general_dir = knowledge_dir / "filtered_general"
            if general_dir.exists():
                for doc_file in general_dir.glob("*.md"):
                    try:
                        with open(doc_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        knowledge.append({{
                            "title": doc_file.stem,
                            "content": content,
                            "type": "filtered_general"
                        }})
                    except Exception as e:
                        continue
        
        return knowledge
    
    def is_query_in_domain(self, query: str) -> bool:
        """Verifica se a query está dentro do domínio vertical."""
        query_lower = query.lower()
        
        # Verificar se contém keywords do domínio
        keyword_matches = sum(1 for keyword in self.keywords if keyword.lower() in query_lower)
        
        # Considerar dentro do domínio se pelo menos 1 keyword for encontrada
        return keyword_matches > 0
    
    def get_relevant_knowledge(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Recupera conhecimento relevante para a query."""
        if not self.is_query_in_domain(query):
            return []
        
        query_lower = query.lower()
        scored_knowledge = []
        
        for doc in self.vertical_knowledge:
            content_lower = doc["content"].lower()
            
            # Calcular relevância
            relevance = 0
            for keyword in self.keywords:
                if keyword.lower() in query_lower and keyword.lower() in content_lower:
                    relevance += content_lower.count(keyword.lower())
            
            if relevance > 0:
                scored_knowledge.append((doc, relevance))
        
        # Ordenar por relevância e retornar os mais relevantes
        scored_knowledge.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, score in scored_knowledge[:limit]]
    
    def process_vertical_query(self, query: str) -> str:
        """Processa query usando conhecimento vertical puro."""
        
        # 1. Verificar se está no domínio
        if not self.is_query_in_domain(query):
            return self._redirect_to_appropriate_specialist(query)
        
        # 2. Recuperar conhecimento relevante
        relevant_knowledge = self.get_relevant_knowledge(query)
        
        # 3. Construir contexto especializado
        knowledge_context = ""
        if relevant_knowledge:
            knowledge_context = "\\n\\nCONHECIMENTO ESPECIALIZADO RELEVANTE:\\n"
            for doc in relevant_knowledge:
                knowledge_context += f"\\n### {{doc['title']}}\\n{{doc['content'][:500]}}...\\n"
        
        # 4. Processar com agente
        enhanced_query = f"""
{{self.vertical_prompt}}

QUERY DO USUÁRIO: {{query}}
{{knowledge_context}}

Responda usando APENAS seu conhecimento vertical especializado. Mantenha-se estritamente dentro do seu domínio.
"""
        
        if self.adk_integrated:
            return self.llm_agent.run(enhanced_query)
        else:
            return f"[{{self.domain_id}}] Processando query vertical: {{query}}"
    
    def _redirect_to_appropriate_specialist(self, query: str) -> str:
        """Redireciona para especialista apropriado."""
        
        # Mapear query para domínio apropriado
        query_lower = query.lower()
        
        domain_mapping = {{
            "analytics": ["analytics", "tracking", "metrics", "performance"],
            "api_integration": ["api", "integration", "webhook", "endpoint"],
            "persuasion": ["persuasion", "copywriting", "conversion"],
            "neurohook": ["hook", "trigger", "psychology"],
            "metaphor": ["metaphor", "analogy", "story"],
            "retention": ["retention", "engagement", "loyalty"],
            "knowledge": ["knowledge", "documentation", "rag"]
        }}
        
        for domain, keywords in domain_mapping.items():
            if any(keyword in query_lower for keyword in keywords):
                return f"Esta query está fora do meu domínio vertical ({{self.specialization}}). Recomendo consultar o especialista em {{domain}}."
        
        return f"Esta query está fora do meu domínio vertical ({{self.specialization}}). Por favor, consulte o especialista apropriado."
    
    def get_vertical_capabilities(self) -> Dict[str, Any]:
        """Retorna capacidades do agente vertical."""
        return {{
            "domain_id": self.domain_id,
            "specialization": self.specialization,
            "keywords": self.keywords,
            "focus_areas": self.focus_areas,
            "knowledge_docs": len(self.vertical_knowledge),
            "specialized_tools": len(self.specialized_tools),
            "adk_integrated": self.adk_integrated,
            "vertical_purity": True,
            "cross_domain_pollution": False
        }}


def create_vertical_agent(**kwargs) -> {class_name}:
    """Factory para criar agente vertical."""
    return {class_name}(**kwargs)


# Exemplo de uso
if __name__ == "__main__":
    # Criar agente vertical
    agent = create_vertical_agent()
    
    # Mostrar capacidades
    capabilities = agent.get_vertical_capabilities()
    print(f"\\n🎯 AGENTE VERTICAL: {{capabilities['domain_id']}}")
    print(f"📋 Especialização: {{capabilities['specialization']}}")
    print(f"🔑 Keywords: {{', '.join(capabilities['keywords'])}}")
    print(f"📚 Conhecimento: {{capabilities['knowledge_docs']}} documentos")
    print(f"🔧 Ferramentas: {{capabilities['specialized_tools']}} especializadas")
    print(f"🎯 Pureza Vertical: {{capabilities['vertical_purity']}}")
    print(f"🚫 Poluição Cruzada: {{capabilities['cross_domain_pollution']}}")
    
    # Teste de domínio
    test_queries = [
        "Como otimizar conversões?",
        "Qual a melhor API de pagamento?",
        "Como criar uma metáfora eficaz?",
        "Estratégias de retenção de clientes"
    ]
    
    print(f"\\n🧪 TESTES DE DOMÍNIO:")
    for query in test_queries:
        in_domain = agent.is_query_in_domain(query)
        print(f"   {'✅' if in_domain else '❌'} '{{query}}' - {{'Dentro do domínio' if in_domain else 'Fora do domínio'}}")
'''
        
        # Salvar arquivo do agente
        agent_file = agent_dir / "vertical_agent.py"
        with open(agent_file, 'w', encoding='utf-8') as f:
            f.write(agent_code)
    
    def _create_vertical_config(self, agent_dir: Path, domain_config: Dict[str, Any]):
        """Cria configuração vertical."""
        
        config = {
            "vertical_agent": {
                "domain_id": domain_config["description"].lower().replace(" ", "_"),
                "specialization": domain_config["description"],
                "keywords": domain_config["keywords"],
                "focus_areas": domain_config["knowledge_focus"],
                "agents_source": domain_config["agents"],
                "purity_level": "maximum",
                "cross_domain_pollution": False
            },
            "knowledge_filtering": {
                "min_relevance_score": 0.3,
                "max_general_docs": 10,
                "keyword_density_threshold": 0.01,
                "diversity_bonus_weight": 0.5
            },
            "domain_validation": {
                "min_keyword_matches": 1,
                "strict_domain_enforcement": True,
                "redirect_on_out_of_domain": True
            }
        }
        
        config_file = agent_dir / "vertical_config.yaml"
        with open(config_file, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False)
    
    def _to_class_name(self, domain_id: str) -> str:
        """Converte domain_id para nome de classe."""
        parts = domain_id.split('_')
        return ''.join(word.capitalize() for word in parts) + 'VerticalAgent'
    
    def _print_vertical_report(self):
        """Imprime relatório de criação de agentes verticais."""
        
        print("\\n" + "="*60)
        print("📊 RELATÓRIO DE AGENTES VERTICAIS ESPECIALIZADOS")
        print("="*60)
        
        print(f"🎯 AGENTES VERTICAIS:")
        print(f"   Total criados: {self.stats['vertical_agents_created']}")
        print(f"   Domínios disponíveis: {len(self.vertical_domains)}")
        print(f"   Taxa de sucesso: {(self.stats['vertical_agents_created']/len(self.vertical_domains)*100):.1f}%")
        
        print(f"\\n📚 CONHECIMENTO VERTICAL:")
        print(f"   Domínios isolados: {self.stats['knowledge_domains_isolated']}")
        print(f"   Prompts puros gerados: {self.stats['pure_prompts_generated']}")
        print(f"   Ferramentas especializadas: {self.stats['specialized_tools_created']}")
        
        if self.stats['errors']:
            print(f"\\n❌ ERROS ({len(self.stats['errors'])}):")
            for error in self.stats['errors'][:3]:
                print(f"   - {error}")
        
        print("\\n🎯 DOMÍNIOS VERTICAIS CRIADOS:")
        for domain_id, config in self.vertical_domains.items():
            print(f"   📂 {domain_id}: {config['description']}")
            print(f"      Keywords: {', '.join(config['keywords'][:3])}...")
            print(f"      Agentes fonte: {len(config['agents'])}")
        
        print("\\n" + "="*60)
        
        if self.stats['vertical_agents_created'] == len(self.vertical_domains):
            print("✅ TODOS OS AGENTES VERTICAIS CRIADOS COM SUCESSO!")
        else:
            completion = (self.stats['vertical_agents_created']/len(self.vertical_domains)*100)
            print(f"⚠️ CRIAÇÃO {completion:.1f}% COMPLETA")
        
        print("="*60)


def main():
    """Executa criação de agentes verticais especializados."""
    
    print("🎯 CRIANDO AGENTES VERTICAIS ESPECIALIZADOS")
    print("="*50)
    print("Agentes com conhecimento PURO e FOCADO")
    print("SEM poluição de outras especialidades")
    print("="*50)
    
    # Inicializar sistema
    creator = VerticalAgentCreator()
    
    # Criar agentes verticais
    success = creator.create_all_vertical_agents()
    
    if success:
        print("\\n🎉 AGENTES VERTICAIS CRIADOS COM SUCESSO!")
        print("\\n🎯 CARACTERÍSTICAS DOS AGENTES VERTICAIS:")
        print("   ✅ Conhecimento PURO e FOCADO")
        print("   ✅ SEM poluição cruzada")
        print("   ✅ Especialização vertical exclusiva")
        print("   ✅ Redirecionamento automático para outros especialistas")
        print("   ✅ Ferramentas especializadas por domínio")
        return True
    else:
        print("\\n⚠️ CRIAÇÃO CONCLUÍDA COM ALGUNS PROBLEMAS")
        return False


if __name__ == "__main__":
    main()

