from app.logs.conversation_logger import ConversationLogger


logger = ConversationLogger()

logger.log_user("Hola E.V.")

logger.log_action(
    action="chat"
)

logger.log_ev("¡Hola! Soy E.V.")

logger.log_user(
    "Recuerda que estoy aprendiendo Python"
)

logger.log_action(
    action="tool",
    tool="memory",
    operation="save"
)

logger.log_ev(
    "Entendido Recordaré que estás aprendiendo Python"
)


print("Logger funcionando correctamente.")