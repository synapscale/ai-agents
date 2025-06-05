#!/usr/bin/env python3
"""
Interface de linha de comando para o gerador de agentes.
"""
import sys
import argparse
import logging
from .facade import AgentGeneratorFacade


def main():
    """Função principal para execução via linha de comando."""
    parser = argparse.ArgumentParser(
        description="Gera configuração completa de agentes a partir de template"
    )
    parser.add_argument(
        "template", help="Caminho para o arquivo de template de input (YAML)"
    )
    parser.add_argument(
        "--output-dir",
        default="agents",
        help="Diretório de saída para os agentes gerados",
    )
    parser.add_argument(
        "--log-level",
        default="info",
        choices=["debug", "info", "warning", "error", "critical"],
        help="Nível de logging",
    )
    args = parser.parse_args()

    # Configurar logging
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("agent_generator.log"),
            logging.StreamHandler(sys.stdout),
        ],
    )

    logger = logging.getLogger("CLI")

    try:
        # Inicializar e executar o gerador
        generator = AgentGeneratorFacade(
            template_path=args.template,
            output_dir=args.output_dir,
            log_level=args.log_level,
        )

        result = generator.run()

        print("\n" + "=" * 80)
        print(f"Geração do agente {result['agent_id']} concluída com sucesso!")
        print("=" * 80)
        print(f"\nLocalização: {result['agent_dir']}")
        print(f"Script de setup: {result['scripts']['setup']}")
        print(f"Documentação: {result['documentation']['readme']}")
        print("\nPróximos passos:")
        print(
            "1. Verifique se as variáveis de ambiente necessárias estão configuradas:"
        )
        print("   - OPENAI_API_KEY")
        print("   - SUPABASE_URL")
        print("   - SUPABASE_KEY")
        print(f"2. Execute o script de setup: bash {result['scripts']['setup']}")
        print("3. Utilize o agente conforme documentação gerada")

        return 0

    except Exception as e:
        logger.critical(f"Erro fatal: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
