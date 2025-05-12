"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""


def is_Monotonic(arr):
    if len(arr) == 1:
        return True
    if len(arr) == 2:
        return arr[0] <= arr[1]
    if arr[0] <= arr[1] <= arr[2]:
        return True
    if arr[0] >= arr[1] >= arr[2]:
        return True
    return False


if __name__ == '__main__':
    print(is_Monotonic([6, 5, 4, 4]))
    print(is_Monotonic([6, 5, 4, 3]))
    print(is_Monotonic([6, 5, 4, 3, 2]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]))
    print(is_Monotonic([6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14