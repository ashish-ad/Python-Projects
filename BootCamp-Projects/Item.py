class Item:
    # Class Attribute
    pay_rate = 0.8 # the pay rate after 20% discount.
    all = []

    def __init__(self, name: str, price: float, quantity=0):
       
        # Run validation to received arguments
        assert price >=0, f"Price {price} is not greater than or equal to zero! "
        assert quantity >= 0, f"Qauntity {quantity} is not greater or equal to zero"
        assert type(name) == str, f"Passed value as {name} should be string not {type(name)}"

        # Assign to self object
        self.name = name
        self.price =  price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"( {self.__class__.__name__} ('{self.name}', {self.price},{self.quantity})"
