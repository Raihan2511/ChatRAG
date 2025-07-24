import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# MySQL Database Configuration
DATABASE_URL = st.secrets["DATABASE_URL"]  # Use secrets for sensitive data
