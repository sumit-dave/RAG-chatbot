# app.py
import streamlit as st
import time
from src.rag_pipeline import rag_chatbot


st.set_page_config(page_title="💬 RAG Chatbot")
st.title("💬 RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for msg in st.session_state.messages:
    with st.chat_message("user"):
        st.markdown(msg["user"])
    with st.chat_message("assistant"):
        st.markdown(msg["bot"])

# Chat input
user_input = st.chat_input("Ask your question...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        answer, sources = rag_chatbot(user_input)

        # Fake word-by-word streaming
        partial = ""
        for word in answer.split():
            partial += word + " "
            placeholder.markdown(partial)
            time.sleep(0.03)

        # Show source chunks
        with st.expander("🔍 Sources"):
            for i, s in enumerate(sources):
                st.markdown(f"**Chunk {i+1}:** {s}")

    st.session_state.messages.append({"user": user_input, "bot": answer})
