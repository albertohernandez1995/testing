from pytest import mark

from Code.People_Strings.Max_length_word import max_word_length

params = [(["frasco", "casco"], ("frasco", 6))]


@mark.parametrize("list_words, word", params)
def test_max_length(list_words, word):
    result = max_word_length(list_words)

    assert result == word
