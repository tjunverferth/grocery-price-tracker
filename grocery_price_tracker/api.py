from fastapi import FastAPI, HTTPException
from grocery_price_tracker.database import initialize_database
from grocery_price_tracker.models.item import Item, ItemResponse
from grocery_price_tracker.models.store import Store
from grocery_price_tracker.services.item_service import add_item, get_cheapest_item, get_all_items
from grocery_price_tracker.services.store_service import get_store_by_name, add_store, get_all_stores

initialize_database()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "welcome to the grocery price tracker API"}


@app.post("/stores/")
def create_store(store: Store):
    """adds a new store to the database"""
    existing_store = get_store_by_name(store.name)
    if existing_store:
        raise HTTPException(status_code=400, detail="store already exists")

    store_id = add_store(store.name)
    return {"message": "store added successfully", "store_id": store_id}


@app.get("/stores/")
def list_stores():
    """returns a list of all stores"""
    stores = get_all_stores()
    return {"stores": stores}


@app.post("/items/")
def create_item(item: Item):
    """adds an item or updates price if it already exists"""
    add_item(item)
    return {"message": f"item '{item.name}' added/updated successfully"}


@app.get("/items/", response_model=list[ItemResponse])
def list_items():
    """returns all items in the database"""
    items = get_all_items()
    return items


@app.get("/items/{name}/cheapest", response_model=list[ItemResponse])
def get_cheapest(name: str):
    """returns all stores with the lowest price for an item"""
    cheapest_items = get_cheapest_item(name)

    if not cheapest_items:
        raise HTTPException(status_code=404, detail=f"no stores found for item '{name}'")

    return cheapest_items
