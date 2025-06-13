# rag_engine.py
# Modul RAG untuk Profiling Pegawai – Early Warning System

from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
import os

# Inisialisasi agent berbasis dokumen PDF pegawai
def initialize_rag_agent(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    rag_tool = create_retriever_tool(
        retriever,
        name="pegawai_profile_tool",
        description="Jawab pertanyaan terkait pegawai dan potensi risiko dari dokumen."
    )

    llm = OpenAI(temperature=0)
    agent = initialize_agent([rag_tool], llm, agent="zero-shot-react-description", verbose=True)
    return agent
