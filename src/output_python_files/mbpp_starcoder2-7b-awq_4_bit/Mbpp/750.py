"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(list, tuple):
    list.extend(tuple)
    return list

print(add_tuple([5, 6, 7], (9, 10)))
/python/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Create a list of numbers from 0 to 9
numbers = [number for number in range(10)]
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = [number for number in range(10) if number % 2 == 0]
print(even_numbers)

# Create a list of squares of numbers from 0 to 9
squares = [number ** 2 for number in range(10)]
print(squares)

# Create a list of cubes of numbers from 0 to 9
cubes = [number ** 3 for number in range(10)]
print(cubes)

# Create a list of numbers from 0 to 9 and their squares
number_squares = [(number, number ** 2) for number in range(10)]
print(number_squares)

# Create a list of numbers from 0 to 9 and their cubes
number_cubes = [(number, number ** 3) for number in range(10)]
print(number_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
number_squares_cubes = [(number, number ** 2, number ** 3) for number in range(10)]
print(number_squares_cubes)
/python/list_comprehension_nested.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Create a list of numbers from 0 to 9
numbers = [number for number in range(10)]
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = [number for number in range(10) if number % 2 == 0]
print(even_numbers)

# Create a list of squares of numbers from 0 to 9
squares = [number ** 2 for number in range(10)]
print(squares)

# Create a list of cubes of numbers from 0 to 9
cubes = [number ** 3 for number in range(10)]
print(cubes)

# Create a list of numbers from 0 to 9 and their squares
number_squares = [(number, number ** 2) for number in range(10)]
print(number_squares)

# Create a list of numbers from 0 to 9 and their cubes
number_cubes = [(number, number ** 3) for number in range(10)]
print(number_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
number_squares_cubes = [(number, number ** 2, number ** 3) for number in range(10)]
print(number_squares_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
number_squares_cubes = [(number, number ** 2, number ** 3) for number in range(10)]
print(number_squares_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
number_squares_cubes = [(number, number ** 2, number ** 3) for number in range(10)]
print(number_squares_cubes)

# Create a list of numbers from 0 to 9 and their squares and cubes
number_squares_cubes = [(number, number ** 2, number ** 3) for number in range(10)]
print(number_squares_cubes)

# Create a list