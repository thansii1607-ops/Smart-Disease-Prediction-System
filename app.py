import streamlit as st

st.set_page_config(page_title="Smart Disease Prediction System")

# Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        # Demo credentials
        if username == "Thansila" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Username or Password")

# HOME + PREDICTION PAGE
else:

    st.title("🩺 Smart Disease Prediction System")

    st.subheader("Disease Prediction")

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

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
