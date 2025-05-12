"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
def find_sum(lst):
    """
    Function to find the sum of non-repeated elements in a given list
    :param lst: list
    :return: int
    """
    return sum(set(lst))

assert find_sum([1,2,3,1,1,4,5,6]) == 21