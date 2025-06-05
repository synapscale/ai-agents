import json
import logging
from pathlib import Path
from datetime import datetime

log = logging.getLogger("DocGenerator")


class DocGenerator:
    """Gera documentação completa do agente e subagentes."""

    def __init__(self, cfg: dict, dirs: dict):
        self.cfg = cfg
        self.dirs = dirs
        self.agent_id = cfg["AGENT_ID"]
        self.root_dir = dirs["root"]
        self.advanced = cfg.get("ADVANCED_SETTINGS", {})

    def generate(self) -> dict:
        """Gera documentação completa do agente e subagentes."""
        try:
            docs_dir = Path("docs")
            docs_dir.mkdir(exist_ok=True)

            # Preparar dados para documentação
            agent_data = {
                "id": self.agent_id,
                "version": self.cfg.get("AGENT_VERSION", "1.0.0"),
                "creation_date": self.cfg.get(
                    "CREATION_DATE", datetime.now().strftime("%Y-%m-%d")
                ),
                "main_agent": self.cfg["MAIN_AGENT"],
                "subagents": self.cfg["SUBAGENTS"],
                "advanced_settings": self.advanced,
            }

            # Gerar README.md para o agente
            readme_path = self.root_dir / "README.md"
            readme_content = self._generate_readme_content(agent_data)

            with open(readme_path, "w", encoding="utf-8") as file:
                file.write(readme_content)

            # Gerar documentação técnica detalhada em JSON
            tech_doc = self._generate_tech_doc(agent_data)
            tech_doc_path = docs_dir / f"{self.agent_id.lower()}_technical_doc.json"

            with open(tech_doc_path, "w", encoding="utf-8") as file:
                json.dump(tech_doc, file, indent=2, ensure_ascii=False)

            log.info(f"Documentação gerada: README.md e {tech_doc_path}")
            return {"readme": readme_path, "tech_doc": tech_doc_path}

        except Exception as e:
            log.error(f"Erro ao gerar documentação: {str(e)}")
            raise

    def _generate_readme_content(self, agent_data):
        """Gera o conteúdo do README.md."""
        return f"""# {self.agent_id}: Sistema Multi-Agente
        
## Visão Geral
**{self.agent_id}** é um sistema multi-agente especializado em {self.cfg["MAIN_AGENT"]["description"]}.
- **Versão**: {agent_data.get("version", "1.0.0")}
- **Data de Criação**: {agent_data.get("creation_date", datetime.now().strftime("%Y-%m-%d"))}
        
## Estrutura do Sistema
### Agente Principal
- **ID**: {self.agent_id}
- **Descrição**: {self.cfg["MAIN_AGENT"]["description"]}
                
### Subagentes
{chr(10).join([f"- **{subagent['id']}**: {subagent['description']}" for subagent in self.cfg["SUBAGENTS"]])}

## Base de Conhecimento
### Domínios do Agente Principal
{chr(10).join([f"- {domain['name']}" for domain in self.cfg["MAIN_AGENT"].get("knowledge_domains", [])])}

### Domínios dos Subagentes
{chr(10).join([f"#### {subagent['id']}\\n" + chr(10).join([f"- {domain['name']}" for domain in subagent.get("knowledge_domains", [])]) for subagent in self.cfg["SUBAGENTS"]])}
                
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
1. Execute o script de setup: `bash scripts/setup_{self.agent_id.lower()}.sh`
2. Verifique se todos os componentes foram instalados corretamente
        
### Uso do Agente
Após a configuração, você pode utilizar o agente através da API ou interface de sua preferência,
apontando para os arquivos de configuração em:
- Agente principal: `agents/{self.agent_id}/config/config.yaml`
- Subagentes: `agents/{self.agent_id}/<SUBAGENTE>/config/config.yaml`
            
## Arquitetura Técnica
            
### Fluxo de Trabalho
1. O agente principal {self.agent_id} recebe as solicitações iniciais
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
"""

    def _generate_tech_doc(self, agent_data):
        """Gera documentação técnica em formato JSON."""
        return {
            "agent_id": self.agent_id,
            "version": agent_data.get("version", "1.0.0"),
            "creation_date": agent_data.get(
                "creation_date", datetime.now().strftime("%Y-%m-%d")
            ),
            "main_agent": {
                "id": self.cfg["MAIN_AGENT"]["id"],
                "name": self.cfg["MAIN_AGENT"]["name"],
                "description": self.cfg["MAIN_AGENT"]["description"],
                "knowledge_domains": [
                    domain["name"]
                    for domain in self.cfg["MAIN_AGENT"].get("knowledge_domains", [])
                ],
                "tools_count": len(self.cfg["MAIN_AGENT"].get("knowledge_domains", []))
                + len(self.cfg["SUBAGENTS"])
                + 1,
            },
            "subagents": [
                {
                    "id": subagent["id"],
                    "name": subagent["name"],
                    "description": subagent["description"],
                    "domain": subagent.get("domain", ""),
                    "knowledge_domains": [
                        domain["name"]
                        for domain in subagent.get("knowledge_domains", [])
                    ],
                    "tools_count": len(subagent.get("knowledge_domains", [])) + 1,
                }
                for subagent in self.cfg["SUBAGENTS"]
            ],
            "settings": {
                "embedding_model": self.advanced.get(
                    "embedding_model", "text-embedding-3-small"
                ),
                "vector_store": self.advanced.get("vector_store", "supabase"),
                "similarity_threshold": self.advanced.get("similarity_threshold", 0.75),
            },
            "directory_structure": {
                "main_agent": str(self.root_dir),
                "config": str(self.root_dir / "config"),
                "knowledge_base": str(self.root_dir / "knowledge_base"),
                "subagents": {
                    subagent["id"]: {
                        "dir": str(self.root_dir / subagent["id"]),
                        "config": str(self.root_dir / subagent["id"] / "config"),
                        "knowledge_base": str(
                            self.root_dir / subagent["id"] / "knowledge_base"
                        ),
                    }
                    for subagent in self.cfg["SUBAGENTS"]
                },
            },
            "scripts": {
                "setup": f"scripts/setup_{self.agent_id.lower()}.sh",
                "embeddings": f"scripts/prepare_{self.agent_id.lower()}_embeddings.sh",
            },
        }
