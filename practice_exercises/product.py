class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return f"Total value of {self.name} in stock is ZAR {self.price * self.quantity}"
    


product1 = Product("Eggs", 5, 219)

print(product1.total_value())