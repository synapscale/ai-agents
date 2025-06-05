#!/usr/bin/env python3
"""
Limpeza Inteligente de Duplicatas
Remove apenas duplicatas reais, preserva agentes válidos
"""

import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class IntelligentCleaner:
    def __init__(self, framework_path="/home/ubuntu/unified-sales-framework"):
        self.framework_path = Path(framework_path)
        
    def clean_duplicate_files_smart(self):
        """Remove apenas duplicatas reais, preserva agentes válidos"""
        logger.info("🧹 Limpeza inteligente de duplicatas...")
        
        removed_count = 0
        
        # 1. Remover apenas arquivos com "copy" no nome (duplicatas reais)
        copy_files = []
        for pattern in ["*copy*", "*Copy*", "*COPY*"]:
            copy_files.extend(list(self.framework_path.rglob(pattern)))
        
        for file_path in copy_files:
            # Verificar se não é um agente principal
            if "vertical_agents" in str(file_path) and file_path.is_dir():
                # Não remover diretórios principais de agentes verticais
                continue
                
            try:
                if file_path.is_file():
                    file_path.unlink()
                    removed_count += 1
                    logger.info(f"  ❌ Removido arquivo duplicado: {file_path.relative_to(self.framework_path)}")
                elif file_path.is_dir():
                    shutil.rmtree(file_path)
                    removed_count += 1
                    logger.info(f"  ❌ Removido diretório duplicado: {file_path.relative_to(self.framework_path)}")
            except Exception as e:
                logger.warning(f"  ⚠️ Erro ao remover {file_path}: {e}")
        
        # 2. Remover apenas arquivos vertical_* que são duplicatas (não diretórios principais)
        vertical_files = list(self.framework_path.rglob("vertical_*"))
        for file_path in vertical_files:
            # Preservar diretórios principais de agentes
            if file_path.parent.name == "vertical_agents":
                continue
                
            try:
                if file_path.is_file():
                    file_path.unlink()
                    removed_count += 1
                    logger.info(f"  ❌ Removido arquivo vertical duplicado: {file_path.relative_to(self.framework_path)}")
            except Exception as e:
                logger.warning(f"  ⚠️ Erro ao remover {file_path}: {e}")
        
        logger.info(f"✅ {removed_count} duplicatas reais removidas")
        return removed_count
    
    def restore_missing_agents(self):
        """Restaura agentes que podem ter sido removidos incorretamente"""
        logger.info("🔄 Verificando agentes faltantes...")
        
        # Lista de agentes que devem existir
        expected_vertical_agents = [
            "analytics_specialist",
            "api_integration_specialist", 
            "persuasion_copywriter",
            "neurohook_specialist",
            "metaphor_architect",
            "retention_optimizer",
            "knowledge_curator",
            "test_agent",
            "exemplo_vertical"
        ]
        
        vertical_path = self.framework_path / "vertical_agents"
        existing_agents = [d.name for d in vertical_path.iterdir() if d.is_dir()]
        
        missing_agents = set(expected_vertical_agents) - set(existing_agents)
        
        if missing_agents:
            logger.info(f"⚠️ Agentes faltantes: {missing_agents}")
            
            # Tentar restaurar do backup se disponível
            backup_path = Path("/tmp/framework_backup/unified-sales-framework/vertical_agents")
            if backup_path.exists():
                for agent_name in missing_agents:
                    backup_agent = backup_path / agent_name
                    if backup_agent.exists():
                        target_agent = vertical_path / agent_name
                        shutil.copytree(backup_agent, target_agent)
                        logger.info(f"  ✅ Restaurado: {agent_name}")
        
        # Verificar contagem final
        final_count = len([d for d in vertical_path.iterdir() if d.is_dir()])
        logger.info(f"✅ Agentes verticais: {final_count}")
        
        return final_count
    
    def create_missing_templates(self):
        """Recria templates que podem ter sido removidos"""
        logger.info("📋 Verificando templates...")
        
        templates_dir = self.framework_path / "templates" / "yaml_examples"
        templates_dir.mkdir(parents=True, exist_ok=True)
        
        # Template vertical
        vertical_template = templates_dir / "vertical_agent.yaml"
        if not vertical_template.exists():
            vertical_content = '''# Template para Agente Vertical
name: "exemplo_vertical"
type: "vertical"
specialization: "exemplo"

agent:
  model_name: "gemini-1.5-pro"
  instructions: |
    Você é um especialista EXCLUSIVO em exemplos.
    Você APENAS responde sobre exemplos.

tools:
  - name: "example_tool"
    description: "Ferramenta de exemplo"

knowledge:
  enabled: true
  domains:
    - "examples_only"
'''
            with open(vertical_template, 'w', encoding='utf-8') as f:
                f.write(vertical_content)
            logger.info("  ✅ Template vertical recriado")
        
        # Template tradicional
        traditional_template = templates_dir / "traditional_agent.yaml"
        if not traditional_template.exists():
            traditional_content = '''# Template para Agente Tradicional
name: "exemplo_tradicional"
type: "traditional"
category: "vendas"
specialization: "exemplo"

agent:
  model_name: "gemini-1.5-pro"
  instructions: |
    Você é um especialista em exemplos de vendas.

tools:
  - name: "sales_tool"
    description: "Ferramenta de vendas"

knowledge:
  enabled: true
  domains:
    - "sales_examples"
'''
            with open(traditional_template, 'w', encoding='utf-8') as f:
                f.write(traditional_content)
            logger.info("  ✅ Template tradicional recriado")
        
        return True
    
    def run_intelligent_cleanup(self):
        """Executa limpeza inteligente completa"""
        logger.info("🚀 Iniciando limpeza inteligente...")
        
        results = {}
        
        # 1. Limpeza inteligente de duplicatas
        results["duplicates_removed"] = self.clean_duplicate_files_smart()
        
        # 2. Restaurar agentes faltantes
        results["vertical_agents_count"] = self.restore_missing_agents()
        
        # 3. Recriar templates
        results["templates_created"] = self.create_missing_templates()
        
        logger.info("✅ Limpeza inteligente completa!")
        return results

if __name__ == "__main__":
    cleaner = IntelligentCleaner()
    results = cleaner.run_intelligent_cleanup()
    
    print("🎉 Limpeza Inteligente Executada!")
    print("📊 Resultados:")
    for key, value in results.items():
        print(f"  ✅ {key}: {value}")

