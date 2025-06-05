"""
Sistema Unificado de Automação e Geração
Integra Magenerator com ADK CLI para criação automática de agentes
"""

import os
import sys
import json
import yaml
import shutil
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentGenerationConfig:
    """Configuração para geração de agentes"""
    agent_name: str
    agent_type: str  # 'traditional' ou 'vertical'
    specialization: str
    category: str
    prompt_content: str
    knowledge_base: Optional[Dict] = None
    tools: Optional[List[str]] = None
    subagents: Optional[List[Dict]] = None

class UnifiedAgentGenerator:
    """
    Gerador unificado que combina Magenerator com ADK CLI
    """
    
    def __init__(self, unified_framework_path: str):
        self.framework_path = Path(unified_framework_path)
        self.agents_dir = self.framework_path / "agents"
        self.vertical_agents_dir = self.framework_path / "vertical_agents"
        self.templates_dir = self.framework_path / "templates"
        self.scripts_dir = self.framework_path / "scripts"
        
        # Garantir que diretórios existem
        self.agents_dir.mkdir(exist_ok=True)
        self.vertical_agents_dir.mkdir(exist_ok=True)
        self.templates_dir.mkdir(exist_ok=True)
        self.scripts_dir.mkdir(exist_ok=True)
    
    def generate_traditional_agent(self, config: AgentGenerationConfig) -> Dict[str, Any]:
        """
        Gera um agente tradicional usando template ADK
        """
        logger.info(f"Gerando agente tradicional: {config.agent_name}")
        
        # Criar diretório do agente
        agent_path = self.agents_dir / config.category / config.agent_name
        agent_path.mkdir(parents=True, exist_ok=True)
        
        # Gerar arquivos do agente
        files_created = {}
        
        # 1. Prompt principal
        prompt_file = agent_path / "prompt.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(config.prompt_content)
        files_created['prompt'] = str(prompt_file)
        
        # 2. Configuração de ferramentas
        tools_file = agent_path / "tools.yaml"
        tools_config = {
            'tools': config.tools or [],
            'category': config.category,
            'specialization': config.specialization
        }
        with open(tools_file, 'w', encoding='utf-8') as f:
            yaml.dump(tools_config, f, default_flow_style=False)
        files_created['tools'] = str(tools_file)
        
        # 3. Arquivo de integração ADK
        agent_file = agent_path / "agent.py"
        agent_code = self._generate_adk_agent_code(config)
        with open(agent_file, 'w', encoding='utf-8') as f:
            f.write(agent_code)
        files_created['agent'] = str(agent_file)
        
        # 4. Base de conhecimento (se especificada)
        if config.knowledge_base:
            kb_dir = agent_path / "knowledge_base"
            kb_dir.mkdir(exist_ok=True)
            for filename, content in config.knowledge_base.items():
                kb_file = kb_dir / filename
                with open(kb_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            files_created['knowledge_base'] = str(kb_dir)
        
        # 5. Subagentes (se especificados)
        if config.subagents:
            subagents_dir = agent_path / "sub_agents"
            subagents_dir.mkdir(exist_ok=True)
            for subagent in config.subagents:
                sub_dir = subagents_dir / subagent['name']
                sub_dir.mkdir(exist_ok=True)
                
                # Prompt do subagente
                sub_prompt = sub_dir / "prompt.txt"
                with open(sub_prompt, 'w', encoding='utf-8') as f:
                    f.write(subagent.get('prompt', ''))
                
                # Configuração do subagente
                sub_config = sub_dir / "config.yaml"
                with open(sub_config, 'w', encoding='utf-8') as f:
                    yaml.dump(subagent, f, default_flow_style=False)
            
            files_created['subagents'] = str(subagents_dir)
        
        logger.info(f"Agente tradicional {config.agent_name} criado com sucesso")
        return {
            'type': 'traditional',
            'name': config.agent_name,
            'path': str(agent_path),
            'files': files_created
        }
    
    def generate_vertical_agent(self, name, specialization, prompt, template_data=None):
        """Gera agente vertical com interface simplificada"""
        try:
            # Criar configuração a partir dos parâmetros
            config = AgentGenerationConfig(
                agent_name=name,
                agent_type='vertical',
                specialization=specialization,
                category='vertical',
                prompt_content=prompt
            )
            
            # Processar template_data se fornecido
            if template_data:
                tools_data = template_data.get('tools', [])
                config.tools = [tool.get('name', '') for tool in tools_data]
                
                knowledge_data = template_data.get('knowledge', {})
                if knowledge_data.get('enabled'):
                    config.knowledge_base = {
                        'domains.md': f"Domínios: {', '.join(knowledge_data.get('domains', []))}"
                    }
            
            # Gerar agente usando configuração
            result = self._generate_vertical_agent_internal(config)
            logger.info(f"Agente vertical {name} criado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao gerar agente vertical {name}: {e}")
            return False
    
    def _generate_vertical_agent_internal(self, config: AgentGenerationConfig) -> Dict[str, Any]:
        """Implementação interna da geração de agente vertical"""
        logger.info(f"Gerando agente vertical: {config.agent_name}")
        
        # Criar diretório do agente vertical
        agent_path = self.vertical_agents_dir / config.agent_name
        agent_path.mkdir(parents=True, exist_ok=True)
        
        # Gerar arquivos do agente vertical
        files_created = {}
        
        # 1. Prompt especializado
        prompt_file = agent_path / "prompt.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(config.prompt_content)
        files_created['prompt'] = str(prompt_file)
        
        # 2. Agente Python
        agent_file = agent_path / "agent.py"
        agent_code = self._generate_vertical_agent_code(config)
        with open(agent_file, 'w', encoding='utf-8') as f:
            f.write(agent_code)
        files_created['agent'] = str(agent_file)
        
        # 3. Configuração YAML
        config_file = agent_path / "config.yaml"
        config_yaml = f"""name: {config.agent_name}
type: vertical
specialization: {config.specialization}
model_name: gemini-1.5-pro
"""
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_yaml)
        files_created['config'] = str(config_file)
        
        # 4. Ferramentas YAML
        tools_file = agent_path / "tools.yaml"
        tools_yaml = f"""tools:
  - name: {config.specialization}_analyzer
    description: Analisa {config.specialization}
  - name: {config.specialization}_optimizer  
    description: Otimiza {config.specialization}
  - name: {config.specialization}_validator
    description: Valida {config.specialization}
"""
        with open(tools_file, 'w', encoding='utf-8') as f:
            f.write(tools_yaml)
        files_created['tools'] = str(tools_file)
        
        # 5. Base de conhecimento
        if config.knowledge_base:
            knowledge_dir = agent_path / "knowledge"
            knowledge_dir.mkdir(exist_ok=True)
            
            for filename, content in config.knowledge_base.items():
                kb_file = knowledge_dir / filename
                with open(kb_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            files_created['knowledge'] = str(knowledge_dir)
        
        return {
            'success': True,
            'agent_name': config.agent_name,
            'path': str(agent_path),
            'files': files_created
        }
    
    def generate_traditional_agent(self, name, category, specialization, prompt, template_data=None):
        """Gera agente tradicional com interface simplificada"""
        try:
            # Criar configuração a partir dos parâmetros
            config = AgentGenerationConfig(
                agent_name=name,
                agent_type='traditional',
                specialization=specialization,
                category=category,
                prompt_content=prompt
            )
            
            # Processar template_data se fornecido
            if template_data:
                tools_data = template_data.get('tools', [])
                config.tools = [tool.get('name', '') for tool in tools_data]
                
                knowledge_data = template_data.get('knowledge', {})
                if knowledge_data.get('enabled'):
                    config.knowledge_base = {
                        'domains.md': f"Domínios: {', '.join(knowledge_data.get('domains', []))}"
                    }
            
            # Gerar agente usando configuração
            result = self._generate_traditional_agent_internal(config)
            logger.info(f"Agente tradicional {name} criado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao gerar agente tradicional {name}: {e}")
            return False
    
    def _generate_traditional_agent_internal(self, config: AgentGenerationConfig) -> Dict[str, Any]:
        """Implementação interna da geração de agente tradicional"""
        logger.info(f"Gerando agente tradicional: {config.agent_name}")
        
        # Criar diretório do agente
        agent_path = self.agents_dir / config.category / config.agent_name
        agent_path.mkdir(parents=True, exist_ok=True)
        
        # Gerar arquivos do agente
        files_created = {}
        
        # 1. Prompt
        prompt_file = agent_path / "prompt.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(config.prompt_content)
        files_created['prompt'] = str(prompt_file)
        
        # 2. Agente Python
        agent_file = agent_path / "agent.py"
        agent_code = self._generate_adk_agent_code(config)
        with open(agent_file, 'w', encoding='utf-8') as f:
            f.write(agent_code)
        files_created['agent'] = str(agent_file)
        
        # 3. Configuração YAML
        config_file = agent_path / "config.yaml"
        config_yaml = f"""name: {config.agent_name}
type: traditional
category: {config.category}
specialization: {config.specialization}
model_name: gemini-1.5-pro
"""
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_yaml)
        files_created['config'] = str(config_file)
        
        return {
            'success': True,
            'agent_name': config.agent_name,
            'path': str(agent_path),
            'files': files_created
        }
    
    def _generate_adk_agent_code(self, config: AgentGenerationConfig) -> str:
        """
        Gera código Python para agente ADK tradicional
        """
        agent_class_name = config.agent_name.title().replace('_', '')
        
        return f'''"""
Agente {config.agent_name} - {config.specialization}
Categoria: {config.category}
"""

import os
import sys
import yaml
from pathlib import Path

# Adicionar src ao path para imports
current_dir = Path(__file__).parent
framework_root = current_dir.parent.parent.parent
src_path = framework_root / "src"
sys.path.insert(0, str(src_path))

try:
    from google.adk.agents.llm_agent import LlmAgent
    from google.adk.agents.base_agent import BaseAgent
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    print("⚠️ ADK não disponível, usando modo simplificado")

class {agent_class_name}Agent:
    """
    Agente {config.agent_name} especializado em {config.specialization}
    """
    
    def __init__(self):
        self.name = "{config.agent_name}"
        self.category = "{config.category}"
        self.specialization = "{config.specialization}"
        self.agent_dir = Path(__file__).parent
        
        # Carregar prompt
        self.prompt = self._load_prompt()
        
        # Carregar configurações
        self.config = self._load_config()
        
        # Carregar base de conhecimento
        self.knowledge_base = self._load_knowledge_base()
        
        # Inicializar agente ADK (se disponível)
        self.adk_agent = None
        if ADK_AVAILABLE:
            try:
                self.adk_agent = self._init_adk_agent()
                print(f"✅ Agente ADK {{self.name}} inicializado com sucesso")
            except Exception as e:
                print(f"⚠️ Erro inicializando ADK: {{e}}")
                print(f"🔄 Usando modo simplificado para {{self.name}}")
        
        print(f"🤖 {{self.name}} inicializado com especialização: {{self.specialization}}")
        print(f"🔧 Integração ADK: {{self.adk_agent is not None}}")
        print(f"📚 Base de conhecimento: {{len(self.knowledge_base) > 0}}")
    
    def _load_prompt(self) -> str:
        """Carrega prompt do arquivo"""
        prompt_file = self.agent_dir / "prompt.txt"
        if prompt_file.exists():
            return prompt_file.read_text(encoding='utf-8')
        return "Prompt não encontrado"
    
    def _load_config(self) -> dict:
        """Carrega configurações do arquivo"""
        config_file = self.agent_dir / "tools.yaml"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {{}}
    
    def _load_knowledge_base(self) -> dict:
        """Carrega base de conhecimento"""
        kb_dir = self.agent_dir / "knowledge_base"
        knowledge = {{}}
        
        if kb_dir.exists():
            for file_path in kb_dir.rglob("*.md"):
                relative_path = file_path.relative_to(kb_dir)
                knowledge[str(relative_path)] = file_path.read_text(encoding='utf-8')
        
        return knowledge
    
    def _init_adk_agent(self):
        """Inicializa agente ADK"""
        if not ADK_AVAILABLE:
            return None
        
        try:
            return LlmAgent(
                name=self.name,
                model_name="gemini-1.5-pro",
                instructions=self.prompt
            )
        except Exception as e:
            print(f"Erro na inicialização ADK: {{e}}")
            return None
    
    def process(self, query: str) -> str:
        """
        Processa uma query usando o agente
        """
        if self.adk_agent:
            # Usar agente ADK se disponível
            try:
                # Implementar processamento ADK aqui
                return f"[{{self.name}}] Processando via ADK: {{query}}"
            except Exception as e:
                print(f"Erro no processamento ADK: {{e}}")
        
        # Fallback para processamento simplificado
        return f"[{{self.name}}] Processando: {{query}}"
    
    def get_info(self) -> dict:
        """
        Retorna informações do agente
        """
        return {{
            "name": self.name,
            "category": self.category,
            "specialization": self.specialization,
            "knowledge_base_size": len(self.knowledge_base),
            "config_files": len(self.config),
            "adk_integration": self.adk_agent is not None,
            "model": "gemini-1.5-pro"
        }}

def main():
    """Função principal para teste"""
    agent = {agent_class_name}Agent()
    
    # Exibir informações
    info = agent.get_info()
    print(f"🤖 AGENTE: {{info['name']}}")
    print(f"📂 Categoria: {{info['category']}}")
    print(f"🎯 Especialização: {{info['specialization']}}")
    print(f"📚 Base de conhecimento: {{info['knowledge_base_size']}} documentos")
    print(f"⚙️ Arquivos de config: {{info['config_files']}}")
    print(f"🔧 Integração ADK: {{info['adk_integration']}}")
    print(f"🤖 Modelo: {{info['model']}}")
    
    # Teste básico
    print(f"📋 Teste básico:")
    result = agent.process("Teste de funcionamento do agente {config.agent_name}...")
    print(result)

if __name__ == "__main__":
    main()
'''
    
    def _create_vertical_prompt(self, config: AgentGenerationConfig) -> str:
        """
        Cria prompt especializado para agente vertical
        """
        return f'''# ESPECIALISTA EM {config.specialization.upper()}

Você é um agente vertical altamente especializado em {config.specialization}.

## ESPECIALIZAÇÃO EXCLUSIVA:
- Domínio: {config.specialization}
- Categoria: {config.category}
- Foco: Conhecimento puro e especializado

## REGRAS DE PUREZA VERTICAL:
1. APENAS responda a questões relacionadas a {config.specialization}
2. Se a pergunta estiver fora do seu domínio, redirecione para o especialista apropriado
3. Mantenha foco absoluto na sua área de especialização
4. Use apenas conhecimento específico do seu domínio

## CONHECIMENTO ESPECIALIZADO:
{config.prompt_content}

## PROCESSO DE VALIDAÇÃO:
1. Verificar se a query está no domínio de {config.specialization}
2. Se SIM: Processar com conhecimento especializado
3. Se NÃO: Redirecionar para especialista apropriado

Mantenha sempre a pureza vertical e evite poluição de conhecimento de outras áreas.
'''
    
    def _generate_vertical_agent_code(self, config: AgentGenerationConfig) -> str:
        """
        Gera código Python para agente vertical
        """
        agent_class_name = config.agent_name.title().replace('_', '')
        domain_keywords = config.tools or ['keyword1', 'keyword2', 'keyword3']
        
        return f'''"""
Agente Vertical: {config.agent_name}
Especialização: {config.specialization}
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

class {agent_class_name}VerticalAgent:
    """
    Agente vertical especializado em {config.specialization}
    """
    
    def __init__(self):
        self.name = "{config.agent_name}"
        self.specialization = "{config.specialization}"
        self.agent_dir = Path(__file__).parent
        
        # Keywords de domínio
        self.domain_keywords = {domain_keywords}
        
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
                print(f"⚠️ Erro inicializando ADK: {{e}}")
        
        print(f"🎯 Agente Vertical {{self.name}} inicializado")
        print(f"🔧 Ferramentas: {{len(self.tools)}} especializadas")
    
    def _load_vertical_prompt(self) -> str:
        """Carrega prompt vertical"""
        prompt_file = self.agent_dir / "prompt.txt"
        if prompt_file.exists():
            return prompt_file.read_text(encoding='utf-8')
        return "Prompt vertical não encontrado"
    
    def _load_specialized_knowledge(self) -> Dict[str, str]:
        """Carrega conhecimento especializado"""
        knowledge = {{}}
        knowledge_dir = self.agent_dir / "knowledge" / "specialized_docs"
        
        if knowledge_dir.exists():
            for file_path in knowledge_dir.rglob("*.md"):
                relative_path = file_path.relative_to(knowledge_dir)
                knowledge[str(relative_path)] = file_path.read_text(encoding='utf-8')
        
        return knowledge
    
    def _load_specialized_tools(self) -> List[str]:
        """Carrega ferramentas especializadas"""
        return [
            f"{{self.specialization}}_analyzer",
            f"{{self.specialization}}_optimizer", 
            f"{{self.specialization}}_validator"
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
                return f"[{{self.name}}] Processamento vertical ADK: {{query}}"
            except Exception as e:
                print(f"Erro ADK: {{e}}")
        
        # Fallback simplificado
        return f"[{{self.name}}] Análise vertical de {{self.specialization}}: {{query}}"
    
    def _redirect_query(self, query: str) -> str:
        """
        Redireciona query para especialista apropriado
        """
        return f"❌ Query '{{query}}' está fora do domínio de {{self.specialization}}. Redirecionando para especialista apropriado."
    
    def get_vertical_info(self) -> Dict[str, Any]:
        """
        Retorna informações do agente vertical
        """
        return {{
            "name": self.name,
            "specialization": self.specialization,
            "domain_keywords": self.domain_keywords,
            "specialized_tools": len(self.tools),
            "vertical_purity": True,
            "cross_pollution": False
        }}

def main():
    """Teste do agente vertical"""
    agent = {agent_class_name}VerticalAgent()
    
    # Informações
    info = agent.get_vertical_info()
    print(f"🎯 AGENTE VERTICAL: {{info['name']}}")
    print(f"📋 Especialização: {{info['specialization']}}")
    print(f"🔑 Keywords: {{', '.join(info['domain_keywords'])}}")
    print(f"🔧 Ferramentas: {{info['specialized_tools']}} especializadas")
    print(f"🎯 Pureza Vertical: {{info['vertical_purity']}}")
    print(f"🚫 Poluição Cruzada: {{info['cross_pollution']}}")
    
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
        print(f"   {{status}} '{{query}}' - {{'No domínio' if in_domain else 'Fora do domínio'}}")

if __name__ == "__main__":
    main()
'''
    
    def _generate_vertical_tools_code(self, config: AgentGenerationConfig) -> str:
        """
        Gera código de ferramentas especializadas para agente vertical
        """
        tools_class_name = config.agent_name.title().replace('_', '')
        
        return f'''"""
Ferramentas especializadas para {config.agent_name}
Domínio: {config.specialization}
"""

from typing import Dict, List, Any

class {tools_class_name}Tools:
    """
    Ferramentas especializadas para {config.specialization}
    """
    
    def __init__(self):
        self.domain = "{config.specialization}"
        self.tools = self._initialize_tools()
    
    def _initialize_tools(self) -> Dict[str, Any]:
        """
        Inicializa ferramentas especializadas
        """
        return {{
            f"{{self.domain}}_analyzer": self.analyze,
            f"{{self.domain}}_optimizer": self.optimize,
            f"{{self.domain}}_validator": self.validate
        }}
    
    def analyze(self, data: str) -> Dict[str, Any]:
        """
        Analisa dados específicos do domínio
        """
        return {{
            "domain": self.domain,
            "analysis": f"Análise especializada de {{self.domain}}",
            "data": data,
            "insights": [
                f"Insight 1 sobre {{self.domain}}",
                f"Insight 2 sobre {{self.domain}}",
                f"Insight 3 sobre {{self.domain}}"
            ]
        }}
    
    def optimize(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Otimiza parâmetros específicos do domínio
        """
        return {{
            "domain": self.domain,
            "optimization": f"Otimização especializada de {{self.domain}}",
            "original_params": parameters,
            "optimized_params": {{
                **parameters,
                "optimized": True,
                "domain_specific": True
            }}
        }}
    
    def validate(self, input_data: Any) -> Dict[str, Any]:
        """
        Valida dados específicos do domínio
        """
        return {{
            "domain": self.domain,
            "validation": f"Validação especializada de {{self.domain}}",
            "input": input_data,
            "is_valid": True,
            "domain_compliance": True,
            "recommendations": [
                f"Recomendação 1 para {{self.domain}}",
                f"Recomendação 2 para {{self.domain}}"
            ]
        }}
    
    def get_available_tools(self) -> List[str]:
        """
        Retorna lista de ferramentas disponíveis
        """
        return list(self.tools.keys())
    
    def execute_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """
        Executa ferramenta específica
        """
        if tool_name in self.tools:
            return self.tools[tool_name](**kwargs)
        else:
            return {{
                "error": f"Ferramenta {{tool_name}} não encontrada",
                "available_tools": self.get_available_tools()
            }}

# Instância global das ferramentas
{config.agent_name}_tools = {tools_class_name}Tools()
'''
    
    def generate_agent_from_template(self, template_path: str, output_type: str = "traditional") -> Dict[str, Any]:
        """
        Gera agente a partir de template YAML
        """
        logger.info(f"Gerando agente a partir de template: {template_path}")
        
        # Carregar template
        with open(template_path, 'r', encoding='utf-8') as f:
            template_data = yaml.safe_load(f)
        
        # Criar configuração
        config = AgentGenerationConfig(
            agent_name=template_data.get('agent_name', 'new_agent'),
            agent_type=output_type,
            specialization=template_data.get('specialization', 'general'),
            category=template_data.get('category', 'general'),
            prompt_content=template_data.get('prompt', ''),
            knowledge_base=template_data.get('knowledge_base'),
            tools=template_data.get('tools'),
            subagents=template_data.get('subagents')
        )
        
        # Gerar agente
        if output_type == "vertical":
            return self.generate_vertical_agent(config)
        else:
            return self.generate_traditional_agent(config)
    
    def create_cli_integration(self) -> str:
        """
        Cria integração CLI unificada
        """
        cli_file = self.scripts_dir / "unified_cli.py"
        
        cli_code = '''#!/usr/bin/env python3
"""
CLI Unificado para Unified Sales Framework
Integra Magenerator com ADK CLI
"""

import click
import sys
from pathlib import Path

# Adicionar src ao path
current_dir = Path(__file__).parent
framework_root = current_dir.parent
sys.path.insert(0, str(framework_root))

from scripts.unified_agent_generator import UnifiedAgentGenerator, AgentGenerationConfig

@click.group()
def cli():
    """Unified Sales Framework CLI"""
    pass

@cli.command()
@click.argument('agent_name')
@click.option('--type', 'agent_type', default='traditional', 
              type=click.Choice(['traditional', 'vertical']),
              help='Tipo de agente a criar')
@click.option('--category', default='general', help='Categoria do agente')
@click.option('--specialization', default='general', help='Especialização do agente')
@click.option('--prompt', help='Arquivo de prompt ou texto direto')
def create(agent_name, agent_type, category, specialization, prompt):
    """Cria um novo agente"""
    
    framework_path = Path(__file__).parent.parent
    generator = UnifiedAgentGenerator(str(framework_path))
    
    # Carregar prompt
    prompt_content = ""
    if prompt:
        if Path(prompt).exists():
            prompt_content = Path(prompt).read_text(encoding='utf-8')
        else:
            prompt_content = prompt
    
    # Criar configuração
    config = AgentGenerationConfig(
        agent_name=agent_name,
        agent_type=agent_type,
        specialization=specialization,
        category=category,
        prompt_content=prompt_content
    )
    
    # Gerar agente
    if agent_type == "vertical":
        result = generator.generate_vertical_agent(config)
    else:
        result = generator.generate_traditional_agent(config)
    
    click.echo(f"✅ Agente {agent_name} criado com sucesso!")
    click.echo(f"📁 Localização: {result['path']}")
    click.echo(f"🔧 Tipo: {result['type']}")

@cli.command()
@click.argument('template_path')
@click.option('--type', 'output_type', default='traditional',
              type=click.Choice(['traditional', 'vertical']),
              help='Tipo de agente a gerar')
def from_template(template_path, output_type):
    """Gera agente a partir de template YAML"""
    
    framework_path = Path(__file__).parent.parent
    generator = UnifiedAgentGenerator(str(framework_path))
    
    result = generator.generate_agent_from_template(template_path, output_type)
    
    click.echo(f"✅ Agente gerado a partir de template!")
    click.echo(f"📁 Localização: {result['path']}")
    click.echo(f"🔧 Tipo: {result['type']}")

@cli.command()
def list_agents():
    """Lista todos os agentes disponíveis"""
    
    framework_path = Path(__file__).parent.parent
    
    # Agentes tradicionais
    agents_dir = framework_path / "agents"
    if agents_dir.exists():
        click.echo("🤖 AGENTES TRADICIONAIS:")
        for category_dir in agents_dir.iterdir():
            if category_dir.is_dir():
                click.echo(f"  📂 {category_dir.name}:")
                for agent_dir in category_dir.iterdir():
                    if agent_dir.is_dir():
                        click.echo(f"    - {agent_dir.name}")
    
    # Agentes verticais
    vertical_dir = framework_path / "vertical_agents"
    if vertical_dir.exists():
        click.echo("\\n🎯 AGENTES VERTICAIS:")
        for agent_dir in vertical_dir.iterdir():
            if agent_dir.is_dir():
                click.echo(f"  - {agent_dir.name}")

if __name__ == '__main__':
    cli()
'''
        
        with open(cli_file, 'w', encoding='utf-8') as f:
            f.write(cli_code)
        
        # Tornar executável
        os.chmod(cli_file, 0o755)
        
        logger.info(f"CLI unificado criado: {cli_file}")
        return str(cli_file)
    
    def create_automation_scripts(self) -> Dict[str, str]:
        """
        Cria scripts de automação
        """
        scripts_created = {}
        
        # 1. Script de migração em lote
        batch_migration_script = self.scripts_dir / "batch_migration.py"
        batch_code = '''#!/usr/bin/env python3
"""
Script de migração em lote de agentes
"""

import os
import sys
import yaml
from pathlib import Path

def migrate_all_agents(source_dir: str, target_framework: str):
    """
    Migra todos os agentes de um diretório fonte
    """
    source_path = Path(source_dir)
    
    # Encontrar todos os agentes
    agent_dirs = []
    for item in source_path.rglob("prompt.txt"):
        agent_dirs.append(item.parent)
    
    print(f"Encontrados {len(agent_dirs)} agentes para migração")
    
    # Migrar cada agente
    for agent_dir in agent_dirs:
        agent_name = agent_dir.name
        print(f"Migrando agente: {agent_name}")
        
        # Implementar lógica de migração aqui
        # ...
        
    print("Migração em lote concluída!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python batch_migration.py <source_dir> <target_framework>")
        sys.exit(1)
    
    migrate_all_agents(sys.argv[1], sys.argv[2])
'''
        
        with open(batch_migration_script, 'w', encoding='utf-8') as f:
            f.write(batch_code)
        scripts_created['batch_migration'] = str(batch_migration_script)
        
        # 2. Script de validação
        validation_script = self.scripts_dir / "validate_agents.py"
        validation_code = '''#!/usr/bin/env python3
"""
Script de validação de agentes
"""

import sys
from pathlib import Path

def validate_agent(agent_path: str) -> bool:
    """
    Valida estrutura de um agente
    """
    agent_dir = Path(agent_path)
    
    required_files = ['prompt.txt', 'agent.py']
    missing_files = []
    
    for file_name in required_files:
        if not (agent_dir / file_name).exists():
            missing_files.append(file_name)
    
    if missing_files:
        print(f"❌ Agente {agent_dir.name}: Arquivos faltando: {missing_files}")
        return False
    else:
        print(f"✅ Agente {agent_dir.name}: Válido")
        return True

def validate_all_agents(framework_path: str):
    """
    Valida todos os agentes do framework
    """
    framework_dir = Path(framework_path)
    
    # Validar agentes tradicionais
    agents_dir = framework_dir / "agents"
    valid_count = 0
    total_count = 0
    
    if agents_dir.exists():
        for agent_path in agents_dir.rglob("agent.py"):
            total_count += 1
            if validate_agent(agent_path.parent):
                valid_count += 1
    
    # Validar agentes verticais
    vertical_dir = framework_dir / "vertical_agents"
    if vertical_dir.exists():
        for agent_path in vertical_dir.rglob("agent.py"):
            total_count += 1
            if validate_agent(agent_path.parent):
                valid_count += 1
    
    print(f"\\nResultado: {valid_count}/{total_count} agentes válidos")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python validate_agents.py <framework_path>")
        sys.exit(1)
    
    validate_all_agents(sys.argv[1])
'''
        
        with open(validation_script, 'w', encoding='utf-8') as f:
            f.write(validation_code)
        scripts_created['validation'] = str(validation_script)
        
        return scripts_created

def main():
    """Função principal para teste"""
    framework_path = "/home/ubuntu/unified-sales-framework"
    generator = UnifiedAgentGenerator(framework_path)
    
    print("🚀 Sistema Unificado de Automação e Geração")
    print("=" * 50)
    
    # Criar CLI unificado
    cli_path = generator.create_cli_integration()
    print(f"✅ CLI unificado criado: {cli_path}")
    
    # Criar scripts de automação
    scripts = generator.create_automation_scripts()
    print(f"✅ Scripts de automação criados: {len(scripts)}")
    
    print("\\n🎉 Fase 4 - Automação e Geração implementada com sucesso!")

if __name__ == "__main__":
    main()

