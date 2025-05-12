"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""

def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count

# Testing the function
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1)) # Output: 3
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 7) # Output: 2
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 15) # Output: 1
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 2) # Output: 0

# Testing with empty list
print(count_element_in_list([], 1) # Output: 0

# Testing with list with single element
print(count_element_in_list([[1], [2], [3], [4]], 1) # Output: 1

# Testing with list with multiple occurrences of element
print(count_element_in_list([[1, 1, 1, 1, 1, 1], [2, 2, 2], [3, 3], [4, 4]], 1) # Output: 5

# Testing with list with no element
print(count_element_in_list([[], [], [], []], 1) # Output: 0

# Testing with list with negative numbers
print(count_element_in_list([[-1, -2, -3], [-4, -5], [-6, -7], [-8, -9]], -1) # Output: 1

# Testing with list with strings
print(count_element_in_list([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']], 'a') # Output: 1

# Testing with list with empty sublist
print(count_element_in_list([[], [], [1, 2, 3], []], 1) # Output: 1

# Testing with list with empty list
print(count_element_in_list([[], [], [], []], 1) # Output: 0

# Testing with list with empty list
print(count_element_in_list([[], [], [], []], '') # Output: 0

# Testing with list with empty list
print(count_element_in_list([[], [], [], []], []) # Output: 0

# Testing with list with empty list
print(count_element_in_list([[], [], [], []], None) # Output: 0

# Testing with list with empty list
print(count_element_in_list([[], [], [], []], 1, 2, 3) # Output: TypeError: count_element_in_list() takes exactly one argument (4 given)

# Testing with list with empty list
print(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 1, 2, 3) # Output: TypeError: count_element_in_list() takes exactly one argument (5 given)

# Testing with list with empty list
print(count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], 1, 2, 3) # Output: TypeError: count_element_in_list() takes exactly one argument (7 given)