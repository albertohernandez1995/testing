from pytest import mark

from Code.People_Strings.more_five_characters import more_five_characters

params = [(["Javier", "Papa", "Alberto", "Mama"], 2)]


@mark.parametrize("words, count", params)
def test_five_characters(words, count):
    result = more_five_characters(words)

    assert result == count
