"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""


def swap_List(lst):
    return lst[1:len(lst)-1] + lst[0:1] + lst[2:]

# Test the function
print(swap_List([12, 35, 9, 56, 24]))<|endoftext|>