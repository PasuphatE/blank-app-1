import streamlit as st

key=""
with st.sidebar:
    st.title("🎈 Input Your OpenAI API Key 🎈")
    title = st.text_input("Type your key here", key,type="password")
    key=title
    if key=="":
        Currkey="None"
    else:
        Currkey=key
    if len(Currkey)>10:
        showKey=Currkey[0:4]+"..."+Currkey[-4:]
    else:
        showKey=Currkey
    st.write("Your current key:\n ", showKey)

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
#import openai
#client = openai.OpenAI(api_key=Currkey)
#messages_so_far = [
#    {"role": "system", "content": "You are a helpful assistant."},
#    {"role": "user", "content": "Who won the world series in 2020?"},
#    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#    {"role": "user", "content": "Where was it played?"}
#  ]
#response = client.chat.completions.create(
#  model="gpt-4o-mini",
#  messages=messages_so_far
#)
#st.write(f"Respond:\n{response}")
#st.write(f"\nRespond[0]:\n{response.choices[0].message.content}")

import nltk
import pythainlp
import attacut
import re
from collections import Counter

nltk.download('punkt')

if yrText!="":
    lines = yrText
    #obj = []
    #for line in lines:
    #    line = line.strip()
    #    if line:  # Skip empty lines
    #       line = re.sub(r"^- |^-\s{1,}|^\s{1,}", "", line)
    #        # Retain only the specified characters
    #        line = "".join(re.findall(r"[a-zA-Z0-9ก-์๐-๙\s\u0E30-\u0E39\u0E47\u0E48\u0E31-\u0E3A]", line))
    #        obj.append(line)
    obj_tokenized=pythainlp.word_tokenize(lines, engine='attacut')
    #obj_tokenized=[]
    #for i in obj:
        #obj_tokenized.append(nltk.tokenize.word_tokenize(i))
        #obj_tokenized.append(pythainlp.word_tokenize(i,engine='attacut'))
    #obj_tokenized.append(pythainlp.sent_tokenize(i,))
    
    obj_tokenized_no_stop_words = []
    stopset = set(pythainlp.corpus.thai_stopwords())
    #for i in range(len(obj_tokenized)):
    #    for t in obj_tokenized[i]:
    #        if t not in stopset:
    #            obj_tokenized_no_stop_words.append(t)
    for t in obj_tokenized:
            if t not in stopset:
                obj_tokenized_no_stop_words.append(t)

    word_count = obj_tokenized_no_stop_words
    word_count2 = []
    for word in word_count:
        word = word.strip()
        if word:
            word="".join(re.findall(r"[a-zA-Z0-9ก-์๐-๙\s\u0E30-\u0E39\u0E47\u0E48\u0E31-\u0E3A]", word))
            word_count2.append(word)
   
    # นับความถี่ของคำ
    word_count = Counter(word_count2)
    # เรียงคำตามความถี่จากมากไปน้อย
    sorted_word_dict = dict(word_count.most_common())
    sorted_word_dict.pop('""')

#st.write(obj_tokenized)
#st.write(obj_tokenized_no_stop_words)
st.write(sorted_word_dict)


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ข้อมูลลิสต์ข้อความ
word_list = word_count2
word_freq = sorted_word_dict
# รวมคำจากลิสต์เป็นสตริงเดียว (เว้นวรรคแต่ละคำ)
text = " ".join(word for word in word_list if word.strip())
# สร้าง WordCloud โดยกำหนด path ฟอนต์ภาษาไทย
wordcloud = WordCloud(
    #font_path=font_path,  # กำหนด path ฟอนต์ภาษาไทย
    width=800,
    height=400,
    background_color='white',
    colormap='viridis'
).generate_from_frequencies(word_freq)


# แสดงผล WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
