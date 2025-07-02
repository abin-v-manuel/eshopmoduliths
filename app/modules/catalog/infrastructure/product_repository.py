from app.shared.database.session import SessionLocal
from app.modules.catalog.infrastructure.models import ProductModel

class ProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, name: str, price: float) -> ProductModel:
        product = ProductModel(name=name, price=price)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all(self):
        return self.db.query(ProductModel).all()

    def get_by_id(self, product_id: int):
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

    def update(self, product_id: int, name: str, price: float):
        product = self.get_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            self.db.commit()
            self.db.refresh(product)
        return product

    def delete(self, product_id: int):
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
        return product

# class ProductRepository:
#     def create(self, name: str, price: float):
#         db = SessionLocal()
#         try:
#             product = ProductModel(name=name, price=price)
#             db.add(product)
#             db.commit()
#             db.refresh(product)
#             return product
#         except Exception as e:
#             db.rollback()
#             print("Error:", e)
#             raise e
#         finally:
#             db.close()