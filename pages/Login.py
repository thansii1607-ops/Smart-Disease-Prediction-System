import streamlit as st
import json
import os

USER_FILE = "users.json"

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if not os.path.exists(USER_FILE):
        st.error("No users found. Please register first.")

    else:
        with open(USER_FILE, "r") as f:
            users = json.load(f)

        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username

            st.success(f"Welcome {username}! 🎉")
            st.info("Go to the Home page from the sidebar.")

        else:
            st.error("Invalid Username or Password")
