import os

from dotenv import load_dotenv
from groq import Groq

from app.brain.prompts import EV_ROUTER_PROMPT
from app.brain.action_parser import EVActionParser
from app.brain.action_executor import EVActionExecutor
from app.brain.router import EVRouter

from app.tools.registry import ToolRegistry
from app.tools.test_tool import TestTool


load_dotenv()


# ==========================================
# GROQ
# ==========================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ==========================================
# TOOLS
# ==========================================

registry = ToolRegistry()

registry.register(
    TestTool()
)


# ==========================================
# ROUTER
# ==========================================

router = EVRouter(registry)


# ==========================================
# PARSER
# ==========================================

parser = EVActionParser()


# ==========================================
# EXECUTOR
# ==========================================

executor = EVActionExecutor(router)


# ==========================================
# USER
# ==========================================

message = input("Tú: ")


# ==========================================
# GROQ
# ==========================================

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": EV_ROUTER_PROMPT
        },
        {
            "role": "user",
            "content": message
        }
    ]
)


raw_response = response.choices[0].message.content


# ==========================================
# PARSE
# ==========================================

action = parser.parse(raw_response)


# ==========================================
# EXECUTE
# ==========================================

result = executor.execute(action)


print("\nAcción:")
print(action)

print("\nResultado:")
print(result)