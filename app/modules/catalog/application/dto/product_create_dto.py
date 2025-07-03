from pydantic import BaseModel
from typing import List

class ProductCreateDTO(BaseModel):
    Name: str
    Category: List[str]
    Description: str
    ImageFile: str
    Price: float

class ProductRequest(BaseModel):
    Product: ProductCreateDTO
