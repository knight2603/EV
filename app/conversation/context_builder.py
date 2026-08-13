from app.brain.memory_intent_detector import MemoryIntentDetector

class ContextBuilder:

    def __init__(
        self,
        conversation,
        memory,
        memory_intent_detector
    ):
        self.conversation = conversation
        self.memory = memory
        self.memory_intent_detector = memory_intent_detector

    def build(self, query: str):

        history = self.conversation.get_history()

        intent = self.memory_intent_detector.detect(
            query
        )

        memories = []

        if intent == MemoryIntentDetector.SEARCH:

            search_query = self._extract_search_query(
                query
            )

            memories = self.memory.search_memories(
                search_query
            )


        elif intent == MemoryIntentDetector.LIST:

            memories = self.memory.recall()

        return {
            "history": history,
            "memories": memories,
            "memory_intent": intent
        }

    def _extract_search_query(self, query: str):

        query = query.lower().strip()

        # Eliminar signos de interrogación
        query = query.strip("¿?")

        prefixes = [
            "qué recuerdas sobre ",
            "que recuerdas sobre ",
            "qué recuerdas de ",
            "que recuerdas de ",
            "qué recuerdas acerca de ",
            "que recuerdas acerca de "
        ]

        for prefix in prefixes:

            if query.startswith(prefix):

                return query[len(prefix):].strip(
                    " ?¿."
                )

        return query