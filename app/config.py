import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "sk-ant-default")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "pinecone-default")

# Pinecone Config
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east1-aws")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "portico-policies")

# LLM Config
MODEL_NAME = "claude-3-5-sonnet-20241022"
EMBEDDING_MODEL = "nomic-embed-text-v1.5"  # Using Pinecone's recommended model

# FastAPI Config
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# RAG Config
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RETRIEVAL = 5
MAX_CONTEXT_LENGTH = 4000

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "policies")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Create logs directory if not exists
os.makedirs(LOGS_DIR, exist_ok=True)
