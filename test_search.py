from app.memory.memory_manager import MemoryManager


memory = MemoryManager()

results = memory.search_memories("python")

print("=== RESULTADOS ===")

for result in results:
    print("-", result[1])