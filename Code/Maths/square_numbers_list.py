# Implement a function that takes a list of numbers and returns a new list with the squared values.

lista_numeros = [2, 3, 4]


def squared_numbers(list):
    squared_list = []
    for x in list:
        squared_list.append(x ** 2)
    return squared_list


# With this function, we create a list with the squared values of a list of numbers.
if __name__ == '__main__':
    print(squared_numbers(lista_numeros))
