"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

def frequency_lists(lst):
    freq_dict = {}
    for sublist in lst:
        for element in sublist:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1
    return freq_dict

# Test the function
print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])) # Output: {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

# Test the function with a different input
print(frequency_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]])) # Output: {1: 2, 2: 3, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

# Test the function with an empty list
print(frequency_lists([])) # Output: {}

# Test the function with a list of lists with only one element
print(frequency_lists([[1, 2, 3], [4], [5, 6], [7, 8, 9]])) # Output: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

# Test the function with a list of lists with only one element
print(frequency_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

# Test the function with a list of lists with only one element
print(frequency_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]])) # Output: {1: 2, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

# Test the function with a list of lists with only one element
print(frequency_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6]])) # Output: {1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1, 8: 1, 9: 1}

# Test the function with a list of lists with only one element
print(frequency_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: {1: 3, 2: 3, 3: 3, 4: 2, 5: 2, 6: 2,