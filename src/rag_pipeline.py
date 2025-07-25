# Combining Retrieval and Generation

from src.retriever import semantic_search
from src.generator import generate_answer

def rag_chatbot(query):
    chunks = semantic_search(query)
    answer, sources = generate_answer(query, chunks)
    return answer, sources
