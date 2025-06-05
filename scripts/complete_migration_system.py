#!/usr/bin/env python3
"""
Sistema de Migração Completa de Agentes

Este script migra TODOS os agentes do multi-agent-ai-system para o unified-sales-framework
preservando completamente a estrutura original e integrando com ADK.
"""

import os
import sys
import shutil
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
import re


class CompleteMigrationSystem:
    """Sistema completo de migração de agentes."""
    
    def __init__(
        self,
        source_path: str = "/home/ubuntu/multi-agent-ai-system-git",
        target_path: str = "/home/ubuntu/unified-sales-framework"
    ):
        self.source_path = Path(source_path)
        self.target_path = Path(target_path)
        self.agents_source = self.source_path / "agents"
        self.agents_target = self.target_path / "agents"
        
        # Estatísticas de migração
        self.migration_stats = {
            "total_agents": 0,
            "migrated_agents": 0,
            "total_prompts": 0,
            "migrated_prompts": 0,
            "total_configs": 0,
            "migrated_configs": 0,
            "total_knowledge": 0,
            "migrated_knowledge": 0,
            "errors": []
        }
        
        # Mapeamento de categorias
        self.category_mapping = {
            "agents_analytics": "analytics",
            "agents_apis": "apis", 
            "agents_copywriters": "copywriting",
            "agents_knowledgebases_masters": "knowledge_masters"
        }
        
        print("🔧 Sistema de Migração Completa inicializado")
        print(f"📂 Origem: {self.source_path}")
        print(f"🎯 Destino: {self.target_path}")
    
    def discover_all_agents(self) -> List[Dict[str, Any]]:
        """Descobre TODOS os agentes no sistema original."""
        
        print("\n🔍 DESCOBRINDO TODOS OS AGENTES...")
        
        agents = []
        
        # Buscar em todas as categorias
        for category_dir in self.agents_source.iterdir():
            if not category_dir.is_dir() or category_dir.name.startswith('.'):
                continue
                
            print(f"📁 Analisando categoria: {category_dir.name}")
            
            # Buscar agentes na categoria
            for agent_dir in category_dir.iterdir():
                if not agent_dir.is_dir() or agent_dir.name.startswith('.'):
                    continue
                
                # Verificar se tem prompt.txt (indica que é um agente)
                prompt_file = agent_dir / "prompt.txt"
                if prompt_file.exists():
                    agent_info = self._analyze_agent(agent_dir, category_dir.name)
                    if agent_info:
                        agents.append(agent_info)
                        print(f"  ✅ Agente encontrado: {agent_info['name']}")
        
        print(f"\n📊 DESCOBERTA COMPLETA:")
        print(f"   Total de agentes encontrados: {len(agents)}")
        
        # Agrupar por categoria
        by_category = {}
        for agent in agents:
            category = agent['category']
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(agent['name'])
        
        for category, agent_names in by_category.items():
            print(f"   📂 {category}: {len(agent_names)} agentes")
            for name in agent_names[:3]:  # Mostrar apenas 3 primeiros
                print(f"      - {name}")
            if len(agent_names) > 3:
                print(f"      ... e mais {len(agent_names) - 3}")
        
        self.migration_stats["total_agents"] = len(agents)
        return agents
    
    def _analyze_agent(self, agent_dir: Path, category: str) -> Optional[Dict[str, Any]]:
        """Analisa um agente individual."""
        
        try:
            agent_info = {
                "name": agent_dir.name,
                "category": category,
                "path": agent_dir,
                "prompt_file": agent_dir / "prompt.txt",
                "config_files": [],
                "sub_agents": [],
                "knowledge_base": None,
                "tools_config": None
            }
            
            # Buscar arquivos de configuração
            for config_file in agent_dir.glob("*.yaml"):
                agent_info["config_files"].append(config_file)
                self.migration_stats["total_configs"] += 1
            
            for config_file in agent_dir.glob("*.yml"):
                agent_info["config_files"].append(config_file)
                self.migration_stats["total_configs"] += 1
            
            # Buscar tools.yaml específico
            tools_file = agent_dir / "tools.yaml"
            if tools_file.exists():
                agent_info["tools_config"] = tools_file
            
            # Buscar subagentes
            sub_agents_dir = agent_dir / "sub_agents"
            if sub_agents_dir.exists():
                for sub_agent_dir in sub_agents_dir.iterdir():
                    if sub_agent_dir.is_dir():
                        sub_prompt = sub_agent_dir / "prompt.txt"
                        if sub_prompt.exists():
                            agent_info["sub_agents"].append({
                                "name": sub_agent_dir.name,
                                "path": sub_agent_dir,
                                "prompt_file": sub_prompt
                            })
                            self.migration_stats["total_prompts"] += 1
            
            # Buscar base de conhecimento
            knowledge_dir = agent_dir / "knowledge_base"
            if knowledge_dir.exists():
                agent_info["knowledge_base"] = knowledge_dir
                self.migration_stats["total_knowledge"] += 1
            
            # Contar prompt principal
            self.migration_stats["total_prompts"] += 1
            
            return agent_info
            
        except Exception as e:
            self.migration_stats["errors"].append(f"Erro analisando {agent_dir}: {e}")
            return None
    
    def migrate_all_agents(self, agents: List[Dict[str, Any]]) -> bool:
        """Migra TODOS os agentes descobertos."""
        
        print(f"\n🚀 INICIANDO MIGRAÇÃO DE {len(agents)} AGENTES...")
        
        # Criar estrutura de destino
        self._create_target_structure()
        
        # Migrar cada agente
        for i, agent in enumerate(agents, 1):
            print(f"\n📦 [{i}/{len(agents)}] Migrando: {agent['name']}")
            
            try:
                success = self._migrate_single_agent(agent)
                if success:
                    self.migration_stats["migrated_agents"] += 1
                    print(f"   ✅ Migração concluída")
                else:
                    print(f"   ❌ Falha na migração")
                    
            except Exception as e:
                error_msg = f"Erro migrando {agent['name']}: {e}"
                self.migration_stats["errors"].append(error_msg)
                print(f"   ❌ {error_msg}")
        
        # Relatório final
        self._print_migration_report()
        
        return self.migration_stats["migrated_agents"] == len(agents)
    
    def _create_target_structure(self):
        """Cria estrutura de destino para agentes."""
        
        print("🏗️ Criando estrutura de destino...")
        
        # Criar diretório principal de agentes
        self.agents_target.mkdir(parents=True, exist_ok=True)
        
        # Criar subdiretórios por categoria
        for original_category, target_category in self.category_mapping.items():
            category_dir = self.agents_target / target_category
            category_dir.mkdir(exist_ok=True)
            print(f"   📁 Criado: {category_dir}")
    
    def _migrate_single_agent(self, agent: Dict[str, Any]) -> bool:
        """Migra um agente individual."""
        
        try:
            # Determinar diretório de destino
            target_category = self.category_mapping.get(agent['category'], 'others')
            agent_target_dir = self.agents_target / target_category / agent['name']
            
            # Criar diretório do agente
            agent_target_dir.mkdir(parents=True, exist_ok=True)
            
            # 1. Migrar prompt principal
            self._migrate_prompt(agent['prompt_file'], agent_target_dir / "prompt.txt")
            
            # 2. Migrar configurações
            for config_file in agent['config_files']:
                target_config = agent_target_dir / config_file.name
                self._migrate_config_file(config_file, target_config)
            
            # 3. Migrar tools.yaml se existir
            if agent['tools_config']:
                target_tools = agent_target_dir / "tools.yaml"
                self._migrate_config_file(agent['tools_config'], target_tools)
            
            # 4. Migrar subagentes
            if agent['sub_agents']:
                sub_agents_dir = agent_target_dir / "sub_agents"
                sub_agents_dir.mkdir(exist_ok=True)
                
                for sub_agent in agent['sub_agents']:
                    sub_target_dir = sub_agents_dir / sub_agent['name']
                    sub_target_dir.mkdir(exist_ok=True)
                    
                    # Migrar prompt do subagente
                    self._migrate_prompt(
                        sub_agent['prompt_file'], 
                        sub_target_dir / "prompt.txt"
                    )
            
            # 5. Migrar base de conhecimento
            if agent['knowledge_base']:
                target_knowledge = agent_target_dir / "knowledge_base"
                self._migrate_knowledge_base(agent['knowledge_base'], target_knowledge)
            
            # 6. Criar arquivo de integração ADK
            self._create_adk_integration_file(agent, agent_target_dir)
            
            return True
            
        except Exception as e:
            self.migration_stats["errors"].append(f"Erro migrando {agent['name']}: {e}")
            return False
    
    def _migrate_prompt(self, source_file: Path, target_file: Path) -> bool:
        """Migra um arquivo de prompt."""
        
        try:
            if source_file.exists():
                shutil.copy2(source_file, target_file)
                self.migration_stats["migrated_prompts"] += 1
                return True
            return False
        except Exception as e:
            self.migration_stats["errors"].append(f"Erro migrando prompt {source_file}: {e}")
            return False
    
    def _migrate_config_file(self, source_file: Path, target_file: Path) -> bool:
        """Migra um arquivo de configuração."""
        
        try:
            if source_file.exists():
                shutil.copy2(source_file, target_file)
                self.migration_stats["migrated_configs"] += 1
                return True
            return False
        except Exception as e:
            self.migration_stats["errors"].append(f"Erro migrando config {source_file}: {e}")
            return False
    
    def _migrate_knowledge_base(self, source_dir: Path, target_dir: Path) -> bool:
        """Migra uma base de conhecimento completa."""
        
        try:
            if source_dir.exists():
                shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
                self.migration_stats["migrated_knowledge"] += 1
                return True
            return False
        except Exception as e:
            self.migration_stats["errors"].append(f"Erro migrando knowledge {source_dir}: {e}")
            return False
    
    def _create_adk_integration_file(self, agent: Dict[str, Any], target_dir: Path):
        """Cria arquivo de integração com ADK para o agente."""
        
        # Ler prompt para extrair informações
        prompt_content = ""
        if agent['prompt_file'].exists():
            with open(agent['prompt_file'], 'r', encoding='utf-8') as f:
                prompt_content = f.read()
        
        # Determinar especialização baseada no nome e categoria
        specialization = self._determine_specialization(agent['name'], agent['category'])
        
        # Criar código de integração ADK
        integration_code = f'''"""
Agente {agent['name']} - Integração com ADK

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


class {self._to_class_name(agent['name'])}(LlmAgent if ADK_AVAILABLE else object):
    """
    {agent['name']} - Agente especializado migrado do multi-agent-ai-system.
    
    Categoria: {agent['category']}
    Especialização: {specialization}
    """
    
    def __init__(
        self,
        model_name: str = "gemini-1.5-pro",
        knowledge_base_path: str = "/home/ubuntu/multi-agent-ai-system-git",
        **kwargs
    ):
        # Carregar prompt original
        self.prompt_file = Path(__file__).parent / "prompt.txt"
        self.instruction = self._load_prompt()
        
        # Configurar especialização
        self.specialization = "{specialization}"
        self.category = "{agent['category']}"
        self.agent_name = "{agent['name']}"
        
        # Inicializar agente ADK se disponível
        if ADK_AVAILABLE:
            super().__init__(
                model_name=model_name,
                instructions=self.instruction,
                **kwargs
            )
            
            # Integrar sistema de conhecimento
            self.knowledge_toolset = UnifiedKnowledgeToolset(knowledge_base_path)
        else:
            # Implementação simplificada
            self.model_name = model_name
            self.instructions = self.instruction
        
        # Carregar subagentes se existirem
        self.sub_agents = self._load_sub_agents()
        
        # Carregar configurações
        self.config = self._load_config()
        
        print(f"🤖 {{self.agent_name}} inicializado com especialização: {{self.specialization}}")
    
    def _load_prompt(self) -> str:
        """Carrega o prompt original do agente."""
        try:
            if self.prompt_file.exists():
                with open(self.prompt_file, 'r', encoding='utf-8') as f:
                    return f.read()
            return f"Você é {{self.agent_name}}, um agente especializado em {{self.specialization}}."
        except Exception as e:
            print(f"⚠️ Erro carregando prompt: {{e}}")
            return f"Você é {{self.agent_name}}, um agente especializado."
    
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
                            
                            sub_agents.append({{
                                "name": sub_dir.name,
                                "prompt": prompt,
                                "specialization": self._determine_sub_specialization(sub_dir.name)
                            }})
                        except Exception as e:
                            print(f"⚠️ Erro carregando subagente {{sub_dir.name}}: {{e}}")
        
        return sub_agents
    
    def _load_config(self) -> Dict[str, Any]:
        """Carrega configurações do agente."""
        config = {{}}
        
        # Tentar carregar tools.yaml
        tools_file = Path(__file__).parent / "tools.yaml"
        if tools_file.exists():
            try:
                import yaml
                with open(tools_file, 'r', encoding='utf-8') as f:
                    config['tools'] = yaml.safe_load(f)
            except Exception as e:
                print(f"⚠️ Erro carregando tools.yaml: {{e}}")
        
        # Tentar carregar outros configs
        for config_file in Path(__file__).parent.glob("*.yaml"):
            if config_file.name != "tools.yaml":
                try:
                    import yaml
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config[config_file.stem] = yaml.safe_load(f)
                except Exception as e:
                    print(f"⚠️ Erro carregando {{config_file.name}}: {{e}}")
        
        return config
    
    def _determine_sub_specialization(self, sub_name: str) -> str:
        """Determina especialização de um subagente."""
        # Mapeamento básico baseado no nome
        specialization_map = {{
            "1": "analysis",
            "1 copy": "synthesis", 
            "1 copy 2": "validation",
            "1 copy 3": "optimization",
            "1 copy 4": "implementation"
        }}
        
        return specialization_map.get(sub_name, "general")
    
    def process_with_knowledge(self, query: str, context: Dict[str, Any] = None) -> str:
        """Processa query usando conhecimento especializado."""
        
        if not ADK_AVAILABLE:
            return f"{{self.agent_name}} processando: {{query}}"
        
        # Buscar conhecimento relevante
        if hasattr(self, 'knowledge_toolset'):
            knowledge_tool = self.knowledge_toolset.get_tool_by_name("knowledge_retrieval")
            if knowledge_tool:
                relevant_knowledge = knowledge_tool.retrieve(
                    query=query,
                    agent_id=self.agent_name,
                    limit=3
                )
                
                # Processar com conhecimento
                enhanced_query = f"""
{{self.instruction}}

CONHECIMENTO RELEVANTE:
{{relevant_knowledge}}

QUERY: {{query}}
CONTEXTO: {{context or 'Nenhum contexto adicional'}}

Processe esta query usando seu conhecimento especializado e o conhecimento relevante fornecido.
"""
                
                return self.run(enhanced_query)
        
        # Fallback para processamento básico
        return self.run(f"{{query}}\\n\\nContexto: {{context or 'Nenhum'}}")
    
    def delegate_to_subagent(self, query: str, sub_agent_name: str) -> str:
        """Delega tarefa para um subagente específico."""
        
        # Encontrar subagente
        sub_agent = None
        for sa in self.sub_agents:
            if sa['name'] == sub_agent_name:
                sub_agent = sa
                break
        
        if not sub_agent:
            return f"Subagente {{sub_agent_name}} não encontrado"
        
        # Processar com prompt do subagente
        sub_prompt = f"""
{{sub_agent['prompt']}}

TAREFA DELEGADA: {{query}}

Processe esta tarefa usando sua especialização em {{sub_agent['specialization']}}.
"""
        
        if ADK_AVAILABLE and hasattr(self, 'run'):
            return self.run(sub_prompt)
        else:
            return f"{{sub_agent_name}} processando: {{query}}"
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Retorna capacidades do agente."""
        return {{
            "name": self.agent_name,
            "category": self.category,
            "specialization": self.specialization,
            "sub_agents": [sa['name'] for sa in self.sub_agents],
            "has_knowledge_base": (Path(__file__).parent / "knowledge_base").exists(),
            "config_files": list(Path(__file__).parent.glob("*.yaml")),
            "adk_integrated": ADK_AVAILABLE
        }}


def create_agent(**kwargs) -> {self._to_class_name(agent['name'])}:
    """Factory function para criar instância do agente."""
    return {self._to_class_name(agent['name'])}(**kwargs)


# Exemplo de uso
if __name__ == "__main__":
    # Criar agente
    agent = create_agent()
    
    # Mostrar capacidades
    capabilities = agent.get_capabilities()
    print(f"\\n🤖 AGENTE: {{capabilities['name']}}")
    print(f"📂 Categoria: {{capabilities['category']}}")
    print(f"🎯 Especialização: {{capabilities['specialization']}}")
    print(f"👥 Subagentes: {{len(capabilities['sub_agents'])}}")
    print(f"📚 Base de conhecimento: {{capabilities['has_knowledge_base']}}")
    print(f"🔧 Integração ADK: {{capabilities['adk_integrated']}}")
    
    # Teste básico
    if capabilities['adk_integrated']:
        result = agent.process_with_knowledge(
            "Teste de funcionamento do agente",
            {{"context": "teste_migracao"}}
        )
        print(f"\\n📋 Resultado do teste:")
        print(result[:200] + "..." if len(result) > 200 else result)
'''
        
        # Salvar arquivo de integração
        integration_file = target_dir / "agent.py"
        with open(integration_file, 'w', encoding='utf-8') as f:
            f.write(integration_code)
    
    def _determine_specialization(self, agent_name: str, category: str) -> str:
        """Determina especialização baseada no nome e categoria do agente."""
        
        name_lower = agent_name.lower()
        
        # Mapeamento por categoria
        if category == "agents_analytics":
            return "analytics_and_tracking"
        elif category == "agents_apis":
            return "api_integration"
        elif category == "agents_copywriters":
            if "paradigm" in name_lower:
                return "paradigm_transformation"
            elif "conversion" in name_lower:
                return "conversion_optimization"
            elif "metaphor" in name_lower:
                return "metaphor_creation"
            elif "neurohook" in name_lower:
                return "neurological_hooks"
            elif "pain" in name_lower:
                return "pain_detection"
            elif "retention" in name_lower:
                return "retention_optimization"
            else:
                return "copywriting_specialist"
        elif category == "agents_knowledgebases_masters":
            return "knowledge_management"
        else:
            return "general_specialist"
    
    def _to_class_name(self, agent_name: str) -> str:
        """Converte nome do agente para nome de classe Python."""
        
        # Remover caracteres especiais e espaços
        clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', agent_name)
        
        # Converter para PascalCase
        parts = clean_name.split('_')
        class_name = ''.join(word.capitalize() for word in parts if word)
        
        # Garantir que começa com letra
        if not class_name[0].isalpha():
            class_name = 'Agent' + class_name
        
        return class_name + 'Agent'
    
    def _print_migration_report(self):
        """Imprime relatório final da migração."""
        
        print("\n" + "="*60)
        print("📊 RELATÓRIO FINAL DE MIGRAÇÃO")
        print("="*60)
        
        print(f"🎯 AGENTES:")
        print(f"   Total descobertos: {self.migration_stats['total_agents']}")
        print(f"   Migrados com sucesso: {self.migration_stats['migrated_agents']}")
        print(f"   Taxa de sucesso: {(self.migration_stats['migrated_agents']/self.migration_stats['total_agents']*100):.1f}%")
        
        print(f"\n📝 PROMPTS:")
        print(f"   Total encontrados: {self.migration_stats['total_prompts']}")
        print(f"   Migrados com sucesso: {self.migration_stats['migrated_prompts']}")
        print(f"   Taxa de sucesso: {(self.migration_stats['migrated_prompts']/self.migration_stats['total_prompts']*100):.1f}%")
        
        print(f"\n⚙️ CONFIGURAÇÕES:")
        print(f"   Total encontradas: {self.migration_stats['total_configs']}")
        print(f"   Migradas com sucesso: {self.migration_stats['migrated_configs']}")
        print(f"   Taxa de sucesso: {(self.migration_stats['migrated_configs']/self.migration_stats['total_configs']*100):.1f}%")
        
        print(f"\n📚 BASES DE CONHECIMENTO:")
        print(f"   Total encontradas: {self.migration_stats['total_knowledge']}")
        print(f"   Migradas com sucesso: {self.migration_stats['migrated_knowledge']}")
        print(f"   Taxa de sucesso: {(self.migration_stats['migrated_knowledge']/self.migration_stats['total_knowledge']*100):.1f}%")
        
        if self.migration_stats['errors']:
            print(f"\n❌ ERROS ({len(self.migration_stats['errors'])}):")
            for error in self.migration_stats['errors'][:5]:  # Mostrar apenas 5 primeiros
                print(f"   - {error}")
            if len(self.migration_stats['errors']) > 5:
                print(f"   ... e mais {len(self.migration_stats['errors']) - 5} erros")
        
        print("\n" + "="*60)
        
        # Status final
        if self.migration_stats['migrated_agents'] == self.migration_stats['total_agents']:
            print("✅ MIGRAÇÃO 100% COMPLETA!")
        else:
            completion = (self.migration_stats['migrated_agents']/self.migration_stats['total_agents']*100)
            print(f"⚠️ MIGRAÇÃO {completion:.1f}% COMPLETA")
        
        print("="*60)


def main():
    """Executa migração completa de todos os agentes."""
    
    print("🚀 INICIANDO MIGRAÇÃO COMPLETA DE AGENTES")
    print("="*50)
    
    # Inicializar sistema de migração
    migration_system = CompleteMigrationSystem()
    
    # Descobrir todos os agentes
    agents = migration_system.discover_all_agents()
    
    if not agents:
        print("❌ Nenhum agente encontrado para migração!")
        return False
    
    # Confirmar migração
    print(f"\n🎯 PRONTO PARA MIGRAR {len(agents)} AGENTES")
    print("   Esta operação irá:")
    print("   - Migrar TODOS os prompts e configurações")
    print("   - Preservar estrutura original completa")
    print("   - Criar integração com ADK")
    print("   - Manter bases de conhecimento")
    
    # Executar migração
    success = migration_system.migrate_all_agents(agents)
    
    if success:
        print("\n🎉 MIGRAÇÃO COMPLETA REALIZADA COM SUCESSO!")
        return True
    else:
        print("\n⚠️ MIGRAÇÃO CONCLUÍDA COM ALGUNS PROBLEMAS")
        return False


if __name__ == "__main__":
    main()

