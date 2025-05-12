"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""


def centered_hexagonal_number(n):
    """
    Write a function to find nth centered hexagonal number.
    assert centered_hexagonal_number(10) == 271
    """
    return (2 * n - 1) * (2 * n - 1)


if __name__ == "__main__":
    print(centered_hexagonal_number(10))
