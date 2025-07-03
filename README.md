💬 RAG Chatbot with Local LLM (Mistral via Ollama)

A Retrieval-Augmented Generation chatbot designed to answer questions based on the content of a provided AI training document. This chatbot integrates semantic search with a local language model to generate grounded, real-time responses within a Streamlit interface.

📦 Features

✅ Parses and chunks custom documents into semantically meaningful sections

✅ Generates embeddings using all-MiniLM-L6-v2

✅ Vector similarity search powered by FAISS

✅ Local LLM inference using Mistral 7B via Ollama

✅ Fully offline and privacy-friendly (no API key required)

✅ Token-wise streaming responses in Streamlit

✅ Expandable source chunk display for traceability

🧠 RAG Pipeline Overview

1. Chunking

Tool: RecursiveCharacterTextSplitter

Source: AI training task PDF

Config: chunk_size=500, chunk_overlap=100

Output: chunks/chunks.json

2. Embedding

Model: sentence-transformers/all-MiniLM-L6-v2

Output Dim: 384

Stored using FAISS IndexFlatL2 similarity search

Files: vectordb/faiss_index.bin, faiss_index_chunks.json

3. Prompt Format

Answer based only on this context:

[chunk_1]
[chunk_2]
...

Q: [user query]
A:

4. Generation

Backend: Ollama running mistral

Interaction: HTTP POST via local server

Model runs locally, supports GPU/CPU

Output streamed via Streamlit st.empty()

🚀 Quickstart

Step 1: Setup

git clone https://github.com/YOUR_USERNAME/rag-chatbot
cd rag-chatbot
python -m venv .venv
source .venv/Scripts/activate  # For Git Bash / Windows
pip install -r requirements.txt

Step 2: Build Vector Index

python scripts/build_faiss_index.py

Step 3: Start Ollama (First Time)

ollama run mistral

Step 4: Run Streamlit App

streamlit run app.py

📸 Demo Video

🎥 Watch the full demo (YouTube/Drive)

🧪 Includes:

Overview of setup

Live queries with streaming

Working + failure query examples

UI walkthrough and code folders

❓ Sample Queries

Query

Response Type

What are the deliverables for this project?

✅ Success

Which LLM is being used in the chatbot?

✅ Success

Who is the CEO of OpenAI?

⚠️ Graceful fail

Explain supervised learning.

⚠️ Graceful fail

What is the role of the retriever?

✅ Success

📁 Folder Structure

├── app.py                  # Streamlit interface
├── requirements.txt        # All dependencies
├── README.md
├── scripts/
│   └── build_faiss_index.py
├── chunks/                 # Text chunks JSON
├── vectordb/               # FAISS index & metadata
├── src/
│   ├── generator.py
│   ├── retriever.py
│   └── rag_pipline.py

⚠️ Known Limitations

RAG answers only based on pre-loaded content

No external knowledge or internet retrieval

Ollama model load can be slow initially

Streamed output is simulated, not token-authentic


