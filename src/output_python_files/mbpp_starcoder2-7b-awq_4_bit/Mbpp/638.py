"""
Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
assert wind_chill(120,35)==40
"""

def wind_chill(wind_velocity, temperature):
    if wind_velocity < 4.8:
        return temperature
    else:
        return 13.12 + 0.6215 * temperature - 11.37 * wind_velocity ** 0.16 + 0.3965 * temperature * wind_velocity ** 0.16

print(wind_chill(120,35))/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of squares of numbers
squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)

# List comprehension
squares = [number ** 2 for number in numbers]
print(squares)

# Example 2

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# List comprehension
even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(even_numbers)

#