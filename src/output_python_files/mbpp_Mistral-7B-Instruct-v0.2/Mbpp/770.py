"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""
def odd_num_sum(n):
    """
    This function takes an integer n as an argument and returns the sum of the fourth power of the first n odd natural numbers.
    """
    sum = 0
    i = 1
    while i <= n:
        if i % 2 != 0:
            sum += i ** 4
        i += 1
    return sum

assert odd_num_sum(2) == 82</s>