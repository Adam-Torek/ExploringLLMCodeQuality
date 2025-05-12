"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""

def next_Perfect_Square(n):
    """
    This function takes an integer as an input and returns the next perfect square greater than the given number.
    """
    sqrt = int(n ** 0.5)
    if sqrt * sqrt != n:
        sqrt += 1
    return sqrt * sqrt


# Testing the function
assert next_Perfect_Square(35) == 36