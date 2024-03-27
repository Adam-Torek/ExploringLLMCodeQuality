"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""
def first_digit(number):
    """
    This function takes an integer as an argument and returns the first digit of the number.
    """
    # Find the first digit by taking the absolute value and finding the remainder when divided by 10.
    return abs(number) % 10

# Test the function
assert first_digit(123) == 1
assert first_digit(-123) == 1
assert first_digit(0) == 0
assert first_digit(100) == 1</s>