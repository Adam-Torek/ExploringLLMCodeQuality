"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def heap_sort(lst):
    def heapify(lst, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and lst[i] < lst[left]:
            largest = left

        if right < n and lst[largest] < lst[right]:
            largest = right

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(lst, n, largest)

    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)

    return lst


assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]