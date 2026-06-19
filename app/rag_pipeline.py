import logging
from typing import List, Tuple, Optional
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from anthropic import Anthropic
import pinecone
import os

from app.config import (
    ANTHROPIC_API_KEY,
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    PINECONE_ENVIRONMENT,
    MODEL_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K_RETRIEVAL,
    MAX_CONTEXT_LENGTH,
)
from app.static_qa import get_static_answer

logger = logging.getLogger(__name__)


class PorticoPolicyRAG:
    def __init__(self):
        """Initialize RAG pipeline with Pinecone and Claude."""
        self.chunk_size = CHUNK_SIZE
        self.chunk_overlap = CHUNK_OVERLAP
        self.top_k = TOP_K_RETRIEVAL
        self.max_context = MAX_CONTEXT_LENGTH

        # Initialize embeddings using Ollama (local embedding model)
        # For production, use Pinecone's ServerlessEmbedding
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text-v1.5", base_url="http://localhost:11434")

        # Initialize Pinecone
        self._init_pinecone()

        # Initialize Anthropic client directly
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
        self.model = MODEL_NAME

        # Setup RAG chain
        self.qa_chain = None
        self._setup_qa_chain()

        logger.info("PorticoPolicyRAG initialized successfully")

    def _init_pinecone(self):
        """Initialize Pinecone index."""
        try:
            pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

            # Check if index exists
            indexes = pinecone.list_indexes()
            if PINECONE_INDEX_NAME not in indexes:
                logger.warning(f"Index {PINECONE_INDEX_NAME} not found. Please create it in Pinecone console.")
                logger.info("For demo, using in-memory vector store fallback.")
                self.use_pinecone = False
            else:
                self.use_pinecone = True
                logger.info(f"Connected to Pinecone index: {PINECONE_INDEX_NAME}")
        except Exception as e:
            logger.warning(f"Pinecone initialization failed: {e}. Using in-memory fallback.")
            self.use_pinecone = False

    def _setup_qa_chain(self):
        """Setup the QA chain with RAG."""
        # Note: In production, vectorstore would be Pinecone
        # For demo purposes, this is a placeholder
        template = """Use the following policy documents from Portico to answer the question.
If the answer is not in the documents, say "This information is not covered in our policy documents."

Context:
{context}

Question: {question}

Answer with specific policy details and cite the relevant policy section when applicable:"""

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        # This will be properly initialized when documents are ingested
        logger.info("QA chain initialized")

    def ingest_documents(self, documents: List[Tuple[str, str]]):
        """
        Ingest documents into vector database.

        Args:
            documents: List of (document_name, content) tuples
        """
        logger.info(f"Starting document ingestion for {len(documents)} documents...")

        try:
            # Split documents into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n", "\n", ". ", " ", ""]
            )

            all_chunks = []
            for doc_name, content in documents:
                chunks = splitter.split_text(content)
                for i, chunk in enumerate(chunks):
                    all_chunks.append({
                        "content": chunk,
                        "metadata": {
                            "source": doc_name,
                            "chunk": i,
                            "section": self._extract_section(chunk)
                        }
                    })

            logger.info(f"Created {len(all_chunks)} chunks from {len(documents)} documents")

            # Store in Pinecone or in-memory (demo)
            if self.use_pinecone:
                self._store_in_pinecone(all_chunks)
            else:
                self._store_in_memory(all_chunks)

            logger.info("Document ingestion completed successfully")
            return {"status": "success", "chunks_created": len(all_chunks)}

        except Exception as e:
            logger.error(f"Error during document ingestion: {e}")
            return {"status": "error", "message": str(e)}

    def _store_in_pinecone(self, chunks: List[dict]):
        """Store chunks in Pinecone (placeholder for demo)."""
        # In production, use Pinecone client to upload vectors
        logger.info("Would store in Pinecone here")

    def _store_in_memory(self, chunks: List[dict]):
        """Store chunks in memory for demo."""
        self.chunks = chunks
        logger.info(f"Stored {len(chunks)} chunks in memory")

    def _extract_section(self, text: str) -> str:
        """Extract section heading from text."""
        lines = text.split("\n")
        for line in lines:
            if line.startswith("#"):
                return line.replace("#", "").strip()
        return "General"

    def answer_question(self, question: str, use_retrieval: bool = True) -> dict:
        """
        Answer a question using static Q&A mapping first, then fallback to API.

        Args:
            question: User question
            use_retrieval: Whether to use retrieval (RAG) or just LLM

        Returns:
            Dictionary with answer and sources
        """
        logger.info(f"Processing question: {question}")

        try:
            # Step 1: Check static Q&A mapping first (no API needed)
            static_result = get_static_answer(question)
            if static_result:
                logger.info(f"Found static answer for question: {question}")
                return {
                    "status": "success",
                    "question": question,
                    "answer": static_result["answer"],
                    "sources": [
                        {
                            "document": static_result["document"],
                            "section": static_result["section"],
                            "chunk": 0
                        }
                    ],
                    "context_used": True,
                    "source_type": "static"
                }

            # Step 2: If not in static mapping, retrieve from documents
            if use_retrieval and hasattr(self, 'chunks'):
                sources = self._retrieve_documents(question)
                context = "\n\n".join([s["content"] for s in sources])
            else:
                context = ""
                sources = []

            # Step 3: Generate answer using Anthropic SDK (if available)
            prompt = f"""You are an expert on Portico property management policies.
Answer the following question accurately using only the provided policy information.
If the answer is not in the policies, clearly state that.

Policy Context:
{context}

Question: {question}

Provide a clear, actionable answer with specific policy references where relevant."""

            answer = None
            try:
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=1000,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = message.content[0].text
                logger.info(f"Generated answer using API for: {question}")
            except Exception as api_error:
                # Fallback: return answer from retrieved documents if API fails
                logger.warning(f"API error: {api_error}. Using retrieved documents instead.")
                if sources:
                    answer = f"Based on Portico policies:\n\n{sources[0]['content'][:500]}..."
                else:
                    answer = "I could not find this information in the policy database. Please contact property management for assistance."

            return {
                "status": "success",
                "question": question,
                "answer": answer,
                "sources": [
                    {
                        "document": s["metadata"]["source"],
                        "section": s["metadata"].get("section", "General"),
                        "chunk": s["metadata"]["chunk"]
                    } for s in sources
                ] if sources else [],
                "context_used": len(sources) > 0,
                "source_type": "api" if answer else "documents"
            }

        except Exception as e:
            logger.error(f"Error generating answer: {e}")
            return {
                "status": "error",
                "message": str(e),
                "question": question
            }

    def _retrieve_documents(self, question: str, k: int = None) -> List[dict]:
        """
        Retrieve relevant documents for a question.

        Args:
            question: User question
            k: Number of documents to retrieve

        Returns:
            List of relevant document chunks
        """
        if k is None:
            k = self.top_k

        if not hasattr(self, 'chunks'):
            logger.warning("No documents ingested yet")
            return []

        # Simple keyword and semantic matching (in production, use embeddings)
        question_words = set(question.lower().split())
        scored_chunks = []

        for chunk in self.chunks:
            content = chunk["content"].lower()
            # Score based on keyword overlap
            score = sum(1 for word in question_words if word in content)
            if score > 0:
                scored_chunks.append((score, chunk))

        # Sort by score and return top k
        scored_chunks.sort(reverse=True, key=lambda x: x[0])
        return [chunk for _, chunk in scored_chunks[:k]]

    def get_ingested_documents(self) -> dict:
        """Get list of ingested documents."""
        if not hasattr(self, 'chunks'):
            return {"documents": [], "total_chunks": 0}

        # Group by document source
        docs = {}
        for chunk in self.chunks:
            source = chunk["metadata"]["source"]
            if source not in docs:
                docs[source] = 0
            docs[source] += 1

        return {
            "documents": list(docs.keys()),
            "total_chunks": len(self.chunks),
            "chunks_per_document": docs
        }
