"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(tup):
    return tuple(tup[i] + tup[i+1] for i in range(len(tup)-1))

print(add_pairwise((1, 5, 7, 8, 10)))
/python/list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Example 1

# Create a list of squares of numbers from 1 to 10

squares = []
for i in range(1, 11):
    squares.append(i**2)

print(squares)

# Using list comprehension

squares = [i**2 for i in range(1, 11)]
print(squares)

# Example 2

# Create a list of even numbers from 1 to 10

even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

# Using list comprehension

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# Example 3

# Create a list of numbers from 1 to 100 which are divisible by 3

divisible_by_3 = []
for i in range(1, 101):
    if i % 3 == 0:
        divisible_by_3.append(i)

print(divisible_by_3)

# Using list comprehension

divisible_by_3 = [i for i in range(1, 101) if i % 3 == 0]
print(divisible_by_3)

# Example 4

# Create a list of numbers from 1 to 100 which are divisible by 3 and 5

divisible_by_3_and_5 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        divisible_by_3_and_5.append(i)

print(divisible_by_3_and_5)

# Using list comprehension

divisible_by_3_and_5 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(divisible_by_3_and_5)

# Example 5

# Create a list of numbers from 1 to 100 which are divisible by 3 or 5

divisible_by_3_or_5 = []
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        divisible_by_3_or_5.append(i)

print(divisible_by_3_or_5)

# Using list comprehension

divisible_by_3_or_5 = [i for i in range(1, 101) if i % 3 == 0 or i % 5 == 0]
print(divisible_by_3_or_5)

# Example 6

# Create a list of numbers from 1 to 100 which are divisible by 3 and 5 but not by 7

divisible_by_3_and_5_but_not_by_7 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0 and i % 7!= 0:
        divisible_by_3_and_5_but_not_by_7.append(i)

print(divisible_by_3_and_5_but_not_by_7)

# Using list comprehension

divisible_by_3_and_5_but_not_by_7 = [i for i in range(1, 101) if i % 3