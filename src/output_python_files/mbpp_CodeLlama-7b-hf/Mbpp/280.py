"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return True, i
    return False, -1

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],32))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],12))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],19))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],100))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],1111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],1111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],111111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],1111111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11111111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],111111111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],1111111111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],11111111111111))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],111111111111111))
print(sequential_search([1