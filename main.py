import csv

class Item:
    # class attribute
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    # constructor
    def __init__(self,name: str, price: float, quantity = 0): 
        # Validations to recieved arguments
        assert price >= 0, f"Price {price} is not greater than  or equal to zero"
        assert quantity >= 0, f"Price {quantity} is not greater than  or equal to  zero"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) # converts to dict
            items = list(reader) # converts to list
        for item in items:
            # print(item)
            Item(
                name=item.get('name'), 
                price=int(item.get('price')), 
                quantity=int(item.get('quantity')), 
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# item1 = Item("Phone", 12000, 5)
# item2 = Item("Laptop",340000, 23)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)


Item.instantiate_from_csv()
print(Item.all)


# print(item1.total_price())
# print(item2.total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)

# print(Item.__dict__) #atrributes for class level
# print(item1.__dict__) #atrributes for instance level

# item1.apply_discount()
# print(item1.price)

# # diff discount rate
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)



