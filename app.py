import streamlit as st
import json
import os

USER_FILE = "users.json"

# users file create
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

st.title("🔐 Smart Disease Prediction System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Login", "Register"]
)

if menu == "Register":
    st.subheader("Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        users = load_users()

        if new_user in users:
            st.error("Username already exists")
        else:
            users[new_user] = new_pass
            save_users(users)
            st.success("Registration Successful")

elif menu == "Login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()

        if username in users and users[username] == password:
            st.success(f"Welcome {username} 🎉")

            st.header("🩺 Disease Prediction System")
            st.write("Login successful.")
        else:
            st.error("Invalid Username or Password")

# ===== MAIN WEBSITE =====
else:
    st.title("🩺 Smart Disease Prediction System")

    age = st.number_input("Age", 1, 120)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    fever = st.selectbox("Fever", ["Yes", "No"])

    if st.button("Predict"):
        st.success("Prediction Result Here")

st.set_page_config(page_title="Smart Disease Prediction System")

st.title("🩺 Smart Disease Prediction System")

st.write("Enter your symptoms to get a disease prediction.")

age = st.number_input("Age", min_value=1, max_value=120)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

fever = st.selectbox("Fever", ["Yes", "No"])
cough = st.selectbox("Cough", ["Yes", "No"])
fatigue = st.selectbox("Fatigue", ["Yes", "No"])

if st.button("Predict Disease"):

    if fever == "Yes" and cough == "Yes":
        disease = "Flu"
    elif fever == "Yes" and fatigue == "Yes":
        disease = "Viral Infection"
    elif cough == "Yes":
        disease = "Common Cold"
    else:
        disease = "Healthy"

    st.success(f"Predicted Disease: {disease}")
