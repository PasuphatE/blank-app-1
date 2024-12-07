import streamlit as st

st.title("🎈 Input Your OpenAI API Key 🎈")

st.write(
    "This application will help you to create your own world cloud"
)
with st.sidebar:
    st.title("🎈 Input Some Text 🎈")
    messages = st.container(height=300)
    if prompt := st.chat_input("Type some text here"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
