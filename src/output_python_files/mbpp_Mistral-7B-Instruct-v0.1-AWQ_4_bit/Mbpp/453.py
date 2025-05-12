"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""

def sumofFactors(n):
    """
    :param n: int
    :return: sum of even factors of n
    """
    if n < 2:
        return 0
    else:
        sum = 0
        for i in range(2, n+1):
            if n % i == 0:
                if i % 2 == 0:
                    sum += i
        return sum

assert sumofFactors(18) == 26