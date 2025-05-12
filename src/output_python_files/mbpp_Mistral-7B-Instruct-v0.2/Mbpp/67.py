"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
from math import comb


def bell_number(n):
    """
    Bell number is the number of ways to partition a set into non-empty subsets.
    """
    return sum(comb(n, i) for i in range(1, n + 1))


if __name__ == "__main__":
    assert bell_number(2) == 2
    assert bell_number(3) == 5
    assert bell_number(4) == 15
    assert bell_number(5) == 28
    assert bell_number(10) == 220
    print("All tests passed!")