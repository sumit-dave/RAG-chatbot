from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import os

def build_faiss_index(chunk_path="../chunks/chunks.json", db_path="../vectordb/faiss_index"):
    with open(chunk_path, "r") as f:
        chunks = json.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, f"{db_path}.bin")

    with open(f"{db_path}_chunks.json", "w") as f:
        json.dump(chunks, f)

    return index, chunks

def semantic_search(query, top_k=4):
    index = faiss.read_index("../vectordb/faiss_index.bin")
    with open("../vectordb/faiss_index_chunks.json") as f:
        chunks = json.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vec = model.encode([query])

    D, I = index.search(query_vec, top_k)
    return [chunks[i] for i in I[0]]
