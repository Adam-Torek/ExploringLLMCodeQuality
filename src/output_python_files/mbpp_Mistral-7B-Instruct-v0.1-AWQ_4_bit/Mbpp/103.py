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
    if m == 1:
        return n
    else:
        return sum(eulerian_num(n, k) for k in range(1, m))