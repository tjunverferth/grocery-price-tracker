import sqlite3
from .config import DB_PATH


def get_connection():
    """establishes a connection to the SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    """creates the stores and items tables if they do not exist"""
    with get_connection() as conn:
        # create stores table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')

        # create items table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                store_id INTEGER NOT NULL,
                price REAL NOT NULL,
                UNIQUE(name, store_id),
                FOREIGN KEY (store_id) REFERENCES stores(id) ON DELETE CASCADE
            )
        ''')
