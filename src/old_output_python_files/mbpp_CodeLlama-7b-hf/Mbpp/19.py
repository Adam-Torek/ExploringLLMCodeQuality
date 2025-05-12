"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""


def test_duplicate(arr):
    """
    :param arr: list of integers
    :return: True if duplicate else False
    """
    if len(arr) == len(set(arr)):
        return False
    else:
        return True


if __name__ == '__main__':
    print(test_duplicate([1, 2, 3, 4, 5]))
    print(test_duplicate([1, 2, 3, 4, 5, 6]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    print(test_duplicate([1, 2, 3, 4, 5, 6, 7,