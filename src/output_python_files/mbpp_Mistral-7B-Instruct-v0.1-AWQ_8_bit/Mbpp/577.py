"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""

def last_Digit_Factorial(n):
    if n == 0:
        return 0
    else:
        return n % 10


if __name__ == "__main__":
    assert last_Digit_Factorial(4) == 4