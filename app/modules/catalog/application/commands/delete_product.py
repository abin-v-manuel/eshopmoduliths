
from app.modules.catalog.infrastructure.product_repository import ProductRepository

class DeleteProductCommand:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int):
        return self.repository.delete(product_id)
