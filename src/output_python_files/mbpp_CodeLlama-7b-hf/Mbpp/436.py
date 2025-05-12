"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""


def neg_nos(lst):
    """
    :param lst: list of numbers
    :return: list of negative numbers
    """
    return [x for x in lst if x < 0]


if __name__ == '__main__':
    print(neg_nos([-1, 4, 5, -6]))
    print(neg_nos([1, 4, 5, -6]))
    print(neg_nos([-1, 4, 5, -6, 0]))
    print(neg_nos([-1, 4, 5, -6, 0, 1]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(neg_nos([-1, 4, 5, -6, 0, 1, -2, 3, 4, 5, 6, 7,