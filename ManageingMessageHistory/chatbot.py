import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

llm = ChatGroq(model="llama-3.3-70b-versatile")
outputparser=StrOutputParser()

prompts = ChatPromptTemplate(
    [
        ("system","You are usefull AI assistant answer users query to the best."),
        (MessagesPlaceholder("chat_history")),
        ("user","{input_text}")

    ]
)



normalchain = prompts|llm|outputparser

def getsession(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state:
        st.session_state[session_id] = ChatMessageHistory()
    return st.session_state[session_id]


chain_with_message_history = RunnableWithMessageHistory(
    normalchain,
    get_session_history=getsession,
    input_messages_key="input_text",
    history_messages_key="chat_history"
)

st.title("AI Assistant:")
userInput = st.text_input("Enter your Query")
if userInput:
    
    config ={
        "configurable":{"session_id":"chat1"}
    }
    res = chain_with_message_history.invoke(
        {"input_text":userInput},
        config=config
    )
    st.write(res)