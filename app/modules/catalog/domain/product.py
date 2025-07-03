from app.shared.base.entity import Entity

class Product(Entity):
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id)
        self.name = name
        self.price = price
