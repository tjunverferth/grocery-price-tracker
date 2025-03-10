from fastapi import HTTPException

from grocery_price_tracker.database import get_connection
from grocery_price_tracker.models.item import Item
from grocery_price_tracker.services.store_service import get_store_by_name


def add_item(item: Item):
    """adds or updates an item in the database"""
    with get_connection() as conn:
        # ensure store exists
        store = get_store_by_name(item.store)
        if not store:
            raise HTTPException(status_code=400, detail=f"store '{item.store}' does not exist")

        store_id = store["id"]

        # check if item already exists for this store
        existing_item = conn.execute(
            "SELECT id FROM items WHERE name = ? AND store_id = ?",
            (item.name, store_id)
        ).fetchone()

        if existing_item:
            conn.execute(
                "UPDATE items SET price = ? WHERE id = ?",
                (item.price, existing_item["id"])
            )
        else:
            # insert new item
            conn.execute(
                "INSERT INTO items (name, store_id, price) VALUES (?, ?, ?)",
                (item.name, store_id, item.price)
            )


def get_cheapest_item(name: str):
    """finds the cheapest item by name across all stores"""
    with get_connection() as conn:
        # find the lowest price for the item
        min_price_row = conn.execute('''
            SELECT MIN(price) AS min_price FROM items WHERE name = ?
        ''', (name,)).fetchone()

        if not min_price_row or min_price_row["min_price"] is None:
            return []

        min_price = min_price_row["min_price"]

        # get all stores that sell at the lowest price
        results = conn.execute('''
            SELECT items.id, items.name, stores.name AS store, items.price
            FROM items
            JOIN stores ON items.store_id = stores.id
            WHERE items.name = ? AND items.price = ?
        ''', (name, min_price)).fetchall()

        return [dict(row) for row in results] if results else []


def get_all_items():
    """fetches all items from the database, including store names"""
    with get_connection() as conn:
        results = conn.execute('''
            SELECT items.id, items.name, stores.name AS store, items.price
            FROM items
            JOIN stores ON items.store_id = stores.id
        ''').fetchall()

        return [dict(row) for row in results]
