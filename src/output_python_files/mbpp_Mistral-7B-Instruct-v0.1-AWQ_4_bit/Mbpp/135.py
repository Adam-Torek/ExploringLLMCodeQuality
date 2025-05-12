"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""

def hexagonal_num(n):
    """
    :type n: int
    :rtype: int
    """
    n += 1
    return n*(n**2-1)/2


if __name__ == '__main__':
    assert hexagonal_num(10) == 190