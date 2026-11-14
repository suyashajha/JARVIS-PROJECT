
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is missing!")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-6.1-terra",
    input="What is coding?"
)

print(response.output_text)
