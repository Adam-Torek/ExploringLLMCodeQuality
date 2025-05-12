"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""

def split_two_parts(lst, L):
    return lst[:L], lst[L:]

print(split_two_parts([1,1,2,3,4,4,5,1],3))
<file_sep>/python/python_basics/03_lists/03_list_comprehension.py
"""
List comprehension is a way to create lists in a concise way.
"""

# Example 1
# Create a list of the first 10 square numbers

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Example 2
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 3
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 4
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 5
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 6
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 7
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 8
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print(squares)

# List comprehension
squares = [x**2 for x in range(10) if x**2 % 2 == 0]
print(squares)

# Example 9
# Create a list of the first 10 square numbers that are even

squares = []
for x in range(10):
    if x**2 % 2 == 0:
        squares.append(x**2)

print