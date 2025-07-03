from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.dialects.postgresql import ARRAY
from app.shared.database.session import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(ARRAY(String))  # PostgreSQL array
    description = Column(Text)
    image_file = Column(String)
    price = Column(Float)
