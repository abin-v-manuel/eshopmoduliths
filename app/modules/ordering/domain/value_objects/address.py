class Address:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email_address: str,
        address_line: str,
        country: str,
        state: str,
        zip_code: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.address_line = address_line
        self.country = country
        self.state = state
        self.zip_code = zip_code 
