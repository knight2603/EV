class MemoryIntentDetector:

    NONE = "none"
    SEARCH = "search"
    SAVE = "save"
    LIST = "list"

    def detect(self, message: str) -> str:

        message_lower = message.lower().strip()

        # ==========================================
        # GUARDAR MEMORIA
        # ==========================================

        if message_lower.startswith("recuerda que"):
            return self.SAVE

        # ==========================================
        # LISTAR MEMORIAS
        # ==========================================

        if (
            "qué recuerdas" in message_lower
            or "que recuerdas" in message_lower
            or "qué recuerdos tienes" in message_lower
            or "que recuerdos tienes" in message_lower
        ):

            # Si pregunta por un tema concreto,
            # debe utilizar SEARCH.
            
            if (
                "sobre " in message_lower
                or "de " in message_lower
                or "acerca de " in message_lower
            ):
                return self.SEARCH

            return self.LIST

        # ==========================================
        # NINGUNA INTENCIÓN DE MEMORIA
        # ==========================================

        return self.NONE