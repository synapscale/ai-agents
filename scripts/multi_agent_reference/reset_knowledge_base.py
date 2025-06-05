# scripts/reset_knowledge_base.py
import os
import logging
import argparse
from dotenv import load_dotenv
from supabase import create_client

# Importe seu módulo de ingestão
import sys

sys.path.append(".")
from ingestion.main import run_ingestion

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_supabase_client():
    """Retorna um cliente Supabase inicializado"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)


def truncate_knowledge_base(agent_id=None):
    """
    Limpa dados da tabela knowledge_base

    Args:
        agent_id: Se especificado, limpa apenas dados deste agente
    """
    client = get_supabase_client()
    try:
        if agent_id:
            # Deletar apenas os dados do agente específico
            logger.info(f"Limpando dados do agente {agent_id}...")
            response = (
                client.table("knowledge_base")
                .delete()
                .eq("metadata->>agent_id", agent_id)
                .execute()
            )
            logger.info(f"Dados do agente {agent_id} limpos com sucesso")
        else:
            # Truncar a tabela inteira
            logger.info("Limpando toda a base de conhecimento...")
            client.table("knowledge_base").delete().execute()
            logger.info("Base de conhecimento limpa com sucesso")
        return True
    except Exception as e:
        logger.error(f"Erro ao limpar a base de conhecimento: {str(e)}")
        return False


def reset_and_reload(knowledge_dir, max_tokens=500, agent=None):
    """Limpa a base de conhecimento e recarrega os dados"""
    # Passo 1: Limpar a base de conhecimento
    if not truncate_knowledge_base(
        agent_id=DOMAIN_TO_AGENT.get(agent) if agent else None
    ):
        logger.error("Falha ao limpar a base de conhecimento. Abortando.")
        return False

    # Passo 2: Recarregar os dados
    logger.info("Iniciando recarga de dados...")

    # Ajustar o diretório se um agente específico foi solicitado
    if agent:
        knowledge_dir = os.path.join(knowledge_dir, f"{agent}_knowledge")

    run_ingestion(knowledge_dir, max_tokens=max_tokens)

    logger.info("Reset e recarga completos!")
    return True


# Mapeamento de domínios para agentes principais (copiado de metadata.py)
DOMAIN_TO_AGENT = {
    "neurohook": "NEUROHOOK-ULTRA",
    "retention": "RETENTION-ARCHITECT",
    "pain": "PAIN-DETECTOR",
    "paradigm": "PARADIGM-ARCHITECT",
    "metaphor": "METAPHOR-ARCHITECT",
    "conversion": "CONVERSION-CATALYST",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Reset e recarga da base de conhecimento"
    )
    parser.add_argument(
        "--knowledge_dir",
        default="knowledge_base_source",
        help="Diretório da base de conhecimento",
    )
    parser.add_argument(
        "--max_tokens", type=int, default=500, help="Número máximo de tokens por chunk"
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
        help="Recarregar apenas um agente específico",
    )

    args = parser.parse_args()
    reset_and_reload(args.knowledge_dir, args.max_tokens, args.agent)
