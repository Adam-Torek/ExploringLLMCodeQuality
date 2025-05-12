"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""
def last_digit(number):
    """
    This function takes an integer as an argument and returns the last digit of the number.
    """
    return number % 10

# Test the function
assert last_digit(123) == 3
assert last_digit(456) == 6
assert last_digit(1024) == 4
assert last_digit(0) == 0
assert last_digit(-123) == 3
assert last_digit(10000) == 0