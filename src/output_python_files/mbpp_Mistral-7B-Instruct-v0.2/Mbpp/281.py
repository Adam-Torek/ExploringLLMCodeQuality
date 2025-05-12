"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
def all_unique(lst):
    """
    :param lst: list
    :return: bool
    """
    return len(lst) == len(set(lst))

# Test
assert all_unique([1,2,3]) == True
assert all_unique([1,2,3,3]) == False
assert all_unique([1,2,3,3,3]) == False
assert all_unique([]) == True
assert all_unique([1]) == True
assert all_unique([1,1]) == False