from datetime import datetime
from pathlib import Path


class ConversationLogger:

    def __init__(self):

        base_dir = Path(__file__).resolve().parents[2]

        self.log_dir = base_dir / "data" / "conversations"

        self.log_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def _get_log_file(self):

        date = datetime.now().strftime("%Y-%m-%d")

        return self.log_dir / f"{date}.log"

    def log_user(self, message: str, session_id: str = None):

        self._write(
            "USUARIO",
            f"[SESSION: {session_id}] {message}"
        )

    def log_ev(self, message: str, session_id: str = None):

        self._write(
            "E.V.",
            f"[SESSION: {session_id}] {message}"
        )

    def log_action(
        self,
        action: str,
        tool: str = "",
        operation: str = "",
        session_id: str = None
    ):
        self._write(
                "ACCIÓN",
                (
                    f"[SESSION: {session_id}] "
                    f"action={action} "
                    f"tool={tool} "
                    f"operation={operation}"
                )
            )
        
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        line = (
            f"[{timestamp}] ACCIÓN | "
            f"action={action} "
            f"tool={tool} "
            f"operation={operation}"
        )

        self._append(line)

    def _write(
        self,
        role: str,
        message: str
    ):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        line = (
            f"[{timestamp}] "
            f"{role}: {message}"
        )

        self._append(line)

    def _append(self, line: str):

        log_file = self._get_log_file()

        with open(
            log_file,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                line + "\n"
            )
            
    def log_error(
        self,
        error: str,
        session_id: str = None
    ):

        self._write(
            "ERROR",
            f"[SESSION: {session_id}]\n{error}"
        )