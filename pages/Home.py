import streamlit as st

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

st.title("🩺 Disease Prediction System")

age = st.number_input("Age", 1, 120)
gender = st.selectbox("Gender", ["Male", "Female"])

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
    st.session_state["logged_in"] = False
    st.session_state["user"] = ""
    st.rerun()
