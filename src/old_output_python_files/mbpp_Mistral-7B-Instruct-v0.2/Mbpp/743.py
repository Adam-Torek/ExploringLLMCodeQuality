"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(lst, n):
    """
    :param lst: list to rotate
    :param n: number of items to rotate
    :return: rotated list
    """
    if len(lst) < n:
        raise ValueError("List length is less than number of items to rotate")
    return lst[-n:] + lst[:-n]

if __name__ == "__main__":
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert rotate_right([], 1) == []
    assert rotate_right([1], 1) == [1]
    assert rotate_right([1], 2) == []
    assert rotate_right([1], 3) == []
    assert rotate_right([1], 10) == []
    assert rotate_right([1], -1) == [1]
    assert rotate_right([1], -2) == [1]
    assert rotate_right([1], -3) == [1]
    assert rotate_right([1], -10) == []
    assert rotate_right([1], float('inf')) == [1]
    assert rotate_right([1], -float('inf')) == [1]
    assert rotate_right([1], 1000000) == []
    assert rotate_right([1], -1000000) == [1]
    assert rotate_right([1], 1000000000) == []
    assert rotate_right([1], -1000000000) == [1]
    assert rotate_right([1], 1000000000000) == []
    assert rotate_right([1], -1000000000000) == [1]
    assert rotate_right([1], 1000000000000000) == []
    assert rotate_right([1], -1000000000000000) == [1]
    assert rotate_right([1], 1000000000000000000) == []
    assert rotate_right([1], -1000000000000000000) == [1]
    assert rotate_right([1], 1000000000000000000000) == []
    assert rotate_right([1], -1000000000000000000000) == [1]
    assert rotate_right([1], 1000000000000000000000000) == []
    assert rotate_right([1], -1000000000000000000000000) == [1]
    assert rotate_right([1], 1000000000000000000000000000) == []
    assert rotate_right([1], -100000000000000000000