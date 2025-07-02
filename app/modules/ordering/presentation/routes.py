
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_ordering():
    return {"message": "Ordering module is alive"}
