"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""


def Extract(L):
    return [i[0] for i in L]


print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))
