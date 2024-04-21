"""
Write a python function to check if the elements of a given list are unique or not.
assert all_unique([1,2,3]) == True
"""
def all_unique(lst):
    """
    Function to check if all elements in a given list are unique or not.

    Args:
        lst: List to check for unique elements.

    Returns:
        True if all elements in the list are unique, False otherwise.
    """
    if len(lst) == len(set(lst)):
        return True
    else:
        return False</s>