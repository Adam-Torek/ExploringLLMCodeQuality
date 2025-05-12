"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""


def positive_count(arr):
    """
    :param arr: array of integers
    :return: ratio of positive numbers in the array
    """
    if not arr:
        return 0
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count / len(arr)


if __name__ == '__main__':
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
    print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,