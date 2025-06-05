# Makefile

.PHONY: install check dirs agent-retention agent-pain agent-paradigm agent-metaphor agent-conversion all upload-% clean

# Variáveis
SHELL=/bin/bash

# Instalar dependências
install:
    @echo "Instalando dependências..."
    @pip install openai supabase python-dotenv tqdm pyyaml colorama requests

# Verificar requisitos
check:
    @python -c "import openai, supabase, dotenv, tqdm" || (echo "Algumas dependências estão faltando. Execute 'make install' primeiro."; exit 1)

# Criar diretórios necessários
dirs:
    @mkdir -p data/embeddings
    @mkdir -p agents
    @echo "✅ Diretórios criados"

# Configurar RETENTION-ARCHITECT
agent-retention: check dirs
    @./scripts/setup_retention_architect.sh

# Configurar PAIN-DETECTOR
agent-pain: check dirs
    @./scripts/setup_pain_detector.sh

# Configurar PARADIGM-ARCHITECT
agent-paradigm: check dirs
    @./scripts/setup_paradigm_architect.sh

# Configurar METAPHOR-ARCHITECT
agent-metaphor: check dirs
    @./scripts/setup_metaphor_architect.sh

# Configurar CONVERSION-CATALYST
agent-conversion: check dirs
    @./scripts/setup_conversion_catalyst.sh

# Configurar todos os agentes
all: agent-retention agent-pain agent-paradigm agent-metaphor agent-conversion
    @echo "✅ Todos os agentes configurados!"

# Fazer upload de embeddings para um agente específico
upload-%: check
    @if [ -f "data/embeddings/$*-embedding-data.jsonl" ]; then \
        python scripts/upload_to_supabase.py data/embeddings/$*-embedding-data.jsonl; \
    else \
        echo "❌ Arquivo de embeddings para $* não encontrado. Execute 'make agent-$*' primeiro."; \
    fi

# Limpar arquivos temporários
clean:
    @rm -f *.log *.tmp
    @rm -f data/embeddings/*.progress
    @echo "🧹 Arquivos temporários removidos"

