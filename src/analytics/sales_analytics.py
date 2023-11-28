import streamlit as st
import pandas as pd
import os
import plotly.express as px
from st_aggrid import AgGrid
from openpyxl import load_workbook
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from constants import openai_key

# Function to load and process the uploaded Excel file
def load_data(file):
    df = pd.read_csv(file, delimiter=',') #, engine='openpyxl')
    return df

def askGPT(sales_data):

    print("I am GPT")
    print(sales_data)
    os.environ["OPENAI_API_KEY"] = openai_key
    ##OpenAI LLMs
    llm=OpenAI(temperature=0.8)
    
    sales_analysis_prompt=PromptTemplate(
        input_variables=['sales_data'],#which was loaded in a python program through a csv, so maybe you need to adjust the format before using it .
        template="""As a data analyst, please review the sales data in {sales_data} 
        This contains sales order information of different orders over the years.
        The data is for columns: order_id, product_ID, order_date, customer_id and price (in the same order) 
        Your job is:
        1. to tell me the order ID and price of the order that has the highest price
        2. Tell me if you see any trend in the data in terms of which material has been ordered more lately"""
    )
    chain = LLMChain(llm=llm, prompt=sales_analysis_prompt) #,verbose=True)
    if sales_data:
        st.write(chain.run(sales_data))

# Streamlit UI
def main():

    st.title('Sales Analytics')

    uploaded_file = st.file_uploader('Upload Excel file', type=['xlsx', 'csv'])

    if uploaded_file is not None:
        try:
            df = load_data(uploaded_file)
            st.dataframe(df)
            print(df.head)            
            askGPT(df.head)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
