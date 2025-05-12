"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

def flatten_list(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Test cases
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])) # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(flatten_list([1, [2, [3, [4, [5, [6, 7], 8], 9], 10], 11], 12])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(flatten_list([[1, 2, 3], [4, 5, [6, 7, [8, 9, [10, 11, [12, 13]]]]])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(flatten_list([[[[1], [2, 3], [4, [5, [6, 7, [8, 9, [10, [11, [12]]]]]]]]])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(flatten_list([[[[[[[[[[[[[[1]]]]]]]]]]]]]]]) # Output: [1]
print(flatten_list([1, [2, [3, [4, [5, [6, 7], 8], 9], 10], 11])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(flatten_list([[[[[[[[[[[[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]]]]]]]]]]]]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(flatten_list([[[[[[[[[[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]]]]]]]]]]])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(flatten_list([[[[[[[[[[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]]]]]]]]]]])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(flatten_list([[[[[[[[[[1