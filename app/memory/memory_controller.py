from app.memory.memory_manager import MemoryManager


class MemoryController:

    def __init__(self):
        self.memory = MemoryManager()

    def remember(
        self,
        content: str,
        category: str = "general",
        importance: int = 3
    ):

        if self.memory.memory_exists(content):
            return False

        self.memory.save_memory(
            content=content,
            category=category,
            importance=importance
        )

        return True

    def recall(self):
        return self.memory.get_memories()

    def search_memories(self, query):
        return self.memory.search_memories(query)

    def forget(self, memory_id: int):
        return self.memory.delete_memory(memory_id)