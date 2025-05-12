"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def heap_sort(arr):
    """
    :param arr: list
    :return: list
    """
    if len(arr) <= 1:
        return arr

    def heapify(arr, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, largest, n)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr


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
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(heap_sort([1, 3, 5, 7, 9,