#!/bin/bash
# scripts/process_knowledge_files.sh

# Cores para saída
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parâmetros
MAIN_AGENT=$1
SUB_AGENT=$2
SOURCE_DIR=$3
DOMAIN=${4:-$(echo $SUB_AGENT | tr '[:upper:]' '[:lower:]' | tr '-' '_')}

if [ -z "$MAIN_AGENT" ] || [ -z "$SUB_AGENT" ] || [ -z "$SOURCE_DIR" ]; then
  echo -e "${RED}❌ Erro: Parâmetros insuficientes.${NC}"
  echo "Uso: ./scripts/process_knowledge_files.sh AGENTE_PRINCIPAL SUB_AGENTE DIRETORIO_FONTE [DOMINIO]"
  exit 1
fi

# Verificar se o diretório fonte existe
if [ ! -d "$SOURCE_DIR" ]; then
  echo -e "${RED}❌ Erro: Diretório fonte '$SOURCE_DIR' não existe.${NC}"
  exit 1
fi

echo -e "${BLUE}-------------------------------------${NC}"
echo -e "${BLUE}📚 Processando arquivos de conhecimento${NC}"
echo -e "${BLUE}Agente: ${GREEN}$MAIN_AGENT${NC}"
echo -e "${BLUE}Sub-agente: ${GREEN}$SUB_AGENT${NC}"
echo -e "${BLUE}Domínio: ${GREEN}$DOMAIN${NC}"
echo -e "${BLUE}-------------------------------------${NC}"

# Criar diretório de destino se não existir
TARGET_DIR="agents/$MAIN_AGENT/knowledge_base/${DOMAIN}"
mkdir -p "$TARGET_DIR"

# Contador para arquivos processados
COUNT=0

# Processar arquivos recursivamente
find "$SOURCE_DIR" -type f -name "*.md" | while read -r file; do
  filename=$(basename "$file")
  target="$TARGET_DIR/$filename"
  
  # Verificar se o arquivo já contém metadados YAML
  if grep -q "^---$" "$file"; then
    echo -e "${YELLOW}⚠️ Arquivo $filename já contém metadados. Verificando...${NC}"
    
    # Extrair metadados existentes
    HAS_AGENT_ID=$(grep -q "agent_id:" "$file" && echo "true" || echo "false")
    HAS_SUB_AGENT_ID=$(grep -q "sub_agent_id:" "$file" && echo "true" || echo "false")
    HAS_DOMAIN=$(grep -q "domain:" "$file" && echo "true" || echo "false")
    
    if [[ "$HAS_AGENT_ID" == "true" && "$HAS_SUB_AGENT_ID" == "true" && "$HAS_DOMAIN" == "true" ]]; then
      echo -e "${YELLOW}ℹ️ Metadados completos encontrados. Atualizando...${NC}"
      # Criar um arquivo temporário
      TEMP_FILE=$(mktemp)
      
      # Extrair a seção YAML e o conteúdo
      sed -n '1,/^---$/p' "$file" > "$TEMP_FILE.yaml"
      sed '1,/^---$/d' "$file" | sed '1,/^---$/d' > "$TEMP_FILE.content"
      
      # Atualizar metadados
      sed -i "s/agent_id:.*/agent_id: $MAIN_AGENT/" "$TEMP_FILE.yaml"
      sed -i "s/sub_agent_id:.*/sub_agent_id: $SUB_AGENT/" "$TEMP_FILE.yaml"
      sed -i "s/domain:.*/domain: $DOMAIN/" "$TEMP_FILE.yaml"
      
      # Recombinar
      cat "$TEMP_FILE.yaml" > "$target"
      echo "---" >> "$target"
      cat "$TEMP_FILE.content" >> "$target"
      
      # Limpar arquivos temporários
      rm "$TEMP_FILE.yaml" "$TEMP_FILE.content"
    else
      echo -e "${YELLOW}⚠️ Metadados incompletos. Substituindo...${NC}"
      # Extrair conteúdo (ignorando qualquer metadado existente)
      CONTENT=$(sed '1,/^---$/d' "$file" | sed '1,/^---$/d')
      
      # Criar novo arquivo com metadados corretos
      cat > "$target" << EOF
---
agent_id: $MAIN_AGENT
sub_agent_id: $SUB_AGENT
domain: $DOMAIN
source_file: "$filename"
date_processed: $(date +"%Y-%m-%d")
last_updated: $(date +"%Y-%m-%d")
version: 1.0
---

$CONTENT
EOF
    fi
  else
    echo -e "${YELLOW}ℹ️ Adicionando metadados ao arquivo $filename${NC}"
    
    # Adicionar metadados ao arquivo
    cat > "$target" << EOF
---
agent_id: $MAIN_AGENT
sub_agent_id: $SUB_AGENT
domain: $DOMAIN
source_file: "$filename"
date_processed: $(date +"%Y-%m-%d")
last_updated: $(date +"%Y-%m-%d")
version: 1.0
---

$(cat "$file")
EOF
  fi
  
  echo -e "${GREEN}✅ Processado: $filename${NC}"
  COUNT=$((COUNT+1))
done

echo -e "${GREEN}✅ $COUNT arquivos processados para $SUB_AGENT no domínio $DOMAIN${NC}"

