from app.conversation.conversation_manager import ConversationManager
from app.memory.memory_controller import MemoryController
from app.conversation.context_builder import ContextBuilder


conversation = ConversationManager(
    max_messages=4
)

memory = MemoryController()


conversation.add_user_message(
    "Estoy trabajando en E.V."
)

conversation.add_assistant_message(
    "Perfecto."
)

conversation.add_user_message(
    "Estoy aprendiendo Python."
)

conversation.add_assistant_message(
    "Excelente."
)


context_builder = ContextBuilder(
    conversation,
    memory
)


context = context_builder.build(
    "Python"
)


print("=== HISTORIAL ===")

for message in context["history"]:

    print(
        f"{message['role']}: "
        f"{message['content']}"
    )


print("\n=== MEMORIAS ===")

for memory_item in context["memories"]:

    print(
        f"- {memory_item[1]}"
    )