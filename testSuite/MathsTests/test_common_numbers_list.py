from pytest import mark
from Code.Maths.Common_numbers_list import common_numbers_list

params = [([2, 4, 5], [2, 6], [2])]


@mark.parametrize("list1, list2, reference", params)
def test_common_numbers(list1, list2, reference):
    result = common_numbers_list(list1, list2)

    assert result == reference
