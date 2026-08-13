class ContextBuilder:

    def __init__(self, conversation, memory):
        self.conversation = conversation
        self.memory = memory

    def build(self, query: str):

        history = self.conversation.get_history()

        memories = self.memory.search_memories(
            query
        )

        return {
            "history": history,
            "memories": memories
        }