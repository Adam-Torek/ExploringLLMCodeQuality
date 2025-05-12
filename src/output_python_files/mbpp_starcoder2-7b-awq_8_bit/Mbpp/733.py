"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""

def find_first_occurrence(arr, num):
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
    if arr[0] > num:
        return -1
    if arr[-1] < num:
        return -1
    if arr[0] < num < arr[-1]:
        mid = len(arr) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return find_first_occurrence(arr[:mid], num)
        else:
            return mid + find_first_occurrence(arr[mid:], num)

assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 6) == 4
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 9) == 7
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 10) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 1) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 8) == 6
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 2) == 0
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 3) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 7) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 0) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 100) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], -1) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 1000) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 10000) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 100000) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 1000000) == -1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9,