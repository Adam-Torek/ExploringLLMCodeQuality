"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""
def frequency(lst, num):
    """
    :param lst: list
    :param num: int
    :return: int
    """
    return sum(1 for i in lst if i == num)

# Test
assert frequency([1,2,3], 4) == 0
assert frequency([1,2,3,3,3], 3) == 3
assert frequency([], 1) == 0
assert frequency([1], 1) == 1
assert frequency([1,1,1,1], 1) == 4