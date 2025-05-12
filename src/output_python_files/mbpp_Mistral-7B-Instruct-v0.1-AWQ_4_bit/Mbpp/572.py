"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

def two_unique_nums(lst):
    """
    This function removes the duplicate numbers from a given list.
    """
    # Using set to remove the duplicates
    # If the element is present in set it will remove the element
    # If the element is not present in set it will add the element
    return list(set(lst))

# Testing the function
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]