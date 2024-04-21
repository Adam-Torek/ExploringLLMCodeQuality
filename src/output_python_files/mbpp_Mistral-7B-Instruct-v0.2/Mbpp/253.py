"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""
def count_integer(lst):
    """
    Function that returns the number of integer elements in a given list.

    Parameters:
    lst (list): The list to check for integer elements.

    Returns:
    int: The number of integer elements in the list.
    """
    return sum(1 for i in lst if isinstance(i, int))</s>