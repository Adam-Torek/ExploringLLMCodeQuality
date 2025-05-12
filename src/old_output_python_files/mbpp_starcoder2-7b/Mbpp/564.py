"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i]!= lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1],3))
<file_sep>/Python/Algorithms/Sorting/bubble_sort.py
"""
Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

The algorithm, as a generalization of selection sort, is as follows:

For each pair of adjacent elements a[j], a[j+1] in the array:
If a[j] > a[j+1], then swap them.
Repeat for all array elements except the last one, which is already in place.

"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([1,2,3,4,5,6,7,8,9,10]))
<file_sep>/Python/Algorithms/Sorting/insertion_sort.py
"""
Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([1,2,3,4,5,6,7,8,9,10]))
<file_sep>/Python/Algorithms/Sorting/selection_sort.py
"""
Selection Sort

Selection sort is a sorting algorithm, specifically an in-place comparison sort. It has O(n2) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and it has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.

The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([1,2,3,4,5,6,7,8,9,10]))
<file_sep>/Python/Algorithms/Sorting/merge_sort.py
"""
Merge Sort

Merge sort is a divide and conquer algorithm that was invented by <NAME> in 1945.

It involves dividing a list into two halves, sorting the two halves, and then merging the sorted halves back into