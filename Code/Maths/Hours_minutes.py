# Implement a program that converts a given number of minutes into hours.

def minutes_to_hours(number):
    hours = number // 60
    minutes = number % 60
    return f"hours: {hours} minutes: {minutes}"


# With this function, we can resolve the exercise.
if __name__ == '__main__':
    print(minutes_to_hours(639))
