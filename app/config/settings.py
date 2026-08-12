import os

from dotenv import load_dotenv

load_dotenv()

# ==========================================
# GROQ
# ==========================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)


# ==========================================
# E.V.
# ==========================================

EV_NAME = os.getenv(
    "EV_NAME",
    "E.V."
)


# ==========================================
# MEMORIA
# ==========================================

MEMORY_DB_PATH = os.getenv(
    "MEMORY_DB_PATH",
    "data/memory.db"
)


# ==========================================
# LOGS
# ==========================================

LOG_DIRECTORY = os.getenv(
    "LOG_DIRECTORY",
    "data/conversations"
)