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
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

# Create a list of squares of numbers from 0 to 9 using list comprehension
squares = [number ** 2 for number in numbers]
print(squares)

# Example 2

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 3

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 4

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 5

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 6

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Example 7

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers