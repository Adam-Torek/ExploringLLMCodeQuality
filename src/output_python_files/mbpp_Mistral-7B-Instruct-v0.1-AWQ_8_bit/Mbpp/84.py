"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""

def sequence(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(n-1) + sequence(n-2)

assert sequence(10) == 6