"""
Write a function to rotate a given list by specified number of items to the right direction. https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""
def rotate_right(lst, k):
    """
    :type lst: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == 0:
        return lst
    else:
        return lst[k:] + lst[:k]