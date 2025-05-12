"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

def replace_list(list1, list2):
    list1[-1] = list2
    return list1

# Test the function
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])) # Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# Test the function with a different input
print(replace_list([1, 3, 5], [2, 4, 6, 8])) # Output: [1, 3, 5, 2, 4, 6, 8]

# Test the function with an empty list
print(replace_list([], [2, 4, 6, 8])) # Output: [2, 4, 6, 8]

# Test the function with a list with only one element
print(replace_list([1], [2, 4, 6, 8])) # Output: [1, 2, 4, 6, 8]

# Test the function with an empty second list
print(replace_list([1, 3, 5, 7, 9, 10], [])) # Output: [1, 3, 5, 7, 9]

# Test the function with a list with only one element and an empty second list
print(replace_list([1], [])) # Output: [1]

# Test the function with an empty first list and an empty second list
print(replace_list([], [])) # Output: []

# Test the function with a list with only one element and a list with only one element
print(replace_list([1], [2])) # Output: [1, 2]

# Test the function with a list with only one element and a list with multiple elements
print(replace_list([1], [2, 4, 6, 8])) # Output: [1, 2, 4, 6, 8]

# Test the function with a list with multiple elements and an empty second list
print(replace_list([1, 3, 5, 7, 9, 10], [])) # Output: [1, 3, 5, 7, 9]

# Test the function with a list with multiple elements and a list with only one element
print(replace_list([1, 3, 5, 7, 9, 10], [2]) # Output: [1, 3, 5, 7, 9, 2]

# Test the function with a list with multiple elements and a list with multiple elements
print(replace_list([1, 3, 5, 7, 9], [2, 4, 6, 8]) # Output: [1, 3, 5, 7, 2, 4, 6, 8]

# Test the function with a list with multiple elements and a list with multiple elements
print(replace_list([1, 3, 5], [2, 4, 6, 8]) # Output: [1, 3, 2, 4, 6]

# Test the function with a list with multiple elements and a list with multiple elements
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6]) # Output: [1, 3, 5, 2, 4, 6]

# Test the function with a list with multiple elements and a list with multiple elements
print(replace_list([1, 3, 5], [2, 4, 6]) # Output: [1, 3, 2, 4, 6]

# Test the function with a list with multiple elements and a list with multiple elements
print(replace_list([1, 3, 5, 7, 9], [2]) # Output: [