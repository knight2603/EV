from app.tools.base import EVTool


class ToolRegistry:

    def __init__(self):
        self.tools: dict[str, EVTool] = {}

    def register(self, tool: EVTool):

        self.tools[tool.name] = tool

    def get(self, name: str):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.values())