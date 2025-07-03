from redis import Redis
import json
from app.modules.basket.domain.entities import ShoppingCart

class BasketRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_basket(self, username: str) -> ShoppingCart:
        data = self.redis.get(username)
        if data:
            return ShoppingCart.parse_raw(data)
        return ShoppingCart(UserName=username, Items=[])

    def update_basket(self, cart: ShoppingCart) -> ShoppingCart:
        self.redis.set(cart.UserName, cart.json())
        return cart

    def delete_basket(self, username: str):
        self.redis.delete(username)

