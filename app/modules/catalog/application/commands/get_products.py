# app/modules/catalog/application/commands/get_products.py

from app.modules.catalog.infrastructure.product_repository import ProductRepository

class GetProductsCommand:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()
