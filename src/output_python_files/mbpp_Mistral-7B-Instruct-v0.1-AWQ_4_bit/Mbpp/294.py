"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""

def max_val(lst):
    """
    This function takes a list as an input and returns the maximum value in it.
    """
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

# Test the function
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5