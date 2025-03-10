from grocery_price_tracker.database import get_connection
from grocery_price_tracker.models.item import Item


def add_item(item: Item):
    """adds or updates an item in the database"""
    with get_connection() as conn:
        conn.execute(
            '''
            INSERT INTO items (name, price, store)
            VALUES (?, ?, ?)
            ON CONFLICT(name, store) DO UPDATE SET price = excluded.price
            ''',
            (item.name, item.price, item.store)
        )


def get_cheapest_item(name: str):
    """finds the cheapest item by name across all stores"""
    with get_connection() as conn:
        result = conn.execute(
            'SELECT * FROM items WHERE name = ? ORDER BY price ASC LIMIT 1',
            (name,)
        ).fetchone()

        return dict(result) if result else None


def get_all_items():
    """fetches all items from the database"""
    with get_connection() as conn:
        results = conn.execute('SELECT * FROM items ORDER BY name ASC').fetchall()
        return [dict(row) for row in results]
