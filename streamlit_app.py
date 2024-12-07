import streamlit as st

st.title("🎈 Input Your OpenAI API Key 🎈")

st.write(
    "This application will help you to create your own world cloud"
)

st.title("🎈 Input Some Text 🎈")

prompt = st.chat_input("Type some text here")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
