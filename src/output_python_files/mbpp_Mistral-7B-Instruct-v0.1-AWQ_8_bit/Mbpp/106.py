"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(lst, tuples):
    """
    This function takes two arguments, a list and a tuple, and returns a tuple with the list appended to it.
    """
    new_tuple = tuple(lst + tuple)
    return new_tuple

# Test the function
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)