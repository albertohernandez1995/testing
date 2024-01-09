# Implement a program that uses a Circle class to calculate the area and circumference
# of multiple circles
class Circle:
    def __init__(self, pi, radio):
        self.pi = pi
        self.radio = radio

    @property
    def circle_area(self):
        return self.pi * self.radio**2
