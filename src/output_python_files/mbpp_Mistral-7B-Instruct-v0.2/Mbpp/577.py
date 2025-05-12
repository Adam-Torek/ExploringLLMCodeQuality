"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""
def last_digit_factorial(n):
    """
    This function calculates the last digit of the factorial of a given number.

    Parameters:
    n: An integer number.

    Returns:
    An integer number representing the last digit of the factorial of n.
    """
    if n == 0:
        return 0
    elif n % 2 == 0:
        return pow(5, n // 2) * (pow(10, n // 2) % 10)
    else:
        return pow(5, (n - 1) // 2) * pow(2, n // 2) % 10

assert last_digit_factorial(4) == 4
assert last_digit_factorial(5) == 5
assert last_digit_factorial(10) == 0
assert last_digit_factorial(15) == 5
assert last_digit_factorial(20) == 0