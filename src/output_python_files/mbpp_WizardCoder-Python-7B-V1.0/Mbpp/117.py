"""
Write a function to convert all possible convertible elements in a list of lists to floats.
assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
"""

def list_to_float(lst):
    result = []
    for sublist in lst:
        subresult = []
        for element in sublist:
            try:
                subresult.append(float(element))
            except ValueError:
                subresult.append(element)
        result.append(tuple(subresult))
    return result

# Test the function
print(list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")])) # Output: [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
print(list_to_float([("apple", "banana"), ("orange", "123"), ("12", "3.5"), ("4", "8")])) # Output: [('apple', 'banana'), ('orange', 123.0), (12.0, 3.5), (4.0, 8.0)]
print(list_to_float([("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9")])) # Output: [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
print(list_to_float([("1", "2", "3.5"), ("4", "5", "6"), ("7", "8", "9")])) # Output: [(1.0, 2.0, 3.5), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
print(list_to_float([("1", "2", "3.5", "4"), ("4", "5", "6", "7"), ("7", "8", "9", "10")])) # Output: [(1.0, 2.0, 3.5, 4.0), (4.0, 5.0, 6.0, 7.0), (7.0, 8.0, 9.0, 10.0)]
print(list_to_float([("1", "2", "3.5", "4", "5"), ("4", "5", "6", "7", "8"), ("7", "8", "9", "10", "11")])) # Output: [(1.0, 2.0, 3.5, 4.0, 5.0), (4.0, 5.0, 6.0, 7.0, 8.0), (7.0, 8.0, 9.0, 10.0, 11.0)]
print(list_to_float([("1", "2", "3.5", "4", "5", "6"), ("4", "5", "6", "7", "8", "9"), ("7", "8", "9", "10", "11", "12")])) # Output: [(1.0, 2.0, 3.5, 4.0, 5.0, 6.0), (4.0, 5.0, 6.0, 7.0, 8.0, 9.0), (7.0, 8.0, 9.0, 10.0, 11.0, 12.0)]
print(list_to_float([("1", "2", "3.5", "4", "5", "6", "7"), ("4", "5", "6", "7", "8", "9", "10"), ("7", "8", "9", "1