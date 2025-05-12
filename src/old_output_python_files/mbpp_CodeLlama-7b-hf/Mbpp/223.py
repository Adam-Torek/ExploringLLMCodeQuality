"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""


def is_majority(arr, n, elem):
    """
    :param arr: sorted array
    :param n: length of array
    :param elem: element to check
    :return: True if elem is majority element, False otherwise
    """
    if n == 0:
        return False
    if arr[0] == elem:
        return True
    if arr[n - 1] == elem:
        return True
    if arr[n // 2] == elem:
        return True
    return False


if __name__ == '__main__':
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 1))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 10))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 4))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 11))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 1))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 10))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 4))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 11))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 1))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 10))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 4))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 11))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 1))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 10))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 4))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 11))
    print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 2))
    print(is_majority([1, 2, 3, 3, 3, 3, 10],