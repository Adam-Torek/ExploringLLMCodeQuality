"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(lst):
    """
    This function takes a list as an input and returns the negative numbers in the list.
    """
    neg_nums = []
    for num in lst:
        if num < 0:
            neg_nums.append(num)
    return neg_nums

# Test the function
assert neg_nos([-1,4,5,-6]) == [-1,-6]