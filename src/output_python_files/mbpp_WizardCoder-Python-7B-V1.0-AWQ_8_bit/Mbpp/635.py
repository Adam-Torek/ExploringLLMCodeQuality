"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]