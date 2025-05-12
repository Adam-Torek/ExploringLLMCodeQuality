"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]!= arr[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3))
/Python/Algorithms/Sorting/bubble_sort.py
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

print(bubble_sort([1,2,3,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/insertion_sort.py
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

print(insertion_sort([1,2,3,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/selection_sort.py
"""
Selection Sort

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

print(selection_sort([1,2,3,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/merge_sort.py
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

print(merge_sort([1,2,3,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/quick_sort.py
"""
Quick Sort

Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""

def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    else:
        return arr

print(quick_sort([1,2,3,4,5,6,7,8,9,10]))
/Python/Algorithms/Sorting/heap_sort