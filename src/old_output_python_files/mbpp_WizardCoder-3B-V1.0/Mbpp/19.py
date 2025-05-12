"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
def test_duplicate(arr):
    return len(arr)!= len(set(arr))

# Test cases
print(test_duplicate(([1,2,3,4,5]))) # False
print(test_duplicate(([1,2,3,4,5,5]))) # True<|endoftext|>