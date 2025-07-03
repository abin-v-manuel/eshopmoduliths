from pydantic import BaseModel
from typing import List

class BasketItemRequest(BaseModel):
    ProductId: int #check uuid whenever
    Quantity: int
    Color: str
    Price: float
    ProductName: str

class BasketRequest(BaseModel):
    UserName: str
    Items: List[BasketItemRequest]
