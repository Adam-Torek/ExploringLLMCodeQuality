"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""


def shell_sort(arr):
    """
    Sort the given array by using shell sort.
    :param arr: the given array
    :return: the sorted array
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


if __name__ == '__main__':
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000, 100000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000, 100000, 1000000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000, 100000, 1000000, 10000000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]))
    print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000