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

print(min_Swaps("1101","1110"))/Python/Algorithms/Sorting/bubble_sort.py
"""
Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Example:

First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([5,1,4,2,8]))/Python/Algorithms/Sorting/selection_sort.py
"""
Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

Example:

First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm picks the minimum element in unsorted array and swaps it with the first element
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Here, algorithm picks the minimum element in the unsorted array and swaps it with the first element
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Here, algorithm picks the minimum element in the unsorted array and swaps it with the first element
( 1 4 2 5 8 ) –>  ( 1 4 2 5 8 ), Now, the array is already sorted.

Second Pass:
( 1 4 2 5 8 ) –> ( 1