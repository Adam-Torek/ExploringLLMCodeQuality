"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""

def Find_Min_Length(lst):
    min_length = float('inf')
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
    return min_length

# Test the function
assert Find_Min_Length([[1],[1,2]]) == 1<|endoftext|>