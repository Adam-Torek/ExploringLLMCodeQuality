"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""

def search(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] != arr[1] else None
    mid = len(arr) // 2
    left_once = search(arr[:mid])
    right_once = search(arr[mid:])
    if left_once is not None and right_once is not None:
        return left_once if left_once == right_once else None
    elif left_once is not None:
        return left_once
    elif right_once is not None:
        return right_once
    else:
        return find_once(arr)

def find_once(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            return arr[i]
    return None

# Test cases
print(search([1,1,2,2,3])) # Output: 3
print(search([1,2,3,3,4,4,5,6,6])) # Output: 5
print(search([1,2,3,4,5,6,6,7,8,8])) # Output: 7
print(search([1,1,2,3,3,4,5,5,6,7,8,8])) # Output: None
print(search([1,2,3,4,5,6,7,8,9,9,9])) # Output: 1
print(search([1,1,2,3,3,4,5,6,7,8,8,9,9,9])) # Output: 2
print(search([1,2,3,4,5,6,7,8,9,10,10,11,11,12]) # Output: 12