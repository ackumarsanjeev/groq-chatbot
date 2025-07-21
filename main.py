from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv() # Load the .env file

api = os.getenv("GROQ_API_KEY")
print("API Key loaded:", api)

client=Groq(api_key=api)

while True:
    inp = input("You: ")
    if inp.lower() == "exit":
        break

    result = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": inp
            }
        ]
    )

    print(f"Model: {result.choices[0].message.content}")

