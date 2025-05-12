"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""

def tuple_size(t):
    return sys.getsizeof(t)

assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
/python/python_fundamentals/python_fundamentals_pt1/04_lists/04_list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.

The syntax is:

new_list = [expression for member in iterable]

The expression can be any Python expression, including another list comprehension.

The iterable can be either a list, a tuple, a string, a set, or a dictionary.

"""

# Example 1

# Create a list of the first 10 square numbers

squares = [x**2 for x in range(1,11)]
print(squares)

# Example 2

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 3

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 4

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 5

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 6

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 7

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 8

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 9

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 10

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 11

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 12

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 13

# Create a list of the first 10 square numbers, but only if the number is even

squares = [x**2 for x in range(1,11) if x%2 == 0]
print(squares)

# Example 14

# Create a list of the first 10 square numbers, but only if the number