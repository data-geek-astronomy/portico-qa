#!/bin/bash

# Portico Policy Q&A RAG System - Setup Script

echo "🏢 Portico Policy Q&A System Setup"
echo "===================================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Create virtual environment
echo ""
echo "📦 Setting up virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🚀 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if not exists
echo ""
echo "⚙️  Configuring environment..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✓ Created .env file from .env.example"
    echo "  Please edit .env with your API keys"
else
    echo "✓ .env file already exists"
fi

# Create necessary directories
echo ""
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p data/policies

# Summary
echo ""
echo "✅ Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your API keys:"
echo "   - ANTHROPIC_API_KEY"
echo "   - PINECONE_API_KEY"
echo ""
echo "2. Start the backend API:"
echo "   python -m uvicorn app.main:app --reload"
echo ""
echo "3. In another terminal, start the frontend:"
echo "   streamlit run ui/app.py"
echo ""
echo "4. Open http://localhost:8501 in your browser"
echo ""
