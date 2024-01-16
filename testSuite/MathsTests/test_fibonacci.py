from pytest import mark

from Code.Maths.Fibonacci import fibonacci

params_correct = [(3, 2)]

params_error = [("", 2)]


@mark.parametrize("position, reference", params_correct)
def test_fibonacci(position, reference):
    result = fibonacci(position)

    assert result == reference
