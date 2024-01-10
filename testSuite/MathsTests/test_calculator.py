from pytest import mark

from Code.Maths.Calculator import Calculator

params_addition = [(8, 3, 11), (5, 6, 11)]

params_subtraction = [(5, 6, -1), (9, 3, 6), (1, 8, -7)]

params_multiplication = [(-5, -5, 25), (3, 3, 9)]

params_division = [(-9, -9, 1), (8, 4, 2)]


@mark.parametrize("a, b, reference", params_addition)
def test_addition(a, b, reference):
    obj = Calculator(a, b)

    assert obj.addition == reference


@mark.parametrize("a, b, reference", params_subtraction)
def test_subtraction(a, b, reference):
    obj = Calculator(a, b)

    assert obj.subtraction == reference


@mark.parametrize("a, b, reference", params_multiplication)
def test_multiplication(a, b, reference):
    obj = Calculator(a, b)

    assert obj.multiplication == reference


@mark.parametrize("a, b, reference", params_division)
def test_division(a, b, reference):
    obj = Calculator(a, b)

    assert obj.division == reference
