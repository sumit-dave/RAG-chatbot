from src.retriever import semantic_search
from src.generator import generate_answer

def rag_chatbot(query):
    top_chunks = semantic_search(query)
    answer = generate_answer(query, top_chunks)
    return answer, top_chunks
