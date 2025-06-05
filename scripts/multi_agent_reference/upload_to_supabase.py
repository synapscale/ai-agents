#!/usr/bin/env python3
# upload_to_supabase.py – Gera embeddings e faz upload para Supabase

import os, json, time, argparse, requests, sys

try:
    from tqdm import tqdm
except ImportError:

    class tqdm:
        def __init__(self, iterable=None, **kw):
            self.iterable, self.n, self.total = iterable, 0, len(iterable)

        def __iter__(self):
            for x in self.iterable:
                yield x
                self.n += 1
                if self.n % max(1, self.total // 100) == 0:
                    print(f"{self.n/self.total:.0%}")

        def update(self, n=1):
            self.n += n


def generate_embeddings(texts, model="text-embedding-3-small", api_key=None):
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY não definida")
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    resp = requests.post(
        "https://api.openai.com/v1/embeddings",
        headers=headers,
        json={"input": texts, "model": model},
    )
    if resp.status_code != 200:
        raise RuntimeError(resp.text)
    return [d["embedding"] for d in resp.json()["data"]]


def upload_to_supabase(rows, url=None, key=None):
    url, key = url or os.getenv("SUPABASE_URL"), key or os.getenv("SUPABASE_KEY")
    if not (url and key):
        raise ValueError("SUPABASE_URL/KEY faltando")
    headers = {
        "Content-Type": "application/json",
        "apikey": key,
        "Authorization": f"Bearer {key}",
    }
    total, ok = 0, 0
    for batch in tqdm(
        [rows[i : i + 100] for i in range(0, len(rows), 100)], desc="Upload"
    ):
        r = requests.post(f"{url}/rest/v1/knowledge_base", headers=headers, json=batch)
        if r.status_code == 201:
            ok += len(batch)
        else:
            print("⚠️  erro:", r.text[:200])
        total += len(batch)
    return ok, total


def main():
    p = argparse.ArgumentParser()
    p.add_argument("jsonl_file")
    p.add_argument("--model", default="text-embedding-3-small")
    p.add_argument("--openai-key")
    p.add_argument("--supabase-url")
    p.add_argument("--supabase-key")
    p.add_argument("--batch-size", type=int, default=50)
    a = p.parse_args()

    rows = [json.loads(l) for l in open(a.jsonl_file, encoding="utf-8") if l.strip()]
    out = []
    for i in range(0, len(rows), a.batch_size):
        texts = [r["content"] for r in rows[i : i + a.batch_size]]
        embs = generate_embeddings(texts, a.model, a.openai_key)
        for r, e in zip(rows[i : i + a.batch_size], embs):
            out.append(
                {"content": r["content"], "embedding": e, "metadata": r["metadata"]}
            )
        time.sleep(0.5)

    ok, total = upload_to_supabase(out, a.supabase_url, a.supabase_key)
    print(f"✅  {ok}/{total} linhas enviadas ao Supabase")


if __name__ == "__main__":
    sys.exit(main())
