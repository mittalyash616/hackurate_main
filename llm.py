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
message3 = [
    ("system", "You are an advanced AI designed for seamlessly merging staggered transcripts from two overlapping recordings into a single, continuous transcript without loss of information"),
    ("human", '''You will be provided a transcript that follows the following pattern:
•	Recording 1 starts at t = 0 and runs for 4 seconds, then stops.
•	Recording 2 starts at t = 2 and runs for 4 seconds, overlapping with the end of Recording 1 and capturing content missed during its pause.
•	This alternating pattern continues, ensuring full coverage of the conversation.

Your task is to:
1. Merge the transcripts from both recordings into a smooth, coherent conversation.
2. Eliminate duplicate text caused by overlap while preserving the full meaning and structure.
3. Maintain speaker labels (if provided) and ensure correct sentence flow.
4. Format the output for readability, keeping natural pauses and sentence structures intact.

Input:
• Transcript of Recording 1: {transcript1}
• Transcript of Recording 2: {transcript2}''')
]




def llm1(api_key,message):
    LLM1=ChatOpenAI(api_key=api_key,model="gpt-4o-mini")
    
def llm2(api_key,message):
    LLM2=ChatOpenAI(api_key=api_key,model="gpt-4o-mini")

def llm3(api_key,message):
    LLM3=ChatOpenAI(api_key=api_key,model="gpt-4o-mini")