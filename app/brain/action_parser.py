import json 

class EVActionParser:
    
    def parse(self, response: str):
        
        try:
            data = json.loads(response)
            
            if not isinstance(data, dict):
                return {
                    "action": "chat",
                    "response": response
                }
            return data
        
        except json.JSONDecodeError:
            
            return{
                "action":"chat",
                "response":response
            }