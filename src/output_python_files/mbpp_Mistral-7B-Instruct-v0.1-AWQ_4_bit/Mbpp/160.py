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
        return (x, y)
    for i in range(1, y):
        if a * x + b * i == n:
            return (x, i)
    return None