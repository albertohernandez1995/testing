# Create a loop that prints all prime numbers between 1 and 50.

def is_primo(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


# With this function, we check if a number is prime or not.

def prime_numbers(start, end):
    list_prime_numbers = []
    for x in range(start, end):
        if is_primo(x):
            list_prime_numbers.append(x)
    return list_prime_numbers


# With this function, we get the prime numbers included in the range between two numbers
if __name__ == '__main__':
    print(prime_numbers(2, 50))
