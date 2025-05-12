"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""

def Find_Min_Length(lst):
    """
    This function takes a list of lists as an input and returns the length of the smallest list in the list.
    """
    if not lst:
        return 0
    else:
        return min(len(x) for x in lst)