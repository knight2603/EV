from app.tools.memory_tool import MemoryTool


memory = MemoryTool()


print("=== GUARDAR ===")

print(
    memory.execute(
        operation="save",
        content="Estoy construyendo E.V. 0.4",
        category="project",
        importance=5
    )
)


print("\n=== BUSCAR ===")

print(
    memory.execute(
        operation="search",
        query="E.V."
    )
)


print("\n=== LISTAR ===")

print(
    memory.execute(
        operation="list"
    )
)