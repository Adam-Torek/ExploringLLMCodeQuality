"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1])

print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
<file_sep>/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Without list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# With list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

print(squares)

# Example 2

# Without list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# With list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# Example 3

# Without list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# With list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number ** 2 for number in numbers if number % 2 == 0]

print(even_numbers)

# Example 4

# Without list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# With list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number ** 2 for number in numbers if number % 2 == 0]

print(even_numbers)

# Example 5

# Without list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number ** 2)

print(even_numbers)

# With list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number ** 2 for number in numbers if number % 2 == 0]

print(even_numbers)

# Example 6

# Without list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7,