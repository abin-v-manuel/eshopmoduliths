import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Float
from app.shared.database.session import Base
from sqlalchemy import Integer

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
