# Write a program that finds the largest and smallest elements of a list.

string = ["Alberto", "Ana", "Javier"]


def large_and_smallest_element(elements):
    smallest = ""
    largest = ""
    for x in elements:
        if len(x) > len(largest):
            largest = x
        if smallest == len(x):
            smallest = x

    return smallest, largest


if __name__ == '__main__':
    print(large_and_smallest_element(string))
