"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""

def Find_Min(lst):
    min_len = float('inf')
    min_sublist = []
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist

print(Find_Min([[1],[1,2],[1,2,3]])) # Output: [1]<|endoftext|>