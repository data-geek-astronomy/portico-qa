"""
Portico Policy Q&A Assistant - Streamlit Frontend

Run with: streamlit run ui/app.py
"""

import streamlit as st
import requests
import json
from datetime import datetime
import logging

# Configure page
st.set_page_config(
    page_title="Portico Policy Q&A",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API Configuration
import os
API_BASE_URL = os.getenv("API_URL", "http://localhost:8000")

# Custom CSS
st.markdown("""
<style>
    .stMain {
        padding: 0;
    }
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .answer-box {
        background-color: #f0f4ff;
        padding: 1.5rem;
        border-left: 4px solid #667eea;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .source-box {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border: 1px solid #ddd;
    }
    .question-input {
        border: 2px solid #667eea;
        padding: 0.5rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "question_history" not in st.session_state:
    st.session_state.question_history = []
if "api_connected" not in st.session_state:
    st.session_state.api_connected = False
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None
if "auto_submit" not in st.session_state:
    st.session_state.auto_submit = False


def check_api_health():
    """Check if API is running."""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False


def ask_question(question: str, use_retrieval: bool = True):
    """Submit question to API."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/ask",
            json={"question": question, "use_retrieval": use_retrieval},
            timeout=30
        )
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"status": "error", "message": "Cannot connect to API. Make sure backend is running."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_documents():
    """Get list of ingested documents."""
    try:
        response = requests.get(f"{API_BASE_URL}/documents", timeout=5)
        return response.json()
    except:
        return {"documents": [], "total_chunks": 0}


def get_example_questions():
    """Get example questions."""
    try:
        response = requests.get(f"{API_BASE_URL}/example-questions", timeout=5)
        return response.json().get("example_questions", [])
    except:
        return []


def ingest_documents():
    """Trigger document ingestion."""
    try:
        response = requests.post(f"{API_BASE_URL}/ingest", timeout=30)
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Main UI
st.markdown("""
<div class="header-container">
    <h1>🏢 Portico Policy Q&A Assistant</h1>
    <p>Get instant answers to questions about leases, policies, and procedures</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Settings & Info")

    # Check API status
    st.session_state.api_connected = check_api_health()

    if st.session_state.api_connected:
        st.success("✓ Connected to API")

        # Get document info
        doc_info = get_documents()
        st.subheader("📚 Documents Loaded")
        st.metric("Total Chunks", doc_info.get("total_chunks", 0))

        if doc_info.get("documents"):
            with st.expander("View Documents"):
                for doc in doc_info.get("documents", []):
                    chunks = doc_info.get("chunks_per_document", {}).get(doc, 0)
                    st.write(f"• **{doc}** ({chunks} chunks)")

        # Ingest button
        if st.button("🔄 Re-ingest Documents"):
            with st.spinner("Ingesting documents..."):
                result = ingest_documents()
                if result["status"] == "success":
                    st.success(f"✓ Ingested {result['documents_loaded']} documents")
                    st.rerun()
                else:
                    st.error(f"Error: {result.get('message', 'Unknown error')}")
    else:
        st.error("✗ Cannot connect to API")
        st.warning("Make sure the FastAPI server is running:\n```\npython -m uvicorn app.main:app --reload\n```")

    st.divider()
    st.subheader("ℹ️ About")
    st.write("This RAG system helps Portico site staff get instant answers to policy questions.")
    st.write("Powered by Claude AI and LangChain")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Ask a Question")

    # Question input
    question = st.text_area(
        "What would you like to know about Portico policies?",
        placeholder="e.g., What is the pet policy? How do I handle a maintenance request?",
        height=80,
        value=st.session_state.selected_question if st.session_state.selected_question else ""
    )

    # Options
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        use_retrieval = st.checkbox("Use Policy Documents (RAG)", value=True)
    with col_opt2:
        submit_button = st.button("🔍 Search", use_container_width=True, type="primary")

    # Auto-submit if question was selected from examples
    if st.session_state.selected_question and not st.session_state.auto_submit:
        submit_button = True
        st.session_state.auto_submit = True

    # Process question
    if submit_button and question:
        if not st.session_state.api_connected:
            st.error("API not connected. Please start the backend server.")
        else:
            with st.spinner("Searching policy documents..."):
                try:
                    result = ask_question(question, use_retrieval)
                except Exception as e:
                    st.error(f"Error calling API: {str(e)}")
                    result = {"status": "error", "message": str(e)}

                # Add to history
                st.session_state.question_history.append({
                    "timestamp": datetime.now(),
                    "question": question,
                    "result": result
                })

                # Display result
                if result.get("status") == "success":
                    st.divider()
                    st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                    st.markdown("### Answer")
                    st.write(result["answer"])
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Display sources
                    if result.get("sources") and len(result.get("sources", [])) > 0:
                        st.subheader("📖 Sources")
                        for i, source in enumerate(result["sources"], 1):
                            col_doc, col_section = st.columns([2, 1])
                            with col_doc:
                                st.write(f"**📄 {source.get('document', 'Unknown')}**")
                            with col_section:
                                st.write(f"*{source.get('section', 'General')}*")
                    else:
                        st.info("No specific policy sections found. Answer based on general knowledge.")

                else:
                    st.error(f"Error: {result.get('message', 'Unknown error')}")

                # Clear selected question after processing
                st.session_state.selected_question = None

with col2:
    st.subheader("💡 Example Questions")
    examples = get_example_questions()

    if examples:
        for i, example in enumerate(examples, 1):
            if st.button(f"📌 {example}", key=f"example_{i}", use_container_width=True):
                st.session_state.selected_question = example
                st.session_state.auto_submit = False
                st.rerun()
    else:
        st.write("No examples available")

# History section
if st.session_state.question_history:
    st.divider()
    st.subheader("📋 Question History")

    with st.expander(f"View {len(st.session_state.question_history)} previous questions"):
        for i, item in enumerate(reversed(st.session_state.question_history), 1):
            st.write(f"**Q{len(st.session_state.question_history) - i + 1}:** {item['question']}")
            if item['result']['status'] == 'success':
                st.write(f"**A:** {item['result']['answer'][:200]}...")
            else:
                st.write(f"**Error:** {item['result'].get('message')}")
            st.divider()

    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.question_history = []
        st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #999; font-size: 0.9em;'>
    <p>Portico Policy Q&A Assistant v1.0</p>
    <p>For questions not covered in this system, contact your property manager or corporate office.</p>
</div>
""", unsafe_allow_html=True)
