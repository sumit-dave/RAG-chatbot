import streamlit as st
from src.rag_pipline import rag_chatbot
import time

st.set_page_config(page_title="RAG Chatbot")

st.title("💬 RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message("user"):
        st.markdown(msg["user"])
    with st.chat_message("assistant"):
        st.markdown(msg["bot"])

# Chat input box
user_input = st.chat_input("Ask your question")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        msg = st.empty()
        response, sources = rag_chatbot(user_input)

        # Simple streaming
        partial = ""
        for word in response.split():
            partial += word + " "
            msg.markdown(partial)
            time.sleep(0.02)

        with st.expander("🔍 Sources"):
            for i, s in enumerate(sources):
                st.markdown(f"**Chunk {i+1}:** {s}")

    st.session_state.messages.append({"user": user_input, "bot": response})

    #streamlit run app.py 
    #it's done
