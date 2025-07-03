from fastapi import APIRouter
from app.bootstrapper.startup import get_container
from app.modules.catalog.application.commands.create_product import CreateProductCommand
from app.modules.catalog.application.commands.get_products import GetProductsCommand
from app.modules.catalog.application.commands.update_product import UpdateProductCommand
from app.modules.catalog.application.commands.delete_product import DeleteProductCommand
from app.modules.catalog.application.dto.product_create_dto import ProductRequest

router = APIRouter()  # Ensures URL is like /catalog/products

@router.post("/products")
def create_product(request: ProductRequest):
    product = request.Product
    container = get_container()
    handler = container.resolve(CreateProductCommand)
    return handler.execute(
        product.Name,
        product.Category,
        product.Description,
        product.ImageFile,
        product.Price
    )

@router.get("/products")
def get_products():
    container = get_container()
    handler = container.resolve(GetProductsCommand)
    return handler.execute()

@router.put("/products/{product_id}")
def update_product(product_id: int, request: ProductRequest):
    product = request.Product
    container = get_container()
    handler = container.resolve(UpdateProductCommand)
    return handler.execute(
        product_id,
        product.Name,
        product.Category,
        product.Description,
        product.ImageFile,
        product.Price
    )

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    container = get_container()
    handler = container.resolve(DeleteProductCommand)
    return handler.execute(product_id)
