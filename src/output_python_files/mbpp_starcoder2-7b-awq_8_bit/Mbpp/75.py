"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(tuples, k):
    return [tuple(i for i in t if i % k == 0) for t in tuples]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
/python/list_comprehension.py
"""
List comprehension is a way to create a list in a single line.
"""

# Example 1

# Create a list of numbers from 1 to 10
numbers = [i for i in range(1, 11)]
print(numbers)

# Example 2

# Create a list of numbers from 1 to 10 which are divisible by 2
numbers = [i for i in range(1, 11) if i % 2 == 0]
print(numbers)

# Example 3

# Create a list of numbers from 1 to 10 which are divisible by 2 and 3
numbers = [i for i in range(1, 11) if i % 2 == 0 and i % 3 == 0]
print(numbers)

# Example 4

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 5

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 6

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 7

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 8

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 9

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 10

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 11

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 12

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 11) if i % 2 == 0 or i % 3 == 0]
print(numbers)

# Example 13

# Create a list of numbers from 1 to 10 which are divisible by 2 or 3
numbers = [i for i in range(1, 1