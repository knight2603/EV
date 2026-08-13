from app.conversation.conversation_manager import ConversationManager
from app.memory.memory_controller import MemoryController
from app.conversation.context_builder import ContextBuilder
from app.brain.memory_intent_detector import MemoryIntentDetector


conversation = ConversationManager(
    max_messages=4
)

memory = MemoryController()

memory_intent_detector = MemoryIntentDetector()


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
    memory,
    memory_intent_detector
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

print("\n=== HOLA ===")

context = context_builder.build(
    "hola ev"
)

print(
    "Memorias encontradas:",
    context["memories"]
)

print(
    "Intención:",
    context["memory_intent"]
)


print("\n=== PYTHON ===")

context = context_builder.build(
    "¿qué recuerdas sobre python?"
)

print(
    "Memorias encontradas:",
    context["memories"]
)

print(
    "Intención:",
    context["memory_intent"]
)


print("\n=== LISTA ===")

context = context_builder.build(
    "¿qué recuerdos tienes?"
)

print(
    "Cantidad de memorias:",
    len(context["memories"])
)

print(
    "Intención:",
    context["memory_intent"]
)