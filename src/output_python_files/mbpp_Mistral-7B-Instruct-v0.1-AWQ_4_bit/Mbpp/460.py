"""
Write a python function to get the first element of each sublist.
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
"""

def Extract(lst):
    """
    :param lst: list of lists
    :return: list of first elements of sublists
    """
    result = []
    for sublist in lst:
        result.append(sublist[0])
    return result