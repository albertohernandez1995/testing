# Create a function to count the number of vowels in a given string.

string_one = "ajheskpai"


def number_vowels(string):
    count = 0
    for x in string:
        if x == "a":
            count += 1
        if x == "e":
            count += 1
        if x == "i":
            count += 1
        if x == "o":
            count += 1
        if x == "u":
            count += 1
    return count


# Thanks to the counter, we can know how many vowels are in a given string.

if __name__ == '__main__':
    print(number_vowels(string_one))
