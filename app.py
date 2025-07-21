import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")

# 🌟 Styled Header
st.markdown("""
    <h1 style='text-align: center; color: #2E3B4E;'>🤖 Ultra-Fast Chatbot<br><span style='font-size:22px;'>Powered by <b>Groq</b> + LLaMA 3</span></h1>
    """, unsafe_allow_html=True)

# Sidebar for Info
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This chatbot uses the **Groq API** with **LLaMA 3-70B** to provide ultra-fast responses.
    
    🔐 Add your API key in a `.env` file  
    🧪 Try asking anything about AI, Python, cybersecurity, etc.
    """)
    st.markdown("---")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []

# Groq Client
if api:
    client = Groq(api_key=api)
else:
    st.error("GROQ_API_KEY not found. Please add it to your .env file.")
    st.stop()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("Say something to the chatbot...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call Groq API
    try:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3-3-70b-versatile",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"⚠️ API error: {e}")

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
