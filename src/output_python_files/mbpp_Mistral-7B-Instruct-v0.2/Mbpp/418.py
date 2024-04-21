"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(lst):
    max_len = 0
    max_elem = None
    for elem in lst:
        len_elem = len(elem)
        if len_elem > max_len:
            max_len = len_elem
            max_elem = elem
    return max_elem

# Test case
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']</s>