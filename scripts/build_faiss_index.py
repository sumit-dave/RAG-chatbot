import os
import faiss
import json
from sentence_transformers import SentenceTransformer

# Load chunks
with open("chunks/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks, convert_to_numpy=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index and chunks
os.makedirs("vectordb", exist_ok=True)
faiss.write_index(index, "vectordb/faiss_index.bin")
with open("vectordb/faiss_index_chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f)

print("✅ FAISS index rebuilt successfully.")
