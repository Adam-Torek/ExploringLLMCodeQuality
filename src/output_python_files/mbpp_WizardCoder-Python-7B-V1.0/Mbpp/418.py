"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(lst):
    max_len = 0
    max_elem = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_elem = i
    return max_elem

print(Find_Max([['A'],['A','B'],['A','B','C']]))