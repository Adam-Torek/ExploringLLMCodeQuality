"""
Write a function to find the nth tetrahedral number.
assert tetrahedral_number(5) == 35
"""

def tetrahedral_number(n):
    """
    :type n: int
    :rtype: int
    """
    n += 1
    return n*(n-1)/2 + 1

assert tetrahedral_number(5) == 35