# Create a function to count the number of vowels in a given string.

string_one = "ajheskpai"


def number_vowels(string):
    count = 0
    for x in string:
        if x == "a" or "e" or "i" or "o" or "u":
            count += 1
    return count


# Thanks to the counter, we can know how many vowels are in a given string.

if __name__ == '__main__':
    print(number_vowels(string_one))
