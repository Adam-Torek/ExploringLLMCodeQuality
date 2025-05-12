"""
Write a function to find the index of the first occurrence of a given number in a sorted array.
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
"""

def find_first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1