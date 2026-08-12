class ConversationManager:

    def __init__(self, max_messages=20):
        self.messages = []
        self.max_messages = max_messages

    def add_user_message(self, message: str):

        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_assistant_message(self, message: str):

        self.messages.append({
            "role": "assistant",
            "content": message
        })

    def get_history(self):

        return self.messages[
            -self.max_messages:
        ].copy()

    def clear(self):

        self.messages.clear()