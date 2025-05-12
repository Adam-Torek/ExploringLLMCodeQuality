"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""


def tetrahedral_number(n):
    """
    Write a function to find the nth tetrahedral number.
    assert tetrahedral_number(5) == 35
    """
    return n * (n + 1) * (2 * n + 1) // 6


if __name__ == "__main__":
    print(tetrahedral_number(5))
