"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    """
    Returns the Eulerian number a(n, m) for the given values of n and m.
    """
    if n == 1:
        return m
    elif n == 2:
        return 2 * m - 1
    else:
        return eulerian_num(n - 1, m) + eulerian_num(n - 2, m)

# Test the function
assert eulerian_num(3, 1) == 4<|endoftext|>