from pytest import mark
from Code.People_Strings.vowels import number_vowels

params = [("ajikoa", 4)]


@mark.parametrize("string, reference,", params)
def test_vowles(string, reference):
    count = number_vowels(string)

    assert count == reference
