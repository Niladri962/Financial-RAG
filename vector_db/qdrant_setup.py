from langchain_qdrant import QdrantVectorStore


def create_vector_store(chunks, embeddings):

    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        location=":memory:",
        collection_name="financial_docs"
    )

    return vector_store