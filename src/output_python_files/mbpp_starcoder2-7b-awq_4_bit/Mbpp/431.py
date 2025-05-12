"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""

def common_element(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(common_element([1,2,3,4,5], [5,6,7,8,9]))
/python/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 2

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 3

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 4

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 5

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 6

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 7

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Example 8

# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(numbers)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in numbers]
print(squares)

# Create a list of even numbers from 0 to 9
even_numbers = [x for