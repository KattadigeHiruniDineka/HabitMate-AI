import os

from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from rag.loader import load_documents


CHROMA_PATH = "chroma_db"


def create_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    # ChromaDB already exists
    if os.path.exists(CHROMA_PATH):

        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings
        )

        return db



    # First time create database
    documents = load_documents()


    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory=CHROMA_PATH
    )


    return db