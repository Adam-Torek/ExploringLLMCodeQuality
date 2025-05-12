"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

def similar_elements(list1, list2):
    return set(list1).intersection(list2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))
/python/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1

# Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(numbers)

# Example 2

# Create a list of numbers from 0 to 9 which are even
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 3

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0 or i % 2 == 1]
print(even_odd_numbers)

# Example 4

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 5

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 6

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 7

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 8

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 9

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 10

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 11

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]
print(even_odd_numbers)

# Example 12

# Create a list of numbers from 0 to 9 which are even and odd
even_odd_numbers = [i for i in range(10) if i % 2 == 0] + [i for i in range(10) if i % 2 == 1]