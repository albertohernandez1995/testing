class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def surface(self):
        return self.height * self.width
