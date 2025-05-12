"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(string):
    return string.replace(' ','')

print(remove_all_spaces('python  program'))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line.
"""

# Example 1
# Create a list of numbers from 1 to 10
numbers = [i for i in range(1,11)]
print(numbers)

# Example 2
# Create a list of even numbers from 1 to 10
even_numbers = [i for i in range(1,11) if i%2==0]
print(even_numbers)

# Example 3
# Create a list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1,11)]
print(squares)

# Example 4
# Create a list of squares of even numbers from 1 to 10
even_squares = [i**2 for i in range(1,11) if i%2==0]
print(even_squares)

# Example 5
# Create a list of tuples of numbers from 1 to 10 and their squares
numbers_and_squares = [(i,i**2) for i in range(1,11)]
print(numbers_and_squares)

# Example 6
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 7
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 8
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 9
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 10
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 11
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 12
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 13
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i in range(1,11) if i%2==0]
print(even_numbers_and_squares)

# Example 14
# Create a list of tuples of numbers from 1 to 10 and their squares
# if the number is even
even_numbers_and_squares = [(i,i**2) for i