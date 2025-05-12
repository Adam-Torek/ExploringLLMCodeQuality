"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    """
    :type n: int
    :rtype: int
    """
    if n<0:
        raise ValueError("n should be non-negative")
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum

#test
assert sum_digits(345)==12