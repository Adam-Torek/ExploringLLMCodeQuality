"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""

def test_duplicate(arr):
    """
    Test function to check whether the array contains any duplicate element
    """
    if len(set(arr)) != len(arr):
        return True
    else:
        return False


def find_duplicate(arr):
    """
    Function to find whether a given array of integers contains any duplicate element
    """
    if test_duplicate(arr):
        return True
    else:
        return False