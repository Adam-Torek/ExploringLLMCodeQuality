"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""

def remove_parenthesis(string):
    if string[0] == "(" and string[-1] == ")":
        return remove_parenthesis(string[1:-1])
    else:
        return string

print(remove_parenthesis("python (chrome)"))
/python/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list from another list.
"""

# Example 1

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of squares of numbers
squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)

# List comprehension
squares = [number ** 2 for number in numbers]
print(squares)

# Example 2

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# List comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 3

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# List comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 4

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# List comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 5

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# List comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 6

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# List comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 7

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# List comprehension
even