"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""

def check_min_heap(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i//2]:
            return False
    return True

# Test cases
print(check_min_heap([1, 2, 3, 4, 5, 6])) # True
print(check_min_heap([1, 2, 3, 4, 5])) # False
print(check_min_heap([1, 2, 3, 4])) # False
print(check_min_heap([1, 2, 3])) # False
print(check_min_heap([1])) # False<|endoftext|>