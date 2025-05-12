"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""

def all_unique(lst):
    """
    This function checks if all the elements of a given list are unique or not.
    """
    # Using set() to remove the duplicates from the list
    # If the length of the original list and the set(list) are same then all elements are unique
    return len(lst) == len(set(lst))