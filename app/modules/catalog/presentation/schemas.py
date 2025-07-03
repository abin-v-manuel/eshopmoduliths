from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductRead(ProductCreate):
    id: int
    name: str
    price: float

    model_config = {
        "from_attributes": True}
