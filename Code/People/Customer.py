# Given a json file with costumer data, create a Customer class to store
# and manipulate the data

import json

data = {}
data["Costumers"] = []
data["Costumers"].append({"Name": "Alberto", "Firstname": "Hernandez", "Amount": 369})
data["Costumers"].append({"Name": "Javier", "Firstname": "Hernandez", "Amount": 258})

with open("../../testSuite/PersonsTest/data/costumers.json", "w") as f:
    json.dump(data, f, indent=4)


class Customers:
    def __init__(self, name, firstname, amount):
        self.name = name
        self.firstname = firstname
        self.amount = amount

    @classmethod
    def from_json(cls, filename):  # cls es la referencia a la clase
        with open(filename, "r") as f:
            content = json.load(f)
        objects = []
        for x in content:
            x = {k.lower(): v for k, v in x.items()}
            objects.append(cls(**x))
        return objects
