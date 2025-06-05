import logging
import yaml
from pathlib import Path
from datetime import datetime

log = logging.getLogger("KnowledgeProcessor")


class KnowledgeProcessor:
    """Processa e prepara a base de conhecimento para agentes e subagentes."""

    def __init__(self, cfg: dict, dirs: dict):
        self.cfg = cfg
        self.dirs = dirs
        self.agent_id = cfg["AGENT_ID"]
        self.root_dir = dirs["root"]

    def process(self) -> list:
        """Processa a base de conhecimento, retornando lista de arquivos processados."""
        try:
            processed_files = []

            # Processar base de conhecimento do agente principal
            main_agent = self.cfg["MAIN_AGENT"]
            if "knowledge_domains" in main_agent:
                for domain_info in main_agent["knowledge_domains"]:
                    domain_name = domain_info["name"]
                    source_path = Path(domain_info["path"])

                    if source_path.exists():
                        target_dir = (
                            self.root_dir
                            / "knowledge_base"
                            / domain_name.replace(" ", "_")
                        )
                        target_dir.mkdir(parents=True, exist_ok=True)

                        self._process_domain_files(
                            source_path=source_path,
                            target_dir=target_dir,
                            agent_id=self.agent_id,
                            domain=domain_name,
                            sub_agent_id=None,
                        )

                        processed_files.append(str(target_dir))
                    else:
                        log.warning(
                            f"Diretório de conhecimento não encontrado: {source_path}"
                        )

            # Processar base de conhecimento dos subagentes
            for subagent in self.cfg["SUBAGENTS"]:
                subagent_id = subagent["id"]

                if "knowledge_domains" in subagent:
                    for domain_info in subagent["knowledge_domains"]:
                        domain_name = domain_info["name"]
                        source_path = Path(domain_info["path"])

                        if source_path.exists():
                            target_dir = (
                                self.root_dir
                                / subagent_id
                                / "knowledge_base"
                                / domain_name.replace(" ", "_")
                            )
                            target_dir.mkdir(parents=True, exist_ok=True)

                            self._process_domain_files(
                                source_path=source_path,
                                target_dir=target_dir,
                                agent_id=self.agent_id,
                                domain=domain_name,
                                sub_agent_id=subagent_id,
                            )

                            processed_files.append(str(target_dir))
                        else:
                            # Criar diretório vazio se não existir
                            log.warning(
                                f"Diretório de conhecimento não encontrado: {source_path}"
                            )
                            source_path.mkdir(parents=True, exist_ok=True)
                            log.info(f"Criado diretório vazio: {source_path}")

            log.info(
                f"Base de conhecimento processada: {len(processed_files)} diretórios"
            )
            return processed_files

        except Exception as e:
            log.error(f"Erro ao processar base de conhecimento: {str(e)}")
            raise

    def _process_domain_files(
        self, source_path, target_dir, agent_id, domain, sub_agent_id=None
    ):
        """Processa arquivos de um domínio específico, adicionando metadados YAML."""
        file_count = 0

        # Se não houver arquivos .md, criar um exemplo
        md_files = list(source_path.glob("*.md"))
        if not md_files:
            example_file = (
                source_path / f"{domain.lower().replace(' ', '_')}_exemplo.md"
            )
            example_content = (
                f"# {domain}\n\nEste é um arquivo de exemplo para o domínio {domain}."
            )
            example_file.write_text(example_content, encoding="utf-8")
            md_files = [example_file]
            log.info(f"Criado arquivo de exemplo para {domain}: {example_file}")

        for file_path in md_files:
            filename = file_path.name
            target_file = target_dir / filename

            # Ler conteúdo original
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Preparar metadados
            metadata = {
                "agent_id": agent_id,
                "domain": domain,
                "source_file": filename,
                "date_processed": datetime.now().strftime("%Y-%m-%d"),
                "last_updated": datetime.now().strftime("%Y-%m-%d"),
                "version": "1.0",
            }

            # Adicionar sub_agent_id se aplicável
            if sub_agent_id:
                metadata["sub_agent_id"] = sub_agent_id

            # Converter metadados para YAML
            metadata_yaml = yaml.dump(
                metadata, default_flow_style=False, sort_keys=False, allow_unicode=True
            )

            # Combinar metadados e conteúdo
            final_content = f"---\n{metadata_yaml}---\n\n{content}"

            # Salvar arquivo processado
            with open(target_file, "w", encoding="utf-8") as file:
                file.write(final_content)

            file_count += 1
            log.debug(f"Arquivo processado: {target_file}")

        log.info(f"Processados {file_count} arquivos para domínio '{domain}'")
