"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_digit_factorial(n):
    """
    This function calculates the last digit of the factorial of a given number.
    :param n: The number whose factorial last digit is to be found.
    :return: The last digit of the factorial of the given number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (last_digit_factorial(n-1) * n) % 10

assert last_digit_factorial(4) == 4