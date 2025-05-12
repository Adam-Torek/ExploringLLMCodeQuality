"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""
def Extract(lst):
    """
    Returns a new list containing the first element of each sublist in the input list.
    """
    return [sublist[0] for sublist in lst]

# Test the function
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]