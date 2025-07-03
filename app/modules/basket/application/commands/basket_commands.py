from app.modules.basket.domain.entities import ShoppingCart, ShoppingCartItem
from app.modules.basket.infrastructure.repositories import BasketRepository


class CreateOrUpdateBasketCommand:
    def __init__(self, repo: BasketRepository):
        self.repo = repo

    def execute(self, cart: ShoppingCart):
        return self.repo.update_basket(cart)

class GetBasketCommand:
    def __init__(self, repo: BasketRepository):
        self.repo = repo

    def execute(self, username: str):
        return self.repo.get_basket(username)

class AddItemToBasketCommand:
    def __init__(self, repo: BasketRepository):
        self.repo = repo

    def execute(self, username: str, item: ShoppingCartItem):
        cart = self.repo.get_basket(username)
        cart.Items.append(item)
        return self.repo.update_basket(cart)

class RemoveItemFromBasketCommand:
    def __init__(self, repo: BasketRepository):
        self.repo = repo

    def execute(self, username: str, product_id):
        cart = self.repo.get_basket(username)
        cart.Items = [i for i in cart.Items if str(i.ProductId) != str(product_id)]
        return self.repo.update_basket(cart)

class DeleteBasketCommand:
    def __init__(self, repo: BasketRepository):
        self.repo = repo

    def execute(self, username: str):
        self.repo.delete_basket(username) 
