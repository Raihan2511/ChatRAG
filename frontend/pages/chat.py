import streamlit as st
from sqlalchemy.orm import Session
from backend.models.database import get_db
from backend.models.chat_history import ChatHistory
from backend.services.chat_service import ChatService

st.title("Chat with DeepSeek (Ollama)")

chat_service = ChatService()
db: Session = next(get_db())

user_input = st.text_input("You:", "")

if st.button("Send"):
    response = chat_service.generate_response(user_input)
    st.write("Bot:", response)

    # Save chat in database
    chat_entry = ChatHistory(user_id=1, message=user_input, response=response)  # Assume user_id = 1 for now
    db.add(chat_entry)
    db.commit()
