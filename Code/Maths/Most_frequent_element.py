# Write a program thar finds the most frequent element in a list.
numbers = [1, 1, 2, 1, 2, 3]
dictionary = {}


def most_frequent(elements):
    for x in elements:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary.values()


if __name__ == '__main__':
    print(most_frequent(numbers))
