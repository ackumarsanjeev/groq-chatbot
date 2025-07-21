# 🤖 Ultra-Fast Terminal Chatbot with Groq & LLaMA 3

A blazing-fast, real-time chatbot built using the [Groq API](https://console.groq.com/) and Meta's open-source **LLaMA 3-70B** model. This Python-based terminal assistant demonstrates how powerful and responsive LLMs can be when run on Groq’s custom AI hardware.

![Banner](https://raw.githubusercontent.com/ackumarsanjeev/groq-chatbot/main/chatbot.png)

---

## 🚀 Features

- 🧠 Powered by LLaMA 3 (70B) — no infrastructure needed
- ⚡ Lightning-fast responses via **GroqChip™**
- 🐍 Built with clean, beginner-friendly Python
- 🔐 Secure API access (supports `.env`)
- 🧪 Ideal for learning LLM API integrations
- 🌐 **Streamlit Web UI** included!

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ackumarsanjeev/groq-chatbot.git
cd groq-chatbot


2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt


🔑 Setup Groq API Key

Create a .env file in the root of your project:
GROQ_API_KEY=your_groq_api_key_here

🧠 Usage

🔹 Terminal Chatbot
Run the chatbot in the terminal:

python main.py

Type your queries like:

You: What is zero trust architecture?

Type exit to end the session.


🔹 Streamlit Web UI (Optional)

Run the chatbot in a web browser using Streamlit:

streamlit run app.py
