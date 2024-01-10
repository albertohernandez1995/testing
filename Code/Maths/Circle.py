# Implement a program that uses a Circle class to calculate the area and circumference
# of multiple circles
PI = 3.141592


class Circle:
    def __init__(self, radio):
        self.radio = radio

    @property
    def circle_area(self):
        return round(PI * self.radio ** 2, 3)
        # El numero 3 significa que lo redondeamos a 3 decimales el resultado
        # de la operacion

    @property
    def circle_circunference(self):
        return round(2*PI * self.radio, 3)