# app/modules/catalog/application/commands/update_product.py

from app.modules.catalog.infrastructure.product_repository import ProductRepository

class UpdateProductCommand:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int, name: str, category: list[str], description: str, image_file: str, price: float):
        return self.repository.update(product_id, name, category, description, image_file, price)
