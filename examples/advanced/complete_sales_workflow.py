#!/usr/bin/env python3
"""
Exemplo Avançado: Fluxo de Trabalho Completo de Vendas

Este exemplo demonstra como combinar múltiplos agentes para criar um
fluxo de trabalho completo de vendas, desde a análise de mercado até
o manejo de objeções.
"""

import os
import sys
import argparse
from pathlib import Path
import time

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

class SalesWorkflow:
    """Classe que implementa um fluxo de trabalho completo de vendas."""
    
    def __init__(self, product_name, target_audience, industry, price_point):
        """
        Inicializa o fluxo de trabalho de vendas.
        
        Args:
            product_name (str): Nome do produto ou serviço
            target_audience (str): Descrição do público-alvo
            industry (str): Indústria ou setor
            price_point (str): Faixa de preço
        """
        self.product_name = product_name
        self.target_audience = target_audience
        self.industry = industry
        self.price_point = price_point
        self.results = {}
    
    def run_market_analysis(self):
        """Executa análise de mercado usando o agente de analytics."""
        print("\n🔍 ETAPA 1: ANÁLISE DE MERCADO")
        
        analytics_agent = create_unified_agent('analytics_specialist', 'Especialista em análise')
        
        prompt = f"""
        Analise o mercado para este produto:
        
        Produto: {self.product_name}
        Público-alvo: {self.target_audience}
        Indústria: {self.industry}
        Faixa de preço: {self.price_point}
        
        Forneça:
        1. Tamanho estimado do mercado
        2. 5 principais concorrentes com pontos fortes e fracos
        3. 3 tendências atuais neste mercado
        4. 3 oportunidades de diferenciação
        5. 2 possíveis ameaças ou desafios
        """
        
        print("⏳ Analisando mercado... (pode levar alguns segundos)")
        start_time = time.time()
        result = analytics_agent.process(prompt)
        elapsed_time = time.time() - start_time
        
        print(f"✅ Análise de mercado concluída em {elapsed_time:.2f} segundos")
        self.results['market_analysis'] = result
        return result
    
    def create_persuasive_copy(self):
        """Cria copy persuasivo baseado na análise de mercado."""
        print("\n✍️ ETAPA 2: CRIAÇÃO DE COPY PERSUASIVO")
        
        # Verificar se a análise de mercado foi realizada
        if 'market_analysis' not in self.results:
            print("⚠️ Análise de mercado não encontrada. Executando análise primeiro...")
            self.run_market_analysis()
        
        copy_agent = create_unified_agent('persuasion_copywriter', 'Especialista em persuasão')
        
        prompt = f"""
        Com base nesta análise de mercado, crie um copy persuasivo para uma página de vendas:
        
        {self.results['market_analysis']}
        
        Produto: {self.product_name}
        Público-alvo: {self.target_audience}
        Indústria: {self.industry}
        Faixa de preço: {self.price_point}
        
        O copy deve incluir:
        1. Headline principal impactante
        2. 3 subtítulos persuasivos
        3. 5 benefícios principais com descrições
        4. 3 depoimentos fictícios (indicar que são exemplos)
        5. Seção de garantia e redução de risco
        6. Call to action principal
        7. P.S. final persuasivo
        """
        
        print("⏳ Criando copy persuasivo... (pode levar alguns segundos)")
        start_time = time.time()
        result = copy_agent.process(prompt)
        elapsed_time = time.time() - start_time
        
        print(f"✅ Copy persuasivo criado em {elapsed_time:.2f} segundos")
        self.results['persuasive_copy'] = result
        return result
    
    def generate_email_sequence(self):
        """Gera sequência de emails para nutrição de leads."""
        print("\n📧 ETAPA 3: SEQUÊNCIA DE EMAILS")
        
        email_agent = create_unified_agent('retention_architect', 'Especialista em retenção')
        
        prompt = f"""
        Crie uma sequência de 5 emails para nutrição de leads:
        
        Produto: {self.product_name}
        Público-alvo: {self.target_audience}
        Indústria: {self.industry}
        
        Para cada email, forneça:
        1. Assunto
        2. Corpo do email
        3. Call to action
        4. Momento ideal para envio (ex: dia 1, dia 3, etc.)
        
        A sequência deve seguir esta estrutura:
        - Email 1: Boas-vindas e entrega de valor inicial
        - Email 2: Problema principal e como o produto resolve
        - Email 3: Caso de sucesso/história de transformação
        - Email 4: Objeções comuns respondidas
        - Email 5: Oferta final com senso de urgência
        """
        
        print("⏳ Gerando sequência de emails... (pode levar alguns segundos)")
        start_time = time.time()
        result = email_agent.process(prompt)
        elapsed_time = time.time() - start_time
        
        print(f"✅ Sequência de emails gerada em {elapsed_time:.2f} segundos")
        self.results['email_sequence'] = result
        return result
    
    def create_objection_handling(self):
        """Cria script de manejo de objeções."""
        print("\n🛡️ ETAPA 4: MANEJO DE OBJEÇÕES")
        
        objection_agent = create_unified_agent('paradigm_architect', 'Especialista em objeções')
        
        prompt = f"""
        Crie um script de manejo de objeções para vendedores:
        
        Produto: {self.product_name}
        Público-alvo: {self.target_audience}
        Indústria: {self.industry}
        Faixa de preço: {self.price_point}
        
        Para cada uma das 5 objeções mais comuns, forneça:
        1. A objeção exata
        2. O que realmente significa (subtexto)
        3. Resposta empática inicial
        4. Argumentos principais para superar a objeção
        5. Pergunta de fechamento após responder
        
        Use princípios de psicologia de vendas e persuasão.
        """
        
        print("⏳ Criando script de manejo de objeções... (pode levar alguns segundos)")
        start_time = time.time()
        result = objection_agent.process(prompt)
        elapsed_time = time.time() - start_time
        
        print(f"✅ Script de manejo de objeções criado em {elapsed_time:.2f} segundos")
        self.results['objection_handling'] = result
        return result
    
    def generate_sales_dashboard(self):
        """Gera especificação para dashboard de vendas."""
        print("\n📊 ETAPA 5: DASHBOARD DE VENDAS")
        
        analytics_agent = create_unified_agent('analytics_specialist', 'Especialista em análise')
        
        prompt = f"""
        Crie uma especificação para um dashboard de vendas:
        
        Produto: {self.product_name}
        Indústria: {self.industry}
        
        O dashboard deve incluir:
        1. 5-7 KPIs principais a serem monitorados
        2. Descrição de cada gráfico/visualização
        3. Fontes de dados necessárias
        4. Frequência de atualização recomendada
        5. Alertas e gatilhos automáticos
        
        Foque em métricas que realmente impactam o resultado de vendas.
        """
        
        print("⏳ Gerando especificação de dashboard... (pode levar alguns segundos)")
        start_time = time.time()
        result = analytics_agent.process(prompt)
        elapsed_time = time.time() - start_time
        
        print(f"✅ Especificação de dashboard gerada em {elapsed_time:.2f} segundos")
        self.results['sales_dashboard'] = result
        return result
    
    def run_complete_workflow(self):
        """Executa o fluxo de trabalho completo."""
        print(f"\n🚀 INICIANDO FLUXO DE TRABALHO COMPLETO PARA: {self.product_name}")
        print(f"Público-alvo: {self.target_audience}")
        print(f"Indústria: {self.industry}")
        print(f"Faixa de preço: {self.price_point}")
        
        # Executar todas as etapas
        self.run_market_analysis()
        self.create_persuasive_copy()
        self.generate_email_sequence()
        self.create_objection_handling()
        self.generate_sales_dashboard()
        
        print("\n🎉 FLUXO DE TRABALHO COMPLETO FINALIZADO!")
        return self.results
    
    def save_results(self, output_dir):
        """Salva todos os resultados em arquivos separados."""
        # Criar diretório se não existir
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Salvar cada resultado em um arquivo separado
        for key, content in self.results.items():
            file_path = output_path / f"{key}.md"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📄 {key} salvo em: {file_path}")
        
        # Criar índice
        index_path = output_path / "00_index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(f"# Fluxo de Trabalho de Vendas: {self.product_name}\n\n")
            f.write(f"**Público-alvo:** {self.target_audience}\n")
            f.write(f"**Indústria:** {self.industry}\n")
            f.write(f"**Faixa de preço:** {self.price_point}\n\n")
            f.write("## Arquivos Gerados\n\n")
            for key in self.results.keys():
                f.write(f"- [{key.replace('_', ' ').title()}]({key}.md)\n")
        
        print(f"📄 Índice salvo em: {index_path}")
        return index_path

def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description='Fluxo de Trabalho Completo de Vendas')
    parser.add_argument('--product', default='Software de Automação de Marketing', help='Nome do produto')
    parser.add_argument('--audience', default='Pequenas e médias empresas', help='Público-alvo')
    parser.add_argument('--industry', default='Marketing Digital', help='Indústria ou setor')
    parser.add_argument('--price', default='R$ 497/mês', help='Faixa de preço')
    parser.add_argument('--output', default='./sales_workflow_output', help='Diretório de saída')
    
    args = parser.parse_args()
    
    # Criar e executar fluxo de trabalho
    workflow = SalesWorkflow(
        args.product,
        args.audience,
        args.industry,
        args.price
    )
    
    workflow.run_complete_workflow()
    index_path = workflow.save_results(args.output)
    
    print(f"\n🎯 Fluxo de trabalho completo gerado! Veja o índice em: {index_path}")
    print("💡 Dica: Este é apenas um exemplo. Personalize o fluxo para suas necessidades específicas.")

if __name__ == "__main__":
    main()

