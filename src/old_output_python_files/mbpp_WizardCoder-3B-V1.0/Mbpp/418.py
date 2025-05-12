"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""

def Find_Max(lst):
    max_len = 0
    max_elem = []
    for elem in lst:
        if len(elem) > max_len:
            max_len = len(elem)
            max_elem = elem
    return max_elem

# Test the function
print(Find_Max([['A'],['A','B'],['A','B','C']])) # Output: ['A','B','C']<|endoftext|>