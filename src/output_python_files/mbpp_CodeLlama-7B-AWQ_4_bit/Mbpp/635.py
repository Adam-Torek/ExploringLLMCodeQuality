"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def heap_sort(arr):
    """
    :param arr: list of numbers
    :return: sorted list
    """
    heapify(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr[:i])
    return arr


def heapify(arr):
    """
    :param arr: list of numbers
    :return: sorted list
    """
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify_down(arr, i, len(arr))


def heapify_down(arr, i, n):
    """
    :param arr: list of numbers
    :param i: index of the parent
    :param n: length of the list
    :return: sorted list
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr, largest, n)


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
    print(heap_sort([1, 3, 5, 7, 9, 2, 4,