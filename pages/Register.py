import streamlit as st
import json
import os

USER_FILE = "users.json"

# users.json இல்லையென்றால் create பண்ணும்
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

st.title("📝 Register")

username = st.text_input("Create Username")
password = st.text_input("Create Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):

    if username == "" or password == "":
        st.warning("Please fill all fields")

    elif password != confirm_password:
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
            st.info("Now go to the Login page and login.")
