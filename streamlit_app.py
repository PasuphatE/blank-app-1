import streamlit as st

key=""
with st.sidebar:
    st.title("🎈 Input Your OpenAI API Key 🎈")
    title = st.text_input("Type your key here", key)
    if key=="":
        Currkey="None"
        st.write("Your current key: ", Currkey)
    else:
        Currkey=key
        st.write("Your current key: ", Currkey)

st.title("🎈 Input Some Text 🎈")
st.write(
    "This application will help you to create your own world cloud"
)
    
#messages = st.container(height=300)
#if prompt := st.chat_input("Type some text here"):
#    messages.chat_message("user").write(prompt)
#    messages.chat_message("assistant").write(f"Echo: {prompt}")

txt = st.text_area(
    "Text to analyze",
    "Input some text here",
)
#st.write(f"You wrote {len(txt)} characters.")
yrText=txt
st.write(f"Lastest Text: {yrText}")
