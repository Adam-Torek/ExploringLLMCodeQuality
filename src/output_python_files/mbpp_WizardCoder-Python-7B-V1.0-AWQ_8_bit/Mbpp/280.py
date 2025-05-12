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
print(sequential_search([11,23,58,31,56,77,43,12,65,19],19)) # (True, 7)

# Test cases
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],100) == (False, -1)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],19) == (True, 7)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],11) == (True, 0)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],77) == (True, 4)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],12) == (True, 5)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],65) == (True, 6)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],23) == (True, 1)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],58) == (True, 2)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],11) == (True, 0)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],43) == (True, 4)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],56) == (True, 3)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],2) == (False, -1)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],0) == (False, -1)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],100) == (False, -1)
assert sequential_search([11,23,58,31,56