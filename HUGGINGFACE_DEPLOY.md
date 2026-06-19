# Hugging Face Spaces Deployment

Deploy the Portico Policy Q&A to Hugging Face Spaces for free, public access.

## What is Hugging Face Spaces?

- Free hosting for ML/AI apps
- Auto-deploys from GitHub
- Public or private options
- Generous free tier (CPU)

## Prerequisites

1. Hugging Face account (free at https://huggingface.co)
2. GitHub repository with project code
3. Hugging Face API token

## Step 1: Create Hugging Face Space

1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. **Space name:** `portico-policy-qa`
4. **License:** Openrail
5. **Space SDK:** Streamlit
6. **Visibility:** Private (for now, can make public later)
7. Click "Create Space"

## Step 2: Connect GitHub Repository

In the Space settings:

1. Go to Space Settings (gear icon)
2. **Repository URL:** Paste your GitHub repo URL
3. Click "Update"

HF will now sync with your GitHub repo.

## Step 3: Configure Environment Variables

In Space settings → Secrets and variables:

Add these environment variables:

```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
PINECONE_API_KEY=xxxxxxxxxxxxx
PINECONE_ENVIRONMENT=us-east1-aws
PINECONE_INDEX_NAME=portico-policies
API_URL=http://localhost:8000
DEBUG=False
```

**Important:** Use HF's secret management, not .env files!

## Step 4: Create app.py for HF

Create `hf_app.py` in your project root (modified for HF):

```python
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

# Use HF environment variables
os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY', '')
os.environ['PINECONE_API_KEY'] = os.getenv('PINECONE_API_KEY', '')

# Import and run the Streamlit app
from ui.app import *

# This tells HF to run the Streamlit app
if __name__ == '__main__':
    pass
```

Or simply rename `ui/app.py` to match HF's expected structure.

## Step 5: Update requirements.txt (HF Specific)

The standard `requirements.txt` should work, but HF prefers this format:

```
langchain==0.1.20
langchain-community==0.0.38
langchain-anthropic==0.1.15
pinecone-client==3.0.2
python-dotenv==1.0.0
streamlit==1.31.0
requests==2.31.0
```

## Step 6: Push to GitHub

```bash
git add .
git commit -m "docs: Add Hugging Face deployment configuration"
git push origin main
```

HF will automatically redeploy!

## Step 7: Verify Deployment

1. Go back to your HF Space
2. Wait 5-10 minutes for build/deployment
3. Check **Logs** tab for build status
4. Once "Running" → Click "View" to see live app

## Step 8: Share Your Space

Once working:

1. Settings → Change visibility to **Public**
2. Share the link: `https://huggingface.co/spaces/yourusername/portico-policy-qa`

## Troubleshooting

### Build Fails
- Check logs: Space settings → Logs tab
- Common issues:
  - Missing dependencies (update requirements.txt)
  - Wrong import paths (check imports)
  - Environment variables (check secrets)

### API Errors
- Verify API keys in secrets
- Check that API endpoint is reachable
- For local testing: use `localhost` properly configured

### App Runs but Shows Blank Page
- Check browser console (F12)
- Check Space logs
- Verify Streamlit is properly configured

## Performance Optimization

HF Spaces are CPU-based and free tier is limited. To optimize:

1. **Cache embeddings** so you don't re-embed on every run
2. **Reduce chunk size** if memory is tight
3. **Use smaller model** if needed
4. **Remove unused dependencies**

Example optimization in `app.py`:

```python
import streamlit as st

@st.cache_resource
def init_rag_pipeline():
    from app.rag_pipeline import PorticoPolicyRAG
    return PorticoPolicyRAG()

rag = init_rag_pipeline()
```

## Upgrading to GPU (Paid)

If you need faster processing:

1. Space settings → Hardware
2. Select GPU option (costs ~$3-7/month)
3. Automatically redeploys with GPU support

## Monitoring & Analytics

HF Spaces provides:
- View count
- Visitor analytics
- Error logs
- Runtime statistics

Found in Space settings → Analytics

## Custom Domain (Optional)

For production deployment:

1. Get custom domain
2. Space settings → Custom domain
3. Point DNS to HF
4. HF provides SSL automatically

## Backup & Version Control

Your Space is tied to GitHub, so:
- All changes are version controlled
- Easy rollback: just revert GitHub commit
- No separate backup needed

## Next Steps

Once deployed:

1. **Share with stakeholders** for feedback
2. **Collect usage metrics** (what questions are people asking?)
3. **Gather feedback** for improvements
4. **Plan Phase 2 & 3** integration

## Example Space

Check these for inspiration:
- https://huggingface.co/spaces/huggingface/awesome-spaces
- https://huggingface.co/spaces?search=streamlit

---

## Deployment Checklist

- [ ] Hugging Face account created
- [ ] Space created on HF
- [ ] GitHub repository connected
- [ ] Environment variables configured
- [ ] requirements.txt updated
- [ ] Code pushed to GitHub
- [ ] Build completes successfully
- [ ] App loads and works
- [ ] Share link ready for stakeholders

**Your app is live!** 🚀

Share the Space URL with Portico leadership to showcase the system.
