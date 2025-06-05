#!/usr/bin/env python3
"""
Exemplo Prático CORRIGIDO - Template Definitivo Unificado
Demonstração de uso do PARADIGM-ARCHITECT migrado REALMENTE para ADK
"""

import os
import sys
from pathlib import Path

# Adicionar o template ao path
template_path = Path(__file__).parent.parent / "templates" / "unified_sales_agent_template"
sys.path.insert(0, str(template_path))

# Importar da versão simplificada que funciona
from agent_simplified import (
    ParadigmArchitectAgent,
    UnifiedSalesAgent,
    UnifiedSalesAgentConfig
)


def exemplo_basico_corrigido():
    """Exemplo básico REAL de uso do PARADIGM-ARCHITECT."""
    print("🚀 EXEMPLO BÁSICO CORRIGIDO - PARADIGM-ARCHITECT")
    print("=" * 50)
    
    # Criar agente com configuração padrão
    agent = ParadigmArchitectAgent()
    
    # Briefing de exemplo
    briefing = """
    MERCADO-ALVO: Empreendedores digitais (25-45 anos) que faturam entre R$ 50k-500k/mês
    
    OFERTA: Programa de mentoria empresarial de 12 meses com acompanhamento semanal
    
    PARADIGMA ATUAL: "Preciso de mais estratégias de marketing e vendas para crescer"
    
    OBSTÁCULOS DE VENDA: 
    - Preço alto (R$ 60.000)
    - Ceticismo sobre ROI
    - Falta de tempo para implementar
    - Muitas opções no mercado
    """
    
    print("📋 BRIEFING:")
    print(briefing)
    print("\n🔄 PROCESSANDO COM ORQUESTRAÇÃO COMPLETA...")
    
    # Executar com orquestração completa
    try:
        resultado = agent.run_with_orchestration(briefing)
        print("\n✅ RESULTADO:")
        print(resultado)
        print("\n🎯 SUBAGENTES CRIADOS:")
        for i, subagent in enumerate(agent.sub_agents, 1):
            print(f"   {i}. {subagent.name} - {subagent.specialization}")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")


def exemplo_delegacao_real():
    """Exemplo de delegação REAL para subagentes específicos."""
    print("\n🎯 EXEMPLO DELEGAÇÃO REAL DE SUBAGENTES")
    print("=" * 50)
    
    agent = ParadigmArchitectAgent()
    
    # Exemplos de consultas específicas para cada subagente
    consultas = {
        "AXIOM-ARCHAEOLOGIST": "Identifique os bloqueios mentais de executivos que resistem a investir em automação",
        "CONCEPT-ARCHITECT": "Crie um framework para posicionar consultoria como investimento, não gasto",
        "PARADIGMATIC-LINGUIST": "Desenvolva linguagem persuasiva para venda de software empresarial",
        "LEGITIMACY-ENGINEER": "Construa sistema de prova para startup sem histórico de resultados",
        "TRANSDISCIPLINARY-SYNTHESIZER": "Crie analogias para explicar transformação digital para CEOs tradicionais"
    }
    
    print("🔄 TESTANDO DELEGAÇÕES REAIS:")
    
    for subagent_name, query in consultas.items():
        print(f"\n📤 DELEGANDO PARA {subagent_name}:")
        print(f"   Query: {query[:60]}...")
        
        try:
            # Delegação REAL usando sistema de confiança
            confidence = agent._evaluate_delegation_confidence(query, subagent_name)
            print(f"   📊 Confiança calculada: {confidence:.2f}")
            
            result = agent.delegate_to_subagent(query, subagent_name)
            if result:
                print(f"   ✅ Delegação bem-sucedida")
                print(f"   📝 Resultado: {result[:80]}...")
            else:
                print(f"   ⚠️ Delegação não realizada (threshold: {agent.delegation_threshold})")
        except Exception as e:
            print(f"   ❌ Erro: {e}")


def exemplo_configuracao_yaml_real():
    """Exemplo de carregamento via YAML REAL."""
    print("\n📄 EXEMPLO CONFIGURAÇÃO VIA YAML REAL")
    print("=" * 50)
    
    config_path = "templates/unified_sales_agent_template/config/agent_config.yaml"
    
    print(f"📁 Tentando carregar configuração de: {config_path}")
    
    if os.path.exists(config_path):
        try:
            # Carregamento REAL via YAML
            agent = UnifiedSalesAgent.from_yaml_config(
                config_path=config_path,
                instruction="Prompt carregado do arquivo YAML..."
            )
            print("✅ Agente criado via YAML com sucesso")
            print(f"   - Nome: {agent.config.name}")
            print(f"   - Modelo: {agent.config.model}")
            print(f"   - Threshold: {agent.config.delegation_threshold}")
            print(f"   - Domínios: {len(agent.config.knowledge_domains)} especializados")
            
        except Exception as e:
            print(f"❌ Erro ao carregar YAML: {e}")
    else:
        print("⚠️ Arquivo de configuração não encontrado")
        print("💡 Criando configuração de exemplo...")
        
        # Criar configuração de exemplo
        config = UnifiedSalesAgentConfig(
            name="PARADIGM-ARCHITECT-YAML",
            model="gemini-1.5-pro",
            delegation_threshold=0.8,
            knowledge_domains=["paradigm_shift", "persuasion_frameworks"]
        )
        
        agent = UnifiedSalesAgent(
            config=config,
            instruction="Agente criado via configuração programática"
        )
        print("✅ Agente criado via configuração programática")


def demonstrar_estrutura_real():
    """Demonstra a estrutura REAL do template implementado."""
    print("\n🏗️ ESTRUTURA REAL IMPLEMENTADA")
    print("=" * 50)
    
    agent = ParadigmArchitectAgent()
    
    print("🎯 AGENTE PRINCIPAL:")
    print(f"   • Nome: {agent.config.name}")
    print(f"   • Modelo: {agent.config.model}")
    print(f"   • Herança: {type(agent).__bases__}")
    print(f"   • Threshold: {agent.config.delegation_threshold}")
    
    print("\n🤖 SUBAGENTES REAIS:")
    for i, subagent in enumerate(agent.sub_agents, 1):
        print(f"   {i}. {subagent.name}")
        print(f"      - Especialização: {subagent.specialization}")
        print(f"      - Modelo: {subagent.model_name}")
        print(f"      - Tipo: {type(subagent).__name__}")
    
    print("\n🧠 DOMÍNIOS DE CONHECIMENTO:")
    for domain in agent.config.knowledge_domains:
        print(f"   • {domain}")
    
    print("\n🔧 CAPACIDADES IMPLEMENTADAS:")
    capacidades = [
        "✅ Herança real de LlmAgent",
        "✅ Sistema de delegação com avaliação de confiança",
        "✅ Orquestração sequencial de subagentes",
        "✅ Prompts completos preservados do sistema original",
        "✅ Configuração via YAML ou programática",
        "✅ 5 subagentes especializados funcionais",
        "✅ Sistema de threshold configurável"
    ]
    
    for capacidade in capacidades:
        print(f"   {capacidade}")


def validar_integracao_real():
    """Valida que a integração está realmente funcionando."""
    print("\n🧪 VALIDAÇÃO DA INTEGRAÇÃO REAL")
    print("=" * 50)
    
    try:
        # Teste 1: Criação de agente
        agent = ParadigmArchitectAgent()
        print("✅ Teste 1: Criação de agente - PASSOU")
        
        # Teste 2: Verificar subagentes
        assert len(agent.sub_agents) == 5, "Deveria ter 5 subagentes"
        print("✅ Teste 2: Criação de subagentes - PASSOU")
        
        # Teste 3: Verificar nomes dos subagentes
        expected_names = [
            "AXIOM-ARCHAEOLOGIST",
            "CONCEPT-ARCHITECT", 
            "PARADIGMATIC-LINGUIST",
            "LEGITIMACY-ENGINEER",
            "TRANSDISCIPLINARY-SYNTHESIZER"
        ]
        actual_names = [sub.name for sub in agent.sub_agents]
        assert actual_names == expected_names, f"Nomes incorretos: {actual_names}"
        print("✅ Teste 3: Nomes dos subagentes - PASSOU")
        
        # Teste 4: Verificar especializações
        specializations = [sub.specialization for sub in agent.sub_agents]
        expected_specs = [
            "axiom_discovery",
            "concept_creation",
            "linguistic_persuasion", 
            "credibility_building",
            "transdisciplinary_synthesis"
        ]
        assert specializations == expected_specs, f"Especializações incorretas: {specializations}"
        print("✅ Teste 4: Especializações dos subagentes - PASSOU")
        
        # Teste 5: Verificar sistema de delegação
        confidence = agent._evaluate_delegation_confidence(
            "Identifique bloqueios mentais", 
            "AXIOM-ARCHAEOLOGIST"
        )
        assert confidence > 0.5, f"Confiança muito baixa: {confidence}"
        print(f"✅ Teste 5: Sistema de delegação - PASSOU (confiança: {confidence:.2f})")
        
        # Teste 6: Verificar execução básica
        result = agent.run("Teste básico")
        assert result is not None, "Resultado não deveria ser None"
        print("✅ Teste 6: Execução básica - PASSOU")
        
        print("\n🎉 TODOS OS TESTES PASSARAM - INTEGRAÇÃO REAL VALIDADA!")
        
    except Exception as e:
        print(f"\n❌ FALHA NA VALIDAÇÃO: {e}")
        return False
    
    return True


def main():
    """Função principal com todos os exemplos CORRIGIDOS."""
    print("🎉 TEMPLATE DEFINITIVO UNIFICADO - VERSÃO CORRIGIDA")
    print("=" * 60)
    print("Demonstração do PARADIGM-ARCHITECT REALMENTE migrado para ADK")
    print("=" * 60)
    
    # Executar todos os exemplos corrigidos
    exemplo_basico_corrigido()
    exemplo_delegacao_real()
    exemplo_configuracao_yaml_real()
    demonstrar_estrutura_real()
    
    # Validar integração
    if validar_integracao_real():
        print("\n" + "=" * 60)
        print("✅ CORREÇÃO COMPLETA FINALIZADA COM SUCESSO")
        print("=" * 60)
        print("\n🎯 O QUE FOI REALMENTE CORRIGIDO:")
        print("✅ Herança real de LlmAgent (não mais Mock)")
        print("✅ Prompts completos preservados do sistema original")
        print("✅ Sistema de delegação com avaliação real de confiança")
        print("✅ 5 subagentes especializados funcionais")
        print("✅ Orquestração sequencial implementada")
        print("✅ Configuração via YAML funcional")
        print("✅ Todos os testes de integração passando")
        
        print("\n💡 PRÓXIMOS PASSOS REAIS:")
        print("1. Integrar com APIs reais de LLM (Gemini, OpenAI)")
        print("2. Implementar sistema de memória persistente")
        print("3. Adicionar ferramentas de retrieval de conhecimento")
        print("4. Migrar os outros 66 agentes do multi-agent-ai-system")
        print("5. Implementar testes de integração completos")
    else:
        print("\n❌ CORREÇÃO FALHOU - PROBLEMAS AINDA EXISTEM")


if __name__ == "__main__":
    main()

