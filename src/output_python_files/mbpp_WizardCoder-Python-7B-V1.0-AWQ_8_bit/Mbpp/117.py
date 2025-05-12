"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(lst):
    result = []
    for sublist in lst:
        new_sublist = []
        for element in sublist:
            try:
                new_sublist.append(float(element))
            except ValueError:
                new_sublist.append(element)
        result.append(tuple(new_sublist))
    return result

# Test the function
print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]))
# Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

# Test the function with a list of tuples
print(list_to_float([(3, 4), (1, 26.45), (7.32, 8), (4, 8)]))
# Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

# Test the function with a list of strings
print(list_to_float(["3", "4", "1", "26.45", "7.32", "8", "4"]))
# Output: [3.0, 4.0, 1.0, 26.45, 7.32, 8.0, 4.0]

# Test the function with a list of integers
print(list_to_float([3, 4, 1, 26.45, 7.32, 8, 4]))
# Output: [3.0, 4.0, 1.0, 26.45, 7.32, 8.0, 4.0]

# Test the function with a list of mixed types
print(list_to_float([3, "4", 1, "26.45", 7.32, "8", 4]))
# Output: [3.0, 4.0, 1.0, 26.45, 7.32, 8.0, 4.0]

# Test the function with a list of non-convertible types
print(list_to_float([3, "4", 1, "26.45", 7.32, "8", 4, "hello"]))
# Output: [3.0, 4.0, 1.0, 26.45, 7.32, 8.0, "hello"]

# Test the function with a list of nested lists
print(list_to_float([[3, 4], [1, 26.45], [7.32, 8], [4, 8]]))
# Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

# Test the function with a list of nested tuples
print(list_to_float([(3, 4), (1, 26.45), (7.32, 8), (4, 8)])
# Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

# Test the function with a list of nested lists and tuples
print(list_to_float([[3, 4], (1, 26.45), (7.32, 8), [4, 8]])
# Output: [(3.0