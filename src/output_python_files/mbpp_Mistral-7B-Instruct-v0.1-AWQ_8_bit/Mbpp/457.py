"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""

def Find_Min(lst):
    """
    :param lst: list of lists
    :return: sublist with minimum length
    """
    if len(lst) == 0:
        return []
    else:
        min_len = len(lst[0])
        for i in range(1,len(lst)):
            if len(lst[i]) < min_len:
                min_len = len(lst[i])
                min_sublist = lst[i]
        return min_sublist