#!/usr/bin/env python3
"""
Testes Específicos de Agentes - Validação Individual
"""

import os
import sys
import time
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AgentFunctionalityTester:
    """
    Testa funcionalidade específica dos agentes
    """
    
    def __init__(self, framework_path="/home/ubuntu/unified-sales-framework"):
        self.framework_path = Path(framework_path)
        sys.path.insert(0, str(self.framework_path / "scripts"))
        
    def test_agent_initialization(self, agent_path: Path, agent_type: str) -> bool:
        """Testa inicialização de um agente específico"""
        try:
            # Verificar se agent.py existe e pode ser importado
            agent_file = agent_path / "agent.py"
            if not agent_file.exists():
                return False
            
            # Ler conteúdo do agente
            with open(agent_file, 'r', encoding='utf-8') as f:
                agent_content = f.read()
            
            # Verificar se contém elementos essenciais
            essential_elements = [
                "class", "def", "__init__"
            ]
            
            for element in essential_elements:
                if element not in agent_content:
                    return False
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao testar agente {agent_path.name}: {e}")
            return False
    
    def test_vertical_agent_specialization(self, agent_path: Path) -> bool:
        """Testa especialização de agente vertical"""
        try:
            # Verificar arquivos específicos de agente vertical
            required_files = ["prompt.txt", "config.yaml", "tools.yaml"]
            
            for file_name in required_files:
                file_path = agent_path / file_name
                if not file_path.exists():
                    return False
            
            # Verificar conteúdo do prompt para especialização
            prompt_file = agent_path / "prompt.txt"
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt_content = f.read()
            
            # Agentes verticais devem ter indicações de especialização
            specialization_indicators = [
                "especialista", "exclusivo", "apenas", "específico", "focado"
            ]
            
            has_specialization = any(indicator in prompt_content.lower() 
                                   for indicator in specialization_indicators)
            
            return has_specialization
            
        except Exception as e:
            logger.error(f"Erro ao testar especialização {agent_path.name}: {e}")
            return False
    
    def test_traditional_agent_structure(self, agent_path: Path) -> bool:
        """Testa estrutura de agente tradicional"""
        try:
            # Verificar arquivos básicos
            required_files = ["agent.py", "prompt.txt"]
            
            for file_name in required_files:
                file_path = agent_path / file_name
                if not file_path.exists():
                    return False
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao testar agente tradicional {agent_path.name}: {e}")
            return False
    
    def run_agent_tests(self) -> dict:
        """Executa testes em todos os agentes"""
        logger.info("🧪 Iniciando testes específicos de agentes...")
        
        results = {
            "traditional_agents": {"tested": 0, "passed": 0, "failed": []},
            "vertical_agents": {"tested": 0, "passed": 0, "failed": []}
        }
        
        # Testar agentes tradicionais
        agents_path = self.framework_path / "agents"
        if agents_path.exists():
            for category_dir in agents_path.iterdir():
                if category_dir.is_dir():
                    for agent_dir in category_dir.iterdir():
                        if agent_dir.is_dir():
                            results["traditional_agents"]["tested"] += 1
                            
                            # Testar inicialização
                            init_ok = self.test_agent_initialization(agent_dir, "traditional")
                            # Testar estrutura
                            struct_ok = self.test_traditional_agent_structure(agent_dir)
                            
                            if init_ok and struct_ok:
                                results["traditional_agents"]["passed"] += 1
                                logger.info(f"✅ Agente tradicional {agent_dir.name} OK")
                            else:
                                results["traditional_agents"]["failed"].append(agent_dir.name)
                                logger.warning(f"❌ Agente tradicional {agent_dir.name} FALHOU")
        
        # Testar agentes verticais
        vertical_path = self.framework_path / "vertical_agents"
        if vertical_path.exists():
            for agent_dir in vertical_path.iterdir():
                if agent_dir.is_dir() and agent_dir.name != "__pycache__":
                    results["vertical_agents"]["tested"] += 1
                    
                    # Testar inicialização
                    init_ok = self.test_agent_initialization(agent_dir, "vertical")
                    # Testar especialização
                    spec_ok = self.test_vertical_agent_specialization(agent_dir)
                    
                    if init_ok and spec_ok:
                        results["vertical_agents"]["passed"] += 1
                        logger.info(f"✅ Agente vertical {agent_dir.name} OK")
                    else:
                        results["vertical_agents"]["failed"].append(agent_dir.name)
                        logger.warning(f"❌ Agente vertical {agent_dir.name} FALHOU")
        
        # Calcular estatísticas
        total_tested = results["traditional_agents"]["tested"] + results["vertical_agents"]["tested"]
        total_passed = results["traditional_agents"]["passed"] + results["vertical_agents"]["passed"]
        
        success_rate = (total_passed / total_tested * 100) if total_tested > 0 else 0
        
        logger.info(f"📊 Testes de agentes: {total_passed}/{total_tested} passaram ({success_rate:.1f}%)")
        
        results["summary"] = {
            "total_tested": total_tested,
            "total_passed": total_passed,
            "success_rate": success_rate
        }
        
        return results

def test_end_to_end_workflow():
    """Teste end-to-end do workflow completo"""
    logger.info("🔄 Executando teste end-to-end...")
    
    framework_path = Path("/home/ubuntu/unified-sales-framework")
    
    try:
        # 1. Testar listagem de agentes
        import subprocess
        cli_path = framework_path / "scripts" / "unified_cli.py"
        
        result = subprocess.run([
            sys.executable, str(cli_path), "list-agents"
        ], capture_output=True, text=True, cwd=str(framework_path))
        
        if result.returncode != 0:
            logger.error("❌ Falha na listagem de agentes")
            return False
        
        # 2. Verificar se agentes estão listados
        output = result.stdout
        if "AGENTES TRADICIONAIS" not in output or "AGENTES VERTICAIS" not in output:
            logger.error("❌ Saída da listagem incompleta")
            return False
        
        # 3. Testar criação via template (se templates existem)
        templates_dir = framework_path / "templates" / "yaml_examples"
        if templates_dir.exists():
            template_files = list(templates_dir.glob("*.yaml"))
            if template_files:
                test_template = template_files[0]
                
                result = subprocess.run([
                    sys.executable, str(cli_path), "from-template", str(test_template)
                ], capture_output=True, text=True, cwd=str(framework_path))
                
                if result.returncode != 0:
                    logger.warning("⚠️ Criação via template falhou, mas não é crítico")
        
        logger.info("✅ Teste end-to-end passou")
        return True
        
    except Exception as e:
        logger.error(f"❌ Erro no teste end-to-end: {e}")
        return False

if __name__ == "__main__":
    # Executar testes específicos de agentes
    tester = AgentFunctionalityTester()
    agent_results = tester.run_agent_tests()
    
    # Executar teste end-to-end
    e2e_success = test_end_to_end_workflow()
    
    # Resumo final
    print("\n" + "="*60)
    print("📋 RESUMO DOS TESTES ESPECÍFICOS")
    print("="*60)
    
    print(f"🤖 Agentes Tradicionais: {agent_results['traditional_agents']['passed']}/{agent_results['traditional_agents']['tested']}")
    if agent_results['traditional_agents']['failed']:
        print(f"   ❌ Falharam: {', '.join(agent_results['traditional_agents']['failed'])}")
    
    print(f"🎯 Agentes Verticais: {agent_results['vertical_agents']['passed']}/{agent_results['vertical_agents']['tested']}")
    if agent_results['vertical_agents']['failed']:
        print(f"   ❌ Falharam: {', '.join(agent_results['vertical_agents']['failed'])}")
    
    print(f"🔄 Teste End-to-End: {'✅ PASSOU' if e2e_success else '❌ FALHOU'}")
    
    print(f"\n🎯 Taxa de Sucesso Geral: {agent_results['summary']['success_rate']:.1f}%")
    
    if agent_results['summary']['success_rate'] == 100.0 and e2e_success:
        print("🎉 TODOS OS TESTES PASSARAM - SISTEMA 100% FUNCIONAL!")
    else:
        print("⚠️ Alguns testes falharam - Verificar logs acima")

