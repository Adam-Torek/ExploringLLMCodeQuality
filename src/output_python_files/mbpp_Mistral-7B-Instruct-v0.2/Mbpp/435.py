"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""
def last_digit(n):
    """
    This function takes an integer as an argument and returns the last digit of the number.
    """
    return int(str(abs(n))[-1])

# Test the function
assert last_digit(123) == 3
assert last_digit(-123) == 3
assert last_digit(0) == 0
assert last_digit(1024) == 4
assert last_digit(10000) == 0</s>