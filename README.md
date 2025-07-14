Demo Video: https://drive.google.com/file/d/1fok2YForUe-rAQYnVL0jpOurSNvYaR-c/view?usp=drive_link

Git Hub link: https://github.com/sumit-dave/RAG-chatbot.git

## RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot that answers questions using a document and a local LLM (Mistral) via Ollama.

## How it works

1. **Chunks:** The text is split into parts.
2. **Embeddings:** Each chunk is turned into a vector.
3. **Retriever:** When you ask a question, it finds the most similar chunks.
4. **Generator:** It builds a prompt with those chunks + your question.
5. **LLM:** The local Mistral model answers using only the context.
6. **Streamlit:** The answer is shown with simple word-by-word streaming.

## How to run

```bash
# Clone repo
git clone <https://github.com/sumit-dave/RAG-chatbot.git>
cd rag-chatbot

# Install dependencies
pip install -r requirements.txt

# Build index (only once)
python build_faiss_index.py

# Start Ollama server
ollama run mistral

# Run chatbot
streamlit run app.py
