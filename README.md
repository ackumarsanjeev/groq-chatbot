# 🤖 Ultra-Fast Terminal Chatbot with Groq & LLaMA 3

A blazing-fast, real-time chatbot built using the [Groq API](https://console.groq.com/) and Meta's open-source **LLaMA 3-70B** model. This Python-based terminal assistant demonstrates how powerful and responsive LLMs can be when run on Groq’s custom AI hardware.

![Banner](chatbot.png) <!-- Replace with actual banner file path -->

---

## 🚀 Features

- 🧠 Powered by LLaMA 3 (70B) — no infrastructure needed
- ⚡ Lightning-fast responses via **GroqChip™**
- 🐍 Built with clean, beginner-friendly Python
- 🔐 Secure API access (supports `.env`)
- 🧪 Ideal for learning LLM API integrations

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/groq-chatbot.git
cd groq-chatbot

2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

🔑 Setup Groq API Key
1.Use Environment Variable
Create a file named .env in the project root:

GROQ_API_KEY=your_groq_api_key_here

2.Update main.py to load it:
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("GROQ_API_KEY")

🧠 Usage

Run the chatbot:

python main.py