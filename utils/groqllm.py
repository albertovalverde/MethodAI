import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

PAT = st.secrets["GROQ_API_KEY"]
chat = ChatGroq(temperature=0, groq_api_key=PAT, model_name="mixtral-8x7b-32768")

@st.cache_resource(show_spinner=False)
def query_groq(text_input):   

    template = """Question: {prompt}
    ...
    ... Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["prompt"])

    llm_chain = LLMChain(prompt=prompt, llm=chat)

    reply = llm_chain.run(text_input)
    
    return reply

