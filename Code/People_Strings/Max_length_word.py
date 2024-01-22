# Given a list of words, find the word with the maximum length and its length.

list_words = ["frasco", "casco"]


def max_word_length(list):
    word = ""
    for x in list:
        if len(x) > len(word):
            word = x
    return word, len(word)


# We return the biggest word and its length.
if __name__ == '__main__':
    print(max_word_length(list_words))
