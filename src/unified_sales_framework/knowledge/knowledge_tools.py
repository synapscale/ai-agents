"""
Ferramentas de Conhecimento Unificado

Este módulo implementa ferramentas especializadas para recuperação e uso
do conhecimento integrado do multi-agent-ai-system.
"""

from typing import List, Dict, Any, Optional
import os
import sys
from pathlib import Path

# Importar serviço de conhecimento
from .unified_knowledge_service import (
    UnifiedKnowledgeService,
    UnifiedKnowledgeRetrievalTool,
    KnowledgeDocument,
    KnowledgeDomain
)


class ParadigmShiftKnowledgeTool:
    """Ferramenta especializada em conhecimento de transformação de paradigmas."""
    
    def __init__(self, knowledge_service: UnifiedKnowledgeService):
        self.knowledge_service = knowledge_service
        self.name = "paradigm_shift_knowledge"
        self.description = "Recupera conhecimento especializado em transformação de paradigmas"
        self.domain = "paradigm_shift"
    
    def get_transformation_frameworks(self, context: str) -> str:
        """Recupera frameworks de transformação relevantes para o contexto."""
        
        query = f"frameworks transformação paradigma {context}"
        documents = self.knowledge_service.search_knowledge(
            query=query,
            domain=self.domain,
            limit=3
        )
        
        if not documents:
            return "Nenhum framework de transformação encontrado para este contexto."
        
        result_parts = [f"🔄 FRAMEWORKS DE TRANSFORMAÇÃO PARA: {context}\n"]
        
        for doc in documents:
            result_parts.append(f"## {doc.title}")
            result_parts.append(f"**Aplicação**: {doc.metadata.get('aplicacao', 'Geral')}")
            
            # Extrair frameworks específicos do conteúdo
            frameworks = self._extract_frameworks(doc.content)
            if frameworks:
                result_parts.append("**Frameworks Identificados**:")
                for framework in frameworks[:3]:  # Limitar a 3
                    result_parts.append(f"- {framework}")
            
            result_parts.append("---\n")
        
        return "\n".join(result_parts)
    
    def _extract_frameworks(self, content: str) -> List[str]:
        """Extrai nomes de frameworks do conteúdo."""
        
        frameworks = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Procurar por padrões de frameworks
            if any(keyword in line.lower() for keyword in ['framework', 'modelo', 'metodologia']):
                if line.startswith('#') or line.startswith('*') or line.startswith('-'):
                    # Limpar formatação markdown
                    clean_line = line.lstrip('#*- ').strip()
                    if len(clean_line) > 10 and len(clean_line) < 100:
                        frameworks.append(clean_line)
        
        return frameworks[:5]  # Máximo 5 frameworks
    
    def identify_blocking_patterns(self, market_description: str) -> str:
        """Identifica padrões de bloqueio mental para um mercado específico."""
        
        query = f"bloqueios mentais objeções resistência {market_description}"
        documents = self.knowledge_service.search_knowledge(
            query=query,
            domain=self.domain,
            agent_id="AXIOM-ARCHAEOLOGIST",
            limit=2
        )
        
        if not documents:
            return f"Nenhum padrão de bloqueio identificado para: {market_description}"
        
        result_parts = [f"🧠 PADRÕES DE BLOQUEIO PARA: {market_description}\n"]
        
        for doc in documents:
            # Extrair padrões de bloqueio
            blocking_patterns = self._extract_blocking_patterns(doc.content)
            
            if blocking_patterns:
                result_parts.append(f"## Padrões Identificados ({doc.title})")
                for pattern in blocking_patterns:
                    result_parts.append(f"- **{pattern['type']}**: {pattern['description']}")
                result_parts.append("")
        
        return "\n".join(result_parts)
    
    def _extract_blocking_patterns(self, content: str) -> List[Dict[str, str]]:
        """Extrai padrões de bloqueio do conteúdo."""
        
        patterns = []
        lines = content.split('\n')
        
        current_pattern = None
        for line in lines:
            line = line.strip()
            
            # Identificar tipos de bloqueio
            if any(keyword in line.lower() for keyword in ['pressuposto', 'crença', 'objeção', 'resistência']):
                if line.startswith('#') or line.startswith('*'):
                    pattern_type = line.lstrip('#*- ').strip()
                    current_pattern = {"type": pattern_type, "description": ""}
                elif current_pattern and len(line) > 20:
                    current_pattern["description"] = line[:200]
                    patterns.append(current_pattern)
                    current_pattern = None
        
        return patterns[:3]  # Máximo 3 padrões


class PersuasionFrameworksTool:
    """Ferramenta especializada em frameworks de persuasão."""
    
    def __init__(self, knowledge_service: UnifiedKnowledgeService):
        self.knowledge_service = knowledge_service
        self.name = "persuasion_frameworks"
        self.description = "Recupera frameworks e técnicas de persuasão"
        self.domain = "persuasion_frameworks"
    
    def get_persuasion_techniques(self, context: str, audience: str) -> str:
        """Recupera técnicas de persuasão para contexto e audiência específicos."""
        
        query = f"persuasão técnicas {context} {audience}"
        documents = self.knowledge_service.search_knowledge(
            query=query,
            domain=self.domain,
            limit=3
        )
        
        if not documents:
            return f"Nenhuma técnica de persuasão encontrada para: {context} + {audience}"
        
        result_parts = [f"🎯 TÉCNICAS DE PERSUASÃO PARA: {audience} em {context}\n"]
        
        for doc in documents:
            techniques = self._extract_techniques(doc.content)
            
            if techniques:
                result_parts.append(f"## {doc.title}")
                for technique in techniques:
                    result_parts.append(f"- **{technique['name']}**: {technique['description']}")
                result_parts.append("")
        
        return "\n".join(result_parts)
    
    def _extract_techniques(self, content: str) -> List[Dict[str, str]]:
        """Extrai técnicas de persuasão do conteúdo."""
        
        techniques = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Procurar por técnicas
            if any(keyword in line.lower() for keyword in ['técnica', 'método', 'estratégia', 'abordagem']):
                if line.startswith('#') or line.startswith('*') or line.startswith('-'):
                    technique_name = line.lstrip('#*- ').strip()
                    
                    # Procurar descrição nas próximas linhas
                    description = ""
                    for j in range(i+1, min(i+4, len(lines))):
                        next_line = lines[j].strip()
                        if next_line and not next_line.startswith('#') and not next_line.startswith('*'):
                            description = next_line[:150]
                            break
                    
                    if technique_name and description:
                        techniques.append({
                            "name": technique_name,
                            "description": description
                        })
        
        return techniques[:4]  # Máximo 4 técnicas


class CognitiveBiasesTool:
    """Ferramenta especializada em vieses cognitivos."""
    
    def __init__(self, knowledge_service: UnifiedKnowledgeService):
        self.knowledge_service = knowledge_service
        self.name = "cognitive_biases"
        self.description = "Recupera conhecimento sobre vieses cognitivos aplicados a vendas"
        self.domain = "cognitive_biases"
    
    def identify_relevant_biases(self, sales_context: str) -> str:
        """Identifica vieses cognitivos relevantes para um contexto de vendas."""
        
        query = f"vieses cognitivos {sales_context}"
        documents = self.knowledge_service.search_knowledge(
            query=query,
            domain=self.domain,
            limit=2
        )
        
        if not documents:
            return f"Nenhum viés cognitivo identificado para: {sales_context}"
        
        result_parts = [f"🧠 VIESES COGNITIVOS RELEVANTES PARA: {sales_context}\n"]
        
        for doc in documents:
            biases = self._extract_biases(doc.content)
            
            if biases:
                result_parts.append(f"## {doc.title}")
                for bias in biases:
                    result_parts.append(f"- **{bias['name']}**: {bias['application']}")
                result_parts.append("")
        
        return "\n".join(result_parts)
    
    def _extract_biases(self, content: str) -> List[Dict[str, str]]:
        """Extrai vieses cognitivos do conteúdo."""
        
        biases = []
        lines = content.split('\n')
        
        bias_keywords = ['viés', 'heurística', 'ancoragem', 'disponibilidade', 'confirmação', 'aversão']
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Procurar por vieses
            if any(keyword in line.lower() for keyword in bias_keywords):
                if line.startswith('#') or line.startswith('*'):
                    bias_name = line.lstrip('#*- ').strip()
                    
                    # Procurar aplicação nas próximas linhas
                    application = ""
                    for j in range(i+1, min(i+3, len(lines))):
                        next_line = lines[j].strip()
                        if next_line and 'aplicação' in next_line.lower():
                            application = next_line[:120]
                            break
                    
                    if bias_name:
                        biases.append({
                            "name": bias_name,
                            "application": application or "Aplicação geral em vendas"
                        })
        
        return biases[:3]  # Máximo 3 vieses


class AnalogiesMetaphorsTool:
    """Ferramenta especializada em analogias e metáforas."""
    
    def __init__(self, knowledge_service: UnifiedKnowledgeService):
        self.knowledge_service = knowledge_service
        self.name = "analogies_metaphors"
        self.description = "Recupera analogias e metáforas para comunicação persuasiva"
        self.domain = "analogies_metaphors"
    
    def find_analogies(self, concept: str, target_audience: str) -> str:
        """Encontra analogias relevantes para explicar um conceito."""
        
        query = f"analogia metáfora {concept} {target_audience}"
        documents = self.knowledge_service.search_knowledge(
            query=query,
            domain=self.domain,
            limit=2
        )
        
        if not documents:
            return f"Nenhuma analogia encontrada para: {concept}"
        
        result_parts = [f"🔗 ANALOGIAS PARA: {concept} (Audiência: {target_audience})\n"]
        
        for doc in documents:
            analogies = self._extract_analogies(doc.content)
            
            if analogies:
                result_parts.append(f"## {doc.title}")
                for analogy in analogies:
                    result_parts.append(f"- **{analogy['source']} → {analogy['target']}**: {analogy['explanation']}")
                result_parts.append("")
        
        return "\n".join(result_parts)
    
    def _extract_analogies(self, content: str) -> List[Dict[str, str]]:
        """Extrai analogias do conteúdo."""
        
        analogies = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Procurar por padrões de analogia
            if 'como' in line.lower() and ('é como' in line.lower() or 'similar' in line.lower()):
                parts = line.split('como')
                if len(parts) >= 2:
                    source = parts[0].strip().lstrip('#*- ')
                    target_explanation = parts[1].strip()
                    
                    # Separar target e explanation
                    if ':' in target_explanation:
                        target, explanation = target_explanation.split(':', 1)
                    else:
                        target = target_explanation[:50]
                        explanation = target_explanation
                    
                    analogies.append({
                        "source": source[:50],
                        "target": target.strip()[:50],
                        "explanation": explanation.strip()[:100]
                    })
        
        return analogies[:3]  # Máximo 3 analogias


class UnifiedKnowledgeToolset:
    """
    Conjunto unificado de ferramentas de conhecimento para agentes de vendas.
    """
    
    def __init__(self, knowledge_base_path: str):
        # Inicializar serviço de conhecimento
        self.knowledge_service = UnifiedKnowledgeService(knowledge_base_path)
        
        # Criar ferramentas especializadas
        self.general_retrieval = UnifiedKnowledgeRetrievalTool(self.knowledge_service)
        self.paradigm_shift = ParadigmShiftKnowledgeTool(self.knowledge_service)
        self.persuasion_frameworks = PersuasionFrameworksTool(self.knowledge_service)
        self.cognitive_biases = CognitiveBiasesTool(self.knowledge_service)
        self.analogies_metaphors = AnalogiesMetaphorsTool(self.knowledge_service)
        
        # Lista de todas as ferramentas
        self.tools = [
            self.general_retrieval,
            self.paradigm_shift,
            self.persuasion_frameworks,
            self.cognitive_biases,
            self.analogies_metaphors
        ]
    
    def get_tool_by_name(self, name: str):
        """Recupera ferramenta por nome."""
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None
    
    def get_knowledge_summary(self) -> str:
        """Retorna resumo do sistema de conhecimento."""
        
        summary = self.knowledge_service.get_knowledge_summary()
        
        result_parts = [
            "📚 RESUMO DO SISTEMA DE CONHECIMENTO UNIFICADO\n",
            f"**Total de Documentos**: {summary['total_documents']}",
            f"**Total de Domínios**: {summary['total_domains']}",
            f"**Total de Agentes**: {summary['total_agents']}\n",
            "## 🎯 DOMÍNIOS ESPECIALIZADOS:"
        ]
        
        for domain_id, domain_info in summary['domains'].items():
            result_parts.append(
                f"- **{domain_info['name']}**: {domain_info['document_count']} documentos "
                f"({', '.join(domain_info['agent_ids'])})"
            )
        
        result_parts.append("\n## 🤖 AGENTES COM CONHECIMENTO:")
        for agent_id, doc_count in summary['agents'].items():
            result_parts.append(f"- **{agent_id}**: {doc_count} documentos")
        
        result_parts.append("\n## 🔧 FERRAMENTAS DISPONÍVEIS:")
        for tool in self.tools:
            result_parts.append(f"- **{tool.name}**: {tool.description}")
        
        return "\n".join(result_parts)

