import streamlit as st

st.set_page_config(
    page_title="Smart Disease Prediction System",
    page_icon="🩺",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp {
    background-color: #0A192F;
}

/* Main Heading */
.main-title {
    text-align: center;
    color: white;
    font-size: 60px;
    font-weight: 800;
    margin-bottom: 10px;
}

/* Sub Heading */
.sub-title {
    text-align: center;
    color: #D1D5DB;
    font-size: 20px;
    margin-bottom: 30px;
}

/* Labels */
label {
    color: white !important;
    font-weight: bold !important;
}

/* Input Boxes */
.stTextInput input,
.stNumberInput input {
    background-color: #DDF4FF !important;
    color: black !important;
    border-radius: 10px !important;
}

/* Select Boxes */
.stSelectbox div[data-baseweb="select"] {
    background-color: #DDF4FF !important;
    color: black !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 50px;
    background-color: #38BDF8;
    color: white;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #112240;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Session ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown(
        '<p class="main-title">🩺 Smart Disease Prediction System</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">AI-Powered Disease Prediction and Health Analysis</p>',
        unsafe_allow_html=True
    )

    st.sidebar.title("🔐 Login Info")
    st.sidebar.write("Username: Thansila")
    st.sidebar.write("Password: 1234")

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):

        if username.strip() == "Thansila" and password.strip() == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")

# ---------------- HOME / PREDICTION PAGE ----------------
else:

    st.markdown(
        '<p class="main-title">🩺 Smart Disease Prediction System</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">Disease Prediction Dashboard</p>',
        unsafe_allow_html=True
    )

    st.sidebar.success("✅ Logged In")
    st.sidebar.write("Welcome, Thansila")

    st.success("🎉 Login Successful")

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
