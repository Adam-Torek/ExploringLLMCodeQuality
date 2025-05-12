"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""

def split_two_parts(lst,L):
    return lst[:L],lst[L:]

print(split_two_parts([1,1,2,3,4,4,5,1],3))
/python/list_comprehension.py
"""
List comprehension is a way to create lists in a concise way.
"""

# Example 1

# Create a list of numbers from 0 to 9

numbers = []
for i in range(10):
    numbers.append(i)

print(numbers)

# List comprehension

numbers = [i for i in range(10)]
print(numbers)

# Example 2

# Create a list of squares of numbers from 0 to 9

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

# List comprehension

squares = [i**2 for i in range(10)]
print(squares)

# Example 3

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 4

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 5

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 6

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 7

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 8

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 9

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# List comprehension

even_numbers = [i for i in range