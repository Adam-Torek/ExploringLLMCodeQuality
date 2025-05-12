"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_Sum(lst,n):
    sum = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            sum += lst[i] ^ lst[j]
    return sum

print(pair_xor_Sum([5,9,7,6],4))
/Python/Algorithms/Sorting/bubble_sort.py
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

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

print(bubble_sort([5,9,7,6]))
/Python/Algorithms/Sorting/insertion_sort.py
"""
Insertion Sort

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Algorithm

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example:

Input data: 4, 5, 3, 7, 6, 2, 1

Output array: 1, 2, 3, 4, 5, 6, 7

Initially, the sorted array has one element (1) in it.
4 is removed from the input data.
4 is inserted back to the sorted array at the first position i.e. 0th position.

Next, 5 is removed from the input data.
5 is inserted at the end of the sorted array.

Next, 3 is removed from the input data.
3 is inserted at the correct position i.e. 1st position.

Next, 7 is removed from the input data.
7 is inserted at the correct position i.e. 3rd position.

Next, 6 is removed from the input data.
6 is inserted at the correct position i.e. 4th position.

Next