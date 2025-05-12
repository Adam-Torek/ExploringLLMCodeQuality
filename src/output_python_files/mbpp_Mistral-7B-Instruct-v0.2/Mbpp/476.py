"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
def big_sum(arr):
    """
    Function to find the sum of the largest and smallest value in a given array.

    Args:
        arr: list of numbers

    Returns:
        int: sum of largest and smallest value in the array
    """
    if len(arr) == 0:
        raise ValueError("Array cannot be empty")

    smallest = min(arr)
    largest = max(arr)
    return largest + smallest

# Test the function
assert big_sum([1,2,3]) == 4
assert big_sum([-1,0,1]) == 0
assert big_sum([5,6,7]) == 11
assert big_sum([-5,-6,-7]) == -11
assert big_sum([]) == ValueError("Array cannot be empty")
assert big_sum([1]) == 1
assert big_sum([1,1,1]) == 2
assert big_sum([10,20,30]) == 50