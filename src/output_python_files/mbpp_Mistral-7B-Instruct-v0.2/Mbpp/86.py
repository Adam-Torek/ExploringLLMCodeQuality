"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
from math import sqrt, pi

def centered_hexagonal_number(n):
    """
    :param n: int
    :return: int
    """
    side_length = 2 * (3 * sqrt(3) + 2) * (n - 1)
    return int(side_length ** 2 / 2 + n / 2 * (3 * sqrt(3) + 1))

if __name__ == "__main__":
    assert centered_hexagonal_number(10) == 271
    print(centered_hexagonal_number(10))