import streamlit as st
from pages import login, signup, chat, history

# Streamlit session state for user authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Sign Up", "Chat", "Chat History"])

# Render pages based on selection
if page == "Login":
    login.show()
elif page == "Sign Up":
    signup.show()
elif page == "Chat":
    if st.session_state["authenticated"]:
        chat.show()
    else:
        st.warning("Please log in first!")
elif page == "Chat History":
    if st.session_state["authenticated"]:
        history.show()
    else:
        st.warning("Please log in first!")
