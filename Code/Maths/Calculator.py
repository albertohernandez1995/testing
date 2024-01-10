# Create a class to represent a basic calculator with add, subtract, multiply and divide methods

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def addition(self):
        return self.a + self.b

    @property
    def subtraction(self):
        return self.a - self.b

    @property
    def multiplication(self):
        return self.a * self.b

    @property
    def division(self):
        return self.a // self.b

