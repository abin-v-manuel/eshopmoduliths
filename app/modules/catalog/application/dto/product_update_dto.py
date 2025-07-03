from pydantic import BaseModel
from typing import List, Optional

class ProductUpdateDTO(BaseModel):
    Name: Optional[str]
    Category: Optional[List[str]]
    Description: Optional[str]
    ImageFile: Optional[str]
    Price: Optional[float]
