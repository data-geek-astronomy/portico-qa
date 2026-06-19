#!/usr/bin/env python3
"""
Script to ingest documents into the RAG system.

Usage:
    python scripts/ingest_documents.py
"""

import os
import sys
import logging

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag_pipeline import PorticoPolicyRAG
from app.config import DATA_DIR

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main ingestion function."""
    logger.info("Starting document ingestion...")

    # Check if data directory exists
    if not os.path.exists(DATA_DIR):
        logger.error(f"Data directory not found: {DATA_DIR}")
        return False

    # Initialize RAG pipeline
    try:
        rag = PorticoPolicyRAG()
    except Exception as e:
        logger.error(f"Failed to initialize RAG pipeline: {e}")
        return False

    # Load documents
    documents = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(DATA_DIR, filename)
            logger.info(f"Loading: {filename}")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append((filename, content))
            except Exception as e:
                logger.warning(f"Failed to load {filename}: {e}")
                continue

    if not documents:
        logger.error("No documents found to ingest")
        return False

    logger.info(f"Loaded {len(documents)} documents")

    # Ingest documents
    try:
        result = rag.ingest_documents(documents)
        logger.info(f"Ingestion result: {result}")

        if result["status"] == "success":
            logger.info(f"✓ Successfully ingested {len(documents)} documents")
            logger.info(f"✓ Created {result['chunks_created']} chunks")

            # Print document info
            doc_info = rag.get_ingested_documents()
            logger.info("\nDocument Summary:")
            for doc, chunk_count in doc_info['chunks_per_document'].items():
                logger.info(f"  - {doc}: {chunk_count} chunks")

            return True
        else:
            logger.error(f"Ingestion failed: {result}")
            return False

    except Exception as e:
        logger.error(f"Error during ingestion: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
