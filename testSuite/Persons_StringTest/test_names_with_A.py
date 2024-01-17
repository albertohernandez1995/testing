from pytest import mark
from Code.People_Strings.Names_with_A import names_with_a

param = [(["Javier", "Alberto", "Ana", "Luis"], ["Alberto", "Ana"])]


@mark.parametrize("list_names, only_A", param)
def test_names_with_A(list_names, only_A):
    result = names_with_a(list_names)

    assert result == only_A
