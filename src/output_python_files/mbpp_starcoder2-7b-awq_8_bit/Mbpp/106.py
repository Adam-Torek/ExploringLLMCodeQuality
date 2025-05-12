"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(list1, tuple1):
    return tuple1 + tuple(list1)

print(add_lists([5, 6, 7], (9, 10)))
/python/list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
"""

def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_2.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
"""

def odd_numbers(numbers):
    return [number for number in numbers if number % 2!= 0]

print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_3.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive numbers.
"""

def positive_numbers(numbers):
    return [number for number in numbers if number > 0]

print(positive_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_4.py
"""
Write a function that takes a list of numbers and returns a new list with only the negative numbers.
"""

def negative_numbers(numbers):
    return [number for number in numbers if number < 0]

print(negative_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_5.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers greater than 10.
"""

def greater_than_10(numbers):
    return [number for number in numbers if number > 10]

print(greater_than_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_6.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers less than 10.
"""

def less_than_10(numbers):
    return [number for number in numbers if number < 10]

print(less_than_10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_7.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers divisible by 3.
"""

def divisible_by_3(numbers):
    return [number for number in numbers if number % 3 == 0]

print(divisible_by_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_8.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers divisible by 5.
"""

def divisible_by_5(numbers):
    return [number for number in numbers if number % 5 == 0]

print(divisible_by_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_9.py
"""
Write a function that takes a list of numbers and returns a new list with only the numbers divisible by 7.
"""

def divisible_by_7(numbers):
    return [number for number in numbers if number % 7 == 0