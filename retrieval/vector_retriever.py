def get_vector_retriever(vector_store):

    retriever = vector_store.as_retriever(
        search_kwargs={"k":5}
    )

    return retriever