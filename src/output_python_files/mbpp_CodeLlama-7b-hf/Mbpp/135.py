"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""


def hexagonal_num(n):
    """
    Write a function to find the nth hexagonal number.
    assert hexagonal_num(10) == 190
    """
    return (n * (2 * n - 1)) // 2


if __name__ == "__main__":
    print(hexagonal_num(10))