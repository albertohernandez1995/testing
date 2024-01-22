from pytest import mark

from Code.Maths.square_numbers_list import squared_numbers

params = [([2, 3], [4, 9])]


@mark.parametrize("numbers, squared_values", params)
def test_squared_numbers(numbers, squared_values):
    values = squared_numbers(numbers)

    assert values == squared_values
