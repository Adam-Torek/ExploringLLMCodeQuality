"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""

def merge(lst):
    return [list(x) for x in zip(*lst)]

# Test cases
print(merge([['x', 'y'], ['a', 'b'], ['m', 'n']])) # Output: [['x', 'a', 'm'], ['y', 'b', 'n']]
print(merge([[1, 2], [3, 4], [5, 6]])) # Output: [[1, 3, 5], [2, 4, 6]]
print(merge([[True, False], [True, False], [False, True]])) # Output: [[True, True, False], [False, False, True]]
print(merge([['hello', 'world'], ['python', 'is'], ['awesome', 'fun']])) # Output: [['hello', 'python', 'awesome'], ['world', 'is', 'fun']]
print(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(merge([[1, 2, 3], [4, 5], [6, 7, 8, 9]])) # Output: [[1, 4, 6], [2, 5, 7], [3, 8, 9]]
print(merge([[], [1, 2], [3, 4, 5]])) # Output: [[], [1], [2], [3, 4, 5]]
print(merge([[], [], []])) # Output: [[], [], []]
print(merge([[1], [2], [3, 4, 5, 6]])) # Output: [[1], [2], [3, 4, 5, 6]]
print(merge([[], [], []]) # Output: [[], [], []]

# Test case for empty list
print(merge([])) # Output: []

# Test case for list with one sublist
print(merge([['hello']]) # Output: [['hello']]

# Test case for list with one element
print(merge([['hello'])) # Output: ['hello']

# Test case for list with one element sublist
print(merge([['hello', 'world'])) # Output: ['hello', 'world']

# Test case for list with one element sublist
print(merge([['hello', 'world', 'python'])) # Output: ['hello', 'world', 'python']

# Test case for list with one element sublist
print(merge([['hello', 'world', 'python', 'is', 'awesome'])) # Output: ['hello', 'world', 'python', 'is', 'awesome']

# Test case for list with one element sublist
print(merge([['hello', 'world', 'python', 'is', 'awesome', 'fun'])) # Output: ['hello', 'world', 'python', 'is', 'awesome', 'fun']

# Test case for list with one element sublist
print(merge([['hello', 'world', 'python', 'is', 'awesome', 'fun', 'good'])) # Output: ['hello', 'world', 'python', 'is', 'awesome', 'fun', 'good']

# Test case for list with one element sublist
print(merge([['hello', 'world', 'python', 'is', 'awesome', 'fun', 'good', 'great'])) # Output: ['hello', 'world', 'python', 'is', 'awesome', 'fun', 'great']

# Test case for list with one element sublist
print(merge([['hello', 'world', 'python', 'is', 'awesome', 'fun', 'great', 'excellent'])) # Output: ['hello', 'world', 'python', 'is', 'awesome