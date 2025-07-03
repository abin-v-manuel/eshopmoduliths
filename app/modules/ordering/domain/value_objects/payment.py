class Payment:
    def __init__(
        self,
        card_name: str,
        card_number: str,
        expiration: str,
        cvv: str,
        payment_method: int,
    ):
        self.card_name = card_name
        self.card_number = card_number
        self.expiration = expiration
        self.cvv = cvv
        self.payment_method = payment_method 
