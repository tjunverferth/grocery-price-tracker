import sqlite3
from .config import DB_PATH


def get_connection():
    """establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # enables accessing columns by name
    return conn


def initialize_database():
    """creates the items table if it doesn't exist"""
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                store TEXT NOT NULL,
                price REAL NOT NULL,
                UNIQUE(name, store)
            )
        ''')
