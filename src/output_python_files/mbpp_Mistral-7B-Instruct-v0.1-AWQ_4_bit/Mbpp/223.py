"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""

def is_majority(arr, n, x):
    # check if x is in the array
    if x not in arr:
        return False
    # count the number of occurrences of x
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    # check if x is the majority element
    if count > n//2:
        return True
    else:
        return False