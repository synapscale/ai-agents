# Unified Sales Framework - Makefile

.PHONY: help install install-dev test test-coverage lint format clean docs build deploy

help:  ## Mostra esta ajuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Instala dependências de produção
	pip install -r requirements.txt

install-dev:  ## Instala dependências de desenvolvimento
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

test:  ## Executa todos os testes
	python -m pytest tests/

test-coverage:  ## Executa testes com cobertura
	python -m pytest tests/ --cov=src --cov-report=html --cov-report=term-missing

test-validation:  ## Executa validação completa
	python scripts/real_validation.py

test-agents:  ## Testa agentes específicos
	python scripts/agent_specific_tests.py

lint:  ## Executa linting
	flake8 src/ scripts/ tests/
	mypy src/ scripts/

format:  ## Formata código
	black src/ scripts/ tests/

format-check:  ## Verifica formatação
	black --check src/ scripts/ tests/

clean:  ## Limpa arquivos temporários
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .coverage htmlcov/

docs:  ## Gera documentação
	sphinx-build -b html docs/ docs/_build/

docs-serve:  ## Serve documentação localmente
	python -m http.server 8000 --directory docs/_build/

list-agents:  ## Lista todos os agentes
	python scripts/unified_cli.py list-agents

create-agent:  ## Cria agente via template (uso: make create-agent TEMPLATE=path/to/template.yaml)
	python scripts/unified_cli.py from-template $(TEMPLATE)

validate:  ## Valida sistema completo
	python scripts/real_validation.py

build:  ## Constrói pacote
	python -m build

deploy:  ## Deploy (configurar conforme necessário)
	@echo "Configure deploy target"

setup-dev:  ## Configuração completa para desenvolvimento
	make install-dev
	make format
	make lint
	make test

ci:  ## Pipeline de CI
	make format-check
	make lint
	make test-coverage
	make validate
