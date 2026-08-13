from app.conversation.conversation_manager import ConversationManager


conversation = ConversationManager(
    max_messages=4
)


for i in range(1, 8):

    conversation.add_user_message(
        f"Mensaje usuario {i}"
    )

    conversation.add_assistant_message(
        f"Respuesta E.V. {i}"
    )


print("=== TOTAL ALMACENADO ===")

print(
    len(conversation.messages)
)


print("\n=== HISTORIAL QUE RECIBE GROQ ===")

history = conversation.get_history()

for message in history:

    print(
        f"{message['role']}: "
        f"{message['content']}"
    )
    
print("\n=== LIMPIANDO ===")

conversation.clear()

print(
    f"Mensajes después de limpiar: "
    f"{len(conversation.messages)}"
)