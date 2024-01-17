# Create a class to represent a Car with attributes like make, model and year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def vehicle(self):
        return self.make, self.model, self.year
