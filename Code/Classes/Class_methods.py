# Create a base class Animal with method sound() and create a derived classes Dog and Cat
# with their own sound().

class Animal:
    def __init__(self, animal):
        self.animal = animal
        self.sound = ""


@property
class Dog(Animal):
    def __init__(self, animal):
        super().__init__(animal)
        self.sound = "barks"


@property
class Cat(Animal):
    def __init__(self, animal):
        super().__init__(animal)
        self.sound = "meows"
