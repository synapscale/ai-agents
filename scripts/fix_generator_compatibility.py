#!/usr/bin/env python3
"""
Script para corrigir compatibilidade entre gerador e estrutura corrigida
"""

import os
import re
from pathlib import Path

def fix_unified_agent_generator():
    """Corrige o gerador para usar nomes de arquivo padrão"""
    
    generator_path = Path("/home/ubuntu/unified-sales-framework/scripts/unified_agent_generator.py")
    
    # Ler arquivo atual
    with open(generator_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituições para padronizar nomes de arquivo
    replacements = {
        'vertical_prompt.txt': 'prompt.txt',
        'vertical_agent.py': 'agent.py', 
        'vertical_tools.py': 'tools.py',
        'vertical_config.yaml': 'config.yaml',
        'vertical_knowledge': 'knowledge'
    }
    
    for old_name, new_name in replacements.items():
        content = content.replace(f'"{old_name}"', f'"{new_name}"')
        content = content.replace(f"'{old_name}'", f"'{new_name}'")
    
    # Corrigir método generate_vertical_agent para usar parâmetros corretos
    vertical_method_fix = '''
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
'''
    
    # Substituir método generate_vertical_agent
    pattern = r'def generate_vertical_agent\(self, config: AgentGenerationConfig\).*?(?=def|\Z)'
    content = re.sub(pattern, vertical_method_fix.strip(), content, flags=re.DOTALL)
    
    # Salvar arquivo corrigido
    with open(generator_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Gerador corrigido para compatibilidade com estrutura padrão")

if __name__ == "__main__":
    fix_unified_agent_generator()

