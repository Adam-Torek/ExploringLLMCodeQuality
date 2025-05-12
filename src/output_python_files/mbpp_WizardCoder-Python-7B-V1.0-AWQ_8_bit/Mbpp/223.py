"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""

def is_majority(arr, n, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    if count > n/2:
        return True
    else:
        return False

# Test cases
print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3)) # True
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, 3)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], 9, 1)) # True
print(is_majority([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], 9, 2)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], 9, 3)) # True
print(is_majority([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], 9, 4)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], 9, 10)) # False

# Edge cases
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, 1)) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, 8)) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, 0)) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, -1)) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, None)) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, "a")) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, 1.5)) # False
print(is_majority([1, 2, 3, 4, 5, 6, 7], 6, [1, 2, 3, 4, 5, 6, 7])) # False

# Test case with empty array
print(is_majority([], 0, 1)) # False

# Test case with length 1 array
print(is_majority([1], 1, 1)) # True

# Test case with length 2 array
print(is_majority([1, 1], 2, 1) # True

# Test case with length 3 array
print(is_majority([1, 2, 3], 3, 1) # False

# Test case with length 4 array
print(is_majority([1, 2, 3, 4], 4, 1) # False

# Test case with length 5 array
print(is_majority([1, 2, 3, 4, 5], 5, 1) # False

# Test case with length 6 array
print(is_majority([1, 2, 3, 4, 5, 6], 6, 1) # False

# Test case with length 7 array
print(is_majority([