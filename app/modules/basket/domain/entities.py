from typing import List
from uuid import UUID
from pydantic import BaseModel

class ShoppingCartItem(BaseModel):
    ProductId: int
    ProductName: str
    Quantity: int
    Color: str
    Price: float

class ShoppingCart(BaseModel):
    UserName: str
    Items: List[ShoppingCartItem] = []

    def total_price(self):
        return sum(item.Price * item.Quantity for item in self.Items)
 
