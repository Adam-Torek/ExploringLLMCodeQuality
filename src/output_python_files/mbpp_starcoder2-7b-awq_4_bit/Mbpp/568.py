"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""

def empty_list(n):
    return [{} for i in range(n)]

print(empty_list(5))
/python/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Create a list of squares of numbers from 0 to 9
squares = [i ** 2 for i in range(10)]
print(squares)

# Create a list of cubes of numbers from 0 to 9
cubes = [i ** 3 for i in range(10)]
print(cubes)

# Create a list of numbers from 0 to 9 and their squares
numbers_and_squares = [(i, i ** 2) for i in range(10)]
print(numbers_and_squares)

# Create a list of numbers from 0 to 9 and their cubes
numbers_and_cubes = [(i, i ** 3) for i in range(10)]
print(numbers_and_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
numbers_and_squares_and_cubes = [(i, i ** 2, i ** 3) for i in range(10)]
print(numbers_and_squares_and_cubes)
/python/list_comprehension_with_if_else.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Create a list of odd numbers from 0 to 9
odd_numbers = [i for i in range(10) if i % 2!= 0]
print(odd_numbers)

# Create a list of numbers from 0 to 9 and their squares
numbers_and_squares = [(i, i ** 2) for i in range(10)]
print(numbers_and_squares)

# Create a list of numbers from 0 to 9 and their squares and cubes
numbers_and_squares_and_cubes = [(i, i ** 2, i ** 3) for i in range(10)]
print(numbers_and_squares_and_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
# if the number is even
numbers_and_squares_and_cubes = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(numbers_and_squares_and_cubes)
/python/list_comprehension_with_if_else_and_else.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Create a list of odd numbers from 0 to 9
odd_numbers = [i for i in range(10) if i % 2!= 0]
print(odd_numbers)

# Create a list of numbers from 0 to 9 and their squares
numbers_and_squares = [(i, i ** 2) for i in range(10)]
print(numbers_and_squares)

# Create a list of numbers from 0