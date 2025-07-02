import os
import faiss
import json
from sentence_transformers import SentenceTransformer

# Dynamically find absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "vectordb", "faiss_index.bin")
CHUNKS_PATH = os.path.join(BASE_DIR, "vectordb", "faiss_index_chunks.json")

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query, top_k=4):
    if not os.path.exists(INDEX_PATH):
        raise RuntimeError(f"❌ FAISS index not found at: {INDEX_PATH}")

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)

    return [chunks[i] for i in indices[0]]
