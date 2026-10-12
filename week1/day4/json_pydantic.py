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

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract personal information from the ticket strictly based on this schema and give me in json format.
{schema}
"""
message_system = {
    "role": "system",
    "content": system_prompt
}

text = "My name is Priyanshu Malik. I bought a phone from you guys recently and it's not working. My email is abc@gmail.com. Phone number is 82218. My address is delhi. Do consider my request and make it correct ASAP."

prompt = f"""
This is a customer ticket. Please extract personal information from the text.
{text}
"""

message={
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model = model, messages = messages, response_format = response_format)
answer = response.choices[0].message.content
print(answer)

import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket)
