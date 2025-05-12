"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""

def sum_in_range(l, r):
    """
    :param l: int
    :param r: int
    :return: int
    """
    if l % 2 == 0:
        l += 1
    if r % 2 == 0:
        r -= 1
    return sum(range(l, r + 1, 2))


# assert sum_in_range(2,5) == 8
# print(sum_in_range(2,5))