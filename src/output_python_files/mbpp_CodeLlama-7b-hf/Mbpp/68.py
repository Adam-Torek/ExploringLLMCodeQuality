"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""


def is_Monotonic(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_Monotonic([6, 5, 4, 4]))
    print(is_Monotonic([1, 2, 3, 4]))
    print(is_Monotonic([1, 1, 1, 1]))
    print(is_Monotonic([1, 2, 3, 4, 5]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,