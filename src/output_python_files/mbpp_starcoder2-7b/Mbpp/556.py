"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_Odd_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]^arr[j])%2!= 0:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))<file_sep>/Python/Algorithms/Sorting/SelectionSort.py
"""
Selection Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

print(selectionSort([5,4,3,2,1]))<file_sep>/Python/Algorithms/Sorting/BubbleSort.py
"""
Bubble Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubbleSort([5,4,3,2,1]))<file_sep>/Python/Algorithms/Sorting/InsertionSort.py
"""
Insertion Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertionSort([5,4,3,2,1]))<file_sep>/Python/Algorithms/Sorting/MergeSort.py
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

print(mergeSort([5,4,3,2,1]))<file_sep>/Python/Algorithms/Sorting/QuickSort.py
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

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    return arr

print(quickSort([5,4,3,2,1],0,4))<file_sep>/Python/Algorithms/Sorting/CountingSort.py
"""
Counting Sort

Time Complexity: O(n+k)
Space Complexity: O(n+k)