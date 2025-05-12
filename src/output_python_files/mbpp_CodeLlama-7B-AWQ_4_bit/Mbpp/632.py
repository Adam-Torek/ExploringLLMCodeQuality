"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""


def move_zero(arr):
    """
    :param arr: list of integers
    :return: list of integers
    """
    # Write your code here
    zero_index = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i], arr[zero_index] = arr[zero_index], arr[i]
            zero_index += 1
    return arr


if __name__ == '__main__':
    arr = [1, 0, 2, 0, 3, 4]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 0, 0]

    arr = [1, 2, 3, 4, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 0, 0]

    arr = [0, 0, 1, 2, 3, 4]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 0, 0]

    arr = [1, 2, 3, 4, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 0, 0]

    arr = [1, 2, 3, 4, 5, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 6, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 7, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 6, 7, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 6, 7, 8, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0]
    print(move_zero(arr))
    # expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0]

    arr = [1, 2, 3, 4, 5, 6, 7