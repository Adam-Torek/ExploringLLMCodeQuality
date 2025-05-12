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
    if x == arr[mid]:
        return mid
    if x < arr[mid]:
        return last(arr[:mid], x)
    else:
        return last(arr[mid + 1:], x)


if __name__ == '__main__':
    print(last([1, 2, 3], 1))
    print(last([1, 2, 3], 2))
    print(last([1, 2, 3], 3))
    print(last([1, 2, 3], 4))
    print(last([1, 2, 3], 0))
    print(last([1, 2, 3], 10))
    print(last([1, 2, 3], 100))
    print(last([1, 2, 3], 1000))
    print(last([1, 2, 3], 10000))
    print(last([1, 2, 3], 100000))
    print(last([1, 2, 3], 1000000))
    print(last([1, 2, 3], 10000000))
    print(last([1, 2, 3], 100000000))
    print(last([1, 2, 3], 1000000000))
    print(last([1, 2, 3], 10000000000))
    print(last([1, 2, 3], 100000000000))
    print(last([1, 2, 3], 1000000000000))
    print(last([1, 2, 3], 10000000000000))
    print(last([1, 2, 3], 100000000000000))
    print(last([1, 2, 3], 1000000000000000))
    print(last([1, 2, 3], 10000000000000000))
    print(last([1, 2, 3], 100000000000000000))
    print(last([1, 2, 3], 1000000000000000000))
    print(last([1, 2, 3], 10000000000000000000))
    print(last([1, 2, 3], 100000000000000000000))
    print(last([1, 2, 3], 1000000000000000000000))
    print(last([1, 2, 3], 10000000000000000000000))
    print(last([1, 2, 3], 100000000000000000000000))
    print(last([1, 2, 3], 1000000000000000000000000))
    print(last([1, 2, 3], 100000000000000000