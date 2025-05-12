"""
Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
assert find_solution(2, 3, 7) == (2, 1)
"""

def find_solution(a, b, n):
    """
    :type a: int
    :type b: int
    :type n: int
    :rtype: Tuple[int, int]
    """
    if a == 0:
        return None
    x = n / b
    y = n % b
    if y == 0:
        return (x, 0)
    while y != 0:
        x = x - y // b
        y = y % b
    return (x, y)