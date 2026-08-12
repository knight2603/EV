from app.config.settings import (
    GROQ_API_KEY,
    GROQ_MODEL,
    EV_NAME,
    MEMORY_DB_PATH,
    LOG_DIRECTORY
)


print("=== CONFIGURACIÓN DE E.V. ===")

print(
    "API KEY:",
    "CARGADA" if GROQ_API_KEY else "NO CARGADA"
)

print(
    "MODELO:",
    GROQ_MODEL
)

print(
    "NOMBRE:",
    EV_NAME
)

print(
    "BASE DE DATOS:",
    MEMORY_DB_PATH
)

print(
    "LOGS:",
    LOG_DIRECTORY
)