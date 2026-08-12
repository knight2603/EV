import os

from dotenv import load_dotenv
from groq import Groq

from app.brain.prompts import EV_SYSTEM_PROMPT
from app.memory.memory_manager import MemoryManager


load_dotenv()


class EVAgent:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError(
                "E.V. no encontró GROQ_API_KEY en el archivo .env"
            )

        self.client = Groq(api_key=api_key)

        self.memory = MemoryManager()

    def ask(self, message: str) -> str:

        message_lower = message.lower().strip()

        # ==========================================
        # GUARDAR MEMORIA
        # ==========================================

        if message_lower.startswith("recuerda que"):

            memory_content = message[len("recuerda que"):].strip()

            if not memory_content:
                return "¿Qué quieres que recuerde?"

            self.memory.save_memory(
                content=memory_content,
                category="general",
                importance=3
            )

            return f"Entendido. Recordaré que {memory_content}"

        # ==========================================
        # MOSTRAR MEMORIA
        # ==========================================

        if (
            "qué recuerdas" in message_lower
            or "que recuerdas" in message_lower
            or "recuerdas de mí" in message_lower
            or "recuerdas de mi" in message_lower
        ):

            memories = self.memory.get_memories()

            if not memories:
                return "Todavía no tengo recuerdos guardados."

            memory_text = "\n".join(
                f"- {memory[1]}"
                for memory in memories
            )

            prompt = f"""
            Estas son las memorias que tengo almacenadas:

            {memory_text}

            Responde al usuario utilizando estas memorias.
            No inventes información que no aparezca aquí.
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
        # CONVERSACIÓN NORMAL
        # ==========================================

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": EV_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content