import sqlite3
from pathlib import Path

BASE_DIR = Path (__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "ev.db"

def get_connection():
    DATA_DIR.mkdir(exist_ok=True)
    
    connection = sqlite3.connect(DATABASE_PATH)
    
    return connection