#!/bin/bash
# setup_paradigm-architect.sh - Setup completo para PARADIGM-ARCHITECT e subagentes

echo "Iniciando setup completo para PARADIGM-ARCHITECT..."

# Verificar se o diretório de agentes existe
if [ ! -d "agents/PARADIGM-ARCHITECT" ]; then
  echo "Erro: Diretório do agente não encontrado. Execute o gerador primeiro."
  exit 1
fi

# Etapa 1: Validar estrutura de diretórios
echo "Validando estrutura de diretórios..."
for dir in "agents/PARADIGM-ARCHITECT/config" "agents/PARADIGM-ARCHITECT/knowledge_base"; do
  if [ ! -d "$dir" ]; then
    echo "Erro: Diretório $dir não encontrado."
    exit 1
  fi
done

# Validar existência de subagentes
for subagent in "AXIOM-ARCHAEOLOGIST"; do
  if [ ! -d "agents/PARADIGM-ARCHITECT/$subagent" ]; then
    echo "Erro: Diretório do subagente $subagent não encontrado."
    exit 1
  fi
done

# Etapa 2: Verificar arquivos de configuração
echo "Verificando arquivos de configuração..."
if [ ! -f "agents/PARADIGM-ARCHITECT/config/config.yaml" ]; then
  echo "Erro: Arquivo de configuração do agente principal não encontrado."
  exit 1
fi

for subagent in "AXIOM-ARCHAEOLOGIST"; do
  if [ ! -f "agents/PARADIGM-ARCHITECT/$subagent/config/config.yaml" ]; then
    echo "Erro: Arquivo de configuração do subagente $subagent não encontrado."
    exit 1
  fi
done

# Etapa 3: Preparar embeddings
echo "Preparando embeddings..."
bash scripts/prepare_paradigm-architect_embeddings.sh

# Verificar resultado do processo de embeddings
if [ $? -ne 0 ]; then
  echo "Erro: Processo de embedding falhou."
  exit 1
fi

echo "Setup de PARADIGM-ARCHITECT concluído com sucesso!"
echo ""
echo "Para utilizar o agente, configure seu sistema para usar:"
echo "- Agente principal: agents/PARADIGM-ARCHITECT/config/config.yaml"
echo "- Subagentes: agents/PARADIGM-ARCHITECT/<SUBAGENTE>/config/config.yaml"
echo ""
echo "Boa utilização!"
