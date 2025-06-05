#!/bin/bash
# prepare_paradigm-architect_embeddings.sh - Preparação de embeddings para PARADIGM-ARCHITECT

echo "Preparando embeddings para PARADIGM-ARCHITECT e seus subagentes..."

# Verificar se diretório de dados existe
mkdir -p data/embeddings

# Gerar arquivo JSONL para embeddings
echo "Gerando arquivo JSONL para embeddings..."
python3 scripts/generate_embeddings_jsonl.py \
  --agent-dir agents/PARADIGM-ARCHITECT \
  --output data/embeddings/paradigm-architect-embedding-data.jsonl

# Verificar se o arquivo JSONL foi gerado corretamente
if [ ! -f data/embeddings/paradigm-architect-embedding-data.jsonl ]; then
  echo "Erro: Arquivo JSONL não foi gerado corretamente."
  exit 1
fi

# Verificar se as variáveis de ambiente necessárias estão definidas
if [ -z "$OPENAI_API_KEY" ]; then
  echo "Erro: Variável de ambiente OPENAI_API_KEY não está definida."
  exit 1
fi

if [ -z "$SUPABASE_URL" ] || [ -z "$SUPABASE_KEY" ]; then
  echo "Erro: Variáveis de ambiente SUPABASE_URL e/ou SUPABASE_KEY não estão definidas."
  exit 1
fi

# Gerar embeddings via OpenAI API e fazer upload para Supabase
echo "Gerando embeddings e fazendo upload para Supabase..."
python3 scripts/upload_to_supabase.py \
  data/embeddings/paradigm-architect-embedding-data.jsonl \
  --model text-embedding-3-small \
  --batch-size 50

# Verificar resultado do último comando
if [ $? -ne 0 ]; then
  echo "Erro: Falha ao gerar ou fazer upload de embeddings."
  exit 1
fi

echo "Processo de embedding concluído para PARADIGM-ARCHITECT!"
