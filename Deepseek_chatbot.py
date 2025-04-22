import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not API_KEY:
     print("API Key not found. Check your .env file.")
     exit()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

def chat_with_bot(user_input):
    try:
        completion = client.chat.completions.create(
            model="microsoft/mai-ds-r1:free",
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )
        # Return the bot's response
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Main loop to keep chatting with the bot
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    response = chat_with_bot(user_input)
    print(f"Chatbot: {response}")
