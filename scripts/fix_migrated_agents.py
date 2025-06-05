#!/usr/bin/env python3
"""
Sistema de Correção de Agentes Migrados

Corrige problemas de compatibilidade com Pydantic nos agentes migrados.
"""

import os
import re
from pathlib import Path
from typing import List


class AgentFixSystem:
    """Sistema para corrigir agentes migrados."""
    
    def __init__(self, agents_dir: str = "/home/ubuntu/unified-sales-framework/agents"):
        self.agents_dir = Path(agents_dir)
        self.fixed_count = 0
        self.error_count = 0
    
    def fix_all_agents(self):
        """Corrige todos os agentes migrados."""
        
        print("🔧 INICIANDO CORREÇÃO DE AGENTES MIGRADOS...")
        
        # Encontrar todos os arquivos agent.py
        agent_files = list(self.agents_dir.glob("**/agent.py"))
        
        print(f"📁 Encontrados {len(agent_files)} agentes para correção")
        
        for agent_file in agent_files:
            try:
                self.fix_single_agent(agent_file)
                self.fixed_count += 1
                print(f"   ✅ {agent_file.parent.name} corrigido")
            except Exception as e:
                self.error_count += 1
                print(f"   ❌ Erro em {agent_file.parent.name}: {e}")
        
        print(f"\n📊 CORREÇÃO CONCLUÍDA:")
        print(f"   ✅ Corrigidos: {self.fixed_count}")
        print(f"   ❌ Erros: {self.error_count}")
    
    def fix_single_agent(self, agent_file: Path):
        """Corrige um arquivo de agente individual."""
        
        # Ler conteúdo atual
        with open(agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Aplicar correções
        fixed_content = self.apply_fixes(content)
        
        # Salvar conteúdo corrigido
        with open(agent_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
    
    def apply_fixes(self, content: str) -> str:
        """Aplica todas as correções necessárias."""
        
        # 1. Corrigir problema com Pydantic - usar __dict__ para atributos dinâmicos
        content = re.sub(
            r'(\s+)self\.prompt_file = (.+)',
            r'\1self.__dict__["prompt_file"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.instruction = (.+)',
            r'\1self.__dict__["instruction"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.specialization = (.+)',
            r'\1self.__dict__["specialization"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.category = (.+)',
            r'\1self.__dict__["category"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.agent_name = (.+)',
            r'\1self.__dict__["agent_name"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.knowledge_toolset = (.+)',
            r'\1self.__dict__["knowledge_toolset"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.model_name = (.+)',
            r'\1self.__dict__["model_name"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.instructions = (.+)',
            r'\1self.__dict__["instructions"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.sub_agents = (.+)',
            r'\1self.__dict__["sub_agents"] = \2',
            content
        )
        
        content = re.sub(
            r'(\s+)self\.config = (.+)',
            r'\1self.__dict__["config"] = \2',
            content
        )
        
        # 2. Corrigir acesso aos atributos
        content = re.sub(
            r'self\.prompt_file',
            r'self.__dict__["prompt_file"]',
            content
        )
        
        content = re.sub(
            r'self\.instruction',
            r'self.__dict__["instruction"]',
            content
        )
        
        content = re.sub(
            r'self\.specialization',
            r'self.__dict__["specialization"]',
            content
        )
        
        content = re.sub(
            r'self\.category',
            r'self.__dict__["category"]',
            content
        )
        
        content = re.sub(
            r'self\.agent_name',
            r'self.__dict__["agent_name"]',
            content
        )
        
        content = re.sub(
            r'self\.sub_agents',
            r'self.__dict__["sub_agents"]',
            content
        )
        
        content = re.sub(
            r'self\.config',
            r'self.__dict__["config"]',
            content
        )
        
        # 3. Corrigir f-strings que usam os atributos
        content = re.sub(
            r'{self\.__dict__\["agent_name"\]}',
            r'{self.__dict__.get("agent_name", "Unknown")}',
            content
        )
        
        content = re.sub(
            r'{self\.__dict__\["specialization"\]}',
            r'{self.__dict__.get("specialization", "general")}',
            content
        )
        
        # 4. Adicionar método para acessar atributos de forma segura
        if 'def get_attr(' not in content:
            method_addition = '''
    def get_attr(self, name: str, default=None):
        """Acessa atributo de forma segura."""
        return self.__dict__.get(name, default)
'''
            # Inserir antes do método get_capabilities
            content = content.replace(
                '    def get_capabilities(self)',
                method_addition + '    def get_capabilities(self)'
            )
        
        # 5. Corrigir uso de hasattr
        content = re.sub(
            r'hasattr\(self, \'knowledge_toolset\'\)',
            r'"knowledge_toolset" in self.__dict__',
            content
        )
        
        content = re.sub(
            r'hasattr\(self, \'run\'\)',
            r'hasattr(self, "run")',
            content
        )
        
        return content


def main():
    """Executa correção de todos os agentes."""
    
    print("🔧 SISTEMA DE CORREÇÃO DE AGENTES MIGRADOS")
    print("="*50)
    
    fixer = AgentFixSystem()
    fixer.fix_all_agents()
    
    print("\n✅ CORREÇÃO CONCLUÍDA!")


if __name__ == "__main__":
    main()

