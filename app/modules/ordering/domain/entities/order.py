from typing import List, Optional
from app.modules.order.domain.value_objects.address import Address
from app.modules.order.domain.value_objects.payment import Payment
from app.modules.order.domain.entities.order_item import OrderItem

class Order:
    def __init__(
        self,
        id: int,
        customer_id: str,
        order_name: str,
        shipping_address: Address,
        billing_address: Address,
        payment: Payment,
        items: List[OrderItem]
    ):
        self.id = id
        self.customer_id = customer_id
        self.order_name = order_name
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.payment = payment
        self.items = items 
