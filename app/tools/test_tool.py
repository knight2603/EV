from app.tools.base import EVTool


class TestTool(EVTool):

    @property
    def name(self) -> str:
        return "test"

    @property
    def description(self) -> str:
        return "Herramienta utilizada para comprobar que el sistema de herramientas funciona."

    def execute(self, **kwargs):
        return "La herramienta de E.V. funciona correctamente."