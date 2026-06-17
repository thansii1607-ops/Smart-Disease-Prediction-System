import streamlit as st

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

st.title("🏠 Home Page")
st.write(f"Welcome {st.session_state['user']}")

st.header("🩺 Smart Disease Prediction System")

age = st.number_input("Age", 1, 120)

if st.button("Predict"):
    st.success("Prediction Result Here")
