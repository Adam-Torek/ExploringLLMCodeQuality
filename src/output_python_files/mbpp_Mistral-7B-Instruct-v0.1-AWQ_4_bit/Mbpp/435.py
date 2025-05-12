"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""

def last_digit(n):
    """
    This function takes an integer as an input and returns the last digit of the number.
    """
    # Get the last digit of the number
    last_digit = n % 10
    # Return the last digit
    return last_digit