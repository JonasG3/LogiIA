import os

from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


load_dotenv()


def criar_banco_vetorial():

    # 1. Carregar o CSV
    loader = CSVLoader(
        "procedimentos_sistema_logistica_ficticio.csv",
        encoding="utf-8"
    )

    documentos = loader.load()

    print(f"Documentos carregados: {len(documentos)}")


    # 2. Criar os embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-2"
    )


    # 3. Criar o banco vetorial
    vectorstore = FAISS.from_documents(
        documentos,
        embeddings
    )


    return vectorstore


def buscar_procedimento(vectorstore, pergunta):

    documentos = vectorstore.similarity_search(
        pergunta,
        k=3
    )

    return documentos