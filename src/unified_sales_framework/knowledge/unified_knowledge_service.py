"""
Sistema de Conhecimento Unificado - Unified Sales Framework

Este módulo implementa a integração das bases de conhecimento do multi-agent-ai-system
com o sistema de memória e retrieval do ADK-Python.
"""

import os
import sys
from typing import List, Dict, Any, Optional
from pathlib import Path
import yaml
import json
from dataclasses import dataclass
from datetime import datetime

# Adicionar ADK ao path se disponível
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../src'))
    from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
    from google.adk.tools.retrieval.base_retrieval_tool import BaseRetrievalTool
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False


@dataclass
class KnowledgeDocument:
    """Representa um documento de conhecimento."""
    id: str
    title: str
    content: str
    domain: str
    agent_id: str
    source_file: str
    metadata: Dict[str, Any]
    embeddings: Optional[List[float]] = None
    created_at: datetime = None
    updated_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()


@dataclass
class KnowledgeDomain:
    """Representa um domínio de conhecimento especializado."""
    name: str
    description: str
    agent_ids: List[str]
    document_count: int
    specialization_keywords: List[str]
    retrieval_config: Dict[str, Any]


class UnifiedKnowledgeService:
    """
    Serviço unificado de conhecimento que integra as bases do multi-agent-ai-system
    com as capacidades de memória e retrieval do ADK.
    """
    
    def __init__(
        self,
        knowledge_base_path: str,
        memory_service: Optional[Any] = None,
        use_embeddings: bool = True
    ):
        self.knowledge_base_path = Path(knowledge_base_path)
        self.use_embeddings = use_embeddings
        
        # Configurar serviço de memória
        if memory_service is None:
            if ADK_AVAILABLE:
                self.memory_service = InMemoryMemoryService()
            else:
                self.memory_service = self._create_simple_memory_service()
        else:
            self.memory_service = memory_service
        
        # Estruturas de dados
        self.documents: Dict[str, KnowledgeDocument] = {}
        self.domains: Dict[str, KnowledgeDomain] = {}
        self.agent_knowledge_map: Dict[str, List[str]] = {}
        
        # Índices para busca
        self.keyword_index: Dict[str, List[str]] = {}
        self.domain_index: Dict[str, List[str]] = {}
        
        # Carregar conhecimento
        self._initialize_domains()
        self._load_knowledge_base()
    
    def _create_simple_memory_service(self):
        """Cria serviço de memória simplificado quando ADK não está disponível."""
        class SimpleMemoryService:
            def __init__(self):
                self.memories = {}
            
            def store(self, key: str, value: Any):
                self.memories[key] = value
            
            def retrieve(self, key: str) -> Any:
                return self.memories.get(key)
            
            def search(self, query: str, limit: int = 10) -> List[Any]:
                # Busca simples por substring
                results = []
                for key, value in self.memories.items():
                    if query.lower() in str(value).lower():
                        results.append(value)
                        if len(results) >= limit:
                            break
                return results
        
        return SimpleMemoryService()
    
    def _initialize_domains(self):
        """Inicializa os domínios de conhecimento baseados na estrutura do multi-agent-ai-system."""
        
        # Domínios identificados na análise
        domains_config = {
            "paradigm_shift": {
                "name": "Transformação de Paradigmas",
                "description": "Frameworks e metodologias para transformação de paradigmas de venda",
                "agent_ids": ["PARADIGM-ARCHITECT", "AXIOM-ARCHAEOLOGIST", "CONCEPT-ARCHITECT"],
                "specialization_keywords": [
                    "paradigma", "transformação", "framework", "conceitual", "persuasão",
                    "bloqueios", "objeções", "resistência", "pressupostos", "crenças"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.7,
                    "max_results": 10,
                    "boost_recent": True
                }
            },
            "persuasion_frameworks": {
                "name": "Frameworks de Persuasão",
                "description": "Estruturas conceituais para persuasão e influência em vendas",
                "agent_ids": ["PARADIGMATIC-LINGUIST", "LEGITIMACY-ENGINEER"],
                "specialization_keywords": [
                    "persuasão", "influência", "linguagem", "comunicação", "credibilidade",
                    "prova", "validação", "autoridade", "evidência", "narrativa"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.75,
                    "max_results": 8,
                    "boost_recent": False
                }
            },
            "sales_psychology": {
                "name": "Psicologia de Vendas",
                "description": "Conhecimento sobre psicologia aplicada a vendas e conversão",
                "agent_ids": ["AXIOM-ARCHAEOLOGIST", "TRANSDISCIPLINARY-SYNTHESIZER"],
                "specialization_keywords": [
                    "psicologia", "comportamento", "decisão", "motivação", "emocional",
                    "gatilhos", "vieses", "cognitivo", "mental", "subconsciente"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.8,
                    "max_results": 12,
                    "boost_recent": True
                }
            },
            "cognitive_biases": {
                "name": "Vieses Cognitivos",
                "description": "Conhecimento sobre vieses cognitivos aplicados a vendas",
                "agent_ids": ["AXIOM-ARCHAEOLOGIST", "CONCEPT-ARCHITECT"],
                "specialization_keywords": [
                    "viés", "cognitivo", "heurística", "julgamento", "decisão",
                    "ancoragem", "disponibilidade", "confirmação", "aversão", "perda"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.85,
                    "max_results": 6,
                    "boost_recent": False
                }
            },
            "behavioral_economics": {
                "name": "Economia Comportamental",
                "description": "Princípios de economia comportamental para vendas",
                "agent_ids": ["CONCEPT-ARCHITECT", "LEGITIMACY-ENGINEER"],
                "specialization_keywords": [
                    "economia", "comportamental", "valor", "preço", "custo",
                    "benefício", "utilidade", "escassez", "urgência", "social"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.7,
                    "max_results": 10,
                    "boost_recent": True
                }
            },
            "analogies_metaphors": {
                "name": "Analogias e Metáforas",
                "description": "Biblioteca de analogias e metáforas para comunicação persuasiva",
                "agent_ids": ["TRANSDISCIPLINARY-SYNTHESIZER"],
                "specialization_keywords": [
                    "analogia", "metáfora", "comparação", "símile", "exemplo",
                    "história", "narrativa", "ilustração", "conexão", "domínio"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.6,
                    "max_results": 15,
                    "boost_recent": False
                }
            },
            "credibility_systems": {
                "name": "Sistemas de Credibilidade",
                "description": "Metodologias para estabelecimento de credibilidade e autoridade",
                "agent_ids": ["LEGITIMACY-ENGINEER"],
                "specialization_keywords": [
                    "credibilidade", "autoridade", "confiança", "prova", "evidência",
                    "testemunho", "caso", "estudo", "resultado", "validação"
                ],
                "retrieval_config": {
                    "similarity_threshold": 0.8,
                    "max_results": 8,
                    "boost_recent": True
                }
            }
        }
        
        # Criar objetos de domínio
        for domain_id, config in domains_config.items():
            self.domains[domain_id] = KnowledgeDomain(
                name=config["name"],
                description=config["description"],
                agent_ids=config["agent_ids"],
                document_count=0,  # Será atualizado durante o carregamento
                specialization_keywords=config["specialization_keywords"],
                retrieval_config=config["retrieval_config"]
            )
    
    def _load_knowledge_base(self):
        """Carrega todas as bases de conhecimento do multi-agent-ai-system."""
        
        # Buscar todos os diretórios de knowledge_base
        knowledge_dirs = []
        if self.knowledge_base_path.exists():
            for root, dirs, files in os.walk(self.knowledge_base_path):
                if 'knowledge_base' in root or 'knowledge' in root:
                    knowledge_dirs.append(Path(root))
        
        print(f"📚 Encontrados {len(knowledge_dirs)} diretórios de conhecimento")
        
        total_documents = 0
        for knowledge_dir in knowledge_dirs:
            documents_loaded = self._load_knowledge_directory(knowledge_dir)
            total_documents += documents_loaded
        
        print(f"✅ Carregados {total_documents} documentos de conhecimento")
        
        # Atualizar contadores de domínios
        self._update_domain_counts()
        
        # Construir índices
        self._build_indexes()
    
    def _load_knowledge_directory(self, knowledge_dir: Path) -> int:
        """Carrega documentos de um diretório específico de conhecimento."""
        
        documents_loaded = 0
        
        # Identificar agente pelo caminho
        agent_id = self._extract_agent_id_from_path(knowledge_dir)
        
        # Buscar arquivos markdown
        for md_file in knowledge_dir.rglob("*.md"):
            try:
                document = self._load_knowledge_document(md_file, agent_id)
                if document:
                    self.documents[document.id] = document
                    
                    # Mapear agente -> documentos
                    if agent_id not in self.agent_knowledge_map:
                        self.agent_knowledge_map[agent_id] = []
                    self.agent_knowledge_map[agent_id].append(document.id)
                    
                    # Armazenar na memória
                    self._store_in_memory(document)
                    
                    documents_loaded += 1
                    
            except Exception as e:
                print(f"⚠️ Erro ao carregar {md_file}: {e}")
        
        return documents_loaded
    
    def _extract_agent_id_from_path(self, path: Path) -> str:
        """Extrai o ID do agente a partir do caminho do arquivo."""
        
        path_str = str(path).lower()
        
        # Mapeamento de padrões para agent_ids
        agent_patterns = {
            "paradigm_architect": "PARADIGM-ARCHITECT",
            "axiom-archaeologist": "AXIOM-ARCHAEOLOGIST",
            "concept-architect": "CONCEPT-ARCHITECT",
            "paradigmatic-linguist": "PARADIGMATIC-LINGUIST",
            "legitimacy-engineer": "LEGITIMACY-ENGINEER",
            "transdisciplinary-synthesizer": "TRANSDISCIPLINARY-SYNTHESIZER",
            "analyticsgpt": "ANALYTICS-GPT",
            "apiunifymaster": "API-UNIFY-MASTER",
            "hotmartapimaster": "HOTMART-API-MASTER",
            "kiwifyapimaster": "KIWIFY-API-MASTER",
            "perfectpayapimaster": "PERFECTPAY-API-MASTER"
        }
        
        for pattern, agent_id in agent_patterns.items():
            if pattern in path_str:
                return agent_id
        
        # Fallback: usar nome do diretório pai
        return path.parent.name.upper()
    
    def _load_knowledge_document(self, file_path: Path, agent_id: str) -> Optional[KnowledgeDocument]:
        """Carrega um documento individual de conhecimento."""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair metadados do frontmatter se existir
            metadata = self._extract_frontmatter(content)
            
            # Remover frontmatter do conteúdo
            content = self._remove_frontmatter(content)
            
            # Determinar domínio baseado no conteúdo e agente
            domain = self._determine_domain(content, agent_id)
            
            # Criar documento
            document = KnowledgeDocument(
                id=f"{agent_id}_{file_path.stem}",
                title=metadata.get('title', file_path.stem.replace('_', ' ').title()),
                content=content,
                domain=domain,
                agent_id=agent_id,
                source_file=str(file_path),
                metadata=metadata
            )
            
            return document
            
        except Exception as e:
            print(f"❌ Erro ao processar {file_path}: {e}")
            return None
    
    def _extract_frontmatter(self, content: str) -> Dict[str, Any]:
        """Extrai metadados do frontmatter YAML."""
        
        if content.startswith('---'):
            try:
                end_marker = content.find('---', 3)
                if end_marker != -1:
                    frontmatter = content[3:end_marker].strip()
                    return yaml.safe_load(frontmatter) or {}
            except:
                pass
        
        return {}
    
    def _remove_frontmatter(self, content: str) -> str:
        """Remove frontmatter do conteúdo."""
        
        if content.startswith('---'):
            end_marker = content.find('---', 3)
            if end_marker != -1:
                return content[end_marker + 3:].strip()
        
        return content
    
    def _determine_domain(self, content: str, agent_id: str) -> str:
        """Determina o domínio de conhecimento baseado no conteúdo e agente."""
        
        content_lower = content.lower()
        
        # Pontuação por domínio baseada em keywords
        domain_scores = {}
        
        for domain_id, domain in self.domains.items():
            score = 0
            
            # Pontuação por keywords
            for keyword in domain.specialization_keywords:
                score += content_lower.count(keyword.lower()) * 2
            
            # Pontuação por agente
            if agent_id in domain.agent_ids:
                score += 10
            
            domain_scores[domain_id] = score
        
        # Retornar domínio com maior pontuação
        if domain_scores:
            best_domain = max(domain_scores, key=domain_scores.get)
            if domain_scores[best_domain] > 0:
                return best_domain
        
        # Fallback
        return "paradigm_shift"
    
    def _store_in_memory(self, document: KnowledgeDocument):
        """Armazena documento no serviço de memória."""
        
        try:
            # Criar chave única
            memory_key = f"knowledge_{document.id}"
            
            # Preparar dados para armazenamento
            memory_data = {
                "id": document.id,
                "title": document.title,
                "content": document.content,
                "domain": document.domain,
                "agent_id": document.agent_id,
                "metadata": document.metadata,
                "created_at": document.created_at.isoformat() if document.created_at else None
            }
            
            # Armazenar
            self.memory_service.store(memory_key, memory_data)
            
        except Exception as e:
            print(f"⚠️ Erro ao armazenar na memória {document.id}: {e}")
    
    def _update_domain_counts(self):
        """Atualiza contadores de documentos por domínio."""
        
        for domain_id in self.domains:
            count = sum(1 for doc in self.documents.values() if doc.domain == domain_id)
            self.domains[domain_id].document_count = count
    
    def _build_indexes(self):
        """Constrói índices para busca eficiente."""
        
        # Índice por keywords
        for doc_id, document in self.documents.items():
            words = document.content.lower().split()
            for word in words:
                if len(word) > 3:  # Ignorar palavras muito curtas
                    if word not in self.keyword_index:
                        self.keyword_index[word] = []
                    self.keyword_index[word].append(doc_id)
        
        # Índice por domínio
        for doc_id, document in self.documents.items():
            domain = document.domain
            if domain not in self.domain_index:
                self.domain_index[domain] = []
            self.domain_index[domain].append(doc_id)
    
    def search_knowledge(
        self,
        query: str,
        domain: Optional[str] = None,
        agent_id: Optional[str] = None,
        limit: int = 10
    ) -> List[KnowledgeDocument]:
        """
        Busca documentos de conhecimento baseado em query, domínio e agente.
        """
        
        results = []
        query_lower = query.lower()
        
        # Buscar por keywords
        relevant_docs = set()
        for word in query_lower.split():
            if word in self.keyword_index:
                relevant_docs.update(self.keyword_index[word])
        
        # Filtrar por domínio se especificado
        if domain and domain in self.domain_index:
            relevant_docs = relevant_docs.intersection(set(self.domain_index[domain]))
        
        # Filtrar por agente se especificado
        if agent_id and agent_id in self.agent_knowledge_map:
            relevant_docs = relevant_docs.intersection(set(self.agent_knowledge_map[agent_id]))
        
        # Calcular relevância e ordenar
        scored_docs = []
        for doc_id in relevant_docs:
            if doc_id in self.documents:
                document = self.documents[doc_id]
                score = self._calculate_relevance_score(document, query_lower)
                scored_docs.append((score, document))
        
        # Ordenar por relevância e retornar
        scored_docs.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored_docs[:limit]]
    
    def _calculate_relevance_score(self, document: KnowledgeDocument, query: str) -> float:
        """Calcula score de relevância de um documento para uma query."""
        
        score = 0.0
        content_lower = document.content.lower()
        title_lower = document.title.lower()
        
        # Pontuação por matches no título (peso maior)
        for word in query.split():
            if word in title_lower:
                score += 3.0
        
        # Pontuação por matches no conteúdo
        for word in query.split():
            score += content_lower.count(word) * 1.0
        
        # Boost por domínio relevante
        domain_keywords = self.domains.get(document.domain, {}).specialization_keywords or []
        for keyword in domain_keywords:
            if keyword.lower() in query:
                score += 2.0
        
        return score
    
    def get_domain_knowledge(self, domain: str) -> List[KnowledgeDocument]:
        """Retorna todos os documentos de um domínio específico."""
        
        if domain in self.domain_index:
            return [self.documents[doc_id] for doc_id in self.domain_index[domain] 
                   if doc_id in self.documents]
        return []
    
    def get_agent_knowledge(self, agent_id: str) -> List[KnowledgeDocument]:
        """Retorna todos os documentos de conhecimento de um agente específico."""
        
        if agent_id in self.agent_knowledge_map:
            return [self.documents[doc_id] for doc_id in self.agent_knowledge_map[agent_id]
                   if doc_id in self.documents]
        return []
    
    def get_knowledge_summary(self) -> Dict[str, Any]:
        """Retorna resumo do sistema de conhecimento."""
        
        return {
            "total_documents": len(self.documents),
            "total_domains": len(self.domains),
            "total_agents": len(self.agent_knowledge_map),
            "domains": {
                domain_id: {
                    "name": domain.name,
                    "document_count": domain.document_count,
                    "agent_ids": domain.agent_ids
                }
                for domain_id, domain in self.domains.items()
            },
            "agents": {
                agent_id: len(doc_ids)
                for agent_id, doc_ids in self.agent_knowledge_map.items()
            }
        }


class UnifiedKnowledgeRetrievalTool:
    """
    Ferramenta de recuperação de conhecimento que pode ser usada pelos agentes.
    """
    
    def __init__(self, knowledge_service: UnifiedKnowledgeService):
        self.knowledge_service = knowledge_service
        self.name = "knowledge_retrieval"
        self.description = "Recupera conhecimento especializado baseado em query e contexto"
    
    def retrieve(
        self,
        query: str,
        domain: Optional[str] = None,
        agent_id: Optional[str] = None,
        limit: int = 5
    ) -> str:
        """
        Recupera conhecimento relevante e retorna como texto formatado.
        """
        
        documents = self.knowledge_service.search_knowledge(
            query=query,
            domain=domain,
            agent_id=agent_id,
            limit=limit
        )
        
        if not documents:
            return f"Nenhum conhecimento encontrado para: {query}"
        
        # Formatar resultados
        result_parts = [f"📚 CONHECIMENTO RECUPERADO PARA: {query}\n"]
        
        for i, doc in enumerate(documents, 1):
            result_parts.append(f"## {i}. {doc.title}")
            result_parts.append(f"**Domínio**: {doc.domain}")
            result_parts.append(f"**Agente**: {doc.agent_id}")
            result_parts.append(f"**Conteúdo**:")
            
            # Limitar conteúdo para não sobrecarregar
            content_preview = doc.content[:500]
            if len(doc.content) > 500:
                content_preview += "..."
            
            result_parts.append(content_preview)
            result_parts.append("---\n")
        
        return "\n".join(result_parts)
    
    def get_domain_overview(self, domain: str) -> str:
        """Retorna visão geral de um domínio de conhecimento."""
        
        if domain not in self.knowledge_service.domains:
            return f"Domínio '{domain}' não encontrado."
        
        domain_obj = self.knowledge_service.domains[domain]
        documents = self.knowledge_service.get_domain_knowledge(domain)
        
        overview_parts = [
            f"# 📖 DOMÍNIO: {domain_obj.name}",
            f"**Descrição**: {domain_obj.description}",
            f"**Agentes Especializados**: {', '.join(domain_obj.agent_ids)}",
            f"**Total de Documentos**: {len(documents)}",
            f"**Keywords Especializadas**: {', '.join(domain_obj.specialization_keywords[:10])}",
            "\n## 📑 DOCUMENTOS DISPONÍVEIS:"
        ]
        
        for doc in documents[:10]:  # Limitar a 10 documentos
            overview_parts.append(f"- **{doc.title}** (Agente: {doc.agent_id})")
        
        if len(documents) > 10:
            overview_parts.append(f"... e mais {len(documents) - 10} documentos")
        
        return "\n".join(overview_parts)

