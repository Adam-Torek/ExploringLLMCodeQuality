"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""


def intersection_array(arr1, arr2):
    """
    :param arr1: array
    :param arr2: array
    :return: array
    """
    arr1_set = set(arr1)
    arr2_set = set(arr2)
    return list(arr1_set.intersection(arr2_set))


if __name__ == '__main__':
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13, 14]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8,