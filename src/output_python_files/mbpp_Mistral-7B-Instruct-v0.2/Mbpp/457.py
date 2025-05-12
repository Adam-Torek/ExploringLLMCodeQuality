"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(lst):
    """
    This function finds the sublist having minimum length in the given list.
    :param lst: list of lists
    :return: list having minimum length
    """
    if not lst:
        return []
    min_len = len(lst[0])
    min_sublist = lst[0]
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist

if __name__ == "__main__":
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,2],[1,2,3],[1,2,3,4]]) == [1, 2]
    assert Find_Min([]) == []
    assert Find_Min([[1,2,3],[4,5,6],[7,8,9]]) == [1, 2, 3]
    assert Find_Min([[1],[1,2],[1,2,3],[1,2,3,4]]) == [1]
    assert Find_Min([[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]) == [1, 2]
    assert Find_Min([[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6]]) == [1]