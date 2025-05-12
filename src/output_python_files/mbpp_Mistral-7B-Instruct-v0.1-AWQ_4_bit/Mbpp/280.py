"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return (True, i)
    return (False, -1)

# Test the function
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)