#!/usr/bin/env python3
"""
FIXIT 2.1 – limpa YAML, Python e README, e roda Black/Ruff.
"""
from __future__ import annotations
import re, subprocess, textwrap, sys
from pathlib import Path
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]
yaml_rw = YAML()
yaml_rw.preserve_quotes = True


def indent_block(text: str) -> str:
    out, in_block, base = [], False, ""
    for ln in text.splitlines(keepends=True):
        if not in_block and "|" in ln:
            in_block, base = True, ln[: ln.find("|")]
            out.append(ln)
            continue
        if in_block:
            if ln.strip() == "":
                out.append(base + "  " + ln.lstrip())
            elif ln.startswith(base) and re.match(r"[\w#-]", ln[len(base) :]):
                in_block = False
                out.append(ln)
            else:
                out.append(base + "  " + ln.lstrip())
        else:
            out.append(ln)
    return "".join(out)


def fix_yaml(p: Path):
    raw = indent_block(p.read_text())
    try:
        data = yaml_rw.load(raw)
    except Exception:
        print(f"❌ YAML ainda inválido: {p}")
        return
    yaml_rw.dump(data, p.open("w"))
    print(f"✓ YAML {p.relative_to(ROOT)}")


TSTR = re.compile(r'(""".*?""")', re.S)


def fix_py(p: Path):
    src = p.read_text()
    changed = False

    def repl(m):
        nonlocal changed
        if '"""' in m.group(1)[3:-3]:
            changed = True
            return "r'''" + m.group(1)[3:-3].replace('"""', '# """') + "'''"
        return m.group(1)

    new = TSTR.sub(repl, src)
    if changed:
        p.write_text(new)
        print(f"✓ PY  {p.relative_to(ROOT)}")


def fix_readme(p: Path):
    txt = p.read_text()
    if "{self." not in txt:
        return
    aid = p.parent.name
    txt = txt.replace("{self.agent_id}", aid).replace(
        "{self.agent_id_lower}", aid.lower()
    )
    p.write_text(txt)
    print(f"✓ README {p.relative_to(ROOT)}")


def main():
    for y in ROOT.rglob("*.yml"):
        fix_yaml(y)
    for y in ROOT.rglob("*.yaml"):
        fix_yaml(y)
    for py in ROOT.rglob("*.py"):
        if "site-packages" not in str(py):
            fix_py(py)
    for rd in ROOT.rglob("README.md"):
        fix_readme(rd)

    subprocess.run(["black", "."], cwd=ROOT)
    try:
        # REMOVER COMPLETAMENTE --fix do ruff para versão 0.11
        subprocess.run(["ruff", "."], cwd=ROOT)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
