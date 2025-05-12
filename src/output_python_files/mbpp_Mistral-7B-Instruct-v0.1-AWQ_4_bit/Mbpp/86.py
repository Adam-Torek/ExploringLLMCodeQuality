"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""

def centered_hexagonal_number(n):
    """
    :type n: int
    :rtype: int
    """
    n += 1
    return n*(n**2 + 1)/2


if __name__ == '__main__':
    assert centered_hexagonal_number(10) == 271