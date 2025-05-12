"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""


def right_insertion(arr, value):
    """
    :param arr: sorted array
    :param value: value to be inserted
    :return: index of the right insertion point
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if value < arr[mid]:
            right = mid - 1
        elif value > arr[mid]:
            left = mid + 1
        else:
            return mid
    return left


if __name__ == '__main__':
    print(right_insertion([1, 2, 4, 5], 6))
    print(right_insertion([1, 2, 4, 5], 3))
    print(right_insertion([1, 2, 4, 5], 2))
    print(right_insertion([1, 2, 4, 5], 1))
    print(right_insertion([1, 2, 4, 5], 5))
    print(right_insertion([1, 2, 4, 5], 4))
    print(right_insertion([1, 2, 4, 5], 0))
    print(right_insertion([1, 2, 4, 5], 10))
    print(right_insertion([1, 2, 4, 5], 100))
    print(right_insertion([1, 2, 4, 5], 1000))
    print(right_insertion([1, 2, 4, 5], 10000))
    print(right_insertion([1, 2, 4, 5], 100000))
    print(right_insertion([1, 2, 4, 5], 1000000))
    print(right_insertion([1, 2, 4, 5], 10000000))
    print(right_insertion([1, 2, 4, 5], 100000000))
    print(right_insertion([1, 2, 4, 5], 1000000000))
    print(right_insertion([1, 2, 4, 5], 10000000000))
    print(right_insertion([1, 2, 4, 5], 100000000000))
    print(right_insertion([1, 2, 4, 5], 1000000000000))
    print(right_insertion([1, 2, 4, 5], 10000000000000))
    print(right_insertion([1, 2, 4, 5], 100000000000000))
    print(right_insertion([1, 2, 4, 5], 1000000000000000))
    print(right_insertion([1, 2, 4, 5], 10000000000000000))
    print(right_insertion([1, 2, 4, 5], 100000000000000000))
    print(right_insertion([1, 2, 4, 5], 1000000000000000000))
    print(right_insertion([1, 2, 4, 5], 10000000000000000000))
    print(right_insertion([1, 2, 4, 5], 100000000000000000000))
    print(right_