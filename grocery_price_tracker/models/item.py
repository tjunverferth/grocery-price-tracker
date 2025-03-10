from datetime import datetime

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
    date_added: datetime


class PriceHistoryResponse(BaseModel):
    item_id: int
    name: str
    store: str
    old_price: float
    new_price: float
    change_date: datetime
