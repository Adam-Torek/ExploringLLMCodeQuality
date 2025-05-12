"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, target):
    """
    Find the last position of target in sorted array arr.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            else:
                left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    assert last([1,2,3],1) == 0
    assert last([1,2,3],2) == 2
    assert last([1,2,3],3) == -1
    assert last([], 1) == -1
    assert last([1], 1) == 0
    assert last([1,2,3,3], 3) == 3
    assert last([1,2,3,3], 4) == -1
    assert last([1,2,3,3], 2) == 2
    assert last([1,2,3,3], 1) == 0