from fastapi import FastAPI, HTTPException
from grocery_price_tracker.database import initialize_database
from grocery_price_tracker.models.item import Item
from grocery_price_tracker.services.item_service import add_item, get_cheapest_item, get_all_items

initialize_database()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "welcome to the grocery price tracker API"}


@app.post("/items/")
def create_item(item: Item):
    """adds an item or updates price if it already exists"""
    add_item(item)
    return {"message": f"item '{item.name}' added/updated successfully"}


@app.get("/items/", response_model=list[Item])
def list_items():
    """returns all items in the database"""
    items = get_all_items()
    return items


@app.get("/items/{name}", response_model=Item)
def get_cheapest(name: str):
    """finds the cheapest price for an item"""
    item = get_cheapest_item(name)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    return item
