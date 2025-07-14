# build_faiss_index.py
import os
import json
import faiss
from sentence_transformers import SentenceTransformer

# Example chunks for demo — normally you'd split a big PDF into 100–300 word chunks.
chunks = [
    "This is example chunk 1.",
    "This is example chunk 2.",
    "This is example chunk 3."
]

# Load sentence-transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(chunks, convert_to_numpy=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Make output folders if needed
os.makedirs("chunks", exist_ok=True)
os.makedirs("vectordb", exist_ok=True)

# Save chunks
with open("chunks/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f)

# Save index + chunk file copy
faiss.write_index(index, "vectordb/faiss_index.bin")
with open("vectordb/faiss_index_chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f)

print("✅ FAISS index created successfully.")
