import streamlit as st

with st.sidebar:
    st.title("🎈 Input Your OpenAI API Key 🎈")

st.title("🎈 Input Some Text 🎈")
st.write(
    "This application will help you to create your own world cloud"
)
    
messages = st.container(height=300)
if prompt := st.chat_input("Type some text here"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"Echo: {prompt}")
