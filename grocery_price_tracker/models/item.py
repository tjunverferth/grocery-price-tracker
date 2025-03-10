from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    store: str


class ItemResponse(BaseModel):
    id: int
    name: str
    store: str
    price: float
