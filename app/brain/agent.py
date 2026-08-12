import os

from dotenv import load_dotenv
from groq import Groq

from app.brain.prompts import (EV_SYSTEM_PROMPT, EV_ROUTER_PROMPT)
from app.memory.memory_controller import MemoryController

from app.brain.action_parser import EVActionParser
from app.brain.action_executor import EVActionExecutor
from app.brain.router import EVRouter
from app.tools.default_tools import create_tool_registry

load_dotenv()


class EVAgent:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError(
                "E.V. no encontró GROQ_API_KEY en el archivo .env"
            )

        self.client = Groq(api_key=api_key)

        self.memory = MemoryController()

        self.tool_registry = create_tool_registry()
        
        self.router = EVRouter(
            self.tool_registry
        )
        
        self.action_parser = EVActionParser()
        
        self.action_executor = EVActionExecutor(
            self.router
        )

    def ask(self, message: str) -> str:

        message_lower = message.lower().strip()

        # ==========================================
        # RECORDAR
        # ==========================================

        if message_lower.startswith("recuerda que"):

            memory_content = message[len("recuerda que"):].strip()

            if not memory_content:
                return "¿Qué quieres que recuerde?"

            saved = self.memory.remember(
                content=memory_content,
                category="general",
                importance=3
            )

            if saved:
                return f"Entendido. Recordaré que {memory_content}"

            return "Ya tenía ese recuerdo guardado."

        # ==========================================
        # RECORDAR INFORMACIÓN
        # ==========================================

        if (
            "qué recuerdas" in message_lower
            or "que recuerdas" in message_lower
            or "recuerdas de mí" in message_lower
            or "recuerdas de mi" in message_lower
        ):

            memories = self.memory.recall()

            if not memories:
                return "Todavía no tengo recuerdos guardados."

            memory_text = "\n".join(
                f"- {memory[1]}"
                for memory in memories
            )

            prompt = f"""
                    Estas son las memorias almacenadas de E.V.:

                    {memory_text}

                    Responde al usuario utilizando únicamente estas memorias.
                    No inventes información.

                    Usuario:
                    {message}
                    """

            response = self.client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": EV_SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content

        # ==========================================
        # ROUTER / ACCIONES
        # ==========================================

        response = self.client.chat.completions.create(
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

        action = self.action_parser.parse(
            raw_response
        )

        return self.action_executor.execute(
            action
        )