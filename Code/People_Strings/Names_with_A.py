# Given a list of names, print all names starting with an 'A'.

list_names = ["Javier", "Alberto", "Ana"]


def names_with_a(names):
    letter = "A"
    only_names_start_a = []
    for x in names:
        if letter == x[0]:
            only_names_start_a.append(x)
    return only_names_start_a


# x[0] marks the target of the exercise, which is returning the names that stars with the letter A.

if __name__ == '__main__':
    print(names_with_a(list_names))
