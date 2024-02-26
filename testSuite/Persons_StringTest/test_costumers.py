from pathlib import Path

from pytest import mark

from Code.People_Strings.Customer import Customers

import json

pytestmark = mark.input_path(Path(__file__).parent / "data")


def test_customers(input_path):
    data_file = input_path / 'costumers.json'

    list_customers = Customers.from_json(data_file)
    customer_1, customer_2 = tuple(list_customers)
    assert customer_1.name == "Alberto"
    assert customer_1.firstname == "Hernandez"
    assert customer_1.amount == 369

    assert customer_2.name == "Javier"
    assert customer_2.firstname == "Hernandez"
    assert customer_2.amount == 258
