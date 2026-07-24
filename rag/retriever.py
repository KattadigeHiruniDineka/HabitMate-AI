from rag.vectorstore import create_vector_db


def retrieve_information(query):

    db = create_vector_db()

    retriever = db.as_retriever(
        search_kwargs={"k":2}
    )

    results = retriever.invoke(query)

    context = ""

    for doc in results:
        # Only first 500 characters from each document
        context += doc.page_content[:500]
        context += "\n\n"

    return context