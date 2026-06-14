import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from ingestion.pdf_loader import load_pdf
from ingestion.chunking import chunk_documents
from embeddings.embedding_model import get_embedding_model
from vector_db.qdrant_setup import create_vector_store
from retrieval.vector_retriever import get_vector_retriever
from retrieval.hybrid_retriever import hybrid_search
from chains.rag_chain import chain


# Page config
st.set_page_config(
    page_title="Financial Research Copilot",
    page_icon="📈",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📈 Financial-RAG")
    st.markdown("---")

    st.success("Neo4j Connected")
    st.success("Qdrant Ready")
    st.success("all-MiniLM-L6-v2")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload Financial PDF",
        type=["pdf"]
    )

# Main title
st.title("🤖 Financial Research Copilot")

st.caption(
    "GraphRAG + Neo4j + Qdrant + all-MiniLM-L6-v2 + Llama3"
)

question = st.chat_input(
    "Ask a financial question..."
)

if question:

    with st.spinner("Analyzing documents..."):

        documents = load_pdf(
            "data/reports/apple.pdf"
        )

        chunks = chunk_documents(
            documents
        )

        embeddings = get_embedding_model()

        vector_store = create_vector_store(
            chunks,
            embeddings
        )

        retriever = get_vector_retriever(
            vector_store
        )

        context = hybrid_search(
            question,
            retriever
        )

        response = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        st.write(response)

        with st.expander("Retrieved Context"):
            st.write(context)