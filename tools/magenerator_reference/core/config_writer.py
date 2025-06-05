import yaml
import logging
import datetime as _dt
from pathlib import Path

log = logging.getLogger("ConfigWriter")


class ConfigWriter:
    def __init__(self, cfg: dict, dirs: dict, adv: dict):
        self.cfg, self.dirs, self.adv = cfg, dirs, adv

    def write_main(self) -> Path:
        main = self.cfg["MAIN_AGENT"]
        conf = {
            "name": main["name"],
            "description": main["description"],
            "type": "main_agent",
            "created_at": main.get("created_at", _dt.datetime.now().date().isoformat()),
            "updated_at": _dt.datetime.now().date().isoformat(),
            "system_prompt": main["system_prompt"],
            "tools": [],
        }
        conf_path = self.dirs["config"] / "config.yaml"
        conf_path.write_text(yaml.dump(conf, allow_unicode=True))
        log.info("Configuração do agente principal gerada")
        return conf_path

    def write_subagents(self) -> list[Path]:
        paths = []
        for sa in self.cfg["SUBAGENTS"]:
            conf = {
                "name": sa["name"],
                "parent_agent": self.cfg["AGENT_ID"],
                "description": sa["description"],
                "domain": sa.get("domain", ""),
                "system_prompt": sa["system_prompt"],
                "tools": [],
            }
            path = self.dirs["root"] / sa["id"] / "config" / "config.yaml"
            path.write_text(yaml.dump(conf, allow_unicode=True))
            paths.append(path)
        log.info("Configurações dos subagentes geradas")
        return paths
