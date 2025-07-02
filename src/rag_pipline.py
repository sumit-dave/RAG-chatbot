import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.retriever import semantic_search
from src.generator import generate_answer

def rag_chatbot(query):
    top_chunks = semantic_search(query)
    response, sources = generate_answer(query, top_chunks)
    return response, sources


