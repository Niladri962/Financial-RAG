from retrieval.graph_retriever import graph_search

def hybrid_search(query, retriever):

    docs = retriever.invoke(query)

    graph_results = graph_search()

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    context += str(graph_results)

    return context