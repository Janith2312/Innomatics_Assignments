class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display(self):
        print("Movie:", self.name)
        print("Rating:", self.rating, "/ 5")


m = Movie("Inception", 4.8)
m.display()