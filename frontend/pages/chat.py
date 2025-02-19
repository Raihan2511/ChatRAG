import streamlit as st
from backend.services.chat_service import ChatService

def show():
    st.title("Chat with DeepSeek (via Ollama)")

    chat_service = ChatService()

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            response = chat_service.generate_response(user_input)
            st.write("Bot:", response)
        else:
            st.warning("Please enter a message.")
