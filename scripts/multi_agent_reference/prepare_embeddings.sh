#!/bin/bash
# scripts/prepare_embeddings.sh

# Cores para saída
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parâmetros
MAIN_AGENT=$1
OUTPUT_DIR="data/embeddings"

if [ -z "$MAIN_AGENT" ]; then
  echo -e "${RED}❌ Erro: Nome do agente principal é obrigatório.${NC}"
  echo "Uso: ./scripts/prepare_embeddings.sh AGENTE_PRINCIPAL"
  exit 1
fi

# Verificar se o agente existe
if [ ! -d "agents/$MAIN_AGENT" ]; then
  echo -e "${RED}❌ Erro: Agente '$MAIN_AGENT' não existe.${NC}"
  exit 1
fi

echo -e "${BLUE}-------------------------------------${NC}"
echo -e "${BLUE}🔄 Preparando dados para embeddings${NC}"
echo -e "${BLUE}Agente: ${GREEN}$MAIN_AGENT${NC}"
echo -e "${BLUE}-------------------------------------${NC}"

# Criar diretório de saída
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/${MAIN_AGENT}-embedding-data.jsonl"

# Limpar arquivo de saída se existir
echo "" > "$OUTPUT_FILE"

# Contar o total de arquivos para a barra de progresso
TOTAL_FILES=$(find "agents/$MAIN_AGENT/knowledge_base" -type f -name "*.md" | wc -l)
echo -e "${YELLOW}📂 Total de arquivos: $TOTAL_FILES${NC}"

# Verificar se existem arquivos
if [ $TOTAL_FILES -eq 0 ]; then
  echo -e "${RED}❌ Erro: Nenhum arquivo de conhecimento encontrado para o agente $MAIN_AGENT.${NC}"
  exit 1
fi

# Contador para arquivos processados
COUNT=0

# Processar todos os arquivos do agente
find "agents/$MAIN_AGENT/knowledge_base" -type f -name "*.md" | while read -r file; do
  # Atualizar contador e calcular progresso
  COUNT=$((COUNT+1))
  PROGRESS=$((COUNT*100/TOTAL_FILES))
  
  # Mostrar barra de progresso
  printf "\r${YELLOW}⏳ Processando: [%-50s] %d%%" $(printf '#%.0s' $(seq 1 $((PROGRESS/2)))) $PROGRESS
  
  # Extrair metadados
  agent_id=$(grep -m 1 "agent_id:" "$file" | cut -d":" -f2- | xargs)
  sub_agent_id=$(grep -m 1 "sub_agent_id:" "$file" | cut -d":" -f2- | xargs)
  domain=$(grep -m 1 "domain:" "$file" | cut -d":" -f2- | xargs)
  
  # Verificar se todos os metadados foram extraídos
  if [ -z "$agent_id" ] || [ -z "$sub_agent_id" ] || [ -z "$domain" ]; then
    echo -e "\n${RED}⚠️ Metadados incompletos no arquivo: $(basename "$file")${NC}"
    continue
  fi
  
  # Extrair conteúdo (ignorando cabeçalho YAML)
  CONTENT=""
  READ_CONTENT=0
  YAML_DELIMITERS=0
  
  while IFS= read -r line; do
    if [[ "$line" == "---" ]]; then
      YAML_DELIMITERS=$((YAML_DELIMITERS+1))
      if [[ $YAML_DELIMITERS -eq 2 ]]; then
        READ_CONTENT=1
      fi
      continue
    fi
    
    if [[ $READ_CONTENT -eq 1 ]]; then
      CONTENT="$CONTENT $line"
    fi
  done < "$file"
  
  # Sanitizar para JSON
  CONTENT=$(echo "$CONTENT" | sed 's/"/\\"/g' | tr '\n' ' ' | sed 's/\\n/ /g')
  
  # Quebrar em chunks se o conteúdo for muito longo (5000 caracteres por chunk)
  CONTENT_LENGTH=${#CONTENT}
  CHUNK_SIZE=5000
  
  if [ $CONTENT_LENGTH -le $CHUNK_SIZE ]; then
    # Conteúdo curto, adicionar diretamente ao arquivo JSONL
    echo "{\"text\": \"$CONTENT\", \"metadata\": {\"agent_id\": \"$agent_id\", \"sub_agent_id\": \"$sub_agent_id\", \"domain\": \"$domain\", \"source\": \"$(basename "$file")\"}}" >> "$OUTPUT_FILE"
  else
    # Conteúdo longo, dividir em chunks
    for ((i=0; i<CONTENT_LENGTH; i+=$CHUNK_SIZE)); do
      CHUNK="${CONTENT:$i:$CHUNK_SIZE}"
      echo "{\"text\": \"$CHUNK\", \"metadata\": {\"agent_id\": \"$agent_id\", \"sub_agent_id\": \"$sub_agent_id\", \"domain\": \"$domain\", \"source\": \"$(basename "$file")\", \"chunk\": \"$((i/CHUNK_SIZE+1))\", \"total_chunks\": \"$((CONTENT_LENGTH/CHUNK_SIZE+1))\"}}" >> "$OUTPUT_FILE"
    done
  fi
done

echo -e "\n${GREEN}✅ Dados preparados e salvos em: $OUTPUT_FILE${NC}"
echo -e "${YELLOW}▶️ Próximo passo: Execute python scripts/upload_to_supabase.py para fazer upload dos embeddings${NC}"

