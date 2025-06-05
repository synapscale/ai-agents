"""
Facade para o gerador de agentes.
Coordena os diferentes componentes do processo de geração.
"""

import logging
from pathlib import Path

from .core.template_loader import TemplateLoader
from .core.directory_builder import DirectoryBuilder
from .core.config_writer import ConfigWriter
from .core.knowledge_processor import KnowledgeProcessor
from .core.script_factory import ScriptFactory
from .core.doc_generator import DocGenerator

log = logging.getLogger("AgentGeneratorFacade")


class AgentGeneratorFacade:
    """Facade para coordenar o processo de geração de agentes."""

    def __init__(self, template_path, output_dir="agents", log_level="info"):
        """Inicializa o gerador com o path do template e configurações."""
        # Configurar nível de log
        numeric_level = getattr(logging, log_level.upper(), None)
        if isinstance(numeric_level, int):
            logging.getLogger("AgentGenerator").setLevel(numeric_level)

        # Carregar e validar template
        loader = TemplateLoader(template_path)
        self.cfg = loader.load()
        loader.validate(self.cfg)

        self.output_dir = Path(output_dir)
        self.agent_id = self.cfg["AGENT_ID"]
        self.advanced = self.cfg.get("ADVANCED_SETTINGS", {})

    def run(self):
        """Executa o processo completo de geração do agente."""
        try:
            # Criar estrutura de diretórios
            builder = DirectoryBuilder(self.cfg, self.output_dir)
            dirs = builder.build()

            # Gerar configurações
            writer = ConfigWriter(self.cfg, dirs, self.advanced)
            main_config = writer.write_main()
            subagent_configs = writer.write_subagents()

            # Processar base de conhecimento
            processor = KnowledgeProcessor(self.cfg, dirs)
            processed_files = processor.process()

            # Gerar scripts de suporte
            factory = ScriptFactory(self.cfg, dirs)
            scripts = factory.generate_all()

            # Gerar documentação
            doc_gen = DocGenerator(self.cfg, dirs)
            docs = doc_gen.generate()

            # Resultados completos da geração
            result = {
                "agent_id": self.agent_id,
                "agent_dir": str(dirs["root"]),
                "main_config": str(main_config),
                "subagent_configs": [str(path) for path in subagent_configs],
                "processed_files": processed_files,
                "scripts": {k: str(v) for k, v in scripts.items()},
                "documentation": {k: str(v) for k, v in docs.items()},
            }

            log.info(
                f"Geração completa do agente {self.agent_id} finalizada com sucesso!"
            )
            log.info(f"Para concluir a configuração, execute: bash {scripts['setup']}")

            return result

        except Exception as e:
            log.error(f"Erro durante geração do agente: {str(e)}")
            raise
