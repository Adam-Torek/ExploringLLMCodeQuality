"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""

def frequency(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count

print(frequency([1,2,3], 4))
/python/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
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
        even_numbers.append(number ** 2)

print(even_numbers)

# List comprehension
even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 4

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# List comprehension
even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 5

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# List comprehension
even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 6

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# List comprehension
even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 7

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of even numbers
even_numbers