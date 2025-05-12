"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

def subject_marks(marks):
    return sorted(marks, key=lambda x: x[1])

assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
/python/list_comprehension.py
"""
Write a function to return a list of even numbers from a given list of numbers.
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
/python/list_comprehension_2.py
"""
Write a function to return a list of even numbers from a given list of numbers.
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]

"""
Write a function to return a list of even numbers from a given list of numbers.
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]

"""
Write a function to return a list of even numbers from a given list of numbers.
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]

"""
Write a function to return a list of even numbers from a given list of numbers.
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]

"""
Write a function to return a list of even numbers from a given list of numbers.
assert even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])==[2, 4, 6, 8]
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

assert even_numbers([1, 2, 3, 4, 5