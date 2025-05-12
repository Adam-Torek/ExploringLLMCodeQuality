"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""

def square_sum(n):
    """
    :type n: int
    :rtype: int
    """
    sum = 0
    for i in range(2, n+1):
        sum += i**2
    return sum

assert square_sum(2) == 20