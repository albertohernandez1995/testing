# Write a Python program to count the ocurrences of each element given in a list.

list_elements = [1, 2, 4, 5, 3, 1, 2, 4, 1, 3, 2, 4, 3, 6]
dictionary = {}


def number_ocurrences(elements):
    for x in elements:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


# Thanks to this function, we convert each element in the list into a key and as a value it will
# give us the number of times it appears.

if __name__ == '__main__':
    print(number_ocurrences(list_elements))
