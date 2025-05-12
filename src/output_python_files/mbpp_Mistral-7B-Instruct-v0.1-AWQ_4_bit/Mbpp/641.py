"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""

def is_nonagonal(n):
    """
    Check if a number is nonagonal.
    """
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 15 == 0:
        return False
    return True

def nth_nonagonal_number(n):
    """
    Find the nth nonagonal number.
    """
    if n % 3 == 0:
        return (n // 3) * (n // 3 + 1)
    if n % 5 == 0:
        return (n // 5) * (n // 5 + 1)
    if n % 15 == 0:
        return (n // 15) * (n // 15 + 1)
    else:
        return (n // 3) * (n // 3 + 1) + (n // 5) * (n // 5 + 1) + (n // 15) * (n // 15 + 1)

assert is_nonagonal(10) == True
assert nth_nonagonal_number(10) == 325