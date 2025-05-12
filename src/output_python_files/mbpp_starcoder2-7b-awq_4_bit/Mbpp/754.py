"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""

def extract_index_list(l1,l2,l3):
    return [x for x in l1 if x in l2 and x in l3]

assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
/python/list_comprehension.py
"""
List comprehension is a way to create lists in a concise way.
"""

# Example 1
# Create a list of numbers from 0 to 9

numbers = [x for x in range(10)]
print(numbers)

# Example 2
# Create a list of even numbers from 0 to 9

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Example 3
# Create a list of squares of numbers from 0 to 9

squares = [x ** 2 for x in range(10)]
print(squares)

# Example 4
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 5
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 6
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 7
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 8
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 9
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 10
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 11
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 12
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 13
# Create a list of tuples with two elements

tuples = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(tuples)

# Example 14
# Create