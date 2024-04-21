"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
def zero_count(arr):
    """
    :param arr: list of integers
    :return: float, ratio of zeroes to non-zeroes
    """
    zero_count = sum(1 for i in arr if i == 0)
    non_zero_count = len(arr) - zero_count
    return zero_count / non_zero_count

# Test the function
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)</s>