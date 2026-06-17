import streamlit as st
import streamlit as st

# ===== LOGIN CODE =====
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if username == "admin" and password == "1234":
        st.session_state.logged_in = True
    else:
        st.error("Invalid Credentials")

if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    st.button("Login", on_click=login)

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
