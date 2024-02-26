# Given a json file with costumer data, create a Customer class to store
# and manipulate the data
import json


class Customers:
    def __init__(self, name, firstname, amount):
        self.name = name
        self.firstname = firstname
        self.amount = amount

    @classmethod
    def from_json(cls, filename):  # cls is the reference of the class
        with open(filename, "r") as f:
            content = json.load(f)
        objects = []
        for x in content.values():
            for y in x:
                y = {k.lower(): v for k, v in y.items()}
                objects.append(cls(**y))
        return objects
