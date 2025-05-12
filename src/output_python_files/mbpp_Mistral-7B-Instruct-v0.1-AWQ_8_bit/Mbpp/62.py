"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest_num(lst):
    """
    This function takes a list of numbers as an input and returns the smallest number in the list.
    """
    # check if the list is empty
    if not lst:
        return None
    # sort the list in ascending order
    lst.sort()
    # return the smallest number
    return lst[0]

# test the function
assert smallest_num([10, 20, 1, 45, 99]) == 1