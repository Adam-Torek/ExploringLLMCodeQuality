"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""

def sum_Of_product(n):
    """
    :param n: int
    :return: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum([(n choose k) * (n choose k-1) for k in range(1, n+1)])

assert sum_Of_product(3) == 15