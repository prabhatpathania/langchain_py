## Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SimpleSequentialChain

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
    template="when was {person} born"
)

chain2 = LLMChain(llm=llm, prompt=second_input_prompt,verbose=True,output_key='dob')

parent_Chain=SimpleSequentialChain(chains=[chain, chain2], verbose=True)





if input_text:
    st.write(parent_Chain.run(input_text))