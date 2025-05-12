"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""


def check_min_heap(arr):
    """
    Check if the given array represents min heap or not.
    :param arr: array to check
    :return: True if the array represents min heap, False otherwise
    """
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return arr[0] <= arr[1]
    if arr[0] > arr[1]:
        return False
    return check_min_heap(arr[1:])


if __name__ == '__main__':
    print(check_min_heap([1, 2, 3, 4, 5, 6]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 1