# Azure Deployment Guide — Portico Policy Q&A RAG

**Hosting on Azure Container Instances (ACI) — Easiest & Cheapest**

✅ **Setup time:** 15 minutes  
✅ **Cost:** ~$30-50/month for MVP  
✅ **No servers to manage** — Fully managed containers  

---

## Prerequisites

1. **Azure Account** (free tier available: $200 credits)
2. **Azure CLI** installed on your machine
3. **Docker Hub account** (free)
4. **Your API keys:**
   - ANTHROPIC_API_KEY
   - PINECONE_API_KEY (optional)

---

## Step 1: Prepare Azure

### 1.1 Install Azure CLI

```bash
# macOS
brew install azure-cli

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Windows
# Download from: https://aka.ms/installazurecliwindows
```

### 1.2 Login to Azure

```bash
az login
# Opens browser, login with your credentials
```

### 1.3 Create Resource Group

```bash
# Create a resource group (container for all resources)
az group create \
  --name portico-rg \
  --location eastus

# Verify
az group list --output table
```

---

## Step 2: Push Docker Images to Docker Hub

### 2.1 Build Local Docker Images

```bash
# From project root
docker build -t portico-api:latest .
docker build -f Dockerfile.streamlit -t portico-ui:latest .
```

### 2.2 Login to Docker Hub

```bash
docker login
# Enter your Docker Hub username and password
```

### 2.3 Tag Images for Docker Hub

```bash
docker tag portico-api:latest yourusername/portico-api:latest
docker tag portico-ui:latest yourusername/portico-ui:latest
```

### 2.4 Push to Docker Hub

```bash
docker push yourusername/portico-api:latest
docker push yourusername/portico-ui:latest
```

**Verify:** Go to https://hub.docker.com/repositories and confirm images are there.

---

## Step 3: Deploy API Container to Azure

### 3.1 Create Container for API

```bash
az container create \
  --resource-group portico-rg \
  --name portico-api \
  --image yourusername/portico-api:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8000 \
  --environment-variables \
    ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx \
    PINECONE_API_KEY=your-key-here \
    PINECONE_ENVIRONMENT=us-east1-aws \
    DEBUG=False \
  --dns-name-label portico-api \
  --restart-policy Always
```

**Note:** Replace API key values with your actual keys

### 3.2 Get API URL

```bash
az container show \
  --resource-group portico-rg \
  --name portico-api \
  --query ipAddress.fqdn
```

**Output will be something like:**
```
portico-api.eastus.azurecontainer.io
```

✅ **Your API is now live at:** `http://portico-api.eastus.azurecontainer.io:8000`

### 3.3 Test API

```bash
# Health check
curl http://portico-api.eastus.azurecontainer.io:8000/health

# Should return:
# {"status":"healthy","documents_ingested":0,"pipeline_ready":true}
```

---

## Step 4: Deploy Streamlit Frontend to Azure

### 4.1 Create Frontend Container

```bash
az container create \
  --resource-group portico-rg \
  --name portico-ui \
  --image yourusername/portico-ui:latest \
  --cpu 1 \
  --memory 1.5 \
  --ports 8501 \
  --environment-variables \
    API_URL=http://portico-api.eastus.azurecontainer.io:8000 \
  --dns-name-label portico-ui \
  --restart-policy Always
```

### 4.2 Get UI URL

```bash
az container show \
  --resource-group portico-rg \
  --name portico-ui \
  --query ipAddress.fqdn
```

**Output will be something like:**
```
portico-ui.eastus.azurecontainer.io
```

✅ **Your UI is now live at:** `http://portico-ui.eastus.azurecontainer.io:8501`

---

## Step 5: Ingest Documents

```bash
# Call the ingest endpoint
curl -X POST http://portico-api.eastus.azurecontainer.io:8000/ingest

# Expected response:
# {"status":"success","documents_loaded":9,"chunks_created":145}
```

---

## ✅ You're Done!

Share these URLs with stakeholders:

- **Web UI:** http://portico-ui.eastus.azurecontainer.io:8501
- **API Docs:** http://portico-api.eastus.azurecontainer.io:8000/docs
- **Health Check:** http://portico-api.eastus.azurecontainer.io:8000/health

---

## Management Commands

### View Container Status

```bash
# List all containers
az container list --resource-group portico-rg --output table

# View logs
az container logs \
  --resource-group portico-rg \
  --name portico-api

# View detailed info
az container show \
  --resource-group portico-rg \
  --name portico-api
```

### Update a Container

```bash
# To update API with new environment variables:
az container delete \
  --resource-group portico-rg \
  --name portico-api

# Then recreate with new command
az container create \
  --resource-group portico-rg \
  --name portico-api \
  # ... (same as before with updated values)
```

### Restart Containers

```bash
az container restart \
  --resource-group portico-rg \
  --name portico-api

az container restart \
  --resource-group portico-rg \
  --name portico-ui
```

### Stop Containers (to save costs)

```bash
az container stop \
  --resource-group portico-rg \
  --name portico-api

az container stop \
  --resource-group portico-rg \
  --name portico-ui
```

### Delete Containers

```bash
az container delete \
  --resource-group portico-rg \
  --name portico-api

az container delete \
  --resource-group portico-rg \
  --name portico-ui
```

---

## Cost Estimation

**Azure Container Instances Pricing:**

| Resource | CPU | Memory | Cost/Hour | Cost/Month |
|----------|-----|--------|-----------|-----------|
| API | 1 | 1.5 GB | $0.0475 | ~$35 |
| Frontend | 1 | 1.5 GB | $0.0475 | ~$35 |
| **Total** | 2 | 3 GB | $0.095 | **~$70** |

**Note:** Free tier provides $200/month credit, so this is essentially **free for first 3 months!**

---

## Monitoring & Logs

### View Real-time Logs

```bash
# Follow logs (like tail -f)
az container logs \
  --resource-group portico-rg \
  --name portico-api \
  --follow
```

### Check Container Health

```bash
# Get container status
az container show \
  --resource-group portico-rg \
  --name portico-api \
  --query "containers[0].instanceView.currentState"

# Output should show: "Running"
```

### Monitor from Azure Portal

1. Go to https://portal.azure.com
2. Search for "Container Instances"
3. Click your resource group "portico-rg"
4. See all running containers with status, IP, logs

---

## Troubleshooting

### Container Won't Start

```bash
# Check logs
az container logs --resource-group portico-rg --name portico-api

# Common issues:
# - Wrong API key format
# - Docker image not found (check Docker Hub)
# - Port already in use (change port in az container create)
```

### UI Can't Connect to API

**Ensure API_URL environment variable is correct:**

```bash
# Get actual API FQDN
az container show \
  --resource-group portico-rg \
  --name portico-api \
  --query ipAddress.fqdn

# Use this exact URL in UI container's API_URL environment variable
```

### High Memory Usage

If containers are slow:

```bash
# Increase memory in container creation
--memory 2.5  # Instead of 1.5
```

---

## Advanced: Azure Networking (Optional)

For production, use Azure Container Group (single network):

```bash
# Create container group
az container create \
  --resource-group portico-rg \
  --name portico-app \
  --image yourusername/portico-api:latest \
  --ports 8000 8501 \
  --environment-variables \
    ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx \
    API_URL=localhost:8000 \
  --dns-name-label portico-app \
  --restart-policy Always
```

This allows containers to communicate via `localhost` instead of FQDN.

---

## CI/CD with GitHub Actions (Optional)

Automatically redeploy when you push to GitHub:

Create `.github/workflows/deploy-azure.yml`:

```yaml
name: Deploy to Azure

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build and push Docker images
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/portico-api:latest .
          docker push ${{ secrets.DOCKER_USERNAME }}/portico-api:latest
      
      - name: Deploy to Azure
        uses: azure/CLI@v1
        with:
          azcliversion: 2.30.0
          inlineScript: |
            az container delete --resource-group portico-rg --name portico-api --yes
            az container create --resource-group portico-rg ...
```

---

## Scaling to Production

As you grow, upgrade to:

1. **Azure App Service** — Auto-scaling, better performance
2. **Azure Kubernetes Service (AKS)** — Container orchestration
3. **Azure SQL Database** — Managed database
4. **Azure Cosmos DB** — NoSQL at scale

But for MVP, **ACI is perfect!**

---

## Quick Deployment Script

Save as `deploy-azure.sh`:

```bash
#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Portico Azure Deployment${NC}"
echo "=========================="

# Get user inputs
read -p "Enter Azure Resource Group: " RG
read -p "Enter Docker Hub username: " DOCKER_USER
read -sp "Enter ANTHROPIC API Key: " API_KEY
echo ""

echo -e "${BLUE}Building Docker images...${NC}"
docker build -t portico-api:latest .
docker build -f Dockerfile.streamlit -t portico-ui:latest .

echo -e "${BLUE}Pushing to Docker Hub...${NC}"
docker tag portico-api:latest $DOCKER_USER/portico-api:latest
docker tag portico-ui:latest $DOCKER_USER/portico-ui:latest
docker push $DOCKER_USER/portico-api:latest
docker push $DOCKER_USER/portico-ui:latest

echo -e "${BLUE}Deploying API container...${NC}"
az container create \
  --resource-group $RG \
  --name portico-api \
  --image $DOCKER_USER/portico-api:latest \
  --cpu 1 --memory 1.5 --ports 8000 \
  --environment-variables ANTHROPIC_API_KEY=$API_KEY \
  --dns-name-label portico-api --restart-policy Always

echo -e "${BLUE}Deploying UI container...${NC}"
az container create \
  --resource-group $RG \
  --name portico-ui \
  --image $DOCKER_USER/portico-ui:latest \
  --cpu 1 --memory 1.5 --ports 8501 \
  --environment-variables API_URL=http://portico-api.eastus.azurecontainer.io:8000 \
  --dns-name-label portico-ui --restart-policy Always

echo -e "${GREEN}✅ Deployment complete!${NC}"
echo ""
echo "API: http://portico-api.eastus.azurecontainer.io:8000"
echo "UI: http://portico-ui.eastus.azurecontainer.io:8501"
```

Run with:
```bash
chmod +x deploy-azure.sh
./deploy-azure.sh
```

---

## Next Steps

1. ✅ Get your Azure credentials ready
2. ✅ Install Azure CLI
3. ✅ Run the deployment commands above
4. ✅ Test the URLs
5. ✅ Share with stakeholders
6. ✅ Monitor from Azure Portal

---

## Support

**Need help?** Check:
- Azure Container Instances docs: https://docs.microsoft.com/azure/container-instances/
- Azure CLI docs: https://docs.microsoft.com/cli/azure/
- Container logs in Azure Portal

You got this! 🚀
