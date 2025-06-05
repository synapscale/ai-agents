#!/usr/bin/env python3
"""
Exemplo Prático: Integração de API

Este exemplo demonstra como usar o agente API Integration Specialist para
gerar código de integração com APIs de pagamento.
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

def generate_api_integration(platform, features, output_file):
    """
    Gera código de integração com API usando o agente API Integration Specialist.
    
    Args:
        platform (str): Plataforma de pagamento (ex: Hotmart, Stripe)
        features (list): Lista de funcionalidades desejadas
        output_file (str): Arquivo para salvar o código gerado
        
    Returns:
        str: Código de integração gerado
    """
    print(f"🚀 Gerando integração com API: {platform}")
    
    # Criar agente de integração de API
    agent = create_unified_agent('api_integration_specialist', 'Especialista em APIs')
    
    # Construir lista de funcionalidades
    features_text = "\n".join([f"{i+1}. {feature}" for i, feature in enumerate(features)])
    
    # Construir prompt
    prompt = f"""
    Preciso integrar a API do {platform} para as seguintes funcionalidades:
    {features_text}
    
    Por favor, forneça:
    1. Código Python completo com exemplos
    2. Explicação de cada função
    3. Instruções de configuração
    4. Tratamento de erros
    5. Exemplos de uso
    
    Use as melhores práticas de programação e segurança.
    """
    
    # Processar com o agente
    print("⏳ Processando... (pode levar alguns segundos)")
    result = agent.process(prompt)
    
    # Salvar resultado
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✅ Código de integração gerado e salvo em: {output_file}")
    return result

def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description='Gerador de Integração de API')
    parser.add_argument('--platform', default='Hotmart', help='Plataforma de pagamento')
    parser.add_argument('--output', default='api_integration.py', help='Arquivo de saída')
    
    args = parser.parse_args()
    
    # Funcionalidades padrão
    features = [
        "Verificar status de compra",
        "Gerar link de pagamento",
        "Configurar webhook de compra aprovada",
        "Emitir reembolso",
        "Consultar métricas de vendas"
    ]
    
    # Gerar integração
    generate_api_integration(args.platform, features, args.output)
    
    print("\n🎯 Exemplo concluído! Você pode usar este código para integrar com a API.")
    print("💡 Dica: Revise o código gerado e ajuste conforme necessário para seu caso específico.")
    print("⚠️ Importante: Sempre teste o código em ambiente de desenvolvimento antes de usar em produção.")

if __name__ == "__main__":
    main()

