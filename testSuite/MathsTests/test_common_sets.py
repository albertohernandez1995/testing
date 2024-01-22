from pytest import mark

from Code.Maths.Common_sets import set_common

params = [({2, 4}, {2, 3}, ([2]))]


@mark.parametrize("set1, set2, result", params)
def test_common_sets(set1, set2, result):
    common = set_common(set1, set2)

    assert common == result