# Transformation of data
import os
import json
import faiss
import fitz  # PyMuPDF
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# Function to read and chunk PDF text
def load_pdf_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()

    text = re.sub(r'\n+', '\n', full_text)
    refined_text = re.sub(r'\s+', ' ', text).strip()

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", ".", "!", "?", ",", " ", ""]
    )
    chunks = text_splitter.split_text(refined_text)
    return chunks

# Load and chunk your PDF
path = "Data/AI Training Document.pdf"
chunks = load_pdf_chunks(path)

# Load sentence-transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(chunks, convert_to_numpy=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Make output folders if needed
os.makedirs("vectordb", exist_ok=True)

# Save index + chunk file copy
faiss.write_index(index, "vectordb/faiss_index.bin")
with open("vectordb/faiss_index_chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f)

print("✅ FAISS index created successfully.")
