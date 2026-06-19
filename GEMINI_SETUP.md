# Google Gemini API Setup

Follow these steps to get your Gemini API key.

## Step 1: Get Your Gemini API Key

1. Go to: https://aistudio.google.com/app/apikey
2. Click **"Create API Key"**
3. Select **"Create new API key in new project"**
4. Copy the API key (looks like: `AIza...`)
5. Keep it safe!

---

## Step 2: Rebuild Docker Images

Since we updated requirements.txt, rebuild:

```bash
docker build --no-cache -t portico-api:latest .
docker build -f Dockerfile.streamlit -t portico-ui:latest .
```

---

## Step 3: Tag & Push to Docker Hub

```bash
docker tag portico-api:latest aravind1236/portico-api:latest
docker tag portico-ui:latest aravind1236/portico-ui:latest
docker push aravind1236/portico-api:latest
docker push aravind1236/portico-ui:latest
```

---

## Step 4: Deploy to Azure with Gemini

Replace `AIza-YOUR-KEY` with your actual Gemini API key:

### Deploy API:

```bash
az container create \
  --resource-group portico-rg \
  --name portico-api \
  --image aravind1236/portico-api:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8000 \
  --environment-variables \
    GOOGLE_API_KEY=AIza-YOUR-KEY \
    PINECONE_API_KEY=optional \
    PINECONE_ENVIRONMENT=us-east1-aws \
    DEBUG=False \
  --dns-name-label portico-api \
  --restart-policy Always
```

### Deploy Frontend:

```bash
az container create \
  --resource-group portico-rg \
  --name portico-ui \
  --image aravind1236/portico-ui:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8501 \
  --environment-variables \
    API_URL=http://portico-api.eastus.azurecontainer.io:8000 \
  --dns-name-label portico-ui \
  --restart-policy Always
```

---

## Step 5: Get Your URLs

```bash
az container show --resource-group portico-rg --name portico-api --query ipAddress.fqdn
az container show --resource-group portico-rg --name portico-ui --query ipAddress.fqdn
```

---

## ✅ What Changed

- ✅ requirements.txt → Uses `langchain-google-genai` instead of `langchain-anthropic`
- ✅ app/config.py → Uses `GOOGLE_API_KEY` instead of `ANTHROPIC_API_KEY`
- ✅ app/rag_pipeline.py → Uses `ChatGoogleGenerativeAI` instead of `ChatAnthropic`
- ✅ Model → `gemini-pro` (free, powerful!)

Everything else works the same way!

---

## Gemini Model Options

Free tier includes:
- **gemini-pro** — Best for text (recommended)
- **gemini-pro-vision** — For images + text

Pricing: Free tier with generous limits!

---

Done! 🚀
