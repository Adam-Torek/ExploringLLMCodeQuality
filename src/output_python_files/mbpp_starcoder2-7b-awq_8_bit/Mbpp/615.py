"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""

def average_tuple(tup):
    return [sum(x)/len(x) for x in tup]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
/python_basics/02_lists/02_list_comprehension.py
"""
List comprehension is a way to create lists in a single line of code.
"""

# Example 1
# Create a list of numbers from 0 to 9
numbers = [x for x in range(10)]
print(numbers)

# Example 2
# Create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Example 3
# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

# Example 4
# Create a list of tuples with numbers from 0 to 9 and their squares
tuples = [(x, x**2) for x in range(10)]
print(tuples)

# Example 5
# Create a list of tuples with numbers from 0 to 9 and their squares
# if the number is even
tuples = [(x, x**2) for x in range(10) if x % 2 == 0]
print(tuples)

# Example 6
# Create a list of tuples with numbers from 0 to 9 and their squares
# if the number is even
# and the square is greater than 100
tuples = [(x, x**2) for x in range(10) if x % 2 == 0 and x**2 > 100]
print(tuples)

# Example 7
# Create a list of tuples with numbers from 0 to 9 and their squares
# if the number is even
# and the square is greater than 100
# and the number is less than 5
tuples = [(x, x**2) for x in range(10) if x % 2 == 0 and x**2 > 100 and x < 5]
print(tuples)

# Example 8
# Create a list of tuples with numbers from 0 to 9 and their squares
# if the number is even
# and the square is greater than 100
# and the number is less than 5
# and the square is less than 1000
tuples = [(x, x**2) for x in range(10) if x % 2 == 0 and x**2 > 100 and x < 5 and x**2 < 1000]
print(tuples)

# Example 9
# Create a list of tuples with numbers from 0 to 9 and their squares
# if the number is even
# and the square is greater than 100
# and the number is less than 5
# and the square is less than 1000
# and the number is greater than 2
tuples = [(x, x**2) for x in range(10) if x % 2 == 0 and x**2 > 100 and x < 5 and x**2 < 1000 and x > 2]
print(tuples)

# Example 10
# Create a list of tuples with numbers from 0 to 9 and their squares
# if the number is even
# and the square is greater than 100
# and the number is less than 5
# and the square is less than 1000
# and the number is greater than 2
# and the square is greater than 1000