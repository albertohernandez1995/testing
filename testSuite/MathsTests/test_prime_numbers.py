from pytest import mark

from Code.Maths.prime_numbers import is_primo, prime_numbers

params_is_primo = [(2, True)]

params_prime_numbers = [(2, 10, [2, 3, 5, 7])]


@mark.parametrize("number, reference", params_is_primo)
def test_is_primo(number, reference):
    result = is_primo(number)

    assert result == reference


@mark.parametrize("number1, number2, reference", params_prime_numbers)
def test_prime_numbers(number1, number2, reference):
    result = prime_numbers(number1, number2)

    assert result == reference
