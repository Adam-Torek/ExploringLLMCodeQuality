"""
Write a function to add the given tuple to the given list.
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
"""

def add_tuple(list, tuple):
    list.extend(tuple)
    return list

print(add_tuple([5, 6, 7], (9, 10)))
/python/list_comprehension.py
"""
Write a list comprehension that returns a list of the first 10 square numbers.
"""

print([x**2 for x in range(1, 11)])
/python/list_comprehension_with_if.py
"""
Write a list comprehension that returns a list of the first 10 square numbers that are divisible by 3.
"""

print([x**2 for x in range(1, 11) if x**2 % 3 == 0])
/python/list_comprehension_with_if_else.py
"""
Write a list comprehension that returns a list of the first 10 square numbers that are divisible by 3, and the first 10 square numbers that are not divisible by 3.
"""

print([x**2 if x**2 % 3 == 0 else x**2 for x in range(1, 11)])
/python/list_comprehension_with_if_else_and_nested_if.py
"""
Write a list comprehension that returns a list of the first 10 square numbers that are divisible by 3, and the first 10 square numbers that are not divisible by 3, and the first 10 square numbers that are divisible by 3 and greater than 100.
"""

print([x**2 if x**2 % 3 == 0 else x**2 for x in range(1, 11) if x**2 > 100])
/python/list_comprehension_with_if_else_and_nested_if_else.py
"""
Write a list comprehension that returns a list of the first 10 square numbers that are divisible by 3, and the first 10 square numbers that are not divisible by 3, and the first 10 square numbers that are divisible by 3 and greater than 100, and the first 10 square numbers that are divisible by 3 and less than 100.
"""

print([x**2 if x**2 % 3 == 0 else x**2 for x in range(1, 11) if x**2 > 100 else x**2])
/python/list_comprehension_with_if_else_and_nested_if_else_and_nested_if.py
"""
Write a list comprehension that returns a list of the first 10 square numbers that are divisible by 3, and the first 10 square numbers that are not divisible by 3, and the first 10 square numbers that are divisible by 3 and greater than 100, and the first 10 square numbers that are divisible by 3 and less than 100, and the first 10 square numbers that are divisible by 3 and greater than 100 and less than 1000.
"""

print([x**2 if x**2 % 3 == 0 else x**2 for x in range(1, 11) if x**2 > 100 else x**2 if x**2 < 1000 else x**2])
/python/list_comprehension_with_if_else_and_nested_if_else_and_nested_if_else.py
"""
Write a list comprehension that returns a list of the first 10 square numbers that are divisible by 3, and the first 10 square numbers that are not divisible by 3, and the first 10 square numbers that are divisible by 3 and greater than 100, and the first 10 square numbers that are divisible by 3 and less than 100, and the first 10 square numbers that are divisible by 3 and greater than 100 and less than 1000, and the first 10 square numbers that are divisible by 3 and greater than 100 and less than 1