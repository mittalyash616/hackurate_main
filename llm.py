from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate

message1=[
    ("system","You are a highly experienced and knowledgeable doctor, specializing in all fields of medicine"),
    ("human","Based on the conversation transcript of doctor and patient generate bulleted points of questions which the doctor should ask the patient. the transcript is: {transcript}")
]
message2=[
    ("system","You are a highly experienced and knowledgeable doctor, specializing in all fields of medicine"),
    ("human","Based on the conversation transcript of doctor and patient generate bulleted points of diagnosis which the patient has. the transcript is: {transcript}")
]





def llm1(api_key,message):
    LLM1=ChatOpenAI(api_key=api_key,model="gpt-4o-mini")
    
def llm2(api_key,message):
    LLM2=ChatOpenAI(api_key=api_key,model="gpt-4o-mini")

