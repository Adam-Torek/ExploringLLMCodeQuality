"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
def next_Perfect_Square(n):
    """
    This function finds the next perfect square greater than a given number.
    :param n: The given number
    :return: The next perfect square greater than n
    """
    sqrt = int(n ** 0.5)
    if sqrt * sqrt == n:
        return n + 1
    else:
        return (sqrt + 1) ** 2

assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(25) == 26
assert next_Perfect_Square(16) == 25
assert next_Perfect_Square(1) == 4
assert next_Perfect_Square(0) == 1