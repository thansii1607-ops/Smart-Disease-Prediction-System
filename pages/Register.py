import streamlit as st
import json
import os

USER_FILE = "users.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

st.title("📝 Register")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if password != confirm:
        st.error("Passwords do not match")
    else:
        with open(USER_FILE, "r") as f:
            users = json.load(f)

        if username in users:
            st.error("Username already exists")
        else:
            users[username] = password

            with open(USER_FILE, "w") as f:
                json.dump(users, f)

            st.success("Registration Successful ✅")
