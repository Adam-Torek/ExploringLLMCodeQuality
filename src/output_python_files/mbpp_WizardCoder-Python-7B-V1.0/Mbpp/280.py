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
print(sequential_search([11,23,58,31,56,77,43,12,65,19],12)) # (True, 6)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],1)) # (False, -1)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],65)) # (True, 6)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11)) # (True, 0)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],77)) # (True, 4)
print(sequential_search([11,23,58,31,56,77,43,12,65,19],23)) # (True, 1)

# Test cases
# Test case 1: Element is present in the array
# Test case 2: Element is not present in the array
# Test case 3: Element is present in the array
# Test case 4: Element is not present in the array
# Test case 5: Element is present in the array
# Test case 6: Element is present in the array
# Test case 7: Element is present in the array