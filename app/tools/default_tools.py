from app.tools.registry import ToolRegistry
from app.tools.test_tool import TestTool
from app.tools.memory_tool import MemoryTool


def create_tool_registry():
    
    registry = ToolRegistry()
    
    registry.register(
        TestTool()
    )
    
    registry.register(
        MemoryTool()
    )
    
    return registry