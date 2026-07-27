import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents():

    documents = []

    folder = "knowledge_base"

    for root, dirs, files in os.walk(folder):

        for file in files:

            if file.endswith(".pdf"):

                path = os.path.join(root, file)

                loader = PyPDFLoader(path)

                documents.extend(loader.load())


    # Split documents into smaller chunk
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    split_docs = text_splitter.split_documents(documents)

    return split_docs