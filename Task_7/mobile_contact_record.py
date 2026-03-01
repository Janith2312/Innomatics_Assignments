class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print("Contact Saved")
        print("Name:", self.name)
        print("Phone:", self.phone)


c = Contact("Anita", "9876543210")
c.show()