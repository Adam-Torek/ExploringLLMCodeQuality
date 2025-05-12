"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def amicable_numbers_sum(n):
    """
    :param n: int
    :return: int
    """
    amicable_numbers = []
    for i in range(1, n+1):
        if is_amicable(i):
            amicable_numbers.append(i)
    return sum(amicable_numbers)

def is_amicable(n):
    """
    :param n: int
    :return: bool
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True