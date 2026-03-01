class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_tag(self):
        print("Product:", self.name)
        print("Price: ₹" + str(self.price))


p = Product("Headphones", 2499)
p.price_tag()