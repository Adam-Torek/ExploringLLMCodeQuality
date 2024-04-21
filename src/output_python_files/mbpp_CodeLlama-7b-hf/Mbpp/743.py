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
    if n == 0:
        return lst
    if n > len(lst):
        n = n % len(lst)
    return lst[n:] + lst[:n]


if __name__ == '__main__':
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 16))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 18))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 21))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 23))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 24))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 26))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 27))
    print(rotate_right([