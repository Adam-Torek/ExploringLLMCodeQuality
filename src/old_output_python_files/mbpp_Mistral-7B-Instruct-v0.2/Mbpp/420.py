"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
def cube_sum(n):
    """
    This function computes the sum of cubes of first n even natural numbers.

    :param n: An integer representing the number of even natural numbers to be considered.
    :return: An integer representing the sum of cubes of first n even natural numbers.
    """
    sum = 0
    i = 0
    while i <= n:
        sum += (i**3)
        i += 2
    return sum

assert cube_sum(2) == 72