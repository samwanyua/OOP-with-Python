class Item:
    # constructor
    def __init__(self,name, price, quantity): 
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_price(self, x, y):
        return x * y

item1 = Item("Phone", 12000,5)

print(item1.total_price(item1.price,item1.quantity ))

item2 = Item("Laptop",340000, 23)
print(item2.total_price(item2.price,item2.quantity ))



