# shared/supabase_client.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


def get_supabase_client() -> Client:
    """Retorna um cliente Supabase inicializado com as credenciais do .env"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError(
            "SUPABASE_URL e SUPABASE_KEY devem estar definidos no arquivo .env"
        )

    return create_client(url, key)


def test_connection():
    """Testa a conexão com o Supabase"""
    try:
        client = get_supabase_client()
        # Consulta simples para testar
        result = client.table("knowledge_base").select("id").limit(1).execute()
        print("Conexão com Supabase bem-sucedida!")
        return True
    except Exception as e:
        print(f"Erro ao conectar ao Supabase: {e}")
        return False


if __name__ == "__main__":
    test_connection()
