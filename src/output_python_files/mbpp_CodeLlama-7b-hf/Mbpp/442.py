"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""


def positive_count(arr):
    """
    :param arr: list of integers
    :return: float
    """
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count / len(arr)


if __name__ == '__main__':
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(positive