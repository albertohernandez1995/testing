# Create a program that generates the Fibonacci sequence up to a given numbers of terms.

def fibonacci(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)


# Here we define that if position is equal to 0 or 1, it will return one of those numbers.
# However, when entering the other numbers, it will return the position of a number in the Fibonacci sequence.
