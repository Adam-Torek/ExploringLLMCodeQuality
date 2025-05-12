"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(lst, n):
    """
    :param lst: list to be rotated
    :param n: number of positions to rotate
    :return: rotated list
    """
    if len(lst) < n:
        raise ValueError("List length is less than number of positions to rotate")
    return lst[-n:] + lst[:-n]

if __name__ == "__main__":
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    assert rotate_right([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert rotate_right([], 1) == []
    assert rotate_right([1], 1) == [1]
    assert rotate_right([1], 2) == []
    assert rotate_right([1], 3) == []
    assert rotate_right([1], 4) == []
    assert rotate_right([1], 5) == []
    assert rotate_right([1], 6) == []
    assert rotate_right([1], 7) == []
    assert rotate_right([1], 8) == []
    assert rotate_right([1], 9) == []
    assert rotate_right([1], 10) == []
    assert rotate_right([1], 11) == []
    assert rotate_right([1], 12) == []
    assert rotate_right([1], 13) == []
    assert rotate_right([1], 14) == []
    assert rotate_right([1], 15) == []
    assert rotate_right([1], 16) == []
    assert rotate_right([1], 17) == []
    assert rotate_right([1], 18) == []
    assert rotate_right([1], 19) == []
    assert rotate_right([1], 20) == []
    assert rotate_right([1], 21) == []
    assert rotate_right([1], 22) == []
    assert rotate_right([1], 23) == []
    assert rotate_right([1], 24) == []
    assert rotate_right([1], 25) == []
    assert rotate_right([1], 26) == []
    assert rotate_right([1], 27) == []
    assert rotate_right([1], 28) == []
    assert rotate_right([1], 29) == []
    assert rotate_right([1], 30) == []
    assert rotate_right([1], 31) == []
    assert rotate_right([1], 32) == []
    assert rotate_right([1], 33) == []
    assert rotate_right([1], 34) == []
    assert rotate_right([1], 35) == []
    assert rotate_right([1], 36) == []
    assert rotate_right([1], 37) == []
    assert rotate_right([1], 38) == []
    assert rotate_right([1], 39) == []
    assert rotate_right([1], 40) == []
    assert rotate_right([1], 41) == []
    assert rotate_right([1], 42) == []
    assert rotate_right([1