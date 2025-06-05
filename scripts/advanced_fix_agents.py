#!/usr/bin/env python3
"""
Sistema de Correção Avançada de Agentes Migrados

Corrige problemas de sintaxe e compatibilidade nos agentes migrados.
"""

import os
import re
from pathlib import Path


class AdvancedAgentFixSystem:
    """Sistema avançado para corrigir agentes migrados."""
    
    def __init__(self, agents_dir: str = "/home/ubuntu/unified-sales-framework/agents"):
        self.agents_dir = Path(agents_dir)
        self.fixed_count = 0
        self.error_count = 0
    
    def fix_all_agents(self):
        """Corrige todos os agentes migrados."""
        
        print("🔧 INICIANDO CORREÇÃO AVANÇADA DE AGENTES...")
        
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
        fixed_content = self.apply_advanced_fixes(content)
        
        # Salvar conteúdo corrigido
        with open(agent_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
    
    def apply_advanced_fixes(self, content: str) -> str:
        """Aplica correções avançadas."""
        
        # 1. Corrigir f-strings com aspas aninhadas
        content = re.sub(
            r'print\(f"🤖 \{self\.__dict__\.get\("agent_name", "Unknown"\)\} inicializado com especialização: \{self\.__dict__\.get\("specialization", "general"\)\}"\)',
            r'print(f"🤖 {self.get_attr(\'agent_name\', \'Unknown\')} inicializado com especialização: {self.get_attr(\'specialization\', \'general\')}")',
            content
        )
        
        # 2. Corrigir outras f-strings problemáticas
        content = re.sub(
            r'\{self\.__dict__\.get\("([^"]+)", "([^"]*)"\)\}',
            r'{self.get_attr("\1", "\2")}',
            content
        )
        
        # 3. Simplificar acesso a atributos usando get_attr
        content = re.sub(
            r'self\.__dict__\["([^"]+)"\]',
            r'self.get_attr("\1")',
            content
        )
        
        # 4. Corrigir definições de atributos para usar setattr
        content = re.sub(
            r'(\s+)self\.__dict__\["([^"]+)"\] = (.+)',
            r'\1setattr(self, "\2", \3)',
            content
        )
        
        # 5. Adicionar método get_attr melhorado se não existir
        if 'def get_attr(' not in content:
            method_addition = '''
    def get_attr(self, name: str, default=None):
        """Acessa atributo de forma segura."""
        return getattr(self, name, default)
    
    def set_attr(self, name: str, value):
        """Define atributo de forma segura."""
        setattr(self, name, value)
'''
            # Inserir antes do método get_capabilities
            content = content.replace(
                '    def get_capabilities(self)',
                method_addition + '    def get_capabilities(self)'
            )
        
        # 6. Corrigir verificações de atributos
        content = re.sub(
            r'"([^"]+)" in self\.__dict__',
            r'hasattr(self, "\1")',
            content
        )
        
        # 7. Corrigir uso em f-strings restantes
        content = re.sub(
            r'\{self\.get_attr\("([^"]+)"\)\}',
            r'{self.get_attr("\1", "")}',
            content
        )
        
        return content


def main():
    """Executa correção avançada de todos os agentes."""
    
    print("🔧 SISTEMA DE CORREÇÃO AVANÇADA DE AGENTES")
    print("="*50)
    
    fixer = AdvancedAgentFixSystem()
    fixer.fix_all_agents()
    
    print("\n✅ CORREÇÃO AVANÇADA CONCLUÍDA!")


if __name__ == "__main__":
    main()

