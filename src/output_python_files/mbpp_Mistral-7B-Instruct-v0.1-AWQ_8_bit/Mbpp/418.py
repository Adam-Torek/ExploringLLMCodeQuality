"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""

def Find_Max(lst):
    """
    Function to find the element of a list having maximum length.
    """
    max_len = len(lst[0])
    max_elem = lst[0]
    for elem in lst:
        if len(elem) > max_len:
            max_len = len(elem)
            max_elem = elem
    return max_elem

# Test the function
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']