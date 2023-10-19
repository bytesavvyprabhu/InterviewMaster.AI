import openai as ai
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())
ai.api_key = os.getenv("OPENAI_API_KEY")

def prompting(prompt):
    messages = [{'role':"user",'content':prompt}]
    response = ai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message['content']


