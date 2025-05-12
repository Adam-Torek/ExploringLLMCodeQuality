"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""

def is_majority(arr, n, element):
    count = 0
    for i in range(n):
        if arr[i] == element:
            count += 1
    if count > n/2:
        return True
    else:
        return False

# Test cases
print(is_majority([1, 2, 3, 3, 3, 10], 7, 3)) # True
print(is_majority([1, 2, 3, 4, 5, 6], 5, 3)) # False
print(is_majority([1, 1, 1, 1, 2, 2, 2, 2], 6, 1)) # True
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 1)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 2)) # True
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 3)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 4)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 10)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 100)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 0)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, -1)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, 1.5)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, "a")) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, None)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, True)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, False)) # False
print(is_majority([1, 1, 1, 2, 2, 2, 3], 6, [1, 2, 3])) # False

# Test cases with empty array
print(is_majority([], 0, 3)) # False
print(is_majority([], 0, 100)) # False
print(is_majority([], 0, None)) # False
print(is_majority([], 0, "a")) # False
print(is_majority([], 0, True)) # False
print(is_majority([], 0, False)) # False
print(is_majority([], 0, [])) # False

# Test cases with non-integer length
print(is_majority([1, 2, 3, 3, 3, 10], "7", 3)) # False
print(is_majority([1, 2, 3, 3, 3, 10], 7.5, 3) # False
print(is_majority([1, 2, 3, 3, 3, 10], None, 3) # False
print(is_major