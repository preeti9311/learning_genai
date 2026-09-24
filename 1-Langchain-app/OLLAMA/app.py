## simple genai app using langchain
import os
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]



from langchain_community.llms import Ollama  # pyright: ignore[reportMissingImports]
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]= os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]= os.getenv("LANGCHAIN_TRACING_V2")


## prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant .please respond to the question asked."),
        ("user","Question:{question}"),
    ]
)

st.title("Langchain Ollama App")
input_text=st.text_input("Enter your question here")

##ollama model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))


