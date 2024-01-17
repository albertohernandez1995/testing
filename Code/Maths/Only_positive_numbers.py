# Given a list of numbers, create a function to find the sum of all positive numbers.

list_numbers = [-2, -1, 3, 6]


def sum_positive_numbers(numbers):
    list_positive_numbers = []
    for x in numbers:
        if x >= 0:
            list_positive_numbers.append(x)
    return sum(list_positive_numbers)


if __name__ == '__main__':
    print(sum_positive_numbers(list_numbers))
