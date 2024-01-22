# Write a Python program to count the ocurrences of each element in a given list.

list_elements = ["Hola", "te", "te"]
dictionary = {}


def count_ocurrences(elements):
    for x in elements:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


if __name__ == '__main__':
    print(count_ocurrences(list_elements))
