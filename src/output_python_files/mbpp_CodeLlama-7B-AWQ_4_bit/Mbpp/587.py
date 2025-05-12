"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""


def list_tuple(lst):
    return tuple(lst)


print(list_tuple([5, 10, 7, 4, 15, 3]))