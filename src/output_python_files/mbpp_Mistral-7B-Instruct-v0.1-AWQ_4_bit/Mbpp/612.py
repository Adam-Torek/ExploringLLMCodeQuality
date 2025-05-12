"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""

def merge(lst):
    """
    Takes a list of lists and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
    """
    result = []
    for sublist in lst:
        result.append(sublist[0])
        result.append(sublist[1])
    return result