"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif m == 1:
        return 1
    else:
        return sum(eulerian_num(n - i, m - 1) for i in range(1, n + 1))