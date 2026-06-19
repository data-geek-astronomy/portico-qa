# Quick Start - Portico Policy Q&A RAG

**Get the system running in 3 steps:**

## Step 1: Install & Setup (2 minutes)

```bash
cd portico-rag
chmod +x setup.sh
./setup.sh
```

The script will:
✓ Create Python virtual environment  
✓ Install dependencies  
✓ Create .env file  
✓ Set up directories  

## Step 2: Configure (1 minute)

Edit `.env` file:
```bash
nano .env
```

Add your API keys:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
PINECONE_API_KEY=your-key-here (optional for demo)
```

## Step 3: Run (1 minute)

**Terminal 1 - Start API:**
```bash
source venv/bin/activate
python -m uvicorn app.main:app --reload
```
→ API at http://localhost:8000

**Terminal 2 - Start Frontend:**
```bash
source venv/bin/activate
streamlit run ui/app.py
```
→ UI at http://localhost:8501

**Terminal 3 - Ingest Documents (optional):**
```bash
source venv/bin/activate
python scripts/ingest_documents.py
```

---

## ✅ Done!

Open http://localhost:8501 and ask a question!

Example questions:
- "What is the pet policy?"
- "How much is the security deposit?"
- "What happens if rent is late?"

---

## API Documentation

Visit http://localhost:8000/docs for interactive API docs (Swagger UI)

### Quick API Test

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the pet policy?"}'
```

---

## Docker (Optional)

```bash
docker-compose up
```

Opens at http://localhost:8501 automatically

---

## Next Steps

1. Read GETTING_STARTED.md for detailed setup
2. Check PROJECT_SUMMARY.md for what was built
3. Review PITCH_TO_LEADERSHIP.md for business context
4. Customize policy documents in `data/policies/`

## Troubleshooting

**API won't start?**
```bash
# Check Python version
python3 --version  # Should be 3.9+

# Check port 8000 is free
lsof -i :8000
```

**Frontend won't connect?**
```bash
# Make sure API is running
curl http://localhost:8000/health
```

**Documents not loading?**
```bash
python scripts/ingest_documents.py
# Check for errors in output
```

---

**Questions?** Check the logs in `logs/` directory or read GETTING_STARTED.md
