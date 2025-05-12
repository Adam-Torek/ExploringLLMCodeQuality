"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""


def merge(lst):
    return [list(zip(*lst))[0], list(zip(*lst))[1]]


print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]))