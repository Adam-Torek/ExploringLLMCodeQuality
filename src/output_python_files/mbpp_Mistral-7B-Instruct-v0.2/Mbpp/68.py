"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""
def is_Monotonic(arr):
    """
    :param arr: list of integers
    :return: boolean value
    """
    if len(arr) < 2:
        return True

    is_increasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            is_increasing = False
            break

    if is_increasing:
        return True

    is_decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            is_decreasing = False
            break

    return is_decreasing

if __name__ == "__main__":
    assert is_Monotonic([6, 5, 4, 4]) == True
    assert is_Monotonic([1, 2, 3]) == True
    assert is_Monotonic([1, 2, 3, 4]) == True
    assert is_Monotonic([1, 2, 3, 4, 5]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == True
    assert is_Monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18