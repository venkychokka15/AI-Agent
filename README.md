# AI-Agent
This chatbot uses Streamlit for the UI, Cohere for NLP-based AI responses, SpeechRecognition for converting speech to text, and pyttsx3 for text-to-speech. Users can interact via text or voice, and the bot responds with both text and spoken output, creating a multimodal experience.
Conversational Chatbot with Speech and Text Interaction
This project creates an interactive chatbot application using multiple technologies. It allows users to engage in conversations through both text and speech, leveraging Cohere's NLP API, Streamlit for the web interface, SpeechRecognition for voice input, and pyttsx3 for text-to-speech output.

Project Overview
The chatbot supports both text and voice interactions:

Streamlit: For building the user interface (UI) for chat input/output.
Cohere: For generating AI-based responses using natural language processing (NLP).
SpeechRecognition: Converts spoken language into text for voice-based interactions.
pyttsx3: Converts the chatbot’s text responses into speech.
Components and Libraries Used
Streamlit (st): Creates the web interface and handles chat interactions.
SpeechRecognition (sr): Recognizes speech from the user’s microphone and converts it to text.
pyttsx3: Provides text-to-speech functionality for vocal responses from the bot.
Cohere: Generates text-based responses from the chatbot using the Cohere API.
dotenv (load_dotenv): Loads environment variables for secure API key management.
NumPy, Random, and Time: Used for random data generation and creating natural delays in responses.
Setup Instructions
git clone <repository_url>
cd <project_directory>
pip install -r requirements.txt
COHERE_API_KEY=<your_cohere_api_key>
streamlit run app.py
Usage Guide
Once the app is running, the user can:

Type messages in the chat interface.
Use voice input by clicking the microphone button.
Listen to the bot’s text-based responses, which are also spoken aloud.
Third-Party APIs and Tools
Cohere API: Used for generating AI-based responses. You need to sign up for a Cohere API key.

Cohere Documentation
SpeechRecognition: Used for converting speech to text. Relies on Google Web Speech API for speech recognition.

SpeechRecognition Documentation
pyttsx3: A text-to-speech library that works offline and converts the bot's responses into speech.

pyttsx3 Documentation
Streamlit: A framework for building interactive web applications with minimal code.

Streamlit Documentation
Potential Issues and Suggestions
Speech-to-Text Integration: Currently, speech input might block the UI. Consider implementing an asynchronous approach or adding a button for speech recognition.
Voice Overlap: If a user speaks while the bot is responding, voice overlap may occur. Ensure that speech is completed before processing new input.
Error Handling: Add error handling for API failures, particularly for the Cohere API (e.g., invalid API key or rate limit exceeded).
Conclusion
This application demonstrates an interactive chatbot that combines text and voice interfaces. It uses Cohere for AI-generated responses, Streamlit for the user interface, SpeechRecognition for voice input, and pyttsx3 for voice output. Future improvements can enhance UX and handle edge cases more robustly.
