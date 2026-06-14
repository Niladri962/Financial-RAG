from ingestion.pdf_loader import load_pdf
from ingestion.chunking import chunk_documents

from embeddings.embedding_model import get_embedding_model
from vector_db.qdrant_setup import create_vector_store

from retrieval.vector_retriever import get_vector_retriever
from retrieval.hybrid_retriever import hybrid_search

from chains.rag_chain import chain

# Load PDF
documents = load_pdf("data/reports/apple.pdf")

# Chunking
chunks = chunk_documents(documents)

# Embedding model
embeddings = get_embedding_model()

# Create vector store
vector_store = create_vector_store(
    chunks,
    embeddings
)

# Retriever
retriever = get_vector_retriever(vector_store)

query = "What was Apple's revenue?"

# Hybrid search
context = hybrid_search(
    query,
    retriever
)

response = chain.invoke(
    {
        "context": context,
        "question": query
    }
)

print(response)