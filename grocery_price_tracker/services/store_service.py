from grocery_price_tracker.database import get_connection


def add_store(name: str):
    """adds a store to the database if it doesn't exist"""
    with get_connection() as conn:
        cursor = conn.execute("INSERT INTO stores (name) VALUES (?) RETURNING id", (name,))
        return cursor.fetchone()[0]


def get_store_by_name(name: str):
    """retrieves a store by name"""
    with get_connection() as conn:
        result = conn.execute("SELECT * FROM stores WHERE name = ?", (name,)).fetchone()
        return dict(result) if result else None


def get_all_stores():
    """retrieves all stores from the database"""
    with get_connection() as conn:
        results = conn.execute("SELECT * FROM stores").fetchall()
        return [dict(row) for row in results]
