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
/Python/Algorithms/Sorting/BubbleSort.py
"""
Bubble Sort

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([1,3,2,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/SelectionSort.py
"""
Selection Sort

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selectionSort([1,3,2,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/InsertionSort.py
"""
Insertion Sort

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertionSort([1,3,2,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/MergeSort.py
"""
Merge Sort

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

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

print(mergeSort([1,3,2,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/QuickSort.py
"""
Quick Sort

Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""

def quickSort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]

        return quickSort(left) + [pivot] + quickSort(right)
    return arr

print(quickSort([1,3,2,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/HeapSort.py
"""
Heap Sort

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

def heapSort(arr):
    def heapify(arr