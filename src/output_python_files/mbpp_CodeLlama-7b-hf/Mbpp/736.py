"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""


def left_insertion(arr, value):
    """
    :param arr: list of integers
    :param value: integer
    :return: index of the left insertion point
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        if arr[0] >= value:
            return 0
        else:
            return 1
    if arr[0] >= value:
        return 0
    if arr[len(arr) - 1] < value:
        return len(arr)
    for i in range(1, len(arr)):
        if arr[i] >= value:
            return i
    return len(arr)


if __name__ == '__main__':
    print(left_insertion([1, 2, 4, 5], 6))
    print(left_insertion([1, 2, 4, 5], 3))
    print(left_insertion([1, 2, 4, 5], 2))
    print(left_insertion([1, 2, 4, 5], 1))
    print(left_insertion([1, 2, 4, 5], 4))
    print(left_insertion([1, 2, 4, 5], 5))
    print(left_insertion([1, 2, 4, 5], 0))
    print(left_insertion([1, 2, 4, 5], 10))
    print(left_insertion([1, 2, 4, 5], 100))
    print(left_insertion([1, 2, 4, 5], 1000))
    print(left_insertion([1, 2, 4, 5], 10000))
    print(left_insertion([1, 2, 4, 5], 100000))
    print(left_insertion([1, 2, 4, 5], 1000000))
    print(left_insertion([1, 2, 4, 5], 10000000))
    print(left_insertion([1, 2, 4, 5], 100000000))
    print(left_insertion([1, 2, 4, 5], 1000000000))
    print(left_insertion([1, 2, 4, 5], 10000000000))
    print(left_insertion([1, 2, 4, 5], 100000000000))
    print(left_insertion([1, 2, 4, 5], 1000000000000))
    print(left_insertion([1, 2, 4, 5], 10000000000000))
    print(left_insertion([1, 2, 4, 5], 100000000000000))
    print(left_insertion([1, 2, 4, 5], 1000000000000000))
    print(left_insertion([1, 2, 4, 5], 10000000000000000))
    print(left_insertion([1, 2, 4, 5], 100000000000000000))
    print(left_insertion([1, 2, 4, 5], 10000000000000000