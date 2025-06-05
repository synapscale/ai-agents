"""
Módulo de Conhecimento Unificado

Este módulo integra as bases de conhecimento do multi-agent-ai-system
com as capacidades de memória e retrieval do ADK-Python.
"""

from .unified_knowledge_service import (
    UnifiedKnowledgeService,
    UnifiedKnowledgeRetrievalTool,
    KnowledgeDocument,
    KnowledgeDomain
)

from .knowledge_tools import (
    ParadigmShiftKnowledgeTool,
    PersuasionFrameworksTool,
    CognitiveBiasesTool,
    AnalogiesMetaphorsTool,
    UnifiedKnowledgeToolset
)

__all__ = [
    'UnifiedKnowledgeService',
    'UnifiedKnowledgeRetrievalTool',
    'KnowledgeDocument',
    'KnowledgeDomain',
    'ParadigmShiftKnowledgeTool',
    'PersuasionFrameworksTool',
    'CognitiveBiasesTool',
    'AnalogiesMetaphorsTool',
    'UnifiedKnowledgeToolset'
]

