import streamlit as st

key=""
with st.sidebar:
    st.title("🎈 Input Your OpenAI API Key 🎈")
    title = st.text_input("Type your key here", key)
    key=title
    if key=="":
        Currkey="None"
    else:
        Currkey=key
    
    st.write("Your current key:\n ", Currkey)

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

######OpenAI
import openai
client = openai.OpenAI(api_key=Currkey)
messages_so_far = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=messages_so_far
)
st.write(f"Respond:\n{response}")
st.write(f"\nRespond[0]:\n{response.choices[0].message.content}")
