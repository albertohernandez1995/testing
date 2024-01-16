# Implement a function that takes two list and return their union (all unique elements from both list).

list_1 = [2, 6, 4, 8, 5, 3, 9, 7, 6]

list_2 = [1, 8, 7, 2, 3, 9, 4, 0, 6]

unique_elements = []


def both_list(list1, list2):
    for x in list1:
        if x not in list2:
            unique_elements.append(x)
    for x in list2:
        if x not in list1:
            unique_elements.append(x)
    return unique_elements


# Thanks to this function, we find the unique elements of two lists
if __name__ == '__main__':
    print(both_list(list_1, list_2))
