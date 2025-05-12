"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""

def is_octagonal(n):
    """
    Check if a number is octagonal
    """
    if n % 8 != 0:
        return False
    if n == 0:
        return True
    if n % 2 == 0:
        return False
    if n % 4 == 0:
        return False
    return True

def nth_octagonal_number(n):
    """
    Find the nth octagonal number
    """
    if n % 8 != 0:
        raise ValueError("n must be a multiple of 8")
    if n == 0:
        return 0
    if n % 2 == 0:
        return (n // 2) * (3 * (n // 2) + 1)
    if n % 4 == 0:
        return (n // 4) * (7 * (n // 4) + 1)
    else:
        return (n - 1) * (3 * (n - 1) + 1)