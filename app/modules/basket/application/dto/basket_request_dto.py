from pydantic import BaseModel
from typing import List
from uuid import UUID

class ShoppingCartItemDTO(BaseModel):
    ProductId: UUID
    ProductName: str
    Quantity: int
    Color: str
    Price: float

class ShoppingCartDTO(BaseModel):
    UserName: str
    Items: List[ShoppingCartItemDTO]

class BasketCheckoutDTO(BaseModel):
    userName: str
    CustomerId: UUID
    totalPrice: float
    firstName: str
    lastName: str
    emailAddress: str
    addressLine: str
    country: str
    state: str
    zipCode: str
    cardName: str
    cardNumber: str
    expiration: str
    cvv: str
    paymentMethod: int 
