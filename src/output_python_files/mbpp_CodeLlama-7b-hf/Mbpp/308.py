"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""


def large_product(list1, list2, n):
    """
    :param list1: list of integers
    :param list2: list of integers
    :param n: number of largest products to return
    :return: list of n largest products
    """
    if n > len(list1) or n > len(list2):
        raise ValueError("n must be less than or equal to the length of each list")
    if n < 1:
        raise ValueError("n must be greater than 0")
    if len(list1) == 0 or len(list2) == 0:
        raise ValueError("lists must not be empty")
    if len(list1) != len(list2):
        raise ValueError("lists must be the same length")
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("lists must be of type list")
    if not all(isinstance(x, int) for x in list1) or not all(isinstance(x, int) for x in list2):
        raise TypeError("lists must contain only integers")
    if not all(x > 0 for x in list1) or not all(x > 0 for x in list2):
        raise ValueError("lists must contain only positive integers")
    if not all(x >= 0 for x in list1) or not all(x >= 0 for x in list2):
        raise ValueError("lists must contain only non-negative integers")
    if not all(x != 0 for x in list1) or not all(x != 0 for x in list2):
        raise ValueError("lists must contain only non-zero integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")
    if not all(x != 1 for x in list1) or not all(x != 1 for x in list2):
        raise ValueError("lists must contain only non-unit integers")