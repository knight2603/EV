from app.tools.registry import ToolRegistry
from app.tools.test_tool import TestTool


registry = ToolRegistry()

tool = TestTool()

registry.register(tool)


print("Herramientas disponibles:")

for registered_tool in registry.list_tools():

    print(
        f"- {registered_tool.name}: "
        f"{registered_tool.description}"
    )


print("\nEjecutando herramienta:")

result = registry.get("test").execute()

print(result)