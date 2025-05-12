"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(arr):
    if len(arr) != len(set(arr)):
        return True
    else:
        return False

# Test cases
print(test_duplicate([1,2,3,4,5])) # False
print(test_duplicate([1,2,3,4,5,5])) # True
print(test_duplicate([1,2,3,4,5,6])) # False
print(test_duplicate([1,2,3,4,5,5,6])) # True
print(test_duplicate([1,2,3,4,5,6,6])) # True
print(test_duplicate([1,2,3,4,5,6,7])) # False
print(test_duplicate([1,2,3,4,5,6,7,7])) # True
print(test_duplicate([1,2,3,4,5,6,7,8])) # False
print(test_duplicate([1,2,3,4,5,6,7,8,8])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9])) # False
print(test_duplicate([1,2,3,4,5,6,7,8,9,9])) # True

# Test cases with empty list
print(test_duplicate([])) # False
print(test_duplicate([1])) # False
print(test_duplicate([1,1])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9])) # True
print(test_duplicate([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9,9,9,9,