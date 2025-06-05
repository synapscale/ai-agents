#!/usr/bin/env python3
"""
Sistema de Validação Final - Fase 5
Testa e valida todos os componentes do unified-sales-framework
"""

import os
import sys
import time
import json
import yaml
import logging
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class ValidationResult:
    """Resultado de uma validação"""
    component: str
    test_name: str
    success: bool
    duration: float
    details: str
    error: str = ""

class UnifiedFrameworkValidator:
    """
    Validador completo do unified-sales-framework
    """
    
    def __init__(self, framework_path="/home/ubuntu/unified-sales-framework"):
        self.framework_path = Path(framework_path)
        self.results: List[ValidationResult] = []
        self.start_time = time.time()
        
    def log_result(self, component: str, test_name: str, success: bool, 
                   duration: float, details: str, error: str = ""):
        """Registra resultado de teste"""
        result = ValidationResult(
            component=component,
            test_name=test_name,
            success=success,
            duration=duration,
            details=details,
            error=error
        )
        self.results.append(result)
        
        status = "✅" if success else "❌"
        logger.info(f"{status} {component}.{test_name} ({duration:.2f}s): {details}")
        if error:
            logger.error(f"   Erro: {error}")
    
    def validate_project_structure(self) -> bool:
        """Valida estrutura básica do projeto"""
        logger.info("🔍 Validando estrutura do projeto...")
        start_time = time.time()
        
        required_dirs = [
            "agents", "vertical_agents", "src", "templates", 
            "scripts", "docs", "examples"
        ]
        
        required_files = [
            "pyproject.toml", "requirements.txt", "README.md",
            "Makefile", ".gitignore", "LICENSE"
        ]
        
        missing_dirs = []
        missing_files = []
        
        # Verificar diretórios
        for dir_name in required_dirs:
            dir_path = self.framework_path / dir_name
            if not dir_path.exists():
                missing_dirs.append(dir_name)
        
        # Verificar arquivos
        for file_name in required_files:
            file_path = self.framework_path / file_name
            if not file_path.exists():
                missing_files.append(file_name)
        
        duration = time.time() - start_time
        success = len(missing_dirs) == 0 and len(missing_files) == 0
        
        if success:
            details = f"Estrutura completa: {len(required_dirs)} diretórios, {len(required_files)} arquivos"
        else:
            details = f"Faltando: {missing_dirs + missing_files}"
        
        self.log_result("project", "structure", success, duration, details)
        return success
    
    def validate_agents_structure(self) -> bool:
        """Valida estrutura dos agentes"""
        logger.info("🤖 Validando estrutura dos agentes...")
        start_time = time.time()
        
        # Validar agentes tradicionais
        agents_path = self.framework_path / "agents"
        traditional_count = 0
        traditional_valid = 0
        
        if agents_path.exists():
            for category_dir in agents_path.iterdir():
                if category_dir.is_dir():
                    for agent_dir in category_dir.iterdir():
                        if agent_dir.is_dir():
                            traditional_count += 1
                            if self._validate_agent_files(agent_dir, "traditional"):
                                traditional_valid += 1
        
        # Validar agentes verticais
        vertical_path = self.framework_path / "vertical_agents"
        vertical_count = 0
        vertical_valid = 0
        
        if vertical_path.exists():
            for agent_dir in vertical_path.iterdir():
                if agent_dir.is_dir() and agent_dir.name != "__pycache__":
                    vertical_count += 1
                    if self._validate_agent_files(agent_dir, "vertical"):
                        vertical_valid += 1
        
        duration = time.time() - start_time
        total_count = traditional_count + vertical_count
        total_valid = traditional_valid + vertical_valid
        success = total_valid == total_count and total_count > 0
        
        details = f"Agentes: {total_valid}/{total_count} válidos (T:{traditional_valid}/{traditional_count}, V:{vertical_valid}/{vertical_count})"
        
        self.log_result("agents", "structure", success, duration, details)
        return success
    
    def _validate_agent_files(self, agent_dir: Path, agent_type: str) -> bool:
        """Valida arquivos de um agente específico"""
        required_files = ["agent.py", "prompt.txt"]
        
        for file_name in required_files:
            file_path = agent_dir / file_name
            if not file_path.exists():
                return False
        
        return True
    
    def validate_cli_functionality(self) -> bool:
        """Valida funcionalidade do CLI"""
        logger.info("⚡ Validando funcionalidade do CLI...")
        start_time = time.time()
        
        cli_path = self.framework_path / "scripts" / "unified_cli.py"
        if not cli_path.exists():
            duration = time.time() - start_time
            self.log_result("cli", "existence", False, duration, "CLI não encontrado")
            return False
        
        # Testar comando list-agents
        try:
            result = subprocess.run([
                sys.executable, str(cli_path), "list-agents"
            ], capture_output=True, text=True, cwd=str(self.framework_path))
            
            list_success = result.returncode == 0 and "AGENTES TRADICIONAIS" in result.stdout
            
        except Exception as e:
            list_success = False
        
        duration = time.time() - start_time
        
        if list_success:
            details = "CLI funcional: list-agents operacional"
        else:
            details = "CLI com problemas: list-agents falhou"
        
        self.log_result("cli", "functionality", list_success, duration, details)
        return list_success
    
    def validate_template_system(self) -> bool:
        """Valida sistema de templates"""
        logger.info("📋 Validando sistema de templates...")
        start_time = time.time()
        
        templates_dir = self.framework_path / "templates" / "yaml_examples"
        
        if not templates_dir.exists():
            duration = time.time() - start_time
            self.log_result("templates", "existence", False, duration, "Diretório de templates não encontrado")
            return False
        
        # Verificar templates existentes
        template_files = list(templates_dir.glob("*.yaml"))
        template_count = len(template_files)
        
        # Testar criação via template (se possível)
        test_success = True
        try:
            cli_path = self.framework_path / "scripts" / "unified_cli.py"
            if cli_path.exists() and template_files:
                # Usar primeiro template encontrado
                test_template = template_files[0]
                result = subprocess.run([
                    sys.executable, str(cli_path), "from-template", str(test_template)
                ], capture_output=True, text=True, cwd=str(self.framework_path))
                
                test_success = result.returncode == 0
        except Exception:
            test_success = False
        
        duration = time.time() - start_time
        success = template_count > 0 and test_success
        
        details = f"Templates: {template_count} encontrados, criação {'OK' if test_success else 'FALHOU'}"
        
        self.log_result("templates", "functionality", success, duration, details)
        return success
    
    def validate_performance(self) -> bool:
        """Valida performance do sistema"""
        logger.info("⚡ Validando performance...")
        start_time = time.time()
        
        # Teste de inicialização do CLI
        cli_start = time.time()
        try:
            cli_path = self.framework_path / "scripts" / "unified_cli.py"
            result = subprocess.run([
                sys.executable, str(cli_path), "list-agents"
            ], capture_output=True, text=True, cwd=str(self.framework_path))
            cli_duration = time.time() - cli_start
            cli_success = result.returncode == 0
        except Exception:
            cli_duration = time.time() - cli_start
            cli_success = False
        
        # Critérios de performance
        cli_fast = cli_duration < 5.0  # CLI deve responder em menos de 5s
        
        duration = time.time() - start_time
        success = cli_success and cli_fast
        
        details = f"CLI: {cli_duration:.2f}s ({'OK' if cli_fast else 'LENTO'})"
        
        self.log_result("performance", "cli_speed", success, duration, details)
        return success
    
    def validate_integration(self) -> bool:
        """Valida integração entre componentes"""
        logger.info("🔗 Validando integração...")
        start_time = time.time()
        
        # Verificar se imports funcionam
        try:
            sys.path.insert(0, str(self.framework_path / "scripts"))
            from unified_agent_generator import UnifiedAgentGenerator
            
            generator = UnifiedAgentGenerator(str(self.framework_path))
            integration_success = True
            
        except Exception as e:
            integration_success = False
        
        duration = time.time() - start_time
        
        details = "Integração entre componentes " + ("OK" if integration_success else "FALHOU")
        
        self.log_result("integration", "components", integration_success, duration, details)
        return integration_success
    
    def run_complete_validation(self) -> Dict[str, Any]:
        """Executa validação completa"""
        logger.info("🚀 Iniciando validação completa do unified-sales-framework...")
        
        # Executar todas as validações
        validations = [
            ("Estrutura do Projeto", self.validate_project_structure),
            ("Estrutura dos Agentes", self.validate_agents_structure),
            ("Funcionalidade CLI", self.validate_cli_functionality),
            ("Sistema de Templates", self.validate_template_system),
            ("Performance", self.validate_performance),
            ("Integração", self.validate_integration)
        ]
        
        passed = 0
        total = len(validations)
        
        for name, validation_func in validations:
            logger.info(f"📋 Executando: {name}")
            try:
                if validation_func():
                    passed += 1
            except Exception as e:
                logger.error(f"❌ Erro em {name}: {e}")
        
        # Calcular estatísticas
        total_duration = time.time() - self.start_time
        success_rate = (passed / total) * 100
        
        # Gerar relatório
        report = {
            "summary": {
                "total_tests": len(self.results),
                "passed": sum(1 for r in self.results if r.success),
                "failed": sum(1 for r in self.results if not r.success),
                "success_rate": success_rate,
                "total_duration": total_duration
            },
            "validations": {
                "passed": passed,
                "total": total,
                "validation_rate": (passed / total) * 100
            },
            "details": [
                {
                    "component": r.component,
                    "test": r.test_name,
                    "success": r.success,
                    "duration": r.duration,
                    "details": r.details,
                    "error": r.error
                }
                for r in self.results
            ]
        }
        
        logger.info(f"✅ Validação completa: {passed}/{total} validações passaram ({success_rate:.1f}%)")
        return report

if __name__ == "__main__":
    validator = UnifiedFrameworkValidator()
    report = validator.run_complete_validation()
    
    # Salvar relatório
    report_path = Path("/home/ubuntu/validation_report.json")
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"📊 Relatório salvo em: {report_path}")
    print(f"🎯 Taxa de sucesso: {report['validations']['validation_rate']:.1f}%")

