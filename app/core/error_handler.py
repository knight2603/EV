import traceback

class EVErrorHandler:
    
    def __init__(self, logger):
        self.logger = logger
        
    def handle(self, error: Exception, session_id: str = None) -> str:
        
        error_details = traceback.format_exc()
        
        self.logger.log_error( error_details, session_id)
        
        return (
            "Lo siento, ocurrió un problema "
            "al procesar tu solicitud."
        )