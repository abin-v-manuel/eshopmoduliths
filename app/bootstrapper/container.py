from punq import Container
import redis
from app.modules.basket.infrastructure.repositories import BasketRepository
from app.modules.basket.application.commands.basket_commands import *

container = Container()

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
repo = BasketRepository(r)

container.register(BasketRepository, instance=repo)
container.register(GetBasketCommand, BasketRepository)
container.register(AddItemToBasketCommand, BasketRepository)
container.register(RemoveItemFromBasketCommand, BasketRepository)
container.register(DeleteBasketCommand, BasketRepository)
