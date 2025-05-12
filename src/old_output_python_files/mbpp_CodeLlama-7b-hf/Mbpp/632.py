"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""


def move_zero(arr):
    """
    :param arr: list
    :return: list
    """
    zero_index = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_index.append(i)
    for i in zero_index:
        arr.pop(i)
    arr.extend([0] * len(zero_index))
    return arr


if __name__ == '__main__':
    print(move_zero([1, 0, 2, 0, 3, 4]))
    print(move_zero([1, 2, 3, 4, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 0]))
    print(move_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]))
    print(move_zero([1, 2