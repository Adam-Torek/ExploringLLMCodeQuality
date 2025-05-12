"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(nums):
    return max(nums) - min(nums)

print(big_diff([1,2,3,4]))
/python/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    squares.append(number**2)

print(squares)

# Using list comprehension
squares = [number**2 for number in numbers]
print(squares)

# Example 2
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    if number % 2 == 0:
        squares.append(number**2)

print(squares)

# Using list comprehension
squares = [number**2 for number in numbers if number % 2 == 0]
print(squares)

# Example 3
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    if number % 2 == 0:
        squares.append(number**2)
    else:
        squares.append(number)

print(squares)

# Using list comprehension
squares = [number**2 if number % 2 == 0 else number for number in numbers]
print(squares)
/python/list_comprehension_nested.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    if number % 2 == 0:
        squares.append(number**2)
    else:
        squares.append(number)

print(squares)

# Using list comprehension
squares = [number**2 if number % 2 == 0 else number for number in numbers]
print(squares)

# Example 2
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    if number % 2 == 0:
        squares.append(number**2)
    else:
        squares.append(number)

print(squares)

# Using list comprehension
squares = [number**2 if number % 2 == 0 else number for number in numbers]
print(squares)

# Example 3
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    if number % 2 == 0:
        squares.append(number**2)
    else:
        squares.append(number)

print(squares)

# Using list comprehension
squares = [number**2 if number % 2 == 0 else number for number in numbers]
print(squares)

# Example 4
# Create a list of numbers from 0 to 9
numbers = [0,1,2,3,4,5,6,7,8,9]

# Using for loop
squares = []
for number in numbers:
    if number % 2 == 0:
        squares.append(number**2)
    else:
        squares.append(number)

print(squares)

# Using list comprehension
squares = [number**2 if number %