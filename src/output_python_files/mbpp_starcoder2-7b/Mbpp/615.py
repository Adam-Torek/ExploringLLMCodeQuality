"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""

def average_tuple(tup):
    return [sum(x)/len(x) for x in tup]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
<file_sep>/python_basics/02_lists/02_list_comprehension.py
"""
List comprehension is a way to create lists in a concise way.
"""

# Create a list of numbers from 0 to 9
numbers = [x for x in range(10)]
print(numbers)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# Create a list of cubes of numbers from 0 to 9
cubes = [x**3 for x in range(10)]
print(cubes)

# Create a list of tuples of numbers from 0 to 9
tuples = [(x, x**2, x**3) for x in range(10)]
print(tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples of even numbers from 0 to 9
even_tuples = [(x, x**2, x**3) for x in range(10) if x % 2 == 0]
print(even_tuples)

# Create a list of tuples