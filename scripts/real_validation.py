#!/usr/bin/env python3
"""
Testes de Validação Reais - Detecta Problemas Reais
"""

import os
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RealValidator:
    def __init__(self, framework_path):
        self.framework_path = Path(framework_path)
        
    def test_adk_integration_real(self):
        """Testa se ADK realmente funciona"""
        logger.info("🔧 Testando integração ADK real...")
        
        try:
            sys.path.insert(0, str(self.framework_path / "src"))
            from unified_sales_framework.core.fixed_adk import create_unified_agent
            
            # Tentar criar agente real
            agent = create_unified_agent(
                name="test_agent",
                instructions="Agente de teste"
            )
            
            # Testar funcionalidade básica
            result = agent.process("teste")
            
            if "test_agent" in result and "teste" in result:
                logger.info("✅ ADK integração funcionando")
                return True
            else:
                logger.error("❌ ADK não processa corretamente")
                return False
                
        except Exception as e:
            logger.error(f"❌ ADK falhou: {e}")
            return False
    
    def test_no_duplicates(self):
        """Testa se não há arquivos duplicados"""
        logger.info("🔍 Verificando duplicatas...")
        
        # Verificar arquivos copy (excluindo copywriter e copywriting que são válidos)
        copy_files = [f for f in self.framework_path.rglob("*copy*") 
                     if not any(valid in str(f).lower() for valid in ["copywriter", "copywriting"])]
        if copy_files:
            logger.error(f"❌ {len(copy_files)} arquivos 'copy' encontrados")
            return False
        
        # Verificar arquivos vertical_* (excluindo diretórios válidos e templates)
        vertical_files = [f for f in self.framework_path.rglob("vertical_*") 
                         if not (f.is_dir() and f.name in ["vertical_knowledge", "vertical_agents"]) 
                         and not str(f).endswith(".yaml")]
        if vertical_files:
            logger.error(f"❌ {len(vertical_files)} arquivos 'vertical_*' encontrados")
            return False
        
        logger.info("✅ Nenhuma duplicata encontrada")
        return True
    
    def test_project_size(self):
        """Testa se projeto tem tamanho razoável"""
        logger.info("📦 Verificando tamanho do projeto...")
        
        import subprocess
        result = subprocess.run(['du', '-s', str(self.framework_path)], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            size_kb = int(result.stdout.split()[0])
            size_mb = size_kb / 1024
            
            if size_mb > 100:  # Mais de 100MB é excessivo
                logger.error(f"❌ Projeto muito grande: {size_mb:.1f}MB")
                return False
            else:
                logger.info(f"✅ Tamanho adequado: {size_mb:.1f}MB")
                return True
        
        return False
    
    def test_agents_functional(self):
        """Testa se agentes são realmente funcionais"""
        logger.info("🤖 Testando funcionalidade dos agentes...")
        
        # Contar agentes únicos
        traditional_agents = list(self.framework_path.glob("agents/*/*"))
        traditional_count = len([d for d in traditional_agents if d.is_dir()])
        
        vertical_agents = list(self.framework_path.glob("vertical_agents/*"))
        vertical_count = len([d for d in vertical_agents if d.is_dir() and d.name != "__pycache__"])
        
        total_agents = traditional_count + vertical_count
        
        if total_agents < 15:
            logger.error(f"❌ Poucos agentes: {total_agents}")
            return False
        
        logger.info(f"✅ {total_agents} agentes encontrados")
        return True
    
    def run_real_validation(self):
        """Executa validação real completa"""
        logger.info("🚀 Executando validação real...")
        
        tests = [
            ("ADK Integration", self.test_adk_integration_real),
            ("No Duplicates", self.test_no_duplicates),
            ("Project Size", self.test_project_size),
            ("Agents Functional", self.test_agents_functional)
        ]
        
        passed = 0
        total = len(tests)
        
        for name, test_func in tests:
            logger.info(f"📋 Executando: {name}")
            try:
                if test_func():
                    passed += 1
                    logger.info(f"✅ {name}: PASSOU")
                else:
                    logger.error(f"❌ {name}: FALHOU")
            except Exception as e:
                logger.error(f"❌ {name}: ERRO - {e}")
        
        success_rate = (passed / total) * 100
        logger.info(f"🎯 Taxa de sucesso real: {success_rate:.1f}% ({passed}/{total})")
        
        return success_rate >= 90  # 90% mínimo para aprovação

if __name__ == "__main__":
    validator = RealValidator("/home/ubuntu/unified-sales-framework")
    success = validator.run_real_validation()
    
    if success:
        print("🎉 SISTEMA APROVADO - Validação real passou!")
    else:
        print("❌ SISTEMA REPROVADO - Correções necessárias!")
