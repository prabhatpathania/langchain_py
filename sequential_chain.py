## Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

#Streamlit Framework

st.title('Celebrity Search Resuts')
input_text=st.text_input("Search the topic you want")

##Prompt Templates

first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

##OpenAI LLMs
llm=OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt,verbose=True,output_key='person')

second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="on which date was {person} born"
)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt,verbose=True,output_key='dob')

third_input_prompt=PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around that {dob} in the world"
)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt,verbose=True,output_key='description')



parent_Chain=SequentialChain(
    chains=[chain, chain2, chain3],input_variables=['name'],output_variables=['person','dob','description'],verbose=True)





if input_text:
    st.write(parent_Chain({'name':input_text}))