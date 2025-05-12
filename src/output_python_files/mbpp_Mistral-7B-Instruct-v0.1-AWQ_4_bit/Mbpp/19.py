"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""

def test_duplicate(arr):
    """
    :param arr: array of integers
    :return: True if array contains any duplicate element, False otherwise
    """
    # create a set of integers from array
    set_arr = set(arr)
    # check if length of set is equal to length of array
    if len(set_arr) != len(arr):
        return True
    else:
        return False

# test cases
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4,5,6,7,8,9,10]))
print(test_duplicate([1,2,3,4,5,6,7,8,9,10,11]))