"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""
def sum_in_range(l, r):
    """
    Function to find the sum of all odd natural numbers within the range l and r
    :param l: int, lower limit of the range
    :param r: int, upper limit of the range
    :return: int, sum of all odd natural numbers within the range l and r
    """
    sum = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            sum += i
    return sum

assert sum_in_range(2,5) == 8</s>