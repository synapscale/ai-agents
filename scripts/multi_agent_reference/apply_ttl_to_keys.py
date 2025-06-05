# scripts/apply_ttl_to_keys.py
import os
import redis
import logging
import argparse
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_redis_client():
    """Retorna um cliente Redis inicializado"""
    host = os.getenv("REDIS_HOST")
    port = int(os.getenv("REDIS_PORT", 6379))
    password = os.getenv("REDIS_PASSWORD")
    db = int(os.getenv("REDIS_DB", 0))

    return redis.Redis(
        host=host, port=port, password=password, db=db, decode_responses=True
    )


def apply_ttl_to_keys(prefix, ttl_seconds=86400, dry_run=True):
    """
    Aplica TTL a todas as chaves que correspondem ao prefixo

    Args:
        prefix: prefixo das chaves (ex: 'chat:neurohook:')
        ttl_seconds: TTL a aplicar em segundos (padrão: 24 horas)
        dry_run: se True, apenas mostra o que seria feito sem alterar
    """
    client = get_redis_client()

    # Encontrar as chaves com o prefixo
    keys = client.keys(f"{prefix}*")
    logger.info(f"Encontradas {len(keys)} chaves com prefixo '{prefix}'")

    if not keys:
        return

    # Para cada chave, verificar o TTL atual e aplicar novo TTL se necessário
    updated = 0
    for key in keys:
        current_ttl = client.ttl(key)

        # Se TTL não estiver definido ou for -1 (sem TTL)
        if current_ttl == -1:
            if not dry_run:
                client.expire(key, ttl_seconds)
            logger.info(
                f"{'[DRY RUN] Aplicaria' if dry_run else 'Aplicado'} TTL de {ttl_seconds}s para chave: {key}"
            )
            updated += 1

    logger.info(
        f"{'[DRY RUN] ' if dry_run else ''}Total de {updated} chaves atualizadas"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aplicar TTL a chaves do Redis")
    parser.add_argument(
        "--prefix", default="chat:", help="Prefixo das chaves para aplicar TTL"
    )
    parser.add_argument(
        "--ttl",
        type=int,
        default=86400,
        help="TTL a aplicar em segundos (padrão: 86400 = 24 horas)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Apenas mostrar o que seria feito, sem alterar as chaves",
    )
    parser.add_argument(
        "--agent",
        choices=[
            "neurohook",
            "retention",
            "pain",
            "paradigm",
            "metaphor",
            "conversion",
        ],
        help="Aplicar apenas para um agente específico",
    )

    args = parser.parse_args()

    # Ajustar o prefixo se um agente específico foi solicitado
    prefix = args.prefix
    if args.agent:
        prefix = f"chat:{args.agent}:"

    apply_ttl_to_keys(prefix, args.ttl, args.dry_run)
