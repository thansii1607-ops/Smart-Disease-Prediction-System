import streamlit as st

st.set_page_config(
    page_title="Smart Disease Prediction System",
    page_icon="🩺",
    layout="centered"
)

# Professional CSS
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #0F766E;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #475569;
    font-size: 18px;
    margin-bottom: 25px;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.markdown(
        '<p class="main-title">🩺 Smart Disease Prediction System</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">AI-Powered Disease Prediction and Health Analysis</p>',
        unsafe_allow_html=True
    )

    st.subheader("🔐 Login")

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):

        # Change username/password if needed
        if username == "Thansila" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

# PREDICTION PAGE
else:

    st.markdown(
        '<p class="main-title">🩺 Smart Disease Prediction System</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">AI-Powered Disease Prediction and Health Analysis</p>',
        unsafe_allow_html=True
    )

    st.success("✅ Login Successful")

    st.subheader("🩺 Disease Prediction Form")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    fever = st.selectbox("Fever", ["Yes", "No"])
    cough = st.selectbox("Cough", ["Yes", "No"])
    fatigue = st.selectbox("Fatigue", ["Yes", "No"])

    if st.button("🔍 Predict Disease"):

        if fever == "Yes" and cough == "Yes":
            disease = "Flu"

        elif fever == "Yes" and fatigue == "Yes":
            disease = "Viral Infection"

        elif cough == "Yes":
            disease = "Common Cold"

        else:
            disease = "Healthy"

        st.success(f"🩺 Predicted Disease: {disease}")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
