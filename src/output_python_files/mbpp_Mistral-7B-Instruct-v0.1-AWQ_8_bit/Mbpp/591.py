"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap_List(lst):
    """
    This function takes a list as an input and returns the list with the first and last elements interchanged.
    """
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1] + lst[:-1]]