"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""


def find_first_occurrence(arr, num):
    """
    :param arr: sorted array
    :param num: number to find
    :return: index of the first occurrence of the number
    """
    if not arr:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == num else -1
    mid = len(arr) // 2
    if arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return find_first_occurrence(arr[mid + 1:], num)
    else:
        return find_first_occurrence(arr[:mid], num)


if __name__ == '__main__':
    print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))
    print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 6))
    print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 8))
    print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 9))
    print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 1))
    print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 10))
    print(find_first_occurrence([], 1))
    print(find_first_occurrence([1], 1))
    print(find_first_occurrence([1], 2))
    print(find_first_occurrence([1, 2], 1))
    print(find_first_occurrence([1, 2], 2))
    print(find_first_occurrence([1, 2], 3))
    print(find_first_occurrence([1, 2, 3], 1))
    print(find_first_occurrence([1, 2, 3], 2))
    print(find_first_occurrence([1, 2, 3], 3))
    print(find_first_occurrence([1, 2, 3], 4))
    print(find_first_occurrence([1, 2, 3], 5))
    print(find_first_occurrence([1, 2, 3], 6))
    print(find_first_occurrence([1, 2, 3], 7))
    print(find_first_occurrence([1, 2, 3], 8))
    print(find_first_occurrence([1, 2, 3], 9))
    print(find_first_occurrence([1, 2, 3], 10))
    print(find_first_occurrence([1, 2, 3, 4], 1))
    print(find_first_occurrence([1, 2, 3, 4], 2))
    print(find_first_occurrence([1, 2, 3, 4], 3))
    print(find_first_occurrence([1, 2, 3, 4], 4))
    print(find_first_occurrence([1, 2, 3, 4], 5))
    print(find_first_occurrence([1, 2, 3, 4], 6))
    print(find_first_occurrence([1, 2, 3, 4], 7))
    print(find_first_occurrence([1, 2