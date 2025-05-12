"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return True, i
    return False, -1

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],32))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],33))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],34))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],35))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],36))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],37))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],38))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],39))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],40))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],41))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],42))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],43))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],44))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],45))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],46))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],47))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],48))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],49))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],50))
print(sequential_search([11,23,58,31,56,77,43,12,65,19],51))
print(sequential_search([11,23,58,31