from app.memory.memory_controller import MemoryController


class MemoryTool:

    name = "memory"

    description = """
    Gestiona la memoria de E.V.

    Operaciones disponibles:
    - save: guardar un recuerdo
    - search: buscar recuerdos
    - list: obtener recuerdos almacenados
    """

    def __init__(self):
        self.memory = MemoryController()

    def execute(
        self,
        operation: str,
        content: str = "",
        query: str = "",
        category: str = "general",
        importance: int = 3
    ):

        if operation == "save":

            if not content:
                return "No se proporcionó ningún recuerdo para guardar."

            saved = self.memory.remember(
                content=content,
                category=category,
                importance=importance
            )

            if saved:
                return f"Recuerdo guardado: {content}"

            return "Ese recuerdo ya estaba guardado."

        if operation == "search":

            if not query:
                return "No se proporcionó una búsqueda."

            memories = self.memory.search_memories(query)

            if not memories:
                return "No encontré recuerdos relacionados."

            return "\n".join(
                f"- {memory[1]}"
                for memory in memories
            )

        if operation == "list":

            memories = self.memory.recall()

            if not memories:
                return "No tengo recuerdos almacenados."

            return "\n".join(
                f"- {memory[1]}"
                for memory in memories
            )

        return f"Operación de memoria desconocida: {operation}"