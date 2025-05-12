"""
Write a python function to find nth bell number.
assert bell_Number(2) == 2
"""

def bell_Number(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return sum(bell_Number(i) * bell_Number(n - i - 1) for i in range(1, n))