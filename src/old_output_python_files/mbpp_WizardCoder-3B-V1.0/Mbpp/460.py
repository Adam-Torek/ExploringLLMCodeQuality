"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""

def Extract(lst):
    return [sublist[0] for sublist in lst]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]])) # Output: [1, 3, 6]<|endoftext|>