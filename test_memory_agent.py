from app.tools.default_tools import create_tool_registry
from app.brain.router import EVRouter
from app.brain.action_executor import EVActionExecutor


registry = create_tool_registry()

router = EVRouter(registry)

executor = EVActionExecutor(router)


print("=== SAVE ===")

action = {
    "action": "tool",
    "tool": "memory",
    "arguments": {
        "operation": "save",
        "content": "Estoy probando la memoria de E.V. 0.4",
        "category": "project",
        "importance": 5
    }
}

print(
    executor.execute(action)
)


print("\n=== SEARCH ===")

action = {
    "action": "tool",
    "tool": "memory",
    "arguments": {
        "operation": "search",
        "query": "E.V. 0.4"
    }
}

print(
    executor.execute(action)
)


print("\n=== LIST ===")

action = {
    "action": "tool",
    "tool": "memory",
    "arguments": {
        "operation": "list"
    }
}

print(
    executor.execute(action)
)