## Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key


st.title('Translate your results')
input_text=st.text_input("Enter the text you want to translate to Dutch")

chat = ChatOpenAI()

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to Dutch."
    ),
    HumanMessage(content=input_text),
]

if input_text:
    st.write(chat(messages=messages).content)