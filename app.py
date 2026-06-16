import streamlit as st

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
