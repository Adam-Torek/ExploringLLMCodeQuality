"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(lst):
    flattened_list = []
    for sublist in lst:
        for item in sublist:
            flattened_list.append(item)
    return set(flattened_list)

# Test the function
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]) == set([3, 4, 5, 7, 1])

# Test the function with a nested list
assert set(extract_singly([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with an empty list
assert extract_singly([]) == set()

# Test the function with a list of empty lists
assert extract_singly([[], [], []]) == set()

# Test the function with a list of empty tuples
assert extract_singly([(), (), ()] == set()

# Test the function with a list of tuples
assert extract_singly([(1, 2, 3), (4, 5, 6), (7, 8, 9]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of sets
assert extract_singly([{1, 2, 3}, {4, 5, 6}, {7, 8, 9}] == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of mixed types
assert extract_singly([[1, 2, 3], (4, 5, 6), {7, 8, 9}] == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of mixed types and empty sets
assert extract_singly([[1, 2, 3], (4, 5, 6), {}, {7, 8, 9}] == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of mixed types and empty lists
assert extract_singly([[1, 2, 3], (4, 5, 6), [], [], {7, 8, 9}] == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of mixed types and empty tuples
assert extract_singly([[1, 2, 3], (4, 5, 6), (), (), {7, 8, 9}] == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of mixed types and empty lists and tuples
assert extract_singly([[1, 2, 3], (4, 5, 6), [], (), {}, {7, 8, 9}] == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Test the function with a list of mixed types and empty lists and tuples and sets
assert extract_singly([[1, 2, 3], (4, 5, 6), [], (), {}, set()] == set([1, 2, 3, 4, 5, 6])

# Test the function with a list of mixed types and empty lists and tuples and sets and empty lists
assert extract_singly([[1, 2, 3], (4, 5, 6), [], (), {}, set(), [], (), set()] ==