#!/bin/bash
# scripts/setup_retention_architect.sh

# Cores para saída
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}🚀 Configurando RETENTION-ARCHITECT${NC}"
echo -e "${BLUE}=====================================${NC}"

# Criar diretórios necessários se não existirem
mkdir -p data/embeddings
mkdir -p agents/RETENTION-ARCHITECT/knowledge_base
mkdir -p agents/RETENTION-ARCHITECT/sub_agents

# Processar arquivos de conhecimento para cada sub-agente
echo -e "${YELLOW}📚 Processando arquivos de conhecimento...${NC}"

# TENSION-ENGINEER
./scripts/process_knowledge_files.sh "RETENTION-ARCHITECT" "TENSION-ENGINEER" "knowledge_base_source/retention_techniques/tension_structures/loops_and_arcs" "tension_structures"

# IMMERSION-ARCHITECT
./scripts/process_knowledge_files.sh "RETENTION-ARCHITECT" "IMMERSION-ARCHITECT" "knowledge_base_source/retention_techniques/immersion" "immersion_techniques"

# RHYTHM-PROGRAMMER
./scripts/process_knowledge_files.sh "RETENTION-ARCHITECT" "RHYTHM-PROGRAMMER" "knowledge_base_source/retention_techniques/rhythm_and_pacing/cognitive_breathing" "rhythm_and_pacing"

# TRANSITION-SPECIALIST
./scripts/process_knowledge_files.sh "RETENTION-ARCHITECT" "TRANSITION-SPECIALIST" "knowledge_base_source/retention_techniques/transition_engineering/abandonment_prevention" "transition_engineering"

# JOURNEY-CARTOGRAPHER
./scripts/process_knowledge_files.sh "RETENTION-ARCHITECT" "JOURNEY-CARTOGRAPHER" "knowledge_base_source/master_examples/opening_paragraphs/marketing_masterpieces" "journey_mapping"

# Preparar para embeddings
echo -e "${YELLOW}🔄 Preparando dados para embeddings...${NC}"
./scripts/prepare_embeddings.sh "RETENTION-ARCHITECT"

echo -e "${GREEN}✅ RETENTION-ARCHITECT configurado com sucesso!${NC}"
echo -e "${YELLOW}▶️ Para fazer upload para o Supabase, execute:${NC}"
echo -e "   python scripts/upload_to_supabase.py data/embeddings/RETENTION-ARCHITECT-embedding-data.jsonl"

