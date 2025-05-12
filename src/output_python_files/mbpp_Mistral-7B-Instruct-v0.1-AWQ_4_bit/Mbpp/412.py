"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(lst):
    """
    This function removes odd numbers from a given list.
    """
    return [num for num in lst if num % 2 == 0]

# Test the function
assert remove_odd([1,2,3]) == [2]