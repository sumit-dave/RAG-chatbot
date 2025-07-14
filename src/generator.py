# src/generator.py
import requests

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"Answer ONLY using this context:\n\n{context}\n\nQ: {query}\nA:"

    # Call local LLM server (Ollama)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    output = response.json()["response"]
    return output, context_chunks
