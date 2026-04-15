# PDF RAG Chatbot

A basic Streamlit app that uploads a PDF, extracts text, and splits it into chunks as the first step toward a retrieval-augmented chatbot.

## Features
- Upload PDF
- Extract text with pdfplumber
- Split text into chunks with LangChain text splitter
- Built with Streamlit

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run ragchatbot.py