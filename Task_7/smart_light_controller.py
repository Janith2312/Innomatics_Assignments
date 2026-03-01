class SmartLight:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"

    def show_status(self):
        print(self.name, "is", self.status)


light = SmartLight("Bedroom Light")
light.turn_on()
light.show_status()