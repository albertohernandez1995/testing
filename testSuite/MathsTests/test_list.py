from pytest import mark

from Code.Maths.List import number_ocurrences

from Code.Maths.Two_list_exercise import both_list


params_number_of_appearences = [
    ([1, 2, 2, 4], {1: 1, 2: 2, 4: 1})
]

params_two_list = [
    ([1, 2, 3], [1, 4, 5], [2, 3, 4, 5])
]


@mark.parametrize("numbers, reference", params_number_of_appearences)  # Test exercise "list".
def test_list(numbers, reference):
    classification = number_ocurrences(numbers)

    assert classification == reference


@mark.parametrize("list_1, list_2, reference", params_two_list)  # Test exercise "two list --> unique elements"
def test_two_list_in_one(list_1, list_2, reference):
    result = both_list(list_1, list_2)

    assert result == reference
