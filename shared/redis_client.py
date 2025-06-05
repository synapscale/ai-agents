# shared/redis_client.py
import os
import redis
from dotenv import load_dotenv

load_dotenv()


def get_redis_client():
    """Retorna um cliente Redis inicializado com as credenciais do .env"""
    host = os.getenv("REDIS_HOST")
    port = int(os.getenv("REDIS_PORT", 6379))
    password = os.getenv("REDIS_PASSWORD")
    db = int(os.getenv("REDIS_DB", 0))

    if not host or not password:
        raise ValueError(
            "REDIS_HOST e REDIS_PASSWORD devem estar definidos no arquivo .env"
        )

    return redis.Redis(
        host=host,
        port=port,
        password=password,
        db=db,
        decode_responses=True,  # Para receber strings em vez de bytes
    )


def test_connection():
    """Testa a conexão com o Redis"""
    try:
        client = get_redis_client()
        response = client.ping()
        print(f"Conexão com Redis bem-sucedida: {response}")

        # Teste básico de operações
        test_key = "test:connection"
        client.set(test_key, "Teste de conexão")
        client.expire(test_key, 60)  # Expira em 60 segundos

        value = client.get(test_key)
        print(f"Valor recuperado: {value}")

        ttl = client.ttl(test_key)
        print(f"TTL: {ttl} segundos")

        return True
    except Exception as e:
        print(f"Erro ao conectar ao Redis: {e}")
        return False


if __name__ == "__main__":
    test_connection()
