import requests

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"Answer based only on this:\n\n{context}\n\nQ: {query}\nA:"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    
    output = response.json()["response"]
    return output, context_chunks

## Builds prompt from retrieved chunks

## Sends it to Ollama (local LLM at localhost:11434)

## Gets model-generated answer 