"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_Odd_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] ^ arr[j]) % 2!= 0:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))
/Python/Algorithms/Sorting/bubble_sort.py
"""
Bubble Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([5,4,3,2,1]))
/Python/Algorithms/Sorting/selection_sort.py
"""
Selection Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

print(selection_sort([5,4,3,2,1]))
/Python/Algorithms/Sorting/insertion_sort.py
"""
Insertion Sort

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([5,4,3,2,1]))
/Python/Algorithms/Sorting/merge_sort.py
"""
Merge Sort

Time Complexity: O(nlogn)
Space Complexity: O(n)

"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print(merge_sort([5,4,3,2,1]))
/Python/Algorithms/Sorting/quick_sort.py
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

print(quick_