from backend.models.user import User
import streamlit as st
from backend.auth.authentication import create_user
from backend.models.database import get_db
from sqlalchemy.orm import Session

def show():
    st.title("Sign Up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        db: Session = next(get_db())

        if db.query(User).filter(User.username == username).first():
            st.error("Username already exists!")
        else:
            create_user(db, username, password)
            st.success("User created! Please log in.")

