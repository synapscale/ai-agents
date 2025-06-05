"""
CLI Unificado para Unified Sales Framework - VERSÃO FINAL CORRIGIDA
Integra Magenerator com ADK CLI
"""

import click
import yaml
import sys
import os
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
    else:
        prompt_content = f"Você é um especialista em {specialization}."
    
    try:
        # Criar configuração
        config = AgentGenerationConfig(
            agent_name=agent_name,
            agent_type=agent_type,
            specialization=specialization,
            category=category,
            prompt_content=prompt_content
        )
        
        if agent_type == 'vertical':
            result = generator.generate_vertical_agent(config)
        else:
            result = generator.generate_traditional_agent(config)
        
        if result.get('success', False):
            click.echo(f"✅ Agente {agent_name} criado com sucesso!")
            click.echo(f"📁 Localização: {result.get('agent_path', 'N/A')}")
            click.echo(f"🔧 Tipo: {agent_type}")
        else:
            click.echo(f"❌ Erro ao criar agente {agent_name}: {result.get('error', 'Erro desconhecido')}")
            
    except Exception as e:
        click.echo(f"❌ Erro: {e}")

@cli.command()
def list_agents():
    """Lista todos os agentes disponíveis"""
    
    framework_path = Path(__file__).parent.parent
    
    # Listar agentes tradicionais
    agents_path = framework_path / "agents"
    click.echo("🤖 AGENTES TRADICIONAIS:")
    
    if agents_path.exists():
        for category_dir in agents_path.iterdir():
            if category_dir.is_dir():
                agents_in_category = [d.name for d in category_dir.iterdir() if d.is_dir()]
                if agents_in_category:
                    click.echo(f"  📂 {category_dir.name}:")
                    for agent in agents_in_category:
                        click.echo(f"    - {agent}")
    
    # Listar agentes verticais
    vertical_path = framework_path / "vertical_agents"
    click.echo("🎯 AGENTES VERTICAIS:")
    
    if vertical_path.exists():
        for agent_dir in vertical_path.iterdir():
            if agent_dir.is_dir() and agent_dir.name != "__pycache__":
                click.echo(f"  - {agent_dir.name}")

def load_yaml_template(template_path):
    """Carrega template YAML"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        click.echo(f"❌ Erro ao carregar template: {e}")
        return None

@cli.command()
@click.argument('template_path')
@click.option('--type', type=click.Choice(['traditional', 'vertical']), 
              help='Tipo de agente a gerar')
def from_template(template_path, type):
    """Gera agente a partir de template YAML"""
    click.echo(f"📋 Carregando template: {template_path}")
    
    template_data = load_yaml_template(template_path)
    if not template_data:
        return
    
    # Extrair dados do template
    name = template_data.get('name', 'template_agent')
    agent_type = template_data.get('type', type or 'traditional')
    category = template_data.get('category', 'general')
    specialization = template_data.get('specialization', 'general')
    
    # Extrair prompt das instruções
    agent_config = template_data.get('agent', {})
    prompt = agent_config.get('instructions', 'Agente gerado a partir de template')
    
    click.echo(f"🤖 Gerando agente {name} do tipo {agent_type}")
    
    try:
        framework_path = Path(__file__).parent.parent
        generator = UnifiedAgentGenerator(str(framework_path))
        
        # Criar configuração
        config = AgentGenerationConfig(
            agent_name=name,
            agent_type=agent_type,
            specialization=specialization,
            category=category,
            prompt_content=prompt
        )
        
        if agent_type == 'vertical':
            success = generator.generate_vertical_agent(
                name=name,
                specialization=specialization,
                prompt=prompt,
                template_data=template_data
            )
        else:
            success = generator.generate_traditional_agent(
                name=name,
                category=category,
                specialization=specialization,
                prompt=prompt,
                template_data=template_data
            )
        
        if success:
            click.echo(f"✅ Agente {name} criado com sucesso a partir do template!")
            if agent_type == 'vertical':
                click.echo(f"📁 Localização: {os.path.join(os.getcwd(), 'vertical_agents', name)}")
            else:
                click.echo(f"📁 Localização: {os.path.join(os.getcwd(), 'agents', category, name)}")
            click.echo(f"🔧 Tipo: {agent_type}")
        else:
            click.echo(f"❌ Erro ao criar agente {name}: {result.get('error', 'Erro desconhecido')}")
            
    except Exception as e:
        click.echo(f"❌ Erro: {e}")

if __name__ == '__main__':
    cli()

