from fastapi import APIRouter, HTTPException
from app.bootstrapper.startup import get_container
from app.modules.basket.application.commands.basket_commands import (
    GetBasketCommand,
    AddItemToBasketCommand,
    RemoveItemFromBasketCommand,
    DeleteBasketCommand,
    CreateOrUpdateBasketCommand,
)
from app.modules.basket.application.dto.basket_dto import (
    BasketRequest,
    BasketItemRequest,
)
from app.modules.basket.domain.entities import ShoppingCart

router = APIRouter(prefix="/basket")

@router.post("")
def create_or_update_basket(request: BasketRequest):
    basket = ShoppingCart(**request.dict())  # Converts DTO to domain entity
    container = get_container()
    handler = container.resolve(CreateOrUpdateBasketCommand)
    return handler.execute(basket)

@router.get("/{username}")
def get_basket(username: str):
    container = get_container()
    handler = container.resolve(GetBasketCommand)
    return handler.execute(username)

@router.post("/{username}/items")
def add_item(username: str, request: BasketItemRequest):
    item = request.ShoppingCartItem
    container = get_container()
    handler = container.resolve(AddItemToBasketCommand)
    return handler.execute(username, item)

@router.delete("/{username}/items/{product_id}")
def remove_item(username: str, product_id: int):
    container = get_container()
    handler = container.resolve(RemoveItemFromBasketCommand)
    return handler.execute(username, product_id)

@router.delete("/{username}")
def delete_basket(username: str):
    container = get_container()
    handler = container.resolve(DeleteBasketCommand)
    return handler.execute(username)
