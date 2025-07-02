from app.modules.catalog.domain.product import Product
from app.modules.catalog.infrastructure.product_repository import ProductRepository
from app.shared.result import Result
import uuid

def create_product(name: str, price: float) -> Result:
    new_product = Product(str(uuid.uuid4()), name, price)
    repo = ProductRepository()
    repo.add(new_product)
    return Result.ok(new_product)
