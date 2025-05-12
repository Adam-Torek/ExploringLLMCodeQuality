"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""
def sequential_search(arr, element):
    """
    :param arr: list
    :param element: int
    :return: tuple of boolean and index
    """
    index = -1
    for i, num in enumerate(arr):
        if num == element:
            index = i
            break
    return (element in arr, index)

# Testing
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],12) == (True, 9)
assert sequential_search([11,23,58,31,56,77,43,12,65,19],10) == (False, -1)
assert sequential_search([], 1) == (False, -1)
assert sequential_search([1], 1) == (True, 0)
assert sequential_search([1], 2) == (False, -1)