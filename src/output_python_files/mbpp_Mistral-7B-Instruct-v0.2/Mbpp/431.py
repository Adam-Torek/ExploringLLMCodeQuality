"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""
def common_element(list1, list2):
    """
    :param list1: list
    :param list2: list
    :return: bool
    """
    return bool(set(list1) & set(list2))

assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
assert common_element([1,2,3,4,5], [1,2,3,4,6])==True
assert common_element([1,2,3,4,5], [1,2,3,4,7])==False