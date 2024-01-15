# Implement a program that uses a Circle class to calculate the area and circumference
# of multiple circles
PI = 3.141592


# We define PI, so we can use it in the different operations.

class Circle:
    def __init__(self, radio):
        self.radio = radio

    #
    @property
    def circle_area(self):
        return round(PI * self.radio ** 2, 3)
        # Number 3 means that we round the result to 3 decimal places of the operation

    @property
    def circle_circunference(self):
        return round(2 * PI * self.radio, 3)
