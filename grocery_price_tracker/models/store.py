from pydantic import BaseModel


class Store(BaseModel):
    name: str
