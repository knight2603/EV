from app.logs.conversation_logger import ConversationLogger
from app.core.error_handler import EVErrorHandler


logger = ConversationLogger()

handler = EVErrorHandler(
    logger
)


try:

    raise ValueError(
        "Error de prueba de E.V."
    )

except Exception as error:

    result = handler.handle(
        error
    )

    print(result)