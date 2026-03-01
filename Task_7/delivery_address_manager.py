class Delivery:
    def __init__(self, customer, address):
        self.customer = customer
        self.address = address

    def show(self):
        print("Delivery Details")
        print("Customer:", self.customer)
        print("Address:", self.address)


d = Delivery("Suman", "Hyderabad")
d.show()