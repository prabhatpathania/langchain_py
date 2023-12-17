import os
from constants import openai_key, aai_key
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain.llms import OpenAI
import assemblyai as aai
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key
aai.settings.api_key = aai_key

## Input link
st.title('LangChain Demo')
input_link=st.text_input("Enter the link to audio file")

## Transcribe the input file/link
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(input_link)

## Prompt
chat = ChatOpenAI()
messages = [
    SystemMessage( 
        content="""You are a customer service support bot that goes through the transcript of customer service recorded calls.
                You help to identify the following:
                1. Name of the product
                2. The problem with the product in less than 50 words
                3. Type of customer request(repair or refund).
                """
    ),
    HumanMessage(content=transcript),
]

##Show the output

if input_link:
    st.write(chat(messages=messages).content)