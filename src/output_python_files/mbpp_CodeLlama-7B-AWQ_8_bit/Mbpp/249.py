"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""


def intersection_array(arr1, arr2):
    """
    :param arr1: list of integers
    :param arr2: list of integers
    :return: list of integers
    """
    # Write your code here
    return list(set(arr1).intersection(arr2))


if __name__ == '__main__':
    print("Example:")
    print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13, 14]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13, 14, 15]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13, 14, 15, 16]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5,