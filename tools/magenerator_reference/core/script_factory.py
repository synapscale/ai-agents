from pathlib import Path
import logging
import os
import textwrap

log = logging.getLogger("ScriptFactory")


class ScriptFactory:

    def __init__(self, cfg: dict, dirs: dict):
        self.cfg = cfg
        self.dirs = dirs
        self.agent_id = cfg["AGENT_ID"]
        self.agent_id_lower = self.agent_id.lower()
        self.advanced = cfg.get("ADVANCED_SETTINGS", {})
        self.embedding_model = self.advanced.get(
            "embedding_model", "text-embedding-3-small"
        )
        self.scripts_dir = Path("scripts")

    def generate_all(self) -> dict:
        try:
            self.scripts_dir.mkdir(exist_ok=True)

            # Gerar scripts
            scripts = {
                "jsonl": self._generate_jsonl_script(),
                "uploader": self._generate_uploader_script(),
                "embedding": self._generate_embedding_script(),
                "setup": self._generate_setup_script(),
            }

            log.info(f"Gerados {len(scripts)} scripts de suporte")
            return scripts

        except Exception as e:
            log.error(f"Erro ao gerar scripts: {str(e)}")
            raise

    def _generate_jsonl_script(self) -> Path:
        script_path = self.scripts_dir / "generate_embeddings_jsonl.py"

        script_content = textwrap.dedent(
            r'''#!/usr/bin/env python3
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
'''
        )

        script_path.write_text(script_content, encoding="utf-8")
        os.chmod(script_path, 0o755)
        log.debug(f"Gerado script JSONL: {script_path}")
        return script_path

        # Aplicar dedent para remover a indentação extra
        script_content = textwrap.dedent(script_content)

        with open(script_path, "w", encoding="utf-8") as file:
            file.write(script_content)

        os.chmod(script_path, 0o755)
        log.debug(f"Gerado script JSONL: {script_path}")
        return script_path

    def _generate_uploader_script(self) -> Path:
        """Gera o script para upload de embeddings ao Supabase."""
        script_path = self.scripts_dir / "upload_to_supabase.py"

        script_content = textwrap.dedent(
            r"""#!/usr/bin/env python3
# upload_to_supabase.py – Gera embeddings e faz upload para Supabase

import os, json, time, argparse, requests, sys
try:
    from tqdm import tqdm
except ImportError:
    class tqdm:
        def __init__(self, iterable=None, **kw): self.iterable, self.n, self.total = iterable, 0, len(iterable)
        def __iter__(self):
            for x in self.iterable:
                yield x
                self.n += 1
                if self.n % max(1, self.total//100) == 0:
                    print(f"{self.n/self.total:.0%}")
        def update(self, n=1): self.n += n

def generate_embeddings(texts, model="text-embedding-3-small", api_key=None):
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY não definida")
    headers = {"Content-Type":"application/json","Authorization":f"Bearer {api_key}"}
    resp = requests.post("https://api.openai.com/v1/embeddings",
                         headers=headers, json={"input":texts,"model":model})
    if resp.status_code != 200:
        raise RuntimeError(resp.text)
    return [d["embedding"] for d in resp.json()["data"]]

def upload_to_supabase(rows, url=None, key=None):
    url, key = url or os.getenv("SUPABASE_URL"), key or os.getenv("SUPABASE_KEY")
    if not (url and key): raise ValueError("SUPABASE_URL/KEY faltando")
    headers = {"Content-Type":"application/json","apikey":key,"Authorization":f"Bearer {key}"}
    total, ok = 0, 0
    for batch in tqdm([rows[i:i+100] for i in range(0,len(rows),100)], desc="Upload"):
        r = requests.post(f"{url}/rest/v1/knowledge_base", headers=headers, json=batch)
        if r.status_code == 201: ok += len(batch)
        else: print("⚠️  erro:", r.text[:200])
        total += len(batch)
    return ok, total

def main():
    p = argparse.ArgumentParser()
    p.add_argument("jsonl_file"); p.add_argument("--model", default="text-embedding-3-small")
    p.add_argument("--openai-key"); p.add_argument("--supabase-url"); p.add_argument("--supabase-key")
    p.add_argument("--batch-size", type=int, default=50)
    a = p.parse_args()

    rows = [json.loads(l) for l in open(a.jsonl_file, encoding="utf-8") if l.strip()]
    out = []
    for i in range(0, len(rows), a.batch_size):
        texts = [r["content"] for r in rows[i:i+a.batch_size]]
        embs  = generate_embeddings(texts, a.model, a.openai_key)
        for r,e in zip(rows[i:i+a.batch_size], embs):
            out.append({"content":r["content"], "embedding":e, "metadata":r["metadata"]})
        time.sleep(0.5)

    ok, total = upload_to_supabase(out, a.supabase_url, a.supabase_key)
    print(f"✅  {ok}/{total} linhas enviadas ao Supabase")

if __name__ == "__main__":
    sys.exit(main())
"""
        )

        script_path.write_text(script_content, encoding="utf-8")
        os.chmod(script_path, 0o755)
        log.debug(f"Gerado script uploader: {script_path}")
        return script_path

        script_content = """#!/usr/bin/env python3
# upload_to_supabase.py - Gera embeddings e faz upload para Supabase

import os
import json
import time
import argparse
import requests
import sys

try:
    from tqdm import tqdm
except ImportError:
    # Fallback se tqdm não estiver instalado
    class tqdm:
        def __init__(self, iterable=None, **kwargs):
            self.iterable = iterable
            self.total = len(iterable) if iterable is not None else 0
            self.n = 0
            self.desc = kwargs.get('desc', '')
        
        def __iter__(self):
            for obj in self.iterable:
                yield obj
                self.n += 1
                if self.n % max(1, self.total // 100) == 0:
                    print(f"{self.desc}: {self.n}/{self.total} ({self.n/self.total:.1%})")
        
        def update(self, n=1):
            self.n += n

def generate_embeddings(texts, model="text-embedding-3-small", api_key=None):
    if not api_key:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key não fornecida e não encontrada nas variáveis de ambiente")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "input": texts,
        "model": model
    }
    
    response = requests.post(
        "https://api.openai.com/v1/embeddings",
        headers=headers,
        json=data
    )
    
    if response.status_code != 200:
        raise ValueError(f"Erro da API OpenAI: {response.text}")
    
    result = response.json()
    embeddings = [item['embedding'] for item in result['data']]
    return embeddings

def upload_to_supabase(entries_with_embeddings, supabase_url=None, supabase_key=None):
    if not supabase_url:
        supabase_url = os.environ.get("SUPABASE_URL")
        if not supabase_url:
            raise ValueError("URL do Supabase não fornecida e não encontrada nas variáveis de ambiente")
    
    if not supabase_key:
        supabase_key = os.environ.get("SUPABASE_KEY")
        if not supabase_key:
            raise ValueError("Chave do Supabase não fornecida e não encontrada nas variáveis de ambiente")
    
    headers = {
        "Content-Type": "application/json",
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}"
    }
    
    # Dividir em lotes para evitar sobrecarga
    batch_size = 100
    batches = [entries_with_embeddings[i:i+batch_size] for i in range(0, len(entries_with_embeddings), batch_size)]
    
    total_uploaded = 0
    for batch in tqdm(batches, desc="Enviando lotes para Supabase"):
        response = requests.post(
            f"{supabase_url}/rest/v1/knowledge_base",
            headers=headers,
            json=batch
        )
        
        if response.status_code != 201:
            print(f"Aviso: Erro ao enviar lote: {response.text}")
        else:
            total_uploaded += len(batch)
    
    return total_uploaded

def main():
    parser = argparse.ArgumentParser(description="Gera embeddings e faz upload para Supabase")
    parser.add_argument("jsonl_file", help="Arquivo JSONL com conteúdo para embeddings")
    parser.add_argument("--model", default="text-embedding-3-small", help="Modelo de embedding OpenAI")
    parser.add_argument("--batch-size", type=int, default=50, help="Tamanho do lote para geração de embeddings")
    parser.add_argument("--openai-key", help="Chave API OpenAI (ou definir var. ambiente OPENAI_API_KEY)")
    parser.add_argument("--supabase-url", help="URL Supabase (ou definir var. ambiente SUPABASE_URL)")
    parser.add_argument("--supabase-key", help="Chave Supabase (ou definir var. ambiente SUPABASE_KEY)")
    args = parser.parse_args()
    
    # Verificar variáveis de ambiente
    for var, name in [
        (os.environ.get("OPENAI_API_KEY") or args.openai_key, "OPENAI_API_KEY"),
        (os.environ.get("SUPABASE_URL") or args.supabase_url, "SUPABASE_URL"),
        (os.environ.get("SUPABASE_KEY") or args.supabase_key, "SUPABASE_KEY")
    ]:
        if not var:
            print(f"Erro: Variável de ambiente {name} não definida")
            parser.print_help()
            sys.exit(1)
    
    # Carregar entradas do arquivo JSONL
    entries = []
    with open(args.jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                entries.append(json.loads(line))
    
    print(f"Carregadas {len(entries)} entradas de {args.jsonl_file}")
    
    # Processar em lotes para evitar limites de API
    batch_size = args.batch_size
    batches = [entries[i:i+batch_size] for i in range(0, len(entries), batch_size)]
    all_entries_with_embeddings = []
    
    for i, batch in enumerate(batches):
        print(f"Processando lote {i+1}/{len(batches)} ({len(batch)} entradas)")
        
        # Extrair textos para embeddings
        texts = [entry['content'] for entry in batch]
        
        # Gerar embeddings
        try:
            embeddings = generate_embeddings(texts, model=args.model, api_key=args.openai_key)
            
            # Combinar embeddings com entradas originais
            for j, entry in enumerate(batch):
                entry_with_embedding = {
                    "content": entry['content'],
                    "embedding": embeddings[j],
                    "metadata": entry['metadata']
                }
                all_entries_with_embeddings.append(entry_with_embedding)
            
            # Pequeno delay para evitar rate limits
            if i < len(batches) - 1:
                time.sleep(0.5)
        
        except Exception as e:
            print(f"Erro ao processar lote {i+1}: {e}")
            # Continuar com o próximo lote em caso de erro
            continue
    
    print(f"Gerados embeddings para {len(all_entries_with_embeddings)} entradas")
    
    # Upload para Supabase
    if all_entries_with_embeddings:
        total_uploaded = upload_to_supabase(
            all_entries_with_embeddings,
            supabase_url=args.supabase_url,
            supabase_key=args.supabase_key
        )
        print(f"Enviadas com sucesso {total_uploaded} entradas para Supabase")
        return 0
    else:
        print("Nenhum embedding para enviar")
        return 1

if __name__ == "__main__":
    sys.exit(main())
"""
        # Aplicar dedent para remover a indentação extra
        script_content = textwrap.dedent(script_content)

        with open(script_path, "w", encoding="utf-8") as file:
            file.write(script_content)

        os.chmod(script_path, 0o755)
        log.debug(f"Gerado script de upload: {script_path}")
        return script_path

    def _generate_embedding_script(self) -> Path:
        """Gera o script shell para preparação de embeddings."""
        script_path = self.scripts_dir / f"prepare_{self.agent_id_lower}_embeddings.sh"

        # No caso do shell script, vamos usar uma f-string diretamente
        script_content = f"""#!/bin/bash
# prepare_{self.agent_id_lower}_embeddings.sh - Preparação de embeddings para {self.agent_id}

echo "Preparando embeddings para {self.agent_id} e seus subagentes..."

# Verificar se diretório de dados existe
mkdir -p data/embeddings

# Gerar arquivo JSONL para embeddings
echo "Gerando arquivo JSONL para embeddings..."
python3 scripts/generate_embeddings_jsonl.py \\
  --agent-dir agents/{self.agent_id} \\
  --output data/embeddings/{self.agent_id_lower}-embedding-data.jsonl

# Verificar se o arquivo JSONL foi gerado corretamente
if [ ! -f data/embeddings/{self.agent_id_lower}-embedding-data.jsonl ]; then
  echo "Erro: Arquivo JSONL não foi gerado corretamente."
  exit 1
fi

# Verificar se as variáveis de ambiente necessárias estão definidas
if [ -z "$OPENAI_API_KEY" ]; then
  echo "Erro: Variável de ambiente OPENAI_API_KEY não está definida."
  exit 1
fi

if [ -z "$SUPABASE_URL" ] || [ -z "$SUPABASE_KEY" ]; then
  echo "Erro: Variáveis de ambiente SUPABASE_URL e/ou SUPABASE_KEY não estão definidas."
  exit 1
fi

# Gerar embeddings via OpenAI API e fazer upload para Supabase
echo "Gerando embeddings e fazendo upload para Supabase..."
python3 scripts/upload_to_supabase.py \\
  data/embeddings/{self.agent_id_lower}-embedding-data.jsonl \\
  --model {self.embedding_model} \\
  --batch-size 50

# Verificar resultado do último comando
if [ $? -ne 0 ]; then
  echo "Erro: Falha ao gerar ou fazer upload de embeddings."
  exit 1
fi

echo "Processo de embedding concluído para {self.agent_id}!"
"""

        with open(script_path, "w", encoding="utf-8") as file:
            file.write(script_content)

        os.chmod(script_path, 0o755)
        log.debug(f"Gerado script de embedding: {script_path}")
        return script_path

    def _generate_setup_script(self) -> Path:
        """Gera o script master de setup."""
        script_path = self.scripts_dir / f"setup_{self.agent_id_lower}.sh"

        # Lista de subagentes para validação
        subagents_list = " ".join(
            [f'"{subagent["id"]}"' for subagent in self.cfg["SUBAGENTS"]]
        )

        # No caso do shell script, vamos usar uma f-string diretamente
        script_content = f"""#!/bin/bash
# setup_{self.agent_id_lower}.sh - Setup completo para {self.agent_id} e subagentes

echo "Iniciando setup completo para {self.agent_id}..."

# Verificar se o diretório de agentes existe
if [ ! -d "agents/{self.agent_id}" ]; then
  echo "Erro: Diretório do agente não encontrado. Execute o gerador primeiro."
  exit 1
fi

# Etapa 1: Validar estrutura de diretórios
echo "Validando estrutura de diretórios..."
for dir in "agents/{self.agent_id}/config" "agents/{self.agent_id}/knowledge_base"; do
  if [ ! -d "$dir" ]; then
    echo "Erro: Diretório $dir não encontrado."
    exit 1
  fi
done

# Validar existência de subagentes
for subagent in {subagents_list}; do
  if [ ! -d "agents/{self.agent_id}/$subagent" ]; then
    echo "Erro: Diretório do subagente $subagent não encontrado."
    exit 1
  fi
done

# Etapa 2: Verificar arquivos de configuração
echo "Verificando arquivos de configuração..."
if [ ! -f "agents/{self.agent_id}/config/config.yaml" ]; then
  echo "Erro: Arquivo de configuração do agente principal não encontrado."
  exit 1
fi

for subagent in {subagents_list}; do
  if [ ! -f "agents/{self.agent_id}/$subagent/config/config.yaml" ]; then
    echo "Erro: Arquivo de configuração do subagente $subagent não encontrado."
    exit 1
  fi
done

# Etapa 3: Preparar embeddings
echo "Preparando embeddings..."
bash scripts/prepare_{self.agent_id_lower}_embeddings.sh

# Verificar resultado do processo de embeddings
if [ $? -ne 0 ]; then
  echo "Erro: Processo de embedding falhou."
  exit 1
fi

echo "Setup de {self.agent_id} concluído com sucesso!"
echo ""
echo "Para utilizar o agente, configure seu sistema para usar:"
echo "- Agente principal: agents/{self.agent_id}/config/config.yaml"
echo "- Subagentes: agents/{self.agent_id}/<SUBAGENTE>/config/config.yaml"
echo ""
echo "Boa utilização!"
"""

        with open(script_path, "w", encoding="utf-8") as file:
            file.write(script_content)

        os.chmod(script_path, 0o755)
        log.debug(f"Gerado script master: {script_path}")
        return script_path
