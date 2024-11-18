import streamlit as st
from langchain_community.chat_models import ChatCohere
import os
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
st.title("Langchian Demo")
cohere_api_key = os.environ.get("COHERE_API_KEY")
def generate_response(input_text):
    llm = ChatCohere(
        model = "command",
        max_token=256,
        temperature=0.5,
        cohere_api_key=cohere_api_key)
    messages = [HumanMessage(content=input_text)]
    st.info(llm.invoke(messages).content)
with st.form("chat_form"):
    text = st.text_area("Enter text","What is the important ")
    submitted = st.form_submit_button("submit")

    if submitted:
        generate_response(text)