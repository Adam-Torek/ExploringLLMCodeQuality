"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(lst):
    """
    This function takes a list of numbers as an input and returns the second smallest number in the list.
    """
    # sort the list in ascending order
    lst.sort()
    # return the second element in the list
    return lst[1]

# test the function
assert second_smallest([1, 2, -8, -2, 0, -2])==-2