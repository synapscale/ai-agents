# scripts/monitor_redis.py
import os
import redis
import logging
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


def monitor_redis():
    """Monitora uso e chaves do Redis"""
    client = get_redis_client()

    # Estatísticas de uso de memória
    info = client.info()
    used_memory = info["used_memory_human"]
    peak_memory = info["used_memory_peak_human"]

    logger.info(f"Uso de memória: {used_memory} (pico: {peak_memory})")

    # Total de chaves no banco
    total_keys = client.dbsize()
    logger.info(f"Total de chaves: {total_keys}")

    # Chaves por prefixo (para cada agente)
    prefixes = [
        "chat:neurohook:",
        "chat:retention:",
        "chat:pain:",
        "chat:paradigm:",
        "chat:metaphor:",
        "chat:conversion:",
    ]

    for prefix in prefixes:
        keys = client.keys(f"{prefix}*")
        logger.info(f"Chaves com prefixo '{prefix}': {len(keys)}")

        # Mostrar algumas chaves de exemplo com TTL
        for key in keys[:5]:  # limita a 5 chaves para não sobrecarregar o log
            ttl = client.ttl(key)
            value_type = client.type(key)
            logger.info(f"  - {key}: TTL={ttl}s, Tipo={value_type}")


if __name__ == "__main__":
    monitor_redis()
