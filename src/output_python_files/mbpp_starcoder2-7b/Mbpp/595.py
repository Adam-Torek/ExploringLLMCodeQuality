"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""

def min_Swaps(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            count += 1
    return count

print(min_Swaps("1101","1110"))
/Python/Algorithms/Sorting/SelectionSort.py
"""
Selection Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

print(selection_sort([1,5,3,2,4]))
/Python/Algorithms/Sorting/BubbleSort.py
"""
Bubble Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([1,5,3,2,4]))
/Python/Algorithms/Sorting/InsertionSort.py
"""
Insertion Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([1,5,3,2,4]))
/Python/Algorithms/Sorting/MergeSort.py
"""
Merge Sort

Time Complexity: O(nlogn)
Space Complexity: O(n)

"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
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
    return arr

print(merge_sort([1,5,3,2,4]))
/Python/Algorithms/Sorting/QuickSort.py
"""
Quick Sort

Time Complexity: O(nlogn)
Space Complexity: O(logn)

"""

def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
    return arr

print(quick_sort([1,5,3,2,4],0,4))
/Python/Algorithms/Sorting/HeapSort.py
"""
Heap