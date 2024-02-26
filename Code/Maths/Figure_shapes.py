# Create a base class Shape with methods to calculate area and perimeter,
# and derive classes Circle and Square.

PI = 3.141592


# We define as parent class Shape, and then we create different subclasses with their respective methods.
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    @property
    def calculate_area(self):
        return PI * self.radio ** 2

    @property
    def calculate_perimeter(self):
        return (2 * PI) * self.radio


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def calculate_area(self):
        return self.side ** 2

    @property
    def calculate_perimeter(self):
        return self.side * 4


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class TriangleArea(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def calculate_area(self):
        return (self.base * self.height) / 2
