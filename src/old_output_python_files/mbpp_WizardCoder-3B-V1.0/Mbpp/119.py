"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""

def search(arr):
    if len(arr) == 1:
        return arr[0]
    elif arr[0] == arr[1]:
        return search(arr[2:])
    else:
        return search(arr[1:])

# Test the function
print(search([1,1,2,2,3])) # Output: 3<|endoftext|>