# Given a list of words, count the number of words with more than five characters.

list_words = ["Javier", "Papa", "Alberto", "Mama"]


def more_five_characters(words):
    count = 0
    for x in words:
        if len(x) > 4:
            count += 1
    return count


# With this function, we can count the number of words that have 5 or more characters.

if __name__ == '__main__':
    print(more_five_characters(list_words))
