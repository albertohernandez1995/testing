# Create a class to represent a Student with attributes like name, age and grades:
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    @property
    def datos(self):
        return self.name, self.age, self.grade

