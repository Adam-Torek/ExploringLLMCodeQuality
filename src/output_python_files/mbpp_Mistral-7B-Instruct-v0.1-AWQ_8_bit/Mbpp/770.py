"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""

def odd_num_sum(n):
    """
    :param n: int
    :return: int
    """
    sum = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum += i**4
    return sum

assert odd_num_sum(2) == 82