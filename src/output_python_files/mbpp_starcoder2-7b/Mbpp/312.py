"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""

def volume_cone(r,h):
    return (1/3)*math.pi*r**2*h

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
<file_sep>/python/python_basics/03_lists/03_list_comprehension.py
"""
List comprehension
"""

# List comprehension
# [expression for item in list]

# Example 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list with the square of each number
squares = [number**2 for number in numbers]
print(squares)

# Example 2
# Create a new list with the square of each number
# if the number is even
squares = [number**2 for number in numbers if number % 2 == 0]
print(squares)

# Example 3
# Create a new list with the square of each number
# if the number is even
# and the square is greater than 100
squares = [number**2 for number in numbers if number % 2 == 0 and number**2 > 100]
print(squares)

# Example 4
# Create a new list with the square of each number
# if the number is even
# and the square is greater than 100
# and the square is less than 1000
squares = [number**2 for number in numbers if number % 2 == 0 and number**2 > 100 and number**2 < 1000]
print(squares)

# Example 5
# Create a new list with the square of each number
# if the number is even
# and the square is greater than 100
# and the square is less than 1000
# and the square is odd
squares = [number**2 for number in numbers if number % 2 == 0 and number**2 > 100 and number**2 < 1000 and number**2 % 2 == 1]
print(squares)

# Example 6
# Create a new list with the square of each number
# if the number is even
# and the square is greater than 100
# and the square is less than 1000
# and the square is odd
# and the square is divisible by 3
squares = [number**2 for number in numbers if number % 2 == 0 and number**2 > 100 and number**2 < 1000 and number**2 % 2 == 1 and number**2 % 3 == 0]
print(squares)

# Example 7
# Create a new list with the square of each number
# if the number is even
# and the square is greater than 100
# and the square is less than 1000
# and the square is odd
# and the square is divisible by 3
# and the square is divisible by 5
squares = [number**2 for number in numbers if number % 2 == 0 and number**2 > 100 and number**2 < 1000 and number**2 % 2 == 1 and number**2 % 3 == 0 and number**2 % 5 == 0]
print(squares)

# Example 8
# Create a new list with the square of each number
# if the number is even
# and the square is greater than 100
# and the square is less than 1000
# and the square is odd
# and the square is divisible by 3
# and the square is divisible by 5
# and the square is divisible by 7
squares = [number**2 for number in numbers if number % 2 == 0 and number**2 > 100 and number**2 < 1000 and number**2 % 2 == 1 and number**2 % 3 == 0 and number**2 % 5 == 0 and number