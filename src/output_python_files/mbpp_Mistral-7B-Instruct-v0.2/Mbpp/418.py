"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(lst):
    max_len = len(lst[0]) if len(lst) > 0 else 0
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_elem = i
    return max_elem

# Test case
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']