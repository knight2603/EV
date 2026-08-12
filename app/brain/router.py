class EVRouter:

    def __init__(self, tool_registry):
        self.tool_registry = tool_registry

    def execute(self, tool_name: str, **kwargs):

        tool = self.tool_registry.get(tool_name)

        if not tool:
            return f"No conozco la herramienta '{tool_name}'."

        return tool.execute(**kwargs)