from pytest import mark

from Code.Students.Car import Car

params_car = [("Lamborghini", "Murcielago", 2005), ("Lexus", "coupe_sport", 2021)]


@mark.parametrize("make, model, year", params_car)
def test_car(make, model, year,):
    obj = Car(make, model, year)

    assert obj
