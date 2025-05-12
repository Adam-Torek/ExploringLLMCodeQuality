"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def heap_sort(arr):
    """
    :param arr: list
    :return: list
    """
    heapify(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr[:i])
    return arr


def heapify(arr):
    """
    :param arr: list
    :return: list
    """
    for i in range(len(arr) // 2, -1, -1):
        sift_down(arr, i, len(arr))


def sift_down(arr, i, n):
    """
    :param arr: list
    :param i: int
    :param n: int
    :return: list
    """
    while 2 * i + 1 < n:
        j = 2 * i + 1
        if j + 1 < n and arr[j] < arr[j + 1]:
            j += 1
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i = j
        else:
            break


if __name__ == '__main__':
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9, 2,