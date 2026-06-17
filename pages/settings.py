import streamlit as st

st.title("⚙️ Settings")

target=st.slider(
"Target kcal",
1000,
4000,
2000
)

if st.button("Save"):

    st.session_state.target=target

    st.success("Updated")

if st.button("← Back"):

    st.switch_page("app.py")