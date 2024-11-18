import streamlit as st
import speech_recognition as sr
import pyttsx3
import cohere
import os
from dotenv import load_dotenv
import numpy as np
import time
import random

load_dotenv()
from cohere.responses.chat import StreamEvent

with st.chat_message("user"):
    st.write("hello")
    st.bar_chart(np.random.randn(30,3))
co=cohere.Client(os.environ.get("COHERE_API_KEY"))
st.title("Echo bot")
def response_generator():
    response=[
        "hello there! how can i help you",
        "I im here to help. what do you need?",
        "Hey! what can i do for you?",
        "Hi! what do you need help with?"
    ]
    response=random.choice(response)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
def cohere_response_generator(prompt):
    chat_history=list(map(lambda x:{
        "user_name":"user" if x["role"]=="user" else "Chatbot",
        "text":x["content"]
    },st.session_state.messages))
    for event in co.chat(f'{prompt}.Apply common sense. Answer in less than 100 words.',chat_history=chat_history,stream=True):
        if event.event_type==StreamEvent.TEXT_GENERATION:
            yield event.text
        elif event.event_type==StreamEvent.STREAM_END:
            return ""
# initiaize a chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# display the chat messages from the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("say something.."):
    #display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    #Add the user message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    #Display the assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        response=st.write_stream(response_generator())
        stream=co.chat(prompt,streaming=True)
        response=st.write_stream(cohere_response_generator(prompt))

    #Add the assistant response to the chat history
    st.session_state.messages.append({"role":"assistant","content":response})

def speech_recognition():
    # Create a recognizer object
    recognizer = sr.Recognizer()
    text = ""
    # Capture audio from the default microphone
    with sr.Microphone() as source:
        print("Listening... Say something!")
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize the speech
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Error occurred: {e}")
    return text

def text_to_speech(text, language="en"):
    # Initialize the text-to-speech engine


    # Set the language (if needed, you can check available voices using engine.getProperty('voices'))
    engine.setProperty('rate', 150)  # You can adjust the speaking rate (words per minute)
    engine.setProperty('volume', 0.9)  # You can adjust the volume (0.0 to 1.0)

    # Set the desired language (if available)
    engine.setProperty('voice', language)

    # Speak the given text
    engine.say(text)

    # Wait for the speech to complete
    engine.runAndWait()


engine = pyttsx3.init()
engine.say("hello sir i am intilized tell me what to do")

# Wait for the speech to complete

engine.runAndWait()
user_input = speech_recognition()
while True:
    response = cohere_response_generator(user_input)
    print("Cohere:", response)
    text_input = response
    text_to_speech(text_input)
    user_input = speech_recognition()