from app.modules.catalog.infrastructure.product_repository import ProductRepository

class CreateProductCommand:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name, category, description, image_file, price):
        return self.repository.create_product(name, category, description, image_file, price)