# Azure Deployment Checklist — Quick Reference

**Get your system live on Azure in 30 minutes**

---

## Pre-Deployment Checklist (5 minutes)

### Azure Account
- [ ] Azure account created (https://azure.microsoft.com/free)
- [ ] Have your subscription ID ready
- [ ] Have your Azure credentials

### Local Machine
- [ ] Azure CLI installed: `az login` works
- [ ] Docker installed: `docker --version` works
- [ ] Git installed: `git --version` works

### Credentials & Keys
- [ ] ANTHROPIC_API_KEY copied (starts with `sk-ant-`)
- [ ] PINECONE_API_KEY copied (optional but recommended)
- [ ] Docker Hub account created (https://hub.docker.com)

---

## Deployment Checklist (20 minutes)

### Step 1: Prepare Azure (2 min)
```bash
# Login to Azure
az login

# Create resource group (all resources go here)
az group create --name portico-rg --location eastus

# Verify
az group list --output table
```
- [ ] Azure login successful
- [ ] Resource group created
- [ ] Can see group in output

### Step 2: Build & Push Docker Images (8 min)
```bash
# Build API image
docker build -t portico-api:latest .

# Build Frontend image
docker build -f Dockerfile.streamlit -t portico-ui:latest .

# Login to Docker Hub
docker login

# Tag images
docker tag portico-api:latest YOURUSERNAME/portico-api:latest
docker tag portico-ui:latest YOURUSERNAME/portico-ui:latest

# Push to Docker Hub
docker push YOURUSERNAME/portico-api:latest
docker push YOURUSERNAME/portico-ui:latest
```
- [ ] Both images built successfully
- [ ] Logged into Docker Hub
- [ ] Images pushed to Docker Hub
- [ ] Can see images at hub.docker.com/repositories

### Step 3: Deploy API to Azure (5 min)
```bash
az container create \
  --resource-group portico-rg \
  --name portico-api \
  --image YOURUSERNAME/portico-api:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8000 \
  --environment-variables \
    ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx \
    PINECONE_API_KEY=xxxxxxxxxxxxx \
    PINECONE_ENVIRONMENT=us-east1-aws \
    DEBUG=False \
  --dns-name-label portico-api \
  --restart-policy Always
```
- [ ] API deployment command succeeded
- [ ] Got FQDN in output (something.azurecontainer.io)
- [ ] Container status shows "Running"

### Step 4: Deploy Frontend to Azure (5 min)
```bash
az container create \
  --resource-group portico-rg \
  --name portico-ui \
  --image YOURUSERNAME/portico-ui:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8501 \
  --environment-variables \
    API_URL=http://portico-api.eastus.azurecontainer.io:8000 \
  --dns-name-label portico-ui \
  --restart-policy Always
```
- [ ] Frontend deployment command succeeded
- [ ] Got FQDN in output
- [ ] Container status shows "Running"

---

## Post-Deployment Checklist (5 minutes)

### Get Your URLs
```bash
# Get API URL
az container show \
  --resource-group portico-rg \
  --name portico-api \
  --query ipAddress.fqdn

# Get UI URL
az container show \
  --resource-group portico-rg \
  --name portico-ui \
  --query ipAddress.fqdn
```
- [ ] API URL copied
- [ ] UI URL copied

### Test Everything
```bash
# Test API health
curl http://YOUR-API-URL:8000/health

# Test API docs
curl http://YOUR-API-URL:8000/docs

# Test ingest
curl -X POST http://YOUR-API-URL:8000/ingest
```
- [ ] API responds to /health
- [ ] API responds to /docs
- [ ] API responds to /ingest
- [ ] Response shows documents loaded

### Test UI
Open in browser:
```
http://YOUR-UI-URL:8501
```
- [ ] UI loads without errors
- [ ] Can see question input
- [ ] Example questions visible
- [ ] Can ask a question and get answer

---

## What to Share with Stakeholders

After testing:

```
✅ API Endpoint: http://your-api-url:8000
✅ Web Interface: http://your-ui-url:8501
✅ API Documentation: http://your-api-url:8000/docs

Status: LIVE & READY TO USE
```

---

## Cost Verification

Check your costs:

1. Go to Azure Portal: https://portal.azure.com
2. Search for "Cost Management"
3. Expected cost: ~$70/month (~$35 per container)
4. Remember: Free tier gives $200/month credit for 3 months

---

## Monitoring

### Check Container Status
```bash
az container list --resource-group portico-rg --output table
```
Look for: `Running` status

### View Logs
```bash
# API logs
az container logs --resource-group portico-rg --name portico-api --follow

# Frontend logs
az container logs --resource-group portico-rg --name portico-ui --follow
```

### From Azure Portal
1. https://portal.azure.com
2. Search "Container Instances"
3. Click your resource group
4. See all containers with status, CPU usage, memory usage

---

## Troubleshooting Quick Fixes

### Container won't start?
```bash
# Check detailed error
az container logs --resource-group portico-rg --name portico-api

# Common issues:
# - Wrong API key format
# - Typo in Docker image name
# - API key contains special characters (need escaping)
```

### UI can't connect to API?
```bash
# Get actual API URL
az container show --resource-group portico-rg --name portico-api --query ipAddress.fqdn

# Make sure UI's API_URL environment variable matches exactly
# (including http:// and port)
```

### High costs?
```bash
# Stop containers to save money
az container stop --resource-group portico-rg --name portico-api
az container stop --resource-group portico-rg --name portico-ui

# Restart when needed
az container restart --resource-group portico-rg --name portico-api
az container restart --resource-group portico-rg --name portico-ui
```

---

## Quick Commands Reference

```bash
# List all containers
az container list --resource-group portico-rg --output table

# Get API FQDN
az container show --resource-group portico-rg --name portico-api --query ipAddress.fqdn

# View logs
az container logs --resource-group portico-rg --name portico-api

# Restart container
az container restart --resource-group portico-rg --name portico-api

# Stop container
az container stop --resource-group portico-rg --name portico-api

# Delete container
az container delete --resource-group portico-rg --name portico-api

# Delete resource group (deletes everything)
az group delete --name portico-rg
```

---

## Success Criteria

✅ **All of these should be TRUE:**

- [ ] `az login` works
- [ ] `az group list` shows portico-rg
- [ ] Both Docker images pushed to Docker Hub
- [ ] Both Azure containers show "Running"
- [ ] `curl http://API-URL:8000/health` returns {"status":"healthy"...}
- [ ] `http://UI-URL:8501` loads in browser
- [ ] Can ask question in UI and get answer
- [ ] Sources are cited in response

---

## Next Level (Optional)

Once basic deployment works, upgrade to:

- [ ] **Azure SQL Database** — For storing questions/answers
- [ ] **Azure Key Vault** — For managing API keys securely
- [ ] **Azure Cognitive Services** — For advanced NLP features
- [ ] **Application Insights** — For detailed monitoring
- [ ] **Azure DevOps** — For CI/CD pipelines

But for now, focus on getting it deployed and working! 🚀

---

## Still Need Help?

1. **Azure CLI help:** `az container --help`
2. **Check logs:** `az container logs --resource-group portico-rg --name portico-api`
3. **Azure Portal:** https://portal.azure.com (visual monitoring)
4. **Azure Docs:** https://docs.microsoft.com/azure/container-instances/

---

## Timeline

- **Step 1 (Prepare Azure):** 2 min
- **Step 2 (Build Docker):** 8 min (mostly waiting for Docker)
- **Step 3 (Deploy API):** 2 min + 3 min wait for Azure
- **Step 4 (Deploy UI):** 2 min + 3 min wait for Azure
- **Step 5 (Test):** 5 min

**Total: ~25-30 minutes from start to live! ⏱️**

---

**You're ready to go!** 🎉

Start with the checklist above and you'll have everything live on Azure in under 30 minutes.
