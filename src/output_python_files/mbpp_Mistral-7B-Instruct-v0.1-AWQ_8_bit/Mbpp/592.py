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
        return sum([(n-i)*(n-i-1) for i in range(1,n)])

assert sum_Of_product(3) == 15