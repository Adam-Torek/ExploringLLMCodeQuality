"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""

def find_first_occurrence(arr, num):
    """
    :param arr: sorted array
    :param num: number to find
    :return: index of first occurrence of num in arr
    """
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == num:
            return 0
        else:
            return -1
    if arr[0] == num:
        return 0
    if arr[-1] == num:
        return len(arr) - 1
    if arr[0] > num or arr[-1] < num:
        return -1
    mid = len(arr) // 2
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return find_first_occurrence(arr[:mid], num)
    else:
        return mid + find_first_occurrence(arr[mid:], num)


def find_first_occurrence_binary_search(arr, num):
    """
    :param arr: sorted array
    :param num: number to find
    :return: index of first occurrence of num in arr
    """
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == num:
            return 0
        else:
            return -1
    if arr[0] == num:
        return 0
    if arr[-1] == num:
        return len(arr) - 1
    if arr[0] > num or arr[-1] < num:
        return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            if mid == 0 or arr[mid - 1]!= num:
                return mid
            else:
                high = mid - 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_first_occurrence_binary_search_recursive(arr, num):
    """
    :param arr: sorted array
    :param num: number to find
    :return: index of first occurrence of num in arr
    """
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == num:
            return 0
        else:
            return -1
    if arr[0] == num:
        return 0
    if arr[-1] == num:
        return len(arr) - 1
    if arr[0] > num or arr[-1] < num:
        return -1
    mid = len(arr) // 2
    if arr[mid] == num:
        if mid == 0 or arr[mid - 1]!= num:
            return mid
        else:
            return find_first_occurrence_binary_search_recursive(arr[:mid], num)
    elif arr[mid] > num:
        return find_first_occurrence_binary_search_recursive(arr[:mid], num)
    else:
        return mid + find_first_occurrence_binary_search_recursive(arr[mid:], num)


def find_first_occurrence_binary_search_recursive_2(arr, num):
    """
    :param arr: sorted array
    :param num: number to find
    :return: index of first occurrence of num in arr
    """
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == num:
            return 0
        else:
            return -1
    if arr[0] == num:
        return 0
    if arr[-1] == num:
        return len(arr) - 1
    if arr[0] > num or arr[-1] < num:
        return -1
    mid = len(arr) // 2
    if arr[mid] == num:
        if mid == 0 or arr[mid - 1]!= num:
            return mid
        else:
            return find_first_occurrence_binary_search_recursive_2(arr[:mid], num)
    elif arr[mid] > num:
        return find_first_occurrence_binary_search_recursive_2(arr