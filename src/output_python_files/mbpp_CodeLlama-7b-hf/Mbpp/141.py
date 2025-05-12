"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""


def pancake_sort(arr):
    """
    Sorts the list in ascending order
    :param arr: list of elements
    :return: sorted list
    """
    for i in range(len(arr) - 1, 0, -1):
        max_index = arr.index(max(arr[:i + 1]))
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            arr[0:max_index + 1] = arr[0:max_index + 1][::-1]
    return arr


if __name__ == '__main__':
    print(pancake_sort([15, 79, 25, 38, 69]))
    print(pancake_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(pancake_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(pancake_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(pancake_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
    print(pancake_sort([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54,