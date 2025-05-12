"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(lst):
    """
    This function takes a list as an input and returns the difference between the largest and smallest value in the list.
    """
    if len(lst) == 0:
        return 0
    else:
        return max(lst) - min(lst)

# Test the function
assert big_diff([1,2,3,4]) == 3
assert big_diff([-1,2,3,4]) == 5
assert big_diff([-1,2,3,4,5]) == 5
assert big_diff([]) == 0