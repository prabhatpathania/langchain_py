import os
from constants import openai_key, aai_key
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain.document_loaders.assemblyai import TranscriptFormat
# from langchain.llms import OpenAI
import assemblyai as aai
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key
aai.settings.api_key = aai_key

## Input link
st.title('LangChain Demo')
audio_link=st.text_input("Enter the link to audio file")


#Transcription configuration - Audio intelligence model (https://www.assemblyai.com/docs)
aai_config = aai.TranscriptionConfig(
    speaker_labels=True, 
    auto_chapters=True, 
    entity_detection=True
)

## Transcribe the input file/link
loader = AssemblyAIAudioTranscriptLoader(
    file_path=audio_link,
    transcript_format=TranscriptFormat.SENTENCES,
)


transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_link)

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

if audio_link:
    st.write(chat(messages=messages).content)