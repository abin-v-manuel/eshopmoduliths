from fastapi import APIRouter, HTTPException
from app.modules.catalog.infrastructure.product_repository import ProductRepository
from app.modules.catalog.presentation.schemas import ProductCreate, ProductRead

router = APIRouter()
repo = ProductRepository()

@router.post("/", response_model=ProductRead)
def create_product(product: ProductCreate):
    return repo.create(product.name, product.price)

@router.get("/", response_model=list[ProductRead])
def get_products():
    return repo.get_all()

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int):
    product = repo.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, product: ProductCreate):
    updated = repo.update(product_id, product.name, product.price)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}")
def delete_product(product_id: int):
    deleted = repo.delete(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}
