"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""

def last_Digit_Factorial(n):
    """
    This function calculates the factorial of a given number and returns the last digit.
    """
    if n == 0:
        return 0
    else:
        result = n * last_Digit_Factorial(n-1)
        return result % 10

assert last_Digit_Factorial(4) == 4