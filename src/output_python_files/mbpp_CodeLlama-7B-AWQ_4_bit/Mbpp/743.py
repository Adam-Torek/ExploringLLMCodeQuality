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
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0:
        return lst
    if n > len(lst):
        raise ValueError("n must be less than or equal to the length of the list")
    return lst[n:] + lst[:n]


if __name__ == '__main__':
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -11))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
    print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8,