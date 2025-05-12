"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
from math import sqrt, floor


def centered_hexagonal_number(n):
    """
    :param n: int
    :return: int
    """
    side_length = 2 * (floor(sqrt(1 + 2 * sqrt(5)) / 2) * n)
    return int(side_length * (n // 2) + (side_length // 2) * (floor(sqrt(1 + 8 * sqrt(5)) / 4) * n))


if __name__ == "__main__":
    assert centered_hexagonal_number(10) == 271
    print("Test passed")