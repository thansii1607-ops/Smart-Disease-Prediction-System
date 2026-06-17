import streamlit as st
import json

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    with open("users.json", "r") as f:
        users = json.load(f)

    if username in users and users[username] == password:
        st.session_state["logged_in"] = True
        st.session_state["user"] = username
        st.success("Login Successful ✅")
    else:
        st.error("Invalid Username or Password")
