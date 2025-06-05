from pathlib import Path
import logging

log = logging.getLogger("DirectoryBuilder")


class DirectoryBuilder:
    def __init__(self, cfg: dict, out_dir: Path):
        self.cfg, self.out = cfg, out_dir / cfg["AGENT_ID"]

    def build(self) -> dict:
        dirs = {
            "root": self.out,
            "config": self.out / "config",
            "kb": self.out / "knowledge_base",
        }
        for d in dirs.values():
            d.mkdir(parents=True, exist_ok=True)

        for sa in self.cfg["SUBAGENTS"]:
            sa_dir = self.out / sa["id"]
            (sa_dir / "config").mkdir(parents=True, exist_ok=True)
            (sa_dir / "knowledge_base").mkdir(parents=True, exist_ok=True)

        log.info("Estrutura de diretórios criada")
        return dirs
