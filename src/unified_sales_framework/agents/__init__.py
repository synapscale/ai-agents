"""
Agentes do Unified Sales Framework

Este módulo contém todos os agentes especializados do framework.
"""

# Importar template principal
from ..templates.unified_sales_agent_template.agent import (
    UnifiedSalesAgent,
    UnifiedSalesAgentConfig,
    ParadigmArchitectAgent
)

__all__ = [
    "UnifiedSalesAgent",
    "UnifiedSalesAgentConfig", 
    "ParadigmArchitectAgent"
]

