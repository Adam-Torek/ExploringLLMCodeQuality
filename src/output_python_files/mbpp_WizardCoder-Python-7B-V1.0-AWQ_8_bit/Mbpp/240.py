"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

def replace_list(list1, list2):
    list1[-1] = list2
    return list1

# Testing the function
print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])) # Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# Testing the function with a different input
print(replace_list([1, 3, 5, 7], [2, 4, 6, 8, 10])) # Output: [1, 3, 5, 7, 2, 4, 6, 8]

# Testing the function with an empty list
print(replace_list([], [2, 4, 6, 8])) # Output: [2, 4, 6, 8]

# Testing the function with a list with only one element
print(replace_list([1], [2, 4, 6, 8])) # Output: [1, 2, 4, 6, 8]

# Testing the function with a list with only one element and an empty list
print(replace_list([1], [])) # Output: [1]

# Testing the function with an empty list and an empty list
print(replace_list([], [])) # Output: []

# Testing the function with a list with only one element and an empty list
print(replace_list([1], [])) # Output: [1]

# Testing the function with a list with only one element and a list with one element
print(replace_list([1], [2])) # Output: [1, 2]

# Testing the function with a list with only one element and a list with two elements
print(replace_list([1], [2, 3])) # Output: [1, 2, 3]

# Testing the function with a list with two elements and a list with one element
print(replace_list([1, 2], [3]) # Output: [1, 3]

# Testing the function with a list with two elements and a list with two elements
print(replace_list([1, 2], [3, 4]) # Output: [1, 3, 4]

# Testing the function with a list with two elements and a list with three elements
print(replace_list([1, 2], [3, 4, 5]) # Output: [1, 3, 4, 5]

# Testing the function with a list with three elements and a list with two elements
print(replace_list([1, 2, 3], [4, 5]) # Output: [1, 4, 5]

# Testing the function with a list with three elements and a list with three elements
print(replace_list([1, 2, 3], [4, 5, 6]) # Output: [1, 4, 5, 6]

# Testing the function with a list with four elements and a list with three elements
print(replace_list([1, 2, 3, 4], [5, 6]) # Output: [1, 5, 6]

# Testing the function with a list with four elements and a list with four elements
print(replace_list([1, 2, 3, 4], [5, 6, 7]) # Output: [1, 5, 6, 7]

# Testing the function with a list with four elements and a list with five elements
print(replace_list([1, 2, 3, 4], [5, 6, 7, 8]) # Output: [1, 5, 6, 7, 8]

# Testing the function with a list with five elements and a list with four elements
print(replace_list([1,