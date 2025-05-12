"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31)) # (True, 3)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],100)) # (False, -1)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],19) == (True, 7))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],19) == (False, -1))

# Test cases
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],100) == (False, -1)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],19) == (True, 7)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],100) == (False, -1)

# Test cases for edge cases
assert sequential_search([], 100) == (False, -1)
assert sequential_search([1], 1) == (True, 0)
assert sequential_search([1,2,3,4,5,6,7,8,9], 10) == (False, -1)
assert sequential_search([1,2,3,4,5,6,7,8,9], 0) == (False, -1)
assert sequential_search([1,2,3,4,5,6,7,8,9], 10) == (False, -1)
assert sequential_search([1,2,3,4,5,6,7,8,9], -1) == (False, -1)
assert sequential_search([1,2,3,4,5,6,7,8,9], 1) == (True, 0)
assert sequential_search([1,2,3,4,5,6,7,8,9], 9) == (True, 6)

# Test cases for other inputs
assert sequential_search([1,2,3,4,5,6,7,8,9], 5) == (True, 4)
assert sequential_search([1,2,3,4,5,6,7,8,9], 2) == (True, 1)
assert sequential_search([1,2,3,4,5,6,7,8,9], 8) == (True, 6)
assert sequential_search([1,2,3,4,5,6,7,8,9], 1) == (True, 0)
assert sequential_search([1,2,3,4,5,6,7,8,9], 3) == (True, 2)
assert sequential_search([1,2,3,4,5,6,7,8,9], 4) == (True, 3)
assert sequential_search([1,2,