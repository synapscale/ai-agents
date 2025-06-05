# README

**Fonte:** general_documentation
**Relevância:** 0.350

# PARADIGM-ARCHITECT: Sistema Multi-Agente
        
## Visão Geral
**PARADIGM-ARCHITECT** é um sistema multi-agente especializado em Engenheiro de Transformação Conceitual que cria frameworks persuasivos revolucionários.
- **Versão**: 1.0.0
- **Data de Criação**: 2025-05-09
        
## Estrutura do Sistema
### Agente Principal
- **ID**: PARADIGM-ARCHITECT
- **Descrição**: Engenheiro de Transformação Conceitual que cria frameworks persuasivos revolucionários
                
### Subagentes
- **AXIOM-ARCHAEOLOGIST**: Especialista em escavação de pressupostos fundamentais e bloqueios mentais

## Base de Conhecimento
### Domínios do Agente Principal
- Frameworks de Transformação Paradigmática
- Modelos de Arquitetura Conceitual
- Técnicas de Engenharia de Linguagem Paradigmática
- Metodologias de Legitimação Conceitual

### Domínios dos Subagentes
#### AXIOM-ARCHAEOLOGIST\n- Análise de Pressupostos
- Bloqueios Mentais
- Gatilhos Emocionais
                
## Como Utilizar
### Requisitos
- Python 3.8 ou superior
- Dependências conforme `requirements.txt`
- Chave de API da OpenAI
- Supabase configurado com extensão `pgvector`
            
### Instalação
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure as variáveis de ambiente:
   ```bash
   export OPENAI_API_KEY=sua_chave_aqui
   export SUPABASE_URL=sua_url_aqui
   export SUPABASE_KEY=sua_chave_aqui

### Configuração do Agente
1. Execute o script de setup: `bash scripts/setup_paradigm-architect.sh`
2. Verifique se todos os componentes foram instalados corretamente
        
### Uso do Agente
Após a configuração, você pode utilizar o agente através da API ou interface de sua preferência,
apontando para os arquivos de configuração em:
- Agente principal: `agents/PARADIGM-ARCHITECT/config/config.yaml`
- Subagentes: `agents/PARADIGM-ARCHITECT/<SUBAGENTE>/config/config.yaml`
            
## Arquitetura Técnica
            
### Fluxo de Trabalho
1. O agente principal PARADIGM-ARCHITECT recebe as solicitações iniciais
2. Baseado na análise da solicitação, delega para o subagente especialista apropriado
3. O subagente consulta sua base de conhecimento especializada
4. A resposta é retornada ao agente principal
5. O agente principal integra e entrega o resultado final

### Tecnologias Utilizadas
- Modelos OpenAI para processamento de linguagem natural
- Embeddings OpenAI para recuperação semântica
- Supabase com pgvector para armazenamento e busca vetorial
- Sistema de arquivos para organização de base de conhecimento

## Manutenção e Expansão
Para adicionar novos conhecimentos:
1. Adicione arquivos Markdown na estrutura de diretórios apropriada 
2. Execute o script de embedding para processar os novos documentos
