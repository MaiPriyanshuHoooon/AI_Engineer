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
prompt1 = "Hi!"
prompt2 = "Give me information about time travel in detail."
prompt3 = "Give me 1000 words essay on Quantum Computing and Quantum Computers - The Future after Supercomputers"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message={
    "role": role,
    "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(model = model, messages = messages, max_tokens = 5000)
    usage = response.usage
    print(f"Prompt: {prompt} --> Prompt tokens: {usage.prompt_tokens}, Output tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}, Finish reason: {response.choices[0].finish_reason} ")


