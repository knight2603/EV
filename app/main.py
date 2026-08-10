from app.brain.agent import EVAgent

def main():
    
    ev = EVAgent()
    
    print("=" * 50)
    print("E.V 0.1")
    print("Asistente personal inteligente")
    print("=" * 50)
    print("Escribe 'salir' para cerrar E.V.\n")
    
    while True:
        
        user_message = input ("Tu: ")
        
        if user_message.lower()== "salir":
            print("E.V, Hasta luego Peter")
            break
        
        try:
            response = ev.ask(user_message)
            print(f"\nE.V.: {response}\n")
            
        except Exception as error:
            print(f"\nE.V.: Ocurrió un error: {error}\n")

if __name__ == "__main__":
    main()