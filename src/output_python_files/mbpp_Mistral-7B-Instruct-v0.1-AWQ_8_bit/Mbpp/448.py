"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def cal_sum(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    else:
        return n + cal_sum(n-1) + cal_sum(n-2)

assert cal_sum(9) == 49