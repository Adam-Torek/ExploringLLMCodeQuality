"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    """
    Counts the number of True booleans in the given list.

    Parameters:
    lst (list): A list of boolean values.

    Returns:
    int: The number of True booleans in the list.
    """
    return sum(lst)

assert count([True, False, True]) == 2
assert count([False, False, False]) == 0
assert count([True, True, True]) == 3
assert count([False, True, False]) == 1</s>