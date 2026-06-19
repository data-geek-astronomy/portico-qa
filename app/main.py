import logging
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from app.rag_pipeline import PorticoPolicyRAG
from app.config import API_HOST, API_PORT, DEBUG

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Portico Policy Q&A API",
    description="RAG-based API for answering Portico policy questions",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG pipeline
rag_pipeline = None


# Pydantic models
class QuestionRequest(BaseModel):
    question: str
    use_retrieval: bool = True


class QuestionResponse(BaseModel):
    status: str
    question: str
    answer: str
    sources: List[dict] = []
    context_used: bool = False


class DocumentInfo(BaseModel):
    documents: List[str]
    total_chunks: int
    chunks_per_document: dict


class HealthResponse(BaseModel):
    status: str
    documents_ingested: int
    pipeline_ready: bool


# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize RAG pipeline on startup."""
    global rag_pipeline
    try:
        logger.info("Starting up Portico Policy Q&A API...")
        rag_pipeline = PorticoPolicyRAG()
        logger.info("RAG pipeline initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize RAG pipeline: {e}")
        raise


# Routes

@app.get("/", tags=["Info"])
async def root():
    """API root endpoint."""
    return {
        "name": "Portico Policy Q&A API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint."""
    if rag_pipeline is None:
        raise HTTPException(status_code=503, detail="RAG pipeline not initialized")

    doc_info = rag_pipeline.get_ingested_documents()
    return {
        "status": "healthy",
        "documents_ingested": len(doc_info.get("documents", [])),
        "pipeline_ready": True
    }


@app.post("/ask", response_model=QuestionResponse, tags=["RAG"])
async def ask_question(request: QuestionRequest):
    """
    Submit a question and get an answer from policy documents.

    - **question**: Your question about Portico policies
    - **use_retrieval**: Whether to use document retrieval (RAG)
    """
    if rag_pipeline is None:
        raise HTTPException(status_code=503, detail="RAG pipeline not initialized")

    if not request.question or len(request.question.strip()) < 3:
        raise HTTPException(status_code=400, detail="Question must be at least 3 characters")

    try:
        logger.info(f"Question received: {request.question}")
        response = rag_pipeline.answer_question(
            question=request.question,
            use_retrieval=request.use_retrieval
        )

        if response["status"] != "success":
            raise HTTPException(status_code=500, detail=response.get("message", "Error processing question"))

        return {
            "status": response["status"],
            "question": response["question"],
            "answer": response["answer"],
            "sources": response.get("sources", []),
            "context_used": response.get("context_used", False)
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/documents", response_model=DocumentInfo, tags=["Documents"])
async def get_documents():
    """Get information about ingested documents."""
    if rag_pipeline is None:
        raise HTTPException(status_code=503, detail="RAG pipeline not initialized")

    doc_info = rag_pipeline.get_ingested_documents()
    return {
        "documents": doc_info.get("documents", []),
        "total_chunks": doc_info.get("total_chunks", 0),
        "chunks_per_document": doc_info.get("chunks_per_document", {})
    }


@app.post("/ingest", tags=["Admin"])
async def ingest_documents(file_paths: Optional[List[str]] = None):
    """
    Ingest documents from the data/policies directory.

    - **file_paths**: Optional list of specific files to ingest
    """
    if rag_pipeline is None:
        raise HTTPException(status_code=503, detail="RAG pipeline not initialized")

    try:
        # Load documents from data directory
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "policies")

        if not os.path.exists(data_dir):
            raise HTTPException(status_code=400, detail=f"Data directory not found: {data_dir}")

        documents = []
        if file_paths:
            # Load specific files
            for filename in file_paths:
                filepath = os.path.join(data_dir, filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        documents.append((filename, f.read()))
        else:
            # Load all markdown files
            for filename in os.listdir(data_dir):
                if filename.endswith('.md'):
                    filepath = os.path.join(data_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        documents.append((filename, f.read()))

        if not documents:
            raise HTTPException(status_code=400, detail="No documents found to ingest")

        result = rag_pipeline.ingest_documents(documents)

        logger.info(f"Ingestion result: {result}")
        return {
            "status": result["status"],
            "documents_loaded": len(documents),
            "chunks_created": result.get("chunks_created", 0),
            "message": f"Successfully ingested {len(documents)} documents"
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during ingestion: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/example-questions", tags=["Help"])
async def get_example_questions():
    """Get example questions that can be asked."""
    examples = [
        "What is the pet policy at Portico?",
        "How much is the security deposit?",
        "What happens if rent is late?",
        "What are the fair housing protections?",
        "How long does it take for maintenance requests?",
        "Can I break my lease early?",
        "What is the lease renewal process?",
        "What constitutes normal wear and tear?",
        "Are service animals allowed?",
        "What is the eviction process?"
    ]
    return {"example_questions": examples}


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "status": "error",
        "message": exc.detail,
        "status_code": exc.status_code
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_HOST, port=API_PORT, debug=DEBUG)
