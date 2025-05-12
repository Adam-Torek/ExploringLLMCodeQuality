"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""

def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    inv_count = 0
    inv_count += get_Inv_Count(left)
    inv_count += get_Inv_Count(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            inv_count += len(left) - i
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return inv_count

print(get_Inv_Count([1,20,6,4,5]))
/Python/Algorithms/Sorting/merge_sort.py
"""
Merge Sort
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [1,2,3,4,5,6,7,8,9,10]
merge_sort(arr)
print(arr)
/Python/Algorithms/Sorting/quick_sort.py
"""
Quick Sort
"""

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
/Python/Algorithms/Sorting/insertion_sort.py
"""
Insertion Sort
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
/Python/Algorithms/Sorting/bubble_sort.py
"""
Bubble Sort
"""

def bubble_sort(arr):
    for i in range(len