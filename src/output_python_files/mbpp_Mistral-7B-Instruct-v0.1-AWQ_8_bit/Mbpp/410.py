"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""

def min_val(lst):
    """
    This function takes a list as an input and returns the minimum value in it.
    """
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

# Test the function
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2