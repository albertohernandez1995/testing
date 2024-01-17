from pytest import mark
from Code.Maths.Only_positive_numbers import sum_positive_numbers

params = [([-2, 5, 6], 11)]


@mark.parametrize("numbers, sum", params)
def test_only_positive_numbers(numbers, sum):
    result = sum_positive_numbers(numbers)

    assert result == sum
