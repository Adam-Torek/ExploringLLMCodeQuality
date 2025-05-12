"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
def is_majority(arr, n, element):
    count = 0
    for i in arr:
        if i == element:
            count += 1
    return count > n//2

# Test case
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 1) == False
assert is_majority([1, 1, 1, 2, 2, 2, 2], 7, 2) == True
assert is_majority([1, 1, 1, 2, 2, 2, 2], 7, 1) == False
assert is_majority([1, 1, 1, 2, 2, 2, 2], 7, 3) == False