"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan','rebecca', 'Diana', 'Joanne', 'keith'])==16
"""

def sample_nam(names):
    total = 0
    for name in names:
        if name[0].isupper():
            total += len(name)
    return total

print(sample_nam(['sally', 'Dylan','rebecca', 'Diana', 'Joanne', 'keith']))
<file_sep>/python_practice/practice_problems/practice_problems_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 5])==5
"""

def largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(largest([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 5])==1
"""

def smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print(smallest([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the average of the numbers.
assert average([1, 2, 3, 4, 5])==3
"""

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(average([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_of_numbers([1, 2, 3, 4, 5])==15
"""

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_of_numbers([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the product of the numbers.
assert product([1, 2, 3, 4, 5])==120
"""

def product(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(product([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1, 2, 3, 4, 5])==1
"""

def smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print(smallest([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1, 2, 3, 4, 5])==5
"""

def largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(largest([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the average of the numbers.
assert average([1, 2, 3, 4, 5])==3
"""

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(average([1, 2, 3, 4, 5]))

"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_of_numbers([1, 2, 3, 4, 5])==15
"""

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_of_numbers([1, 2, 3, 4, 5]))