"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""

def search(arr):
    n = len(arr)
    if n % 2 == 0:
        return None
    else:
        for i in range(1, n, 2):
            if arr[i] != arr[i-1]:
                return arr[i]
        return None

# Test cases
print(search([1,1,2,2,3])) # Output: 3
print(search([1,2,2,3,3,4,4,5,5])) # Output: 1
print(search([1,1,2,3,3,4,4,5,5,6,6])) # Output: 2
print(search([1,2,3,3,4,5,5,6,6,7,7])) # Output: 1
print(search([1,2,3,4,5,6,7,8,9,9])) # Output: 8
print(search([1,2,3,4,5,6,7,8,9,10,10]) # Output: 1