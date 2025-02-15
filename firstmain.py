from testfile import voice
import threading
import streamlit as st
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os


message3 = [
    ("system", "You are an advanced AI designed for seamlessly merging staggered transcripts from two overlapping recordings into a single, continuous transcript without loss of information"),
    ("human", '''You will be provided a transcript that follows the following pattern:
•	Recording 1 starts at t = 0 and runs for 4 seconds, then stops.
•	Recording 2 starts at t = 2 and runs for 4 seconds, overlapping with the end of Recording 1 and capturing content missed during its pause.
•   text: pervious transcript
•	This alternating pattern continues, ensuring full coverage of the conversation.

Your task is to:
1. Merge the transcripts from both recordings into a smooth, coherent conversation making sure it maintains content with pervious transcript
2. Eliminate duplicate text caused by overlap while preserving the full meaning and structure.
3. Format the output for readability, keeping natural pauses and sentence structures intact.

Input:
• Transcript of Recording 1: {transcript1}
• Transcript of Recording 2: {transcript2}
• Previous transcript {transcript3}''')
]

prompt_template = ChatPromptTemplate.from_messages(message3)



def llm3(api_key,trans1,trans2,trans3):
    LLM3=ChatOpenAI(api_key=api_key,model="gpt-4o-mini")
    prompt = prompt_template.invoke({"transcript1":trans1 , "transcript2": trans2 , "transcript3": trans3 })
    result_llm = LLM3.invoke(prompt)
    return result_llm.content




l1 = []
l2 = []
l3 = []

def voice_function():
    voice(l1, l2)



def display_function():

    while True:
        if l1 and l2:
            trans_message = " ".join(l3)
            api_key = ...
            result = llm3(api_key,l1[0],l2[0],trans_message)
            l1.pop(0)
            l2.pop(0)
            l3.append(result)
            st.write(result)
            time.sleep(1)

def main():
    voice_thread = threading.Thread(target=voice_function)
    voice_thread.start()
    display_function()
    

if __name__ == '__main__':
    main()








