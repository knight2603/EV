from app.brain.router import EVRouter
from app.tools.registry import ToolRegistry
from app.tools.test_tool import TestTool


registry = ToolRegistry()

registry.register(TestTool())

router = EVRouter(registry)


print("=== TEST ROUTER ===")

result = router.execute("test")

print(result)