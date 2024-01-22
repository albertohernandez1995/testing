# Write a function that takes two list and return their intersection (common elements).

list_number_1 = [2, 4, 6, 8]
list_number_2 = [2, 4, 5, 7]
list_common = []


def common_numbers_list(list1, list2):
    for x in list1:
        if x in list2:
            list_common.append(x)
    return list_common


# With this function, we can create a list with the common elements of two given lists.
if __name__ == '__main__':
    print(common_numbers_list(list_number_1, list_number_2))
