"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""

def zero_count(arr):
    """
    Count the number of zeroes in an array of integers.
    """
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
    return count

def non_zero_count(arr):
    """
    Count the number of non-zeroes in an array of integers.
    """
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            count += 1
    return count

def ratio(arr):
    """
    Calculate the ratio of zeroes to non-zeroes in an array of integers.
    """
    return zero_count(arr) / non_zero_count(arr)

if __name__ == '__main__':
    import math
    assert math.isclose(ratio([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)