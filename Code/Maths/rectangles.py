class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def surface(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * self.height + 2 * self.width
