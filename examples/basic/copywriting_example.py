#!/usr/bin/env python3
"""
Exemplo Prático: Geração de Copy Persuasivo

Este exemplo demonstra como usar o agente Paradigm Architect para criar
copy persuasivo para uma página de vendas.
"""

import os
import sys
import argparse
from pathlib import Path

# Adicionar diretório raiz ao path para importações
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

try:
    from unified_sales_framework.core.fixed_adk import create_unified_agent
except ImportError:
    print("Erro ao importar o framework. Certifique-se de que está no diretório correto.")
    print(f"Diretório atual: {os.getcwd()}")
    print(f"Diretório raiz: {root_dir}")
    sys.exit(1)

def generate_persuasive_copy(product_name, target_audience, main_problem, main_benefit, price):
    """
    Gera copy persuasivo usando o agente Paradigm Architect.
    
    Args:
        product_name (str): Nome do produto ou serviço
        target_audience (str): Descrição do público-alvo
        main_problem (str): Principal problema que o produto resolve
        main_benefit (str): Principal benefício do produto
        price (str): Preço do produto
        
    Returns:
        str: Copy persuasivo gerado
    """
    print(f"🚀 Gerando copy persuasivo para: {product_name}")
    
    # Criar agente de copywriting
    agent = create_unified_agent('paradigm_architect', 'Especialista em transformação paradigmática')
    
    # Construir briefing
    briefing = f"""
    Produto: {product_name}
    Público: {target_audience}
    Problema principal: {main_problem}
    Benefício principal: {main_benefit}
    Preço: {price}
    """
    
    # Construir prompt
    prompt = f"""
    Com base neste briefing, crie uma página de vendas persuasiva:
    {briefing}
    
    Inclua:
    1. Headline principal que capture atenção
    2. 3 subtítulos que mantenham o interesse
    3. 5 benefícios principais com descrições convincentes
    4. 3 objeções comuns respondidas de forma persuasiva
    5. Call to action final irresistível
    6. Elementos de escassez e urgência
    
    Use princípios de persuasão como:
    - Prova social
    - Autoridade
    - Reciprocidade
    - Escassez
    - Compromisso e consistência
    """
    
    # Processar com o agente
    print("⏳ Processando... (pode levar alguns segundos)")
    result = agent.process(prompt)
    
    print("✅ Copy persuasivo gerado com sucesso!")
    return result

def save_to_file(content, output_file):
    """Salva o conteúdo em um arquivo."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"📄 Resultado salvo em: {output_file}")

def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description='Gerador de Copy Persuasivo')
    parser.add_argument('--product', default='Curso de Marketing Digital', help='Nome do produto')
    parser.add_argument('--audience', default='Empreendedores iniciantes', help='Público-alvo')
    parser.add_argument('--problem', default='Dificuldade em atrair clientes online', help='Problema principal')
    parser.add_argument('--benefit', default='Aumento de 300% em leads qualificados em 60 dias', help='Benefício principal')
    parser.add_argument('--price', default='R$ 997,00', help='Preço do produto')
    parser.add_argument('--output', default='copy_persuasivo.md', help='Arquivo de saída')
    
    args = parser.parse_args()
    
    # Gerar copy
    copy = generate_persuasive_copy(
        args.product,
        args.audience,
        args.problem,
        args.benefit,
        args.price
    )
    
    # Salvar resultado
    save_to_file(copy, args.output)
    
    print("\n🎯 Exemplo concluído! Você pode usar este copy para sua página de vendas.")
    print("💡 Dica: Experimente com diferentes produtos e públicos para ver como o resultado muda.")

if __name__ == "__main__":
    main()

