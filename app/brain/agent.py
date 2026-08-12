from app.config.settings import (
    GROQ_API_KEY,
    GROQ_MODEL
)

from groq import Groq

from app.brain.prompts import EV_SYSTEM_PROMPT, EV_ROUTER_PROMPT

from app.brain.action_parser import EVActionParser
from app.brain.action_executor import EVActionExecutor
from app.brain.router import EVRouter

from app.tools.default_tools import create_tool_registry
from app.logs.conversation_logger import ConversationLogger
from app.core.error_handler import EVErrorHandler
from app.core.session_manager import SessionManager
from app.conversation.conversation_manager import ConversationManager


class EVAgent:

    def __init__(self):

        
        if not GROQ_API_KEY:
            raise RuntimeError(
                "E.V. no encontró GROQ_API_KEY en el archivo .env"
            )

        self.client = Groq(
            api_key=GROQ_API_KEY
        )
        
        self.session = SessionManager()
        
        self.logger = ConversationLogger()
        
        self.error_handler = EVErrorHandler(
            self.logger
        )
        
        self.conversation = ConversationManager()

        # ==========================================
        # HERRAMIENTAS
        # ==========================================

        self.tool_registry = create_tool_registry()

        self.router = EVRouter(
            self.tool_registry
        )

        # ==========================================
        # SISTEMA DE ACCIONES
        # ==========================================

        self.action_parser = EVActionParser()

        self.action_executor = EVActionExecutor(
            self.router
        )

    @property
    def session_id(self):
        return self.session.get_session_id()
    
    # ==============================================
    # PROCESAMIENTO DE MENSAJES
    # ==============================================

    def ask(self, message: str) -> str:

        self.logger.log_user(
            message,
            self.session_id
        )

        self.conversation.add_user_message(
            message
        )

        try:

            history = self.conversation.get_history()

            messages = [
                {
                    "role": "system",
                    "content": EV_ROUTER_PROMPT
                }
            ]

            messages.extend(history)
            response = self.client.chat.completions.create(
                model=GROQ_MODEL,
                messages=messages,
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "ev_action",
                        "strict": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "action": {
                                    "type": "string",
                                    "enum": ["chat", "tool"]
                                },
                                "response": {
                                    "type": ["string", "null"]
                                },
                                "tool": {
                                    "type": ["string", "null"],
                                    "enum": [
                                        "test",
                                        "memory",
                                        None
                                    ]
                                },
                                "arguments": {
                                    "type": "object",
                                    "properties": {
                                        "operation": {
                                            "type": ["string", "null"],
                                            "enum": [
                                                "save",
                                                "search",
                                                "list",
                                                None
                                            ]
                                        },
                                        "content": {
                                            "type": ["string", "null"]
                                        },
                                        "category": {
                                            "type": ["string", "null"]
                                        },
                                        "importance": {
                                            "type": ["integer", "null"]
                                        },
                                        "query": {
                                            "type": ["string", "null"]
                                        }
                                    },
                                    "required": [
                                        "operation",
                                        "content",
                                        "category",
                                        "importance",
                                        "query"
                                    ],
                                    "additionalProperties": False
                                }
                            },
                            "required": [
                                "action",
                                "response",
                                "tool",
                                "arguments"
                            ],
                            "additionalProperties": False
                        }
                    }
                }
            )

            raw_response = response.choices[0].message.content

            action = self.action_parser.parse(
                raw_response
            )

            self.logger.log_action(
                action=action.get("action", ""),
                tool=action.get("tool", ""),
                operation=action.get(
                    "arguments", {}
                ).get("operation", ""),
                session_id=self.session_id
            )

            result = self.action_executor.execute(
                action
            )

            self.logger.log_ev(
                result,
                self.session_id
            )

            self.conversation.add_assistant_message(
                result
            )

            return result

        except Exception as error:

            return self.error_handler.handle(
                error,
                self.session_id
            )
