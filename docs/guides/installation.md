# 📦 Guia de Instalação Completo

Este guia fornece instruções detalhadas para instalar e configurar o Unified Sales Framework em diferentes ambientes.

## 📋 Requisitos

- Python 3.9+ (recomendado 3.11)
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)
- 2GB de espaço em disco
- Acesso à internet para download de dependências

## 🚀 Instalação Passo a Passo

### 1️⃣ Clone o Repositório

```bash
# Via HTTPS
git clone https://github.com/seu-usuario/unified-sales-framework.git

# Via SSH (se configurado)
git clone git@github.com:seu-usuario/unified-sales-framework.git

# Entre no diretório
cd unified-sales-framework
```

### 2️⃣ Configure o Ambiente Virtual

#### No Linux/macOS:
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

#### No Windows:
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

### 3️⃣ Instale as Dependências

#### Instalação Básica (Apenas Produção)
```bash
# Instalar dependências de produção
pip install -r requirements.txt
```

#### Instalação para Desenvolvimento
```bash
# Instalar dependências de produção e desenvolvimento
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Ou usando o Makefile
make install-dev
```

### 4️⃣ Configure Variáveis de Ambiente

Copie o arquivo de exemplo de variáveis de ambiente:

```bash
cp .env.example .env.local
```

Edite o arquivo `.env.local` com suas configurações:

```
# Configurações Gerais
DEBUG=False
LOG_LEVEL=INFO

# Configurações de API (opcional)
OPENAI_API_KEY=sua_chave_aqui
GOOGLE_API_KEY=sua_chave_aqui

# Configurações de Banco de Dados (opcional)
DATABASE_URL=sqlite:///database.db
```

### 5️⃣ Verifique a Instalação

Execute o comando de verificação para confirmar que tudo está funcionando:

```bash
# Listar agentes disponíveis
python scripts/unified_cli.py list-agents

# Executar validação do sistema
python scripts/real_validation.py
```

Se você ver a lista de agentes disponíveis, a instalação foi bem-sucedida!

## 🔧 Instalação com Docker

### Usando Docker Compose

1. Certifique-se de ter o Docker e o Docker Compose instalados
2. Execute:

```bash
# Construir e iniciar os containers
docker-compose up -d

# Verificar logs
docker-compose logs -f
```

### Usando Dockerfile Diretamente

```bash
# Construir a imagem
docker build -t unified-sales-framework .

# Executar o container
docker run -it --rm unified-sales-framework python scripts/unified_cli.py list-agents
```

## 🛠️ Configurações Avançadas

### Configuração de Modelos de IA

O framework suporta vários modelos de IA. Para configurar:

1. Edite o arquivo `.env.local`:
   ```
   # Modelos de IA
   DEFAULT_MODEL=gpt-4
   FALLBACK_MODEL=gpt-3.5-turbo
   ```

2. Ou configure diretamente no código:
   ```python
   from unified_sales_framework.core.fixed_adk import create_unified_agent
   
   agent = create_unified_agent(
       'paradigm_architect',
       'Especialista em transformação paradigmática',
       model="gpt-4"
   )
   ```

### Configuração de Memória e Conhecimento

Para configurar o sistema de conhecimento:

```python
from unified_sales_framework.knowledge.unified_knowledge_service import UnifiedKnowledgeService

# Inicializar serviço de conhecimento
knowledge_service = UnifiedKnowledgeService(
    base_path="./knowledge",
    embedding_model="text-embedding-ada-002"
)

# Carregar conhecimento específico
knowledge_service.load_domain("copywriting")

# Usar em agente
agent = create_unified_agent(
    'paradigm_architect',
    'Especialista em transformação paradigmática',
    knowledge_service=knowledge_service
)
```

## ❓ Solução de Problemas

### Erro: "No module named 'unified_sales_framework'"

**Solução**: Certifique-se de que está no diretório raiz do projeto e que o ambiente virtual está ativado.

### Erro: "ImportError: Cannot import name 'create_unified_agent'"

**Solução**: Verifique se todas as dependências foram instaladas corretamente:
```bash
pip install -r requirements.txt
```

### Erro: "ModuleNotFoundError: No module named 'google.adk'"

**Solução**: O sistema usa uma versão adaptada do Google ADK com fallback automático. Não é necessário instalar o ADK separadamente.

### Erro ao executar scripts: "Permission denied"

**Solução**: Adicione permissão de execução aos scripts:
```bash
chmod +x scripts/*.py
```

## 🔄 Atualização

Para atualizar o framework para a versão mais recente:

```bash
# Atualizar o repositório
git pull

# Atualizar dependências
pip install -r requirements.txt --upgrade

# Verificar atualização
python scripts/unified_cli.py --version
```

## 📚 Próximos Passos

Após a instalação, recomendamos:

1. Explorar o [Tutorial Inicial](../tutorials/getting-started.md)
2. Verificar os [Exemplos Práticos](../../examples/README.md)
3. Ler a [Arquitetura do Sistema](../architecture/overview.md)

---

**Precisa de mais ajuda?** Consulte a documentação completa ou execute `python scripts/unified_cli.py --help`.

