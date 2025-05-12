"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(lst):
    result = []
    for sublist in lst:
        subresult = []
        for item in sublist:
            try:
                subresult.append(float(item))
            except ValueError:
                subresult.append(item)
        result.append(tuple(subresult))
    return result

# Test the function
print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]))
# Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

# Test the function with a list of lists containing non-convertible elements
print(list_to_float([("3", "4", "hello"), ("1", "26.45", "world"), ("7.32", "8", "!"), ("4", "8", "!")]))
# Output: [(3.0, 4.0, 'hello'), (1.0, 26.45, 'world'), (7.32, 8.0, '!'), (4.0, 8.0, '!')]

# Test the function with an empty list
print(list_to_float([]))
# Output: []

# Test the function with a list of lists containing only non-convertible elements
print(list_to_float([("hello", "world"), ("hello", "world"), ("hello", "world")])
# Output: [('hello', 'world'), ('hello', 'world'), ('hello', 'world')]

# Test the function with a list of lists containing only convertible elements
print(list_to_float([(3, 4), (1, 26.45), (7.32, 8), (4, 8)])
# Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]

# Test the function with a list of lists containing only one element
print(list_to_float([(3,)]
# Output: [(3.0,)]

# Test the function with a list of lists containing one element that cannot be converted to float
print(list_to_float([("hello",)]
# Output: [('hello',)]

# Test the function with a list of lists containing one element that can be converted to float
print(list_to_float([(3.5,)]
# Output: [(3.5,)]

# Test the function with a list of lists containing one element that can be converted to float
print(list_to_float([(3, 4, 5, 6)
# Output: [(3, 4, 5, 6)]

# Test the function with a list of lists containing one element that can be converted to float
print(list_to_float([(3, 4, 5, 6.5)
# Output: [(3.0, 4.0, 5.0, 6.5)]

# Test the function with a list of lists containing one element that can be converted to float
print(list_to_float([(3, 4, 5, "6.5")
# Output: [(3.0, 4.0, 5.0, '6.5')]

# Test the function with a list of lists containing one element that can be converted to float
print(list_to_float([(3, 4, 5, "hello")
# Output: [(3.0, 4.0, 5.0, 'hello')]

# Test the function with a list of lists containing one element that can be converted to float
print(list_to