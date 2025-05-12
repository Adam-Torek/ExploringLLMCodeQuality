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
    return lst[n:] + lst[:n]


if __name__ == '__main__':
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1000000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10000000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100000000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1000000000000))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10000000000000))
    print(rotate_