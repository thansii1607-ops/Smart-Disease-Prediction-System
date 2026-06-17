import streamlit as st

st.set_page_config(
    page_title="Smart Disease Prediction System",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #E0F2FE, #F0FDF4);
}

.main-title {
    text-align: center;
    color: #0F766E;
    font-size: 60px;
    font-weight: bold;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #475569;
    font-size: 22px;
    margin-bottom: 30px;
}

.login-title {
    text-align: center;
    color: #1E3A8A;
    font-size: 40px;
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.markdown(
        '<p class="login-title">🔐 Login</p>',
        unsafe_allow_html=True
    )

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):

        if username.strip() == "Thansila" and password.strip() == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

# HOME PAGE
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

    age = st.number_input("Age", min_value=1, max_value=120)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    fever = st.selectbox(
        "Fever",
        ["Yes", "No"]
    )

    cough = st.selectbox(
        "Cough",
        ["Yes", "No"]
    )

    fatigue = st.selectbox(
        "Fatigue",
        ["Yes", "No"]
    )

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
