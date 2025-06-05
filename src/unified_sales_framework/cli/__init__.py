"""
CLI do Unified Sales Framework

Este módulo contém a interface de linha de comando do framework.
"""

import click
from .commands import generate_cmd, migrate_cmd, deploy_cmd, run_cmd

@click.group()
@click.version_option()
def main():
    """Unified Sales Framework CLI."""
    pass

# Registrar comandos
main.add_command(generate_cmd)
main.add_command(migrate_cmd)
main.add_command(deploy_cmd)
main.add_command(run_cmd)

if __name__ == "__main__":
    main()

