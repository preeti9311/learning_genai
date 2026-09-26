from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="openai/gpt-oss-20b", groq_api_key=groq_api_key)

## create prompt template
system_template="Translate the following to {language}:"
prompt_template=ChatPromptTemplate.from_messages([
    
       ("system", system_template),
        ("human", '{text}')
    
])

## parse
parser=StrOutputParser()
chain=prompt_template|model|parser
app=FastAPI(title="Lanchain server",
            version="1.0",
            description="A simple translation API")

## ading chain route
add_routes(
    app,chain,path="/chain"
)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)