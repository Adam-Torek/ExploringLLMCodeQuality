"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""


def swap_List(list):
    list[0], list[-1] = list[-1], list[0]
    return list


print(swap_List([12, 35, 9, 56, 24]))