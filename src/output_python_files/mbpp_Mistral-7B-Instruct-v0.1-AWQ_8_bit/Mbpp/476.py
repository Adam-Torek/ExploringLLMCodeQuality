"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""

def big_sum(arr):
    """
    This function takes an array as an input and returns the sum of the largest and smallest value in the array.
    """
    if not arr:
        return 0
    else:
        return max(arr) + min(arr)

# Test the function
assert big_sum([1,2,3]) == 4