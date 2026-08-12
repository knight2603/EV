from app.tools.registry import ToolRegistry
from app.tools.test_tool import TestTool


def create_tool_registry():
    
    registry = ToolRegistry()
    
    registry.register(
        TestTool()
    )
    
    return registry