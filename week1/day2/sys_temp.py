import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API not found")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-20b"
role = "user"
prompt = "Suggest a good name for my food company. Name should be in one word. tell only in one word"

message_system = {
    "role": "system",
    # "content": "You are my strict office colleague"
    # "content": "You are my loving girlfriend"
    "content": "You are a famous brand manager who suggests a good name for food companies."
}

message={
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model = model, messages = messages, temperature=2)
# temperature = 1
# Flavorly

# temperature = 2
# Saporio

# print(response)
# print("_____________________________________________________________________")

answer = response.choices[0].message.content
print(answer)
