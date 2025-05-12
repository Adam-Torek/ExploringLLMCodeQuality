"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""

def remove_elements(list1, list2):
    return [x for x in list1 if x not in list2]

# Test the function with the given example
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])) # Output: [1, 3, 5, 7, 9, 10]

# Test the function with some more examples
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10])) # Output: [1, 3, 5, 7]
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: []
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: []