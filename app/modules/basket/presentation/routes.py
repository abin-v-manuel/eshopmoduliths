 
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_basket():
    return {"message": "Basket module is alive"}