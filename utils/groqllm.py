import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

PAT = st.secrets["GROQ_API_KEY"]
chat = ChatGroq(temperature=0, groq_api_key=PAT, model_name="mixtral-8x7b-32768")

def query_gpt4(text_input):
    system = "Question: {text_input}\n...\n... Answer: Let's think step by step."
    human = text_input
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    
    chain = prompt | chat
    response = chain.invoke({"text_input": text_input})

    return response

st.title("Groq API Integration")

user_input = st.text_input("You: ")

if st.button("Generate GPT-4 Text"):
    response = query_gpt4(user_input)
    st.write("GPT-4 Response:", response)