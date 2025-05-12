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
        return None
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    if n % 4 == 0:
        return 0
    if n % 6 == 0:
        return 0
    if n % 10 == 0:
        return 0
    if n % 12 == 0:
        return 0
    if n % 14 == 0:
        return 0
    if n % 16 == 0:
        return 0
    if n % 18 == 0:
        return 0
    if n % 20 == 0:
        return 0
    if n % 22 == 0:
        return 0
    if n % 24 == 0:
        return 0
    if n % 26 == 0:
        return 0
    if n % 28 == 0:
        return 0
    if n % 30 == 0:
        return 0
    if n % 32 == 0:
        return 0
    if n % 34 == 0:
        return 0
    if n % 36 == 0:
        return 0
    if n % 38 == 0:
        return 0
    if n % 40 == 0:
        return 0
    if n % 42 == 0:
        return 0
    if n % 44 == 0:
        return 0
    if n % 46 == 0:
        return 0
    if n % 48 == 0:
        return 0
    if n % 50 == 0:
        return 0
    if n % 52 == 0:
        return 0
    if n % 54 == 0:
        return 0
    if n % 56 == 0:
        return 0
    if n % 58 == 0:
        return 0
    if n % 60 == 0:
        return 0
    if n % 62 == 0:
        return 0
    if n % 64 == 0:
        return 0
    if n % 66 == 0:
        return 0
    if n % 68 == 0:
        return 0
    if n % 70 == 0:
        return 0
    if n % 72 == 0:
        return 0
    if n % 74 == 0:
        return 0
    if n % 76 == 0:
        return 0
    if n % 78 == 0:
        return 0
    if n % 80 == 0:
        return 0
    if n % 82 == 0:
        return 0
    if n % 84 == 0:
        return 0
    if n % 86 == 0:
        return 0
    if n % 88 == 0:
        return 0
    if n % 90 == 0:
        return 0
    if n % 92 == 0:
        return 0
    if n % 94 == 0:
        return 0
    if n % 96 == 0:
        return 0
    if n % 98 == 0:
        return 0
    if n % 100 == 0:
        return 0
    if n % 102 == 0:
        return 0
    if