from punq import Container
import redis

# Catalog Imports
from app.modules.catalog.infrastructure.product_repository import ProductRepository
from app.modules.catalog.application.commands.create_product import CreateProductCommand
from app.modules.catalog.application.commands.get_products import GetProductsCommand
from app.modules.catalog.application.commands.update_product import UpdateProductCommand
from app.modules.catalog.application.commands.delete_product import DeleteProductCommand

# Basket Imports
from app.modules.basket.infrastructure.repositories import BasketRepository
from app.modules.basket.application.commands.basket_commands import (
    CreateOrUpdateBasketCommand,
    GetBasketCommand,
    AddItemToBasketCommand,
    RemoveItemFromBasketCommand,
    DeleteBasketCommand,
)

_container = None

def get_container():
    global _container
    if _container is None:
        container = Container()

        #  Register Product services
        container.register(ProductRepository)
        container.register(CreateProductCommand)
        container.register(GetProductsCommand)
        container.register(UpdateProductCommand)
        container.register(DeleteProductCommand)

        redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
        container.register(redis.Redis, instance=redis_client)
        #  Register Basket services
        configure_services(container)

        _container = container

    return _container

def configure_services(container: Container):
    # Register the repository
    container.register(BasketRepository, BasketRepository)

    # Register all basket commands
    container.register(CreateOrUpdateBasketCommand, CreateOrUpdateBasketCommand)
    container.register(GetBasketCommand, GetBasketCommand)
    container.register(AddItemToBasketCommand, AddItemToBasketCommand)
    container.register(RemoveItemFromBasketCommand, RemoveItemFromBasketCommand)
    container.register(DeleteBasketCommand, DeleteBasketCommand)
