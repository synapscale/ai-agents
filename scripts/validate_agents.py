#!/usr/bin/env python3
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
        for agent_path in vertical_dir.rglob("vertical_agent.py"):
            total_count += 1
            if validate_agent(agent_path.parent):
                valid_count += 1
    
    print(f"\nResultado: {valid_count}/{total_count} agentes válidos")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python validate_agents.py <framework_path>")
        sys.exit(1)
    
    validate_all_agents(sys.argv[1])
