class Item:
    # constructor
    def __init__(self,name: str, price: float, quantity = 0): 
        # Validations to recieved arguments
        assert price >= 0, f"Price {price} is not greater than  or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater than  or equal to  zero"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        
    def total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 12000, 5)
item2 = Item("Laptop",340000, 23)

print(item1.total_price())
print(item2.total_price())



