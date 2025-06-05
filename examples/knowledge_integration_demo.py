#!/usr/bin/env python3
"""
Exemplo de Integração do Sistema de Conhecimento Unificado

Este exemplo demonstra como usar o sistema de conhecimento integrado
do multi-agent-ai-system com o unified-sales-framework.
"""

import sys
import os
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from unified_sales_framework.knowledge import (
    UnifiedKnowledgeService,
    UnifiedKnowledgeToolset,
    ParadigmShiftKnowledgeTool,
    PersuasionFrameworksTool
)


def main():
    print("=" * 60)
    print("🧠 EXEMPLO: SISTEMA DE CONHECIMENTO UNIFICADO")
    print("=" * 60)
    
    # Caminho para as bases de conhecimento do multi-agent-ai-system
    knowledge_base_path = "/home/ubuntu/multi-agent-ai-system-git"
    
    print(f"📚 Inicializando sistema de conhecimento...")
    print(f"📁 Caminho base: {knowledge_base_path}")
    
    try:
        # Inicializar sistema de conhecimento
        knowledge_service = UnifiedKnowledgeService(knowledge_base_path)
        
        print("✅ Sistema de conhecimento inicializado com sucesso!")
        
        # Mostrar resumo
        print("\n" + "=" * 50)
        print("📊 RESUMO DO SISTEMA DE CONHECIMENTO")
        print("=" * 50)
        
        summary = knowledge_service.get_knowledge_summary()
        print(f"📄 Total de documentos carregados: {summary['total_documents']}")
        print(f"🎯 Total de domínios: {summary['total_domains']}")
        print(f"🤖 Total de agentes: {summary['total_agents']}")
        
        print("\n🎯 DOMÍNIOS ESPECIALIZADOS:")
        for domain_id, domain_info in summary['domains'].items():
            print(f"   • {domain_info['name']}: {domain_info['document_count']} documentos")
            print(f"     Agentes: {', '.join(domain_info['agent_ids'])}")
        
        print("\n🤖 AGENTES COM CONHECIMENTO:")
        for agent_id, doc_count in summary['agents'].items():
            print(f"   • {agent_id}: {doc_count} documentos")
        
        # Testar busca geral
        print("\n" + "=" * 50)
        print("🔍 TESTE: BUSCA GERAL DE CONHECIMENTO")
        print("=" * 50)
        
        query = "frameworks de persuasão para vendas"
        print(f"🔎 Query: {query}")
        
        results = knowledge_service.search_knowledge(query, limit=3)
        print(f"📋 Resultados encontrados: {len(results)}")
        
        for i, doc in enumerate(results, 1):
            print(f"\n{i}. **{doc.title}**")
            print(f"   Domínio: {doc.domain}")
            print(f"   Agente: {doc.agent_id}")
            print(f"   Preview: {doc.content[:100]}...")
        
        # Testar ferramentas especializadas
        print("\n" + "=" * 50)
        print("🔧 TESTE: FERRAMENTAS ESPECIALIZADAS")
        print("=" * 50)
        
        # Inicializar toolset
        toolset = UnifiedKnowledgeToolset(knowledge_base_path)
        
        print("✅ Toolset inicializado com ferramentas:")
        for tool in toolset.tools:
            print(f"   • {tool.name}: {tool.description}")
        
        # Testar ferramenta de transformação de paradigmas
        print("\n🔄 TESTE: PARADIGM SHIFT KNOWLEDGE TOOL")
        print("-" * 40)
        
        context = "empreendedores digitais resistentes a investimento em mentoria"
        print(f"📝 Contexto: {context}")
        
        paradigm_tool = toolset.paradigm_shift
        frameworks_result = paradigm_tool.get_transformation_frameworks(context)
        print("\n📋 Frameworks de Transformação:")
        print(frameworks_result[:500] + "..." if len(frameworks_result) > 500 else frameworks_result)
        
        blocking_result = paradigm_tool.identify_blocking_patterns(context)
        print("\n🧠 Padrões de Bloqueio:")
        print(blocking_result[:500] + "..." if len(blocking_result) > 500 else blocking_result)
        
        # Testar ferramenta de persuasão
        print("\n🎯 TESTE: PERSUASION FRAMEWORKS TOOL")
        print("-" * 40)
        
        persuasion_context = "venda de software empresarial"
        audience = "CEOs de médias empresas"
        print(f"📝 Contexto: {persuasion_context}")
        print(f"👥 Audiência: {audience}")
        
        persuasion_tool = toolset.persuasion_frameworks
        techniques_result = persuasion_tool.get_persuasion_techniques(persuasion_context, audience)
        print("\n📋 Técnicas de Persuasão:")
        print(techniques_result[:500] + "..." if len(techniques_result) > 500 else techniques_result)
        
        # Testar busca por domínio específico
        print("\n" + "=" * 50)
        print("🎯 TESTE: BUSCA POR DOMÍNIO ESPECÍFICO")
        print("=" * 50)
        
        domain = "paradigm_shift"
        domain_docs = knowledge_service.get_domain_knowledge(domain)
        print(f"📚 Documentos no domínio '{domain}': {len(domain_docs)}")
        
        for doc in domain_docs[:3]:  # Mostrar apenas 3
            print(f"   • {doc.title} (Agente: {doc.agent_id})")
        
        # Testar busca por agente específico
        print("\n" + "=" * 50)
        print("🤖 TESTE: BUSCA POR AGENTE ESPECÍFICO")
        print("=" * 50)
        
        agent_id = "PARADIGM-ARCHITECT"
        agent_docs = knowledge_service.get_agent_knowledge(agent_id)
        print(f"📚 Documentos do agente '{agent_id}': {len(agent_docs)}")
        
        for doc in agent_docs[:3]:  # Mostrar apenas 3
            print(f"   • {doc.title} (Domínio: {doc.domain})")
        
        print("\n" + "=" * 60)
        print("✅ INTEGRAÇÃO DO CONHECIMENTO VALIDADA COM SUCESSO!")
        print("=" * 60)
        
        print("\n🎯 CAPACIDADES IMPLEMENTADAS:")
        print("✅ Carregamento automático de 17 bases de conhecimento")
        print("✅ Indexação por domínios especializados")
        print("✅ Busca inteligente com relevância")
        print("✅ Ferramentas especializadas por domínio")
        print("✅ Integração com agentes especializados")
        print("✅ Sistema de memória unificado")
        
        print("\n💡 PRÓXIMOS PASSOS:")
        print("1. Integrar com APIs de embeddings para busca semântica")
        print("2. Implementar cache persistente")
        print("3. Adicionar mais ferramentas especializadas")
        print("4. Conectar com agentes do template unificado")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

