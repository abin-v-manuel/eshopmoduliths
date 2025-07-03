# app/modules/catalog/infrastructure/product_repository.py

from app.shared.database.session import SessionLocal
from app.modules.catalog.infrastructure.models import ProductModel

class ProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_product(self, name, category, description, image_file, price):
        product = ProductModel(
            name=name,
            category=category,
            description=description,
            image_file=image_file,
            price=price
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product


    def get_all(self):
        return self.db.query(ProductModel).all()
    
    def update(self, product_id, name, category, description, image_file, price):
        product = self.db.query(ProductModel).get(product_id)
        if product:
            product.name = name
            product.category = category
            product.description = description
            product.image_file = image_file
            product.price = price
            self.db.commit()
            self.db.refresh(product)
            return product
        return None

    def delete(self, product_id):
        product = self.db.query(ProductModel).get(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return {"message": "Product deleted"}
        return {"error": "Product not found"}