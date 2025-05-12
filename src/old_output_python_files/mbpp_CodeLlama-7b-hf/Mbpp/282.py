"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(list1, list2):
    """
    Subtracts two lists element-wise.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length.")
    else:
        return [list1[i] - list2[i] for i in range(len(list1))]


def test_sub_list():
    assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [-3, -3, -3]
    assert sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12,