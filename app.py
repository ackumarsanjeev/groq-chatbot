import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api)

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")

st.title("🤖 Ultra-Fast Chatbot (Groq + LLaMA 3)")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Say something to the chatbot...")
if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Call Groq API
    response = client.chat.completions.create(
        model="llama-3-3-70b-versatile",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response.choices[0].message.content.strip()

    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
