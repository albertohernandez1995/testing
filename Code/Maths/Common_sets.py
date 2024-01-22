# Write a program that checks if two sets have any elements in common.

set_1 = {2, 4}
set_2 = {2, 3}


def set_common(element1, element2):
    common = []
    for x in element1:
        if x in element2:
            common.append(x)
    return common


if __name__ == '__main__':
    print(set_common(set_1, set_2))
