"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""


def last(arr, x):
    """
    :param arr: sorted array
    :param x: element to be searched
    :return: index of last occurrence of x in arr
    """
    if not arr:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == x else -1
    mid = len(arr) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        return last(arr[mid + 1:], x)
    return last(arr[:mid], x)


if __name__ == '__main__':
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2,