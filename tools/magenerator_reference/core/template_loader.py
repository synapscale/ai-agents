from pathlib import Path
import yaml
import logging

log = logging.getLogger("TemplateLoader")


class TemplateLoader:
    def __init__(self, template_path: str):
        self.path = Path(template_path)

    def load(self) -> dict:
        with self.path.open(encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        log.debug("Template carregado")
        return cfg

    # valida campos essenciais
    def validate(self, cfg: dict):
        req = ["AGENT_ID", "MAIN_AGENT", "SUBAGENTS"]
        for k in req:
            if k not in cfg:
                raise ValueError(f"Campo obrigatório ausente: {k}")

        main_req = ["id", "name", "description", "system_prompt"]
        for k in main_req:
            if k not in cfg["MAIN_AGENT"]:
                raise ValueError(f"Campo obrigatório no MAIN_AGENT ausente: {k}")

        if not isinstance(cfg["SUBAGENTS"], list) or not cfg["SUBAGENTS"]:
            raise ValueError("SUBAGENTS vazio ou inválido")

        sub_req = ["id", "name", "description", "system_prompt"]
        for i, sa in enumerate(cfg["SUBAGENTS"]):
            for k in sub_req:
                if k not in sa:
                    raise ValueError(f"Campo faltando no subagente {i+1}: {k}")

        log.info("Template validado com sucesso")
