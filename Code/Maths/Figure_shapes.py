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

    def calculate_area(self):
        return PI * self.radio ** 2

    def calculate_perimeter(self):
        return (2 * PI) * self.radio


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return self.side * 4


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        return (self.base * self.height) / 2


if __name__ == '__main__':
    triangle = Triangle(base=5, height=2, side1=5, side2=6, side3=9)
    triangle_area = Triangle.calculate_area(triangle)
    print(triangle_area)
