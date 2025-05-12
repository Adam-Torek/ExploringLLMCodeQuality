"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""

def max_aggregate(list_of_tuples):
    max_tuple = list_of_tuples[0]
    for tuple in list_of_tuples:
        if tuple[1] > max_tuple[1]:
            max_tuple = tuple
    return max_tuple

assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
/python_basics/02_lists/02_list_comprehension.py
"""
List comprehension is a way to create a list from another list.
"""

# Create a list of numbers from 0 to 9
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of squares of numbers
squares = []
for number in numbers:
    squares.append(number ** 2)

# Create a list of squares of numbers using list comprehension
squares = [number ** 2 for number in numbers]

# Create a list of even numbers from 0 to 9
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# Create a list of even numbers using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers = [number for number in range(10) if number % 2 == 0]

# Create a list of even numbers from 0 to 9 using list comprehension
even_numbers =