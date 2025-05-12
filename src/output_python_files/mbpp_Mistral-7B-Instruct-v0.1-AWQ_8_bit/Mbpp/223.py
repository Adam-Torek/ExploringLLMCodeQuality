"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def is_majority(arr, n, x):
    # Check if the element is in the array
    if x not in arr:
        return False
    # Count the number of times the element appears
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    # Check if the element appears more than n/2 times
    if count > n//2:
        return True
    else:
        return False