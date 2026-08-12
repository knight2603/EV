class EVActionExecutor:
    
    def __init__(self, router):
        self.router = router
        
    def execute(self, action: dict):
        
        action_type = action.get("action")
        
        if action_type =="chat":
            
            return action.get(
                "response",
                "No tengo una respuesta"
            )
            
        if action_type == "tool":
            
            tool_name = action.get("tool")
            arguments = action.get("arguments", {})
            
            return self.router.execute(
                tool_name,
                **arguments
            )
            
        return"No entendi la accion solicitada"