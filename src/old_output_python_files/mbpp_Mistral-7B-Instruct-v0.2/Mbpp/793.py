"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, target):
    """
    :param arr: sorted array
    :param target: element to find the last position of
    :return: index of the last occurrence of the target in the array
    """
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            if mid == n - 1 or arr[mid + 1] != target:
                return mid
            else:
                start = mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

if __name__ == "__main__":
    assert last([1,2,3],1) == 0
    assert last([1,2,3],2) == 2
    assert last([1,2,3],3) == 2
    assert last([1,2,3],4) == -1
    assert last([],1) == -1
    assert last([1],1) == 0
    assert last([1,1],1) == 1
    assert last([1,1,1],1) == 2
    assert last([1,1,1],2) == 2
    assert last([1,1,1],3) == 2
    assert last([1,1,1],4) == 2
    assert last([1,1,1],5) == -1
    assert last([1,1,1,1],1) == 3
    assert last([1,1,1,1],2) == 3
    assert last([1,1,1,1],3) == 3
    assert last([1,1,1,1],4) == 3
    assert last([1,1,1,1],5) == 3
    assert last([1,1,1,1],6) == -1
    assert last([1,1,1,1,1],1) == 4
    assert last([1,1,1,1,1],2) == 4
    assert last([1,1,1,1,1],3) == 4
    assert last([1,1,1,1,1],4) == 4
    assert last([1,1,1,1,1],5) == 4
    assert last([1,1,1,1,1],6) == 4
    assert last([1,1,1,1,1],7) == -1
    assert last([1,1,1,1,1,1],1) == 5
    assert last([1,1,1,1,1,1],2) == 5
    assert last([1,1,1,1,1,1],3) == 5
    assert last([1,1,1,1,1,1],4) == 5
    assert last([1,1,1,1,1,1],5) == 5
    assert last([1,1,1,1,1,1],6) == 5
    assert last([1,1,1,1,1,1],7) == 5
    assert last([1,1,1,1,1,1],8) == -1
    assert last([1,1,1,1,1,1,1],1) == 6
    assert last([1,1,1,1,1,1,1],2) == 6
    assert last([1,1,1,1,1,1,1],3) == 6
    assert last([1,1,1,1,1,1,1],4) == 6
    assert last([1,1,1,1,1,1,1],5) == 6
    assert last([1,1,1,1,1,1,1],6) == 6
    assert last([1,1,1,1,1,1,1],7) == 6
    assert last([1,1,1,1,1,1,1],8) == 6