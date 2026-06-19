# Getting Started with Portico Policy Q&A RAG

## Prerequisites

- Python 3.9+
- Git
- Anthropic API key (Claude access)
- Pinecone account (optional, uses in-memory fallback for demo)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/portico-rag
cd portico-rag
```

### 2. Run setup script
```bash
chmod +x setup.sh
./setup.sh
```

Or manually:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
PINECONE_API_KEY=xxxxxxxxxxxxx
PINECONE_ENVIRONMENT=us-east1-aws
```

## Running Locally

### Terminal 1: Start the backend API
```bash
source venv/bin/activate
python -m uvicorn app.main:app --reload
```

The API will be available at: http://localhost:8000

API docs (Swagger UI): http://localhost:8000/docs

### Terminal 2: Start the frontend
```bash
source venv/bin/activate
streamlit run ui/app.py
```

The frontend will open at: http://localhost:8501

### Terminal 3: Ingest documents
```bash
source venv/bin/activate
python scripts/ingest_documents.py
```

## Quick Test

### 1. Ingest Policy Documents
```bash
python scripts/ingest_documents.py
```

Output:
```
✓ Successfully ingested 9 documents
✓ Created 145 chunks
```

### 2. Test the API directly
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the pet policy?"}'
```

Response:
```json
{
  "status": "success",
  "question": "What is the pet policy?",
  "answer": "Portico communities welcome responsible pet owners...",
  "sources": [
    {
      "document": "pet_policy.md",
      "section": "OVERVIEW",
      "chunk": 0
    }
  ],
  "context_used": true
}
```

### 3. Use the Web UI
Visit http://localhost:8501 and ask questions like:
- "What is the pet policy?"
- "How much is the security deposit?"
- "What happens if rent is late?"
- "How do I report maintenance?"

## Project Structure

```
portico-rag/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── rag_pipeline.py      # RAG logic
│   └── config.py            # Configuration
├── ui/
│   └── app.py               # Streamlit frontend
├── scripts/
│   ├── ingest_documents.py  # Document ingestion
│   └── setup_pinecone.py    # Pinecone setup
├── data/
│   └── policies/            # Policy markdown files
├── requirements.txt
├── .env.example
└── README.md
```

## API Endpoints

### POST /ask
Submit a question and get an answer.

**Request:**
```json
{
  "question": "What is the pet policy?",
  "use_retrieval": true
}
```

**Response:**
```json
{
  "status": "success",
  "question": "What is the pet policy?",
  "answer": "...",
  "sources": [...],
  "context_used": true
}
```

### GET /documents
List ingested documents and chunk counts.

**Response:**
```json
{
  "documents": ["lease_template.md", "pet_policy.md", ...],
  "total_chunks": 145,
  "chunks_per_document": {
    "lease_template.md": 15,
    "pet_policy.md": 12,
    ...
  }
}
```

### POST /ingest
Re-ingest documents from the data/policies directory.

**Response:**
```json
{
  "status": "success",
  "documents_loaded": 9,
  "chunks_created": 145,
  "message": "Successfully ingested 9 documents"
}
```

### GET /health
API health check.

**Response:**
```json
{
  "status": "healthy",
  "documents_ingested": 9,
  "pipeline_ready": true
}
```

### GET /example-questions
Get example questions that can be asked.

## Customization

### Adding Policy Documents

1. Create a new markdown file in `data/policies/`
2. Format with clear headings and sections
3. Restart the API and run:
   ```bash
   python scripts/ingest_documents.py
   ```

Example:
```markdown
# New Policy Title

## Section 1
Content here...

## Section 2
More content...
```

### Adjusting RAG Parameters

Edit `app/config.py`:
```python
CHUNK_SIZE = 1000          # Document chunk size
CHUNK_OVERLAP = 200        # Overlap between chunks
TOP_K_RETRIEVAL = 5        # Number of documents to retrieve
MAX_CONTEXT_LENGTH = 4000  # Maximum context length for LLM
```

### Changing the LLM Model

Edit `app/config.py`:
```python
MODEL_NAME = "claude-3-opus-20240229"  # Available: opus, sonnet, haiku
```

## Troubleshooting

### API won't start
- Check Python version: `python3 --version` (need 3.9+)
- Check if port 8000 is in use: `lsof -i :8000`
- Ensure virtual environment is activated

### Frontend won't connect to API
- Make sure API is running: `curl http://localhost:8000/health`
- Check API URL in Streamlit sidebar
- Look at browser console (F12) for network errors

### Documents not ingesting
- Check if `data/policies/` directory exists
- Verify markdown files are in correct format
- Run: `python scripts/ingest_documents.py` with verbose logging

### API key errors
- Verify .env file has correct keys
- Check that keys don't have extra whitespace
- Test API key directly: `curl -H "Authorization: Bearer $ANTHROPIC_API_KEY" ...`

## Performance Tips

1. **Increase chunk size** for faster processing but less precise retrieval
2. **Use Pinecone** for production instead of in-memory storage
3. **Enable caching** by running Redis alongside the API
4. **Filter by document type** to narrow search scope
5. **Use async endpoints** for handling concurrent requests

## Next Steps

1. [Deploy to Hugging Face Spaces](#deployment)
2. [Set up GitHub Actions for CI/CD](#github-actions)
3. [Add authentication to API](#authentication)
4. [Connect to your property management system](#integrations)

## Getting Help

- Check logs in `logs/` directory
- Review API documentation: http://localhost:8000/docs
- Open an issue on GitHub

## License

MIT License - see LICENSE file for details
