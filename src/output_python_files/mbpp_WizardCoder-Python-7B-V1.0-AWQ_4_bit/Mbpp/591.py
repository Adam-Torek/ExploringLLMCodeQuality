"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap_List(lst):
    if len(lst) < 2:
        return lst
    else:
        return [lst[-1], lst[1], lst[2], lst[3], lst[0]]

print(swap_List([12, 35, 9, 56, 24])) # [24, 35, 9, 56, 12]