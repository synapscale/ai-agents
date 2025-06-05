#!/usr/bin/env python3
# generate_embeddings_jsonl.py - Gera arquivo JSONL para embeddings

import os
import json
import argparse
from pathlib import Path


def process_markdown_files(agent_dir):
    """
    Varre a árvore de conhecimento do agente (e subagentes) e gera
    uma lista de dicionários {content, metadata}.
    """
    agent_dir = Path(agent_dir)
    entries = []

    # Principal
    knowledge_dir = agent_dir / "knowledge_base"
    if knowledge_dir.exists():
        for md in knowledge_dir.rglob("*.md"):
            entries.extend(process_file(md))

    # Subagentes
    for sub_dir in agent_dir.iterdir():
        if (sub_dir / "knowledge_base").exists():
            for md in (sub_dir / "knowledge_base").rglob("*.md"):
                entries.extend(process_file(md))

    return entries


def process_file(path):
    entries = []
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        yaml_part, _, body = text.split("---", 2)
        import yaml

        try:
            meta = yaml.safe_load(yaml_part)
            entries.append({"content": body.strip(), "metadata": meta})
        except Exception as exc:
            print(f"⚠️  Falha ao ler metadados de {path}: {exc}")
    return entries


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--agent-dir", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    out_dir = Path(args.output).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    data = process_markdown_files(args.agent_dir)
    with open(args.output, "w", encoding="utf-8") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\\n")

    print(f"✅  JSONL gerado com {len(data)} entradas: {args.output}")


if __name__ == "__main__":
    main()
