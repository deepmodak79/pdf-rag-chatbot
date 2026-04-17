import pdfplumber
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(
        "Upload a pdf file and start asking questions",
        type="pdf"
    )

if file is not None:
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(text)
    st.write(chunks)

    #generating embedidings
    embeddings= OpenAIEmbeddings(
        model="text-embedding-3-small",
        open_api_key ="your key"
    )

    #store embeddings in vector db
    vector_store = FAISS.from_texts(chunks,embeddings)