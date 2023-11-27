## Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# User input
st.title('Translate and Learn')
input_text=st.text_input("Enter the text you want to translate to Dutch")

chat = ChatOpenAI()
## Prompt
messages = [
    SystemMessage( 
        content="""You are a helpful assistant that translates English to Dutch for people who do not understand Dutch. 
                Your job is help translate the given text using child friendly language and writing sentence not longer than 12 words. 
                If you are unable to translate a text for the user, you will convey the same in a polite tone.
                For the response to the input, You will : 
                1. translate the user input to simple Dutch
                2. In a separate section, in simple English, explain how to pronounce the translated text. 
                3. In simple english, give 2 examples (as bullet points) of scenarios where dutch people would use such a word/sentence
                """
    ),
    HumanMessage(content=input_text),
]

if input_text:

    st.write(chat(messages=messages).content)