import streamlit as st
from backend.models.database import get_db
from backend.models.chat_history import ChatHistory
from sqlalchemy.orm import Session

def show():
    st.title("Chat History")

    db: Session = next(get_db())
    history = db.query(ChatHistory).all()

    for chat in history:
        st.write(f"You: {chat.message}")
        st.write(f"Bot: {chat.response}")
