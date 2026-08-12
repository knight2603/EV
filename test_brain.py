import os 
import json

from dotenv import load_dotenv
from groq import Groq

from app.brain.prompts import EV_ROUTER_PROMPT
from app.brain.action_parser import EVActionParser

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

parser = EVActionParser()

message = input ("Tú: ")


response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role":"system",
            "content": EV_ROUTER_PROMPT
        },
        {
            "role":"user",
            "content": message
        }
    ]
)

raw_response = response.choices[0].message.content

print("\nRespuesta de Groq:")
print(raw_response)

action = parser.parse(raw_response)

print("\nAcción interpretada:")

print(
    json.dumps(
        action,
        indent=4,
        ensure_ascii=False
    )
)