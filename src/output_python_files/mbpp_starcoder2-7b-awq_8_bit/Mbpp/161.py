"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""

def remove_elements(list1, list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
/python/list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
"""

def even_numbers(list1):
    return [i for i in list1 if i % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_2.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
"""

def odd_numbers(list1):
    return [i for i in list1 if i % 2!= 0]

print(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_3.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive numbers.
"""

def positive_numbers(list1):
    return [i for i in list1 if i > 0]

print(positive_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_4.py
"""
Write a function that takes a list of numbers and returns a new list with only the negative numbers.
"""

def negative_numbers(list1):
    return [i for i in list1 if i < 0]

print(negative_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_5.py
"""
Write a function that takes a list of numbers and returns a new list with only the prime numbers.
"""

def prime_numbers(list1):
    return [i for i in list1 if i > 1 and all(i % j!= 0 for j in range(2, i))]

print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_6.py
"""
Write a function that takes a list of numbers and returns a new list with only the even prime numbers.
"""

def even_prime_numbers(list1):
    return [i for i in list1 if i > 1 and all(i % j!= 0 for j in range(2, i)) and i % 2 == 0]

print(even_prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_7.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd prime numbers.
"""

def odd_prime_numbers(list1):
    return [i for i in list1 if i > 1 and all(i % j!= 0 for j in range(2, i)) and i % 2!= 0]

print(odd_prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python/list_comprehension_8.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive prime numbers.
"""

def positive_prime_numbers(list