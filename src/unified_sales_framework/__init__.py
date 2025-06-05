"""
Unified Sales Framework - Sistema de Conhecimento

Este módulo implementa apenas o sistema de conhecimento unificado,
sem dependências dos templates de agentes.
"""

__version__ = "0.1.0"
__author__ = "Unified Sales Framework Team"

# Importar apenas módulos de conhecimento
try:
    from .knowledge import *
except ImportError:
    # Se houver problemas de importação, definir apenas o básico
    pass

